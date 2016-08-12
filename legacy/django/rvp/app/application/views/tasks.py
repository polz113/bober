__author__ = 'Grega Pompe'

import re
import random

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
import os
from os.path import join as path
from application.models import *
from application.helper import all_ages, all_lang, all_cat, all_dif
from application.settings import *
from json import dumps as to_json

@login_required()
def list_language(request, language_locale):
    language = Language.objects.get(id = language_locale)
    languages = Language.objects.all()
    task_translations = TaskTranslation.objects.all()
    task_translations = language.current_tasks()
    return render_to_response("task/list.html", locals(), context_instance = RequestContext( request ) )


@login_required()
def upload(request, id=0):

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


def handle_uploaded_file(f,name, task_translation):
    #save_path  = path( SITE_ROOT , 'taskresources', 'Image', task_id , task_language )
    save_path  = path( SITE_ROOT , 'resources', 'task', str(task_translation.task_id) , task_translation.language_locale_id, 'resources' )

    # Check if upload folder of a specific task already exists and create it, if it doesn't.
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Write file to disk
    with open(path(save_path, name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Write filename to DB
    resource = Resources(filename = name, type = "image", task = task_translation.task, language = task_translation.language_locale)
    resource.save()

    return save_path


@login_required()
def translate(request, id):
    all_languages = all_lang()
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



        return redirect('/show/' + str(task.id) + '?language=' + str(language))

    return render_to_response("task/translate.html", locals(), context_instance=RequestContext(request))


@login_required()
def new_from(request, id):
    parent_id = None
    all_languages = all_lang()

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
    answer_multiple_choice = AnswerTranslation.objects.filter(answer_multiple_choice_id__in=answers_id,
                                                              language_locale=task_translation.language_locale)

    task_categories = task.categories.all()
    task_age_groups = AgeGroupTask.objects.filter(task_id=task.id)

    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()

    return render_to_response("task/edit.html", locals(), context_instance=RequestContext(request))


@login_required()
def history(request, id):
    language = False
    if request.GET.get('language'):
        language = request.GET.get('language')

    tasks = Task.objects.filter(Q(id=id) | Q(parent_id=id))

    tasks_id = map(lambda task: task.id, tasks)
    all_task_translations = TaskTranslation.objects.filter(task_id__in=tasks_id)
    all_languages = set(map(lambda task: task.language_locale, all_task_translations))
    all_languages = Language.objects.filter(id__in=all_languages)

    if not language:
        language = list(all_languages)[0].id

    task_translations = TaskTranslation.objects.filter(task_id__in=tasks_id, language_locale=language)



    return render_to_response("task/history.html", locals(), context_instance=RequestContext(request))


@login_required()
def edit(request, id):
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


    all_languages = Language.objects.all()

    return render_to_response("task/edit.html", locals(), context_instance=RequestContext(request))


@login_required()
def new(request, language):
    # Generate new task end edit it
    task = Task()
    task.save()
    task_translation = TaskTranslation(task = task)
    task_translation.language_locale_id = language
    task_translation.save()

    return redirect("tasks.edit", task_translation.id)
    #"/task/edit/"+str(task_translation.id))

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
        True

    return redirect("tasks.task", task.id)

@login_required()
def save_translation(request):
    if request.method == 'GET':
        redirect("/")

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
            task_translation.language_locale_id = request.POST['language']
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



    return redirect('/display/' + str(task_translation.id))


@login_required()
def delete(request, id):
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
def display(request, id):
    task_translation = TaskTranslation.objects.get(id=id)
    task = task_translation.task
    answers = task_translation.answer_set.all()
    correct = str(task_translation.correct_answer.id)
    languages = task.available_languages
    versions = TaskTranslation.objects.filter(task = task, language_locale = task_translation.language_locale).order_by("-version")

    return render_to_response("task/display.html", locals(), context_instance=RequestContext(request))


@login_required()
def task(request, id):
    task = Task.objects.get(id=id)
    task_categories = task.categories.all()
    task_age_groups = task.age_group_categories()

    content_categories = all_cat()
    age_groups = all_ages()
    difficulty_levels = all_dif()

    return render_to_response("task/details.html", locals(), context_instance=RequestContext(request))


def resource(request, id, file):
    """Image path redirect for task display. Because images have relative paths for export."""
    task_translation = TaskTranslation.objects.get(id=id)
    file_path = path( SITE_ROOT , 'resources', 'task', str(task_translation.task_id) , task_translation.language_locale_id, 'resources', file )
    image_data = open(file_path, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")


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
