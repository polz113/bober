from bober_tasks.models import *
from django.conf import settings
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.loader import render_to_string
from django.template.context import RequestContext
from bober_tasks.helper import *
import zipfile
import codecs
import re
import os
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView, TemplateView
import django.forms
from django.forms.models import modelform_factory, model_to_dict
from django_tables2 import RequestConfig
from bober_tasks.tables import TaskTable
from bober_tasks.filters import TaskFilter
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from braces.views import LoginRequiredMixin
import StringIO
from json import dumps as to_json
from django.http import HttpResponse
from bober_tasks import forms
from django.contrib import auth, messages
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
import random

def render_to_file(template, filename, template_data, context): # loads template with context data and returns it as a file
    return codecs.open(os.path.join(settings.MEDIA_DIR, 'tasks_private') + filename, 'w', 'utf-8').write(render_to_string(template, template_data, context)) # save file to 'private folder'

def export_task_language_version( request, task_id, language_code, version ):
    task_translation = TaskTranslation.objects.get(language_locale = language_code, task_id=task_id, version=version)
    return export_task_translation(request, task_translation)

def export_task_language( request, task_id, language_code ):
    task = Task.objects.get(id = task_id)
    task_translation = task.get_latest_translation(language_code)
    return export_task_translation(request, task_translation)

def export_task_translation( request, task_translation ):
    version = str(task_translation.version)
    if task_translation: # check if task with given id and translation exists
        answers = task_translation.answer_set.all()
        task = task_translation.task

        SOURCE_RELATIVE_PATH  = []                                                        # paths to other sources
        SOURCE_RELATIVE_PATH_IN_ZIP_FILE = []                                             # relative path to source in zip file (images will reside in 'Images' folder)


        resources = Resources.objects.filter(task = task_translation.task, language = task_translation.language_locale)
        # Check for specific task resources and add them to 'task' section in Manifest.json (default resources are index.html and Functions.js)
        if resources.all().count() > 0:
            current_task_resources  = resources

            current_task_resources_types = []
            current_task_resources_names = []
            for i in range(0, len(current_task_resources)):
                if current_task_resources[i].type == "image":
                    current_task_resources_types.append("image")
                    current_task_resources_names.append("resources/" + current_task_resources[i].filename)
                elif (current_task_resources[i].type == "javascript") and ("jquery" not in current_task_resources[i].filename):
                    current_task_resources_types.append("javascript")
                    current_task_resources_names.append("Javascript/" + current_task_resources[i].filename)
                elif current_task_resources[i].type == "HTML":
                    current_task_resources_types.append("html")
                    current_task_resources_names.append("Html/" + current_task_resources[i].filename)
                elif current_task_resources[i].type == "CSS":
                    current_task_resources_types.append("css")
                    current_task_resources_names.append("Css/" + current_task_resources[i].filename)

            current_task_resources_objects = zip(current_task_resources_types, current_task_resources_names)

        # get all image filenames of a specific task
        image_filenames = []
        number_of_task_images = resources.filter(type = "image").count()
        if(number_of_task_images > 0):
            task_image_entries = resources.filter(type = "image")

            for image_entry in task_image_entries:
                image_filenames.append(image_entry.filename)

        # Generate Manifest.json, index.html, solution.html
        manifest = render_to_file("api/Manifest.html", "Manifest.json", locals(), RequestContext( request ))
        solution_site = render_to_file("api/solution.html", "solution.html",  locals(), RequestContext( request ))
        index_site = render_to_file("api/task_interactive.html", "index.html", locals(), RequestContext( request ))

        # Files to put in the .zip
        filenames = []

        # for every resource add its * savepath: when calling export/task/4/EN, that will be in the folder /taskresources/Images/4/EN/
        #                            * relative savepath in zip file: if f. is picture, that will be in /Images/4/EN

        for resource in resources.all():
            SOURCE_RELATIVE_PATH.append(os.path.join(settings.MEDIA_ROOT, 'task', str(task_translation.task_id) , task_translation.language_locale, 'resources', resource.filename))
            SOURCE_RELATIVE_PATH_IN_ZIP_FILE.append("resources/" + resource.filename)


        # add aditional sources without static filepaths to 'filenames'(such as pictures, ...) which are located in PATH_TO_SOURCE_ON_SERVER
        for source_path in SOURCE_RELATIVE_PATH:
            filenames.append(source_path)

        # ZIP archive filename, Open StringIO to grab in-memory ZIP contents, The zip compressor
        #zip_filename = "task-" + str(task.id) + "-" + task_translation.language_locale + "-v" + task_translation.version
        zip_filename = '%s-%d_%s_v%d' % (slugify(task_translation.title),
            task_translation.task_id, task_translation.language_locale, task_translation.version)
        #zip_filename = task_translation.title
        s = StringIO.StringIO()
        zf = zipfile.ZipFile(s, "w")

        at_root = ["Manifest.html", "index.html"]


        for fpath in filenames:
            # Calculate path for file in zip
            fdir, fname = os.path.split(fpath)

            # Get relative dirpath to file in zip file
            dirpath = ""
            for relative_path in SOURCE_RELATIVE_PATH_IN_ZIP_FILE:
                if fname in relative_path:
                    dirpath, fname = os.path.split(relative_path)
                    break

            # Add file to zip
            if fname in at_root:            # Functions.js,Manifest.html,index.html are at the root of the zip file
                zip_path = os.path.join("", fname)

            else:                           # All other files go into their respective paths
                zip_path = os.path.join(dirpath, fname)


            # Add file, at correct path
            zf.write(fpath, zip_path)

        # Static files
        zf.write(os.path.join(settings.MEDIA_ROOT, 'tasks_private', 'solution.html'),'solution.html')
        zf.write(os.path.join(settings.MEDIA_ROOT, 'tasks_private', 'Manifest.json'), 'Manifest.json')
        zf.write(os.path.join(settings.MEDIA_ROOT, 'tasks_private', 'index.html'), 'index.html')
        #zf.write(path(MEDIA_ROOT, 'private', 'jquery.min.js'), path("lib", 'jquery.min.js'))
        #zf.write(path(MEDIA_ROOT, 'private', 'functions.js'), path('lib', 'functions.js'))


        # Must close zip for all contents to be written
        zf.close()

        # Grab ZIP file from in-memory, make response with correct MIME-type
        resp = HttpResponse(s.getvalue(), content_type = "application/zip")
        # ..and correct content-disposition
        resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
        #if True: return render_to_response("api/task_interactive.html",  locals())
        return resp

        #return HttpResponse(str(current_task_interactive_translated_answer_values))
    else:
        return HttpResponse('Please submit a valid task ID and a valid language locale code')

#TODO: add pager
def parameters(request):
    age_groups = AgeGroup.objects.all()
    difficultys = DifficultyLevel.objects.all()
    categories = Category.objects.all()

    return render_to_response("control-panel/parameters.html", locals(), context_instance = RequestContext( request ) )

# Age groups
def edit_age_group( request, id ):
  ag = AgeGroup.objects.get( id = id )
  if request.method == 'POST':
      form = forms.AgeGroupForm( request.POST, instance = ag )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.age_groups" )
  else:
      form = forms.AgeGroupForm( instance = ag )
  return render_to_response("control-panel/edit-age-group.html", locals(), context_instance = RequestContext( request ) )

def new_age_group( request ):
  if request.method == 'POST':
      form = forms.AgeGroupForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.age_groups" )
  else:
      form = forms.AgeGroupForm()
  return render_to_response("control-panel/edit-age-group.html", locals(), context_instance = RequestContext( request ) )

def delete_age_group( request, id ):
  AgeGroup.objects.get( id = id ).delete()
  return redirect( "control_panel.age_groups" )

# Categories
def edit_category( request, id ):
  category = Category.objects.get( id = id )
  if request.method == 'POST':
      form = forms.CategoryForm( request.POST, instance = category )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.categories" )
  else:
      form = forms.CategoryForm( instance = category )
  return render_to_response("control-panel/edit-category.html", locals(), context_instance = RequestContext( request ) )

def new_category( request ):
  if request.method == 'POST':
      form = forms.CategoryForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.categories" )
  else:
      form = forms.CategoryForm()
  return render_to_response("control-panel/edit-category.html", locals(), context_instance = RequestContext( request ) )

def delete_category( request, id ):
  Category.objects.filter( id = id ).delete()
  return redirect( "control_panel.categories" )

# Difficulties
def edit_difficulty( request, id ):
  difficulty = DifficultyLevel.objects.get( id = id )
  if request.method == 'POST':
      form = forms.DifficultyForm( request.POST, instance = difficulty )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.difficulty_levels" )
  else:
      form = forms.DifficultyForm( instance = difficulty )
  return render_to_response("control-panel/edit-difficultys.html", locals(), context_instance = RequestContext( request ) )

def new_difficulty( request ):
  if request.method == 'POST':
      form = forms.DifficultyForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "control_panel.difficulty_levels" )
  else:
      form = forms.DifficultyForm()
  return render_to_response("control-panel/edit-difficultys.html", locals(), context_instance = RequestContext( request ) )

def delete_difficulty( request, id ):
  DifficultyLevel.objects.get( id = id ).delete()
  return redirect( "control_panel.difficulty_levels" )

# User management
@login_required()
def static_html( request, page ):
    return render_to_response( page, context_instance = RequestContext( request ) )

@login_required()
def index( request ):
    user = request.user
    # user_profile = user.get_profile()
    # if True: return redirect("/list/"+user_profile.interface_lang_code)

    tasks=[]

    """

    ORDERING THE TASK LIST

    ""
    order_by = "timestamp"
    if request.method == "GET" and 'order' in request.GET:
        order = request.GET.get('order')
        order_translation_dict = {
            'title': 'title',
            'category': 'task__category__title',
            'age': 'task__agegroup__value',
            'description': 'body',
            'language': 'language_locale'}
        if order[0] == '-':
            direction = '-'
            order = order[1:]
        else:
            direction = ''
        order_by = direction + order_translation_dict.get(order, order)

    """
"""

    SEARCHING THE TASK LIST

    ""

    if request.method == "GET" and 'search' in request.GET:
        ""

        getting all the search values

        ""

        q_obj= Q()

        if 't' in request.GET and request.GET['t'] != "":
            #if OR
            if request.GET['tc'] == "1":
                q_obj |= Q(title__icontains=request.GET['t'])
            #IF AND
            elif request.GET['tc'] == "2":
                q_obj &= Q(title__icontains=request.GET['t'])
        if 'ca' in request.GET and request.GET['ca'] != "":
            #IF MORE THAN 1 VALUE
            if len(request.GET.getlist('ca')) > 1:
                #IF OR
                if request.GET['cac'] == "1":
                    category=request.GET.getlist('ca')
                    for c in category:
                        q_obj |= Q(task__category__title__icontains=c)
                #IF AND
                elif request.GET['cac'] == "2":
                    category=request.GET.getlist('ca')
                    for c in category:
                        q_obj &= Q(task__category__title__icontains=c)
            #IF 1 VALUE
            else:
                #IF OR
                if request.GET['cac'] == "1":
                    category=request.GET['ca']
                    q_obj |= Q(task__category__title__icontains=category)
                #IF AND
                elif request.GET['cac'] == "2":
                    category=request.GET['ca']
                    q_obj &= Q(task__category__title__icontains=category)
        if 'a' in request.GET and request.GET['a'] != "":
            #IF MORE THAN 1 VALUE
            if len(request.GET.getlist('a')) > 1:
                #IF OR
                if request.GET['ac'] == "1":
                    category=request.GET.getlist('ca')
                    for c in category:
                        q_obj |= Q(task__agegroup__value__icontains=c)
                #IF AND
                elif request.GET['ac'] == "2":
                    category=request.GET.getlist('a')
                    for c in category:
                        q_obj &= Q(task__agegroup__value__icontains=c)
            #IF 1 VALUE
            else:
                #IF OR
                if request.GET['ac'] == "1":
                    category=request.GET['a']
                    q_obj |= Q(task__agegroup__value__icontains=category)
                #IF AND
                elif request.GET['ac'] == "2":
                    category=request.GET['a']
                    q_obj &= Q(task__agegroup__value__icontains=category)
        if 'desc' in request.GET and request.GET['desc'] != "":
            #if OR
            if request.GET['dc'] == "1":
                q_obj |= Q(body__icontains=request.GET['desc'])
            #IF AND
            elif request.GET['dc'] == "2":
                q_obj &= Q(body__icontains=request.GET['desc'])
        if 'l' in request.GET and request.GET['l'] != "":
            #IF MORE THAN 1 VALUE
            if len(request.GET.getlist('l')) > 1:
                #IF OR
                if request.GET['lc'] == "1":
                    category=request.GET.getlist('la')
                    for c in category:
                        q_obj |= Q(language_locale__icontains=c)
                #IF AND
                elif request.GET['lc'] == "2":
                    category=request.GET.getlist('l')
                    for c in category:
                        q_obj &= Q(language_locale__icontains=c)
            #IF 1 VALUE
            else:
                #IF OR
                if request.GET['lc'] == "1":
                    category=request.GET['l']
                    q_obj |= Q(language_locale__icontains=category)
                #IF AND
                elif request.GET['lc'] == "2":
                    category=request.GET['l']
                    q_obj &= Q(language_locale__icontains=category)
        elif 'searchFull' in request.GET and request.GET['searchFull']!="":
            s = request.GET['searchFull']
            q = Q(tasktranslation__language_locale__icontains=s) | Q(tasktranslation__body__icontains=s) | Q(category__title__icontains=s) | Q(agegroup__value__icontains=s) | Q(tasktranslation__title__icontains=s)
            tasks = Task.objects.filter(q)
        else:
            messages.error(request, _("No search field filled."))
        tasks_translations = TaskTranslation.objects.select_related().filter(q_obj).order_by(order_by)

    #we are not searching, display all tasks
    else:
        #tasks_translations = Task.objects.select_related('tasktranslation').filter(parent_id=None).order_by(order_by)
        tasks = Task.objects.order_by('created_at')

    paginator = Paginator( tasks, 5 )
    page = request.GET.get( 'page' )
    categories = Category.objects.values('title').distinct()
    age = AgeGroup.objects.values('value').distinct()
    all_languages = settings.LANGUAGES

    try:
        tasks = paginator.page( page )
    except PageNotAnInteger:
        tasks = paginator.page( 1 )
    except EmptyPage:
        tasks = paginator.page( paginator.num_pages )

    #tasks_translations = TaskTranslation.objects.filter(language_locale=language).order_by(order_by)

    return render_to_response("index.html", locals(), context_instance = RequestContext( request ) )
"""

@login_required

#def tasks_list_language(request, language_locale = None):
    #language = language_locale
    #languages = settings.LANGUAGES
    #all_task_translations = TaskTranslation.objects.all()
    #if language:
        #all_task_translations = task_translations.filter(
            #language_locale = language_locale)
    #all_task_translation = all_task_translations.order_by('task', '-version')
    #task_translations = []
    #prev_task = None
    # collect the tasks with largest versions
    #for translation in all_task_translations:
        #if prev_task != translation.task:
            #task_translations.append(translation)
        #prev_task = translation.task
    #return render(request, "bober_tasks/list.html", locals())

def tasks_list_language(request, language_locale):
    queryset = TaskTranslation.objects.select_related().all()
    f = TaskFilter(request.GET, queryset=queryset)
    table = TaskTable(f.qs)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, "bober_tasks/list.html", {'table': table})

@login_required
def tasks_upload(request, id=0):
    task_translation = TaskTranslation.objects.get(id = id)

    # Clean and add version information to filename (for conflict avoid)
    filetype = "." + str(request.FILES.get('images')).split(".")[-1]
    filename = "".join(str(request.FILES.get('images')).split(".")[:-1])
    rx = re.compile('\W+')
    filename = rx.sub('_', filename).strip()
    filename = filename + "_v" + str(task_translation.version)
    file = filename +filetype
    urlpath = 'resources/'
    handle_uploaded_file(request.FILES.get('images'), file, task_translation)
    return HttpResponse(to_json({'status': 'ok', 'filename': file, 'filepath': urlpath }))

def export_multiple_tasks(request):
    export_values = request.POST.getlist('taskValues')
    for i in range(len(export_values)):
        #TaskTranslation.export_to_simple_competition(export_values[i])
        t = TaskTranslation.objects.get(pk=export_values[i])
        t.export_to_simple_competition()

    return redirect("/tasks")


def handle_uploaded_file(f,name, task_translation):
    #save_path  = path( MEDIA_ROOT , 'taskresources', 'Image', task_id , task_language )
    save_path  = os.path.join(settings.MEDIA_ROOT, 'task', str(task_translation.task_id) , str(task_translation.language_locale), 'resources' )
    # Check if upload folder of a specific task already exists and create it, if it doesn't.
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Write file to disk
    with open(os.path.join(save_path, name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Write filename to DB
    resource = Resources(filename = name, type = "image", task = task_translation.task, language = task_translation.language_locale)
    resource.save()

    return save_path



#TODO fix this!
@login_required()
def tasks_translate(request, id):
    all_languages = settings.LANGUAGES
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task
    answer_multiple_choice = task_translation.answer_set
    categories = task.categories.all()
    task_age_groups = AgeGroupTask.objects.filter(task_id=task.id)
    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        language = request.POST['language']
        solution = request.POST['solution']
        comment = request.POST['diff']
        correctness = request.POST['correctness']
        it_is_informatics = request.POST['informatics']

        answers = get_answers(request.POST)
        age_groups = get_age_groups(request.POST)
        categories = get_categories(request.POST)

        new_trans = TaskTranslation(title=title, body=body, solution=solution,
                                           task_id=task.id, language_locale=language,
                                           it_is_informatics=it_is_informatics, comment=comment)


        new_trans.save()

        for i in range(0, 4):
            answers[i].trans_id = new_trans.id
            answers[i].save()
            if int(i) == int(correctness):
                new_trans.correct_answer_id = answers[i].id

        new_trans.save()



        return redirect(reverse('/show/' + str(task.id) + '?language=' + str(language)))

    return render_to_response("task/translate.html", locals(), context_instance=RequestContext(request))


@login_required()
def tasks_new_from(request, id):
    parent_id = None
    all_languages = settings.LANGUAGES

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        language = request.POST['language']
        solution = request.POST['solution']
        comment = request.POST['diff']
        correctness = request.POST['correctness']
        it_is_informatics = request.POST['informatics']

        answers = get_answers(request.POST, language)
        age_groups = get_age_groups(request.POST)
        categories = get_categories(request.POST)

        new_task = Task(parent_id=parent_id, author=request.user)
        new_task.save()

        for category_id in categories:
            c = Category.objects.get(id=categories[category_id])
            new_task.categories.add(c)

        new_task.save()

        answer_multiple_choice = Answer(task_id=new_task.id, correctness=(int(correctness) + 1))
        answer_multiple_choice.save()

        for i in range(0, 4):
            answers[i].answer_multiple_choice_id = answer_multiple_choice.id
            answers[i].save()

        for i in range(0, len(age_groups)):
            age_groups[i].task_id = new_task.id
            age_groups[i].save()

        national_problem = TaskTranslation(title=title, body=body, solution=solution,
                                           task_id=new_task.id, language_locale=language,
                                           it_is_informatics=it_is_informatics, comment=comment)
        national_problem.save()

        return redirect('/show/' + str(new_task.id))

    task = Task.objects.get(id=id)
    task_translation = TaskTranslation.objects.filter(task_id=id)
    task_translation = task_translation[0]

    answers = Answer.objects.filter(task_id=id)

    answers_id = map(lambda answer: answer.id, answers)
    answer_multiple_choice = \
        AnswerTranslation.objects.filter(answer_multiple_choice_id__in=answers_id,
            language_locale=task_translation.language_locale)
    task_categories = task.categories.all()
    task_age_groups = AgeGroupTask.objects.filter(task_id=task.id)

    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()

    return render_to_response("task/edit.html", locals(), context_instance=RequestContext(request))


@login_required()
def tasks_history(request, id):
    language = False
    if request.GET.get('language'):
        language = request.GET.get('language')

    tasks = Task.objects.filter(Q(id=id) | Q(parent_id=id))

    tasks_id = map(lambda task: task.id, tasks)
    all_task_translations = TaskTranslation.objects.filter(task_id__in=tasks_id)
    all_languages = all_task_translations.values('language_locale', flat=True).distinct()
    if not language:
        language = all_languages[0]

    task_translations = TaskTranslation.objects.filter(task_id__in=tasks_id, language_locale=language)

    return render_to_response("task/history.html", locals(), context_instance=RequestContext(request))

def tasktranslation_render(request, pk): # loads template with context data and returns it as a file
    tt = get_object_or_404(TaskTranslation, pk=pk)
    return HttpResponse(tt.render_to_string(), "text/html")
    # return codecs.open(os.path.join(settings.MEDIA_DIR, 'tasks_private') + filename, 'w', 'utf-8').write(render_to_string(template, template_data, context)) # save file to 'private folder'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'bober_tasks/task_detail.html'

class TaskTranslationUpdate(UpdateWithInlinesView, LoginRequiredMixin):
    model = TaskTranslation
    form_class = forms.TaskTranslationForm
    template_name = 'bober_tasks/tasktranslation_form.html'
    inlines = [ forms.AnswerInline ]
    def get_success_url(self):
        return reverse('tasktranslation_preview', kwargs = {'pk': self.object.pk})
    def get(self, request, *args, **kwargs):
        self.remark_form = forms.InlineRemarkForm()
        return super(TaskTranslationUpdate, self).get(request, *args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super(TaskTranslationUpdate, self).get_form_kwargs()
        return kwargs
    def get_context_data(self, *args, **kwargs):
        context = super(TaskTranslationUpdate, self).get_context_data(*args, **kwargs)
        context['remark_form'] = self.remark_form
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.remark_form = forms.InlineRemarkForm(self.request.POST)
        if self.remark_form.is_valid():
            return super(TaskTranslationUpdate, self).post(request, *args, **kwargs)
        inlines = self.construct_inlines()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.forms_invalid(form, inlines)
    def save(self, *args, **kwargs):
        print "saving", args, kwargs
        self.remark_form.save()
        return super(TaskTranslationUpdate, self).save(*args, **kwargs)

class TaskTranslationPreview(DetailView, LoginRequiredMixin):
    model = TaskTranslation
    template_name = 'bober_tasks/tasktranslation_preview.html'

class TaskTranslationDetail(DetailView, LoginRequiredMixin):
    model = TaskTranslation
    template_name = 'bober_tasks/tasktranslation_detail.html'

@login_required()
def edit_task(request, id):
    language_disabled = True
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task

    if task.parent_id:
        parent_id = task.parent_id
    else:
        parent_id = task.id
    request.session['task_id_variable'] = id
    request.session['language_locale_variable'] = task_translation.language_locale
    answers = task_translation.answer_set.all()
    task_age_groups = AgeGroupTask.objects.filter(task_id=task.id)
    all_languages = settings.LANGUAGES
    return render(request, "task/edit.html", locals())

class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = 'bober_tasks/task_form.html'
    form_class = forms.TaskForm
    def get_success_url(self):
        first_translation = TaskTranslation(task = self.object,
            language_locale = self.cleaned_data['language_locale'])
        first_translation.save()
        first_translation.create_default_answers()
        return reverse('tasktranslation_update', kwargs={'pk': first_translation.pk})
    def form_valid(self, form):
        self.cleaned_data = form.cleaned_data
        return super(TaskCreate, self).form_valid(form)

@login_required()
def save_task(request):
    if request.method == 'GET':
        redirect("/")
    task = Task.objects.get(id=request.POST['id'])
    i = 0
    categories = {}
    try:
        while True:
            categories[i] = request.POST["category[" + str(i) + "]"]
            i += 1
    except Exception, e:
        True
    for category_id in categories:
        c = Category.objects.get(id=categories[category_id])
        task.categories.add(c)

    i = 0
    groups = []
    try:
        while True:
            temp = request.POST.getlist("age_group[" + str(i) + "]")
            if len(temp) < 1:
                break
            agt = AgeGroupTask.objects.get_or_create(age_group_id=temp[0], difficulty_level_id=temp[1], task=task)
            agt.save()
            i += 1
    except Exception, e:
        pass
    return redirect("tasks.task", task.id)

@login_required
def tasktranslation_clone(request, pk):
    t = get_object_or_404(TaskTranslation, id = pk)
    t.author = request.user
    t.save_new_version()
    return redirect("tasktranslation_update", pk = t.id)

@login_required
def export_to_simple_competition(request, pk):
    #if request.method == 'GET':
    #    return redirect("/")
    tt = get_object_or_404(TaskTranslation, id=pk)
    tt.export_to_simple_competition()
    return redirect("tasktranslation_detail", pk = pk)

@login_required
def tasks_save_translation(request):
    if request.method == 'GET':
        return redirect("/")
    if request.method == 'POST':
        if request.POST.has_key('id'): # Updating object
            id = request.POST['id']
            task_translation = TaskTranslation.objects.get(id=request.POST['id'])
            old_task_translation = TaskTranslation.objects.get(id=request.POST['id'])
            if not task_translation.title:
                old_task_translation.delete()
                task_translation.save()
            else:
                task_translation.save_new_version()
            # Delete if no title

        else: # New task
            task = Task()
            task.save()
            task_translation = TaskTranslation(task = task)
            task_translation.language_locale = request.POST['language']
            task_translation.save()

        task_translation.title = request.POST['title']
        task_translation.body = request.POST['body']
        task_translation.solution = request.POST['solution']
        task_translation.comment = request.POST['diff']
        task_translation.it_is_informatics = request.POST['informatics']

        for i in range(0, 4):
            post_answer = request.POST.getlist("answer[" + str(i) + "]")
            answer = Answer(value=post_answer[0])
            answer.task_translation = task_translation
            answer.save()
            if int(i) == int(request.POST['correctness']):
                task_translation.correct_answer = answer

        task_translation.save()



    return redirect('tasks.display', task_translation.id)


@login_required()
def delete_task(request, id):
    task = Task.objects.get(id=id)
    print task
    answers = Answer.objects.filter(task_id=id)
    answers_id = map(lambda answer: answer.id, answers)
    answer_multiple_choice = AnswerTranslation.objects.filter(answer_multiple_choice_id__in=answers_id)
    if task.parent_id is None:
        task.delete()
        TaskTranslation.objects.filter(id=id).delete()
        answers.delete()
        for answer in answer_multiple_choice:
            answer.delete()
    else:
        task.delete()
        TaskTranslation.objects.filter(id=id).delete()
        answers.delete()
        answer_multiple_choice.delete()
        for t in Task.objects.filter(parent_id=id):
            t.delete()
            TaskTranslation.objects.filter(task_id=t.id).delete()
            answers = Answer.objects.filter(task_id=t.id)
            answers_id = map(lambda answer: answer.id, answers)
            answer_multiple_choice = AnswerTranslation.objects.filter(answer_multiple_choice_id__in=answers_id)
            answers.delete()
            answer_multiple_choice.delete()

    return redirect('/')


@login_required()
def display_task(request, id):
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task
    answers = task_translation.answer_set.all()
    correct = str(task_translation.correct_answer.id)
    languages = task.available_languages
    versions = TaskTranslation.objects.filter(task = task, language_locale = task_translation.language_locale).order_by("-version")

    return render_to_response("task/display.html", locals(), context_instance=RequestContext(request))


@login_required()
def task_detail(request, id):
    task = Task.objects.get(id=id)
    task_categories = task.categories.all()
    task_age_groups = task.age_group_categories()

    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()

    return render_to_response("task/details.html", locals(), context_instance=RequestContext(request))


def tasks_resource(request, id, file):
    """Image path redirect for task display. Because images have relative paths for export."""
    task_translation = TaskTranslation.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, 'task', str(task_translation.task_id) , task_translation.language_locale, 'resources', file )
    image_data = open(file_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def get_age_groups(obj):
    i = 0;
    groups = []
    try:
        while True:
            temp = obj.getlist("age_group[" + str(i) + "]")
            groups[i] = AgeGroupTask(age_group_id=temp[0], difficulty_level_id=temp[1], task=tas)
            if len(temp) < 1:
                break
            i += 1
        return groups
    except Exception, e:
        return groups


def get_answers(obj):
    answers = []
    for i in range(0, 4):
        temp = obj.getlist("answer[" + str(i) + "]")
        answers[i] = Answer(value=temp[0])
    return answers


@login_required()
def get_categories(obj):
    i = 0;
    categories = {}
    try:
        while True:
            categories[i] = obj["category[" + str(i) + "]"]
            i += 1
    except Exception, e:
        return categories
