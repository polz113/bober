from django.conf import settings
from django.shortcuts import \
    redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.loader import render_to_string
from django.template.context import RequestContext
from bober_tasks.helper import *
import codecs
import re
import os
from django.views.generic import DetailView, CreateView
from django_tables2 import RequestConfig
from bober_tasks.tables import TaskTable
from bober_tasks.filters import TaskFilter
from extra_views import UpdateWithInlinesView
from braces.views import LoginRequiredMixin
from json import dumps as to_json
from django.http import HttpResponse
from bober_tasks import forms
from django.utils.text import slugify
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.decorators.clickjacking import xframe_options_sameorigin
import mimetypes
from bober_tasks.models import Answer, TaskTranslation, AgeGroupTask, Task,\
    Resources


# loads template with context data and returns it as a file
def render_to_file(template, filename, template_data, context):
    path = os.path.join(settings.MEDIA_DIR, 'tasks_private') + filename
    tp = codecs.open(path, 'w', 'utf-8').write(
        render_to_string(template, template_data, context))
    return tp


def export_task_language_version(request, task_id, language_code, version):
    task_translation = TaskTranslation.objects.get(
        language_locale=language_code, task_id=task_id, version=version)
    return export_task_translation(request, task_translation)


def export_task_language(request, task_id, language_code):
    task = Task.objects.get(id=task_id)
    task_translation = task.get_latest_translation(language_code)
    return export_task_translation(request, task_translation)


@permission_required('bober_tasks.view_tasktranslation')
def export_task_translation(request, pk):
    task_translation = TaskTranslation.objects.get(pk=pk)
    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(task_translation.as_zip(), content_type="application/zip")
    # ..and correct content-disposition
    zip_filename = '{}-{}_{}_v{}.zip'.format(
        slugify(task_translation.title),
        task_translation.task_id, task_translation.language_locale,
        task_translation.version)
    resp['Content-Disposition'] = 'attachment; filename={}'.format(zip_filename)
    return resp


# TODO: add pager
def parameters(request):
    age_groups = AgeGroup.objects.all()
    difficultys = DifficultyLevel.objects.all()
    categories = Category.objects.all()
    return render(request, "control-panel/parameters.html", locals(), context_instance=RequestContext(request))


# Age groups
def edit_age_group(request, id):
    ag = AgeGroup.objects.get(id=id)
    if request.method == 'POST':
        form = forms.AgeGroupForm(request.POST, instance=ag)
        if form.is_valid():
            form.save()
            return redirect("control_panel.age_groups")
    else:
        form = forms.AgeGroupForm(instance=ag)
    return render(request, 
        "control-panel/edit-age-group.html",
        locals(),
        context_instance=RequestContext(request)
    )


def new_age_group(request):
    if request.method == 'POST':
        form = forms.AgeGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control_panel.age_groups")
    else:
        form = forms.AgeGroupForm()
    return render(request, 
        "control-panel/edit-age-group.html", locals(),
        context_instance=RequestContext(request))


def delete_age_group(request, id):
    AgeGroup.objects.get(id=id).delete()
    return redirect("control_panel.age_groups")


# Categories
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("control_panel.categories")
    else:
        form = forms.CategoryForm(instance=category)
    return render(request, "control-panel/edit-category.html", locals(), context_instance=RequestContext(request))


def new_category(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control_panel.categories")
    else:
        form = forms.CategoryForm()
    return render(request, "control-panel/edit-category.html", locals(), context_instance=RequestContext(request))


def delete_category(request, id):
    Category.objects.get(pk=id).delete()
    return redirect("control_panel.categories")


# Difficulties
def edit_difficulty(request, id):
    difficulty = DifficultyLevel.objects.get(id=id)
    if request.method == 'POST':
        form = forms.DifficultyForm(request.POST, instance=difficulty)
        if form.is_valid():
            form.save()
            return redirect("control_panel.difficulty_levels")
    else:
        form = forms.DifficultyForm(instance=difficulty)
    return render(request, "control-panel/edit-difficultys.html", locals(),
                              context_instance=RequestContext(request))


def new_difficulty(request):
    if request.method == 'POST':
        form = forms.DifficultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control_panel.difficulty_levels")
    else:
        form = forms.DifficultyForm()
    return render(request, "control-panel/edit-difficultys.html", locals(),
                              context_instance=RequestContext(request))


def delete_difficulty(request, id):
    DifficultyLevel.objects.get(pk=id).delete()
    return redirect("control_panel.difficulty_levels")


@login_required()
@permission_required('bober_tasks.view_tasktranslation')
def tasks_list_language(request, language_locale=None):
    queryset = TaskTranslation.objects.select_related().all()
    f = TaskFilter(request.GET, queryset=queryset)
    table = TaskTable(f.qs)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, "bober_tasks/list.html", {'table': table})

@xframe_options_sameorigin
@login_required()
@permission_required('bober_tasks.change_tasktranslation')
def tasks_upload(request, id=0):
    task_translation = TaskTranslation.objects.get(pk=id)

    # Clean and add version information to filename (for conflict avoid)
    filetype = "." + str(request.FILES.get('images')).split(".")[-1]
    filename = "".join(str(request.FILES.get('images')).split(".")[:-1])
    rx = re.compile('\W+')
    filename = rx.sub('_', filename).strip()
    filename = filename + "_v" + str(task_translation.version)
    file = filename + filetype
    urlpath = 'resources/'
    handle_uploaded_file(request.FILES.get('images'), file, task_translation)
    return HttpResponse(to_json({'status': 'ok', 'filename': file, 'filepath': urlpath}))


@permission_required('bober_tasks.view_tasktranslation')
def export_multiple_tasks(request):
    export_values = request.POST.getlist('taskValues')
    for i in range(len(export_values)):
        t = TaskTranslation.objects.get(pk=export_values[i])
        t.export_to_simple_competition(rebuild_caches=True)
    return redirect("/tasks")


def handle_uploaded_file(f, name, task_translation):
    save_path = os.path.join(
        settings.MEDIA_ROOT, 'task', str(task_translation.task_id),
        str(task_translation.language_locale), 'resources')
    # Check if upload folder of a specific task already exists and create it, if it doesn't.
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Write file to disk
    with open(os.path.join(save_path, name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Write filename to DB
    resource = Resources(filename=name, type="image", task=task_translation.task,
                         language=task_translation.language_locale)
    resource.save()

    return save_path


# TODO: fix this!
@permission_required('bober_tasks.add_tasktranslation')
@login_required()
def tasks_translate(request, id):
    all_languages = settings.LANGUAGES
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task
    answer_multiple_choice = task_translation.answer_set
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        language = request.POST['language']
        solution = request.POST['solution']
        comment = request.POST['diff']
        correctness = request.POST['correctness']
        it_is_informatics = request.POST['informatics']

        answers = get_answers(request.POST)
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
    return render(request, "task/translate.html", locals(), context_instance=RequestContext(request))


@permission_required('bober_tasks.add_tasktranslation')
@login_required()
def tasks_new_from(request, id):
    task = get_object_or_404(Task, pk=id)
    translation0 = TaskTranslation(task_id=id)
    translation0.save()
    return task_translate(request, translation0.id)


@permission_required('bober_tasks.view_tasktranslation')
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

    return render(request, "task/history.html", locals(), context_instance=RequestContext(request))


@permission_required('bober_tasks.view_tasktranslation')
def tasktranslation_render(request, pk):  # loads template with context data and returns it as a file
    tt = get_object_or_404(TaskTranslation, pk=pk)
    return HttpResponse(tt.render_to_string(), "text/html")


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'bober_tasks/task_detail.html'


class TaskTranslationUpdate(PermissionRequiredMixin, UpdateWithInlinesView, LoginRequiredMixin):
    model = TaskTranslation
    form_class = forms.TaskTranslationForm
    template_name = 'bober_tasks/tasktranslation_form.html'
    inlines = [forms.AnswerInline]
    permission_required = ('bober_tasks.change_tasktranslation')

    def get_success_url(self):
        return reverse('tasktranslation_detail', kwargs={'pk': self.object.pk})

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
        print("saving", args, kwargs)
        self.remark_form.save()
        return super(TaskTranslationUpdate, self).save(*args, **kwargs)


class TaskTranslationPreview(PermissionRequiredMixin, DetailView, LoginRequiredMixin):
    model = TaskTranslation
    template_name = 'bober_tasks/tasktranslation_preview.html'
    permission_required = ('bober_tasks.view_tasktranslation')


class TaskTranslationDetail(PermissionRequiredMixin, DetailView, LoginRequiredMixin):
    model = TaskTranslation
    template_name = 'bober_tasks/tasktranslation_detail.html'
    permission_required = ('bober_tasks.view_tasktranslation')


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


class TaskCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'bober_tasks/task_form.html'
    form_class = forms.TaskForm
    permission_required = ('bober_tasks.add_tasktranslation')

    def get_success_url(self):
        first_translation = TaskTranslation(
            task=self.object,
            language_locale=self.cleaned_data['language_locale'])
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
    except Exception as e:
        # TODO: handle exception
        True
    for category_id in categories:
        c = Category.objects.get(id=categories[category_id])
        task.categories.add(c)
    i = 0
    try:
        while True:
            temp = request.POST.getlist("age_group[" + str(i) + "]")
            if len(temp) < 1:
                break
            agt = AgeGroupTask.objects.get_or_create(age_group_id=temp[0], difficulty_level_id=temp[1], task=task)
            agt.save()
            i += 1
    except Exception as e:
        # TODO: handle exception
        pass
    return redirect("tasks.task", task.id)


@login_required
@permission_required('bober_tasks.add_tasktranslation')
def tasktranslation_clone(request, pk):
    t = get_object_or_404(TaskTranslation, pk=pk)
    t.author = request.user
    t.save_new_version()
    return redirect("tasktranslation_update", pk=t.id)


@login_required
@permission_required('bober_tasks.view_tasktranslation')
def export_to_simple_competition(request, pk):
    tt = get_object_or_404(TaskTranslation, id=pk)
    tt.export_to_simple_competition()
    return redirect("tasktranslation_detail", pk=pk)


@login_required
@permission_required('bober_tasks.view_tasktranslation')
def tasks_save_translation(request):
    if request.method == 'GET':
        return redirect("/")
    if request.method == 'POST':
        if 'id' in request.POST:  # Updating object
            task_translation = TaskTranslation.objects.get(id=request.POST['id'])
            old_task_translation = TaskTranslation.objects.get(id=request.POST['id'])
            if not task_translation.title:
                old_task_translation.delete()
                task_translation.save()
            else:
                task_translation.save_new_version()
            # Delete if no title

        else:  # New task
            task = Task()
            task.save()
            task_translation = TaskTranslation(task=task)
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
@permission_required('bober_tasks.view_tasktranslation')
def display_task(request, id):
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task
    answers = task_translation.answer_set.all()
    correct = str(task_translation.correct_answer.id)
    languages = task.available_languages
    versions = TaskTranslation.objects.filter(
        task=task, language_locale=task_translation.language_locale).order_by("-version")
    return render(request, "task/display.html", locals(), context_instance=RequestContext(request))


@login_required()
@permission_required('bober_tasks.view_tasktranslation')
def task_detail(request, id):
    task = Task.objects.get(id=id)
    task_categories = task.categories.all()
    task_age_groups = task.age_group_categories()

    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()

    return render(request, "task/details.html", locals(), context_instance=RequestContext(request))


@permission_required('bober_tasks.view_tasktranslation')
@login_required()
def tasks_resource(request, pk, filename):
    """Image path redirect for task display. Because images have relative paths for export."""
    # TODO: check permissions
    task_translation = TaskTranslation.objects.get(pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, 'task', str(task_translation.task_id),
                             task_translation.language_locale, 'resources', filename)
    image_data = open(file_path, "rb").read()
    content_type = mimetypes.guess_type(file_path, strict=False)[0]
    return HttpResponse(image_data, content_type)


def get_age_groups(obj):
    i = 0
    groups = []
    try:
        while True:
            temp = obj.getlist("age_group[" + str(i) + "]")
            groups[i] = AgeGroupTask(age_group_id=temp[0], difficulty_level_id=temp[1], task=obj)
            if len(temp) < 1:
                break
            i += 1
        return groups
    except Exception as e:
        # TODO: handle exception
        return groups


def get_answers(obj):
    answers = []
    for i in range(0, 4):
        temp = obj.getlist("answer[" + str(i) + "]")
        answers[i] = Answer(value=temp[0])
    return answers


@login_required()
def get_categories(obj):
    i = 0
    categories = {}
    try:
        while True:
            categories[i] = obj["category[" + str(i) + "]"]
            i += 1
    except Exception as e:
        # TODO: log exception
        return categories
