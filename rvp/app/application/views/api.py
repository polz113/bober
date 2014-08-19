from application.models import *
from application.models import User
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.template.context import RequestContext
import zipfile
import codecs
from os.path import join as path
import StringIO
from django.http import HttpResponse
from application.models import task_translation
from settings import *
from django.contrib.auth import *
from django.shortcuts import render
import random

def render_to_file(template, filename, template_data, context): # loads template with context data and returns it as a file
    return codecs.open(path(os.path.dirname(__file__), '../private/') + filename, 'w', 'utf-8').write(render_to_string(template, template_data, context)) # save file to 'private folder'

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
            SOURCE_RELATIVE_PATH.append(path(SITE_ROOT, 'resources', 'task', str(task_translation.task_id) , task_translation.language_locale_id, 'resources', resource.filename))
            SOURCE_RELATIVE_PATH_IN_ZIP_FILE.append("resources/" + resource.filename)


        # add aditional sources without static filepaths to 'filenames'(such as pictures, ...) which are located in PATH_TO_SOURCE_ON_SERVER
        for source_path in SOURCE_RELATIVE_PATH:
            filenames.append(source_path)

        # ZIP archive filename, Open StringIO to grab in-memory ZIP contents, The zip compressor
        #zip_filename = "task-" + str(task.id) + "-" + task_translation.language_locale + "-v" + task_translation.version
        #zip_filename = 'Task%d_%s_v%d' % (task_translation.task_id, task_translation.language_locale_id, task_translation.version)
        zip_filename = task_translation.title
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
                zip_path = path("", fname)

            else:                           # All other files go into their respective paths
                zip_path = path(dirpath, fname)


            # Add file, at correct path
            zf.write(fpath, zip_path)

        # Static files
        zf.write(path(SITE_ROOT, 'private', 'solution.html'),'solution.html')
        zf.write(path(SITE_ROOT, 'private', 'Manifest.json'), 'Manifest.json')
        zf.write(path(SITE_ROOT, 'private', 'index.html'), 'index.html')
        #zf.write(path(SITE_ROOT, 'private', 'jquery.min.js'), path("lib", 'jquery.min.js'))
        #zf.write(path(SITE_ROOT, 'private', 'functions.js'), path('lib', 'functions.js'))


        # Must close zip for all contents to be written
        zf.close()

        # Grab ZIP file from in-memory, make response with correct MIME-type
        resp = HttpResponse(s.getvalue(), mimetype = "application/zip")
        # ..and correct content-disposition
        resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
        #if True: return render_to_response("api/task_interactive.html",  locals())
        return resp

        #return HttpResponse(str(current_task_interactive_translated_answer_values))
    else:
        return HttpResponse('Please submit a valid task ID and a valid language locale code')
