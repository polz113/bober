from application.models import *
from django.db.models import Q
import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.contrib import auth, messages

@login_required()
def static_html( request, page ):
    return render_to_response( page, context_instance = RequestContext( request ) )

@login_required()
def index( request ):
    user = User.objects.get(id = request.user.id)
    user_profile = user.get_profile()
    if True: return redirect("/list/"+user_profile.interface_lang_code)

    tasks=[]

    """"

    ORDERING THE TASK LIST

    """
    order_by = "timestamp"
    if request.method == "GET" and 'order' in request.GET:
        order = request.GET.get('order')
        if order == 'title':
            order_by = 'title'
        elif order == '-title':
            order_by = '-title'
        elif order == 'category':
            order_by = 'task__category__title'
        elif order == '-category':
            order_by = '-task__category__title'
        elif order == 'age':
            order_by = 'task__agegroup__value'
        elif order == '-age':
            order_by = '-task__agegroup__value'
        elif order == 'description':
            order_by = 'body'
        elif order == '-description':
            order_by = '-body'
        elif order == 'language':
            order_by = 'language_locale'
        elif order == '-language':
            order_by = '-language_locale'


    """

    SEARCHING THE TASK LIST

    """

    if request.method == "GET" and 'search' in request.GET:
        """

        getting all the search values

        """

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
    all_languages = Language.objects.all()

    try:
        tasks = paginator.page( page )
    except PageNotAnInteger:
        tasks = paginator.page( 1 )
    except EmptyPage:
        tasks = paginator.page( paginator.num_pages )

    #tasks_translations = TaskTranslation.objects.filter(language_locale=language).order_by(order_by)

    return render_to_response("index.html", locals(), context_instance = RequestContext( request ) )
