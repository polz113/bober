from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from extra_views import UpdateWithInlinesView
from braces.views import LoginRequiredMixin

from bober_paper_submissions.forms import JuniorMentorshipForm, JuniorYearInline
from bober_si.models import SchoolTeacherCode
from bober_paper_submissions.models import JuniorMentorship, Competition


@login_required
def mentorship_list(request, slug):
    profile = request.profile
    competition = Competition.objects.get(slug=slug)
    mentorship_list = list()
    for sc in SchoolTeacherCode.objects.filter(
            teacher=profile, code__codegenerator=competition.competitor_code_generator):
        for dy in sc.competition_questionset.juniordefaultyear_set.all():
            dy.create_year(sc)
    mentorship_list = JuniorMentorship.objects.filter(
        competition=competition, teacher=profile)
    if len(mentorship_list) == 1:
        return redirect('junior_results', slug=slug, pk=mentorship_list[0].id)
    return render(request, "bober_paper_submissions/school_mentor.html",
                  {'object_list': mentorship_list, 'slug': slug})


class JuniorResults(UpdateWithInlinesView, LoginRequiredMixin):
    model = JuniorMentorship
    form_class = JuniorMentorshipForm
    inlines = [JuniorYearInline]
    template_name = "bober_paper_submissions/junior_results.html"

    def dispatch(self, *args, **kwargs):
        self.competition_slug = kwargs.get('slug', None)
        return super(JuniorResults, self).dispatch(*args, **kwargs)

    def forms_valid(self, form, inlines):
        for inline_set in inlines:
            for inline in inline_set:
                inline.instance.save_results(
                    inline.competitor_data, self.request.profile)
        return super(JuniorResults, self).forms_valid(form, inlines)

    def get_success_url(self):
        return reverse('teacher_overview', kwargs={'slug': self.competition_slug})
