from application import forms
from application.models import *

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


#TODO: add pager
def parameters( request):
    age_groups = AgeGroup.objects.all()
    difficultys = DifficultyLevel.objects.all()
    categories = Category.objects.all()
    languages = Language.objects.all()

    return render_to_response("control-panel/parameters.html", locals(), context_instance = RequestContext( request ) )

# Age groups
def edit_age_group( request, id ):
  ag = AgeGroup.objects.get( id = id )
  if request.method == 'POST':
      form = forms.AgeGroupForm( request.POST, instance = ag )
      if form.is_valid():
        form.save()
        return redirect( "/age-groups/" )
  else:
      form = forms.AgeGroupForm( instance = ag )
  return render_to_response("control-panel/edit-age-group.html", locals(), context_instance = RequestContext( request ) )

def new_age_group( request ):
  if request.method == 'POST':
      form = forms.AgeGroupForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "/age-groups/" )
  else:
      form = forms.AgeGroupForm()
  return render_to_response("control-panel/edit-age-group.html", locals(), context_instance = RequestContext( request ) )

def delete_age_group( request, id ):
  AgeGroup.objects.get( id = id ).delete()
  return redirect( "/age-groups/" )

# Categories
def edit_category( request, id ):
  category = Category.objects.get( id = id )
  if request.method == 'POST':
      form = forms.CategoryForm( request.POST, instance = category )
      if form.is_valid():
        form.save()
        return redirect( "/categories/" )
  else:
      form = forms.CategoryForm( instance = category )
  return render_to_response("control-panel/edit-category.html", locals(), context_instance = RequestContext( request ) )

def new_category( request ):
  if request.method == 'POST':
      form = forms.CategoryForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "/categories/" )
  else:
      form = forms.CategoryForm()
  return render_to_response("control-panel/edit-category.html", locals(), context_instance = RequestContext( request ) )

def delete_category( request, id ):
  Category.objects.filter( id = id ).delete()
  return redirect( "/categories/" )

# Difficulties
def edit_difficulty( request, id ):
  difficulty = DifficultyLevel.objects.get( id = id )
  if request.method == 'POST':
      form = forms.DifficultyForm( request.POST, instance = difficulty )
      if form.is_valid():
        form.save()
        return redirect( "/difficulty-levels/" )
  else:
      form = forms.DifficultyForm( instance = difficulty )
  return render_to_response("control-panel/edit-difficultys.html", locals(), context_instance = RequestContext( request ) )

def new_difficulty( request ):
  if request.method == 'POST':
      form = forms.DifficultyForm( request.POST )
      if form.is_valid():
        form.save()
        return redirect( "/difficulty-levels/" )
  else:
      form = forms.DifficultyForm()
  return render_to_response("control-panel/edit-difficultys.html", locals(), context_instance = RequestContext( request ) )

def delete_difficulty( request, id ):
  DifficultyLevel.objects.get( id = id ).delete()
  return redirect( "/difficulty-levels/" )

# Languages
def new_language(request):
  if request.method == 'POST':
      form = forms.LanguageForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect( "/languages/" )
  else:
      form = forms.LanguageForm()
  return render_to_response("control-panel/edit-language.html", locals(), context_instance = RequestContext( request ) )

def edit_language(request, id):
  language = Language.objects.get(id = id)
  if request.method == 'POST':
      form = forms.LanguageForm(request.POST, instance = language)
      if form.is_valid():
        form.save()
        return redirect("/languages/")
  else:
      form = forms.LanguageForm(instance = language )
  return render_to_response("control-panel/edit-language.html", locals(), context_instance = RequestContext( request ) )

def delete_language(request, id):
  Language.objects.get(id = id).delete()
  return redirect("/languages/")

# User management
@login_required()
def users( request ):
    users = User.objects.all()
    return render_to_response("control-panel/users.html", locals(), context_instance = RequestContext( request ) )


