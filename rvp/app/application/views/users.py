from application import forms
from application import settings
from application.models import Task
from django.core.validators import email_re
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils.translation import ugettext as _

@login_required()
def logout( request ):
    auth.logout( request )

    messages.success(request, _("You have been logged out."))

    return redirect('index')

def login( request ):

    # if user is alreday authenticated
    if request.user.is_authenticated():
        messages.info(request, _("You are already logged in."))
        return redirect("index")

    # try to login user
    if request.POST:

        # Check if parameter username is not empty and if exists
        if ('username' in request.POST and request.POST['username']) \
            and ( 'password' in request.POST and request.POST['password'] ):

            user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])

            # Check if user exists in database and is active.
            if user is not None and user.is_active:

                # Save user ID to session
                auth.login( request, user )

                # Set interface language - read setting from database
                user_profile = user.get_profile()
                request.session['django_language'] = user_profile.interface_lang_code

                # Add success message
                messages.success(request, _("You have been successfully logged in!"))

                # Redirect to previous site. If next parameter does not exist, redirect to index site.
                # TODO: Why next parameter does not work?
                return redirect(request.GET.get('next', 'index'))
            else:
                messages.error(request, _('The username or password are incorrect.'))
        else:
            messages.error(request, _('Please fill the form below.'))

    return render_to_response('user/login.html', locals(), context_instance = RequestContext( request ) )

def register( request ):
    # TODO: field validation and security
    if request.POST:
        message_error = ""

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # check if username already exists and length
        if User.objects.filter( username__exact = username ):
            message_error += "Username already exists. "

        if len( username ) < 4:
            message_error += "Username must have at least 4 characters. "

        # check if email already exists
        if User.objects.filter( email__exact = email ):
            message_error += "Email already exists. "

        if not email_re.search( email ):
            message_error += "Email address is not valid. "

        # check password length and if passwords match
        if len( password1 ) < 4:
            message_error += "Password must have at least 4 characters."

        if ( password1 != password2 ):
            message_error += "Passwords do not match. "

        # register a new user
        if message_error == "":
            user = User.objects.create_user( username, email, password1 )

            try:
                default_group = Group.objects.get( name = settings.DEFAULT_USER_GROUP )
            except Group.DoesNotExist:
                default_group = Group.objects.create( name = settings.DEFAULT_USER_GROUP );

            user.groups.add( default_group )
            user.save()

            # authenticate user and redirect him to profile
            user = auth.authenticate( username = username, password = password1 )
            auth.login( request, user )

            messages.success(request, _("You have been successfully registered."))

            return redirect("users.profile")

    return render_to_response('user/register.html', locals(), context_instance = RequestContext( request ) )

@login_required()
def profile(request):
    user = User.objects.get(id = request.user.id)
    error = None
    form = forms.profileForm( {'username' : user.username,
                              'first_name' : user.first_name,
                              'last_name' : user.last_name,
                              'email' : user.email,
                              } )

    if request.method == 'POST':
        form = forms.profileForm( request.POST )

        if form.is_valid():
            if request.POST['password'] != request.POST['confirm_password']:
                messages.error(request, _("Passwords have to be the same!"))
            else:
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.set_password( request.POST['password'] )
                user.email = request.POST['email']

                user.save()

                messages.success(request, _("Your profile has been updated!"))

                return redirect( request.get_full_path() )
        else:
            messages.error(request, _("Form is not valid!"))

    return render_to_response("user/profile.html", locals(), context_instance = RequestContext( request ) )

#TODO: write more robust and safe!
@login_required()
def set_interface_lang(request):
    if request.POST:
        user = User.objects.get(id = request.user.id)
        user_profile = user.get_profile()

        user_profile.interface_lang_code = request.POST.get("language", "en")
        user_profile.save()

        request.session['django_language'] = request.POST.get("language", "en")

        messages.success(request, _("Your interface language has been changed."))

    return redirect("profile")

@login_required()
def edit_user(request, user_id):
    user = User.objects.get(id = user_id)
    languages = settings.LANGUAGES

    # prepare both forms
    form = forms.EditUserForm(instance=user)
    form_profile = forms.EditUserProfileForm(instance=user.get_profile())

    # if save button is pressed
    if request.method == "POST":

        # User form
        if "user" in request.POST:
            form = forms.EditUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, _("User settings are updated."))

        # User profile form
        if "user-profile" in request.POST:
            form_profile = forms.EditUserProfileForm(request.POST, instance=user.get_profile())
            if form_profile.is_valid():
                form_profile.save()
                messages.success(request, _("User profile is updated."))

    return render_to_response("control-panel/edit-user.html", locals(), context_instance = RequestContext(request))

@login_required()
def delete_user(request, user_id):
    user = User.objects.get(id = user_id)

    if not user.is_active:
        user.delete()
        messages.success(request, _("User is deleted!"))
    else:
        messages.error(request, _("User cannot be deleted! User is still active."))

    return redirect("users")

def show_user(request, user_id):
    user = User.objects.get(id = user_id)
    tasks = Task.objects.filter(author = user)
    task_num = tasks.count()

    return render_to_response("user/show.html", locals(), context_instance = RequestContext(request))
