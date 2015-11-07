#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, HiddenInput, Textarea, CharField
from django.utils.translation import ugettext_lazy as _
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, JuniorAttempt, Competitor, DEFAULT_EXAMPLES
from extra_views import InlineFormSet
from django.core.exceptions import ValidationError
import re

class JuniorYearForm(ModelForm):
    class Meta:
        model = JuniorYear
        widgets = {
            'raw_data': Textarea(attrs={'rows': 3, 'cols': 30})
        }
        labels = {
            'raw_data': ''
        }
        fields = ['raw_data']
    def clean(self):
        retval = super(JuniorYearForm, self).clean()
        raw_data = self.cleaned_data['raw_data']
        if raw_data in DEFAULT_EXAMPLES:
            raise ValidationError(_('Remove the provided examples'), code='remove_examples')
        self.competitor_data = list()
        #re_rez = re.compile(r"(\d+\.?\s*)?(?P<name>([A-Za-zřéöčćžüšđČĆŽŠĐ]+[\s.-]+){1,4}"
        #            r"[A-Za-zřéöüčćžšđČĆŽŠĐ.]+)[\s;:-]*(?P<points>\d+)\s*")
        re_rez = re.compile(ur"(\d+\.?\s*)?(?P<name>([^\W\d_]+[\s.-]+){1,4}"
                    ur"([^\W\d_]|.)+)[\s;:-]+(?P<points>\d+)\s*", re.UNICODE)
        # re_rez = re.compile(ur"(\d+\.?\s*)?(?P<name>[^\W\d_]*)(?P<points>.*)",re.UNICODE)
        seen_students = set()
        for line, rezultat in enumerate(raw_data.split("\n")):
            rezultat = rezultat.strip()
            mo = re_rez.match(rezultat)
            if len(rezultat) < 1:
                continue
            try:
                split_name = mo.group("name").split()
                parts = len(split_name)
                first_name = " ".join(split_name[:parts/2])
                last_name = " ".join(split_name[parts/2:])
                points = int(mo.group("points"))
                self.competitor_data.append((first_name, last_name, points))
                assert (first_name.upper(), last_name.upper()) not in seen_students
                seen_students.add((first_name.upper(), last_name.upper()))
            except:
                raise ValidationError(
                    _('Error in line %(line)d.'),
                    code='error_parsing',
                    params = {'line': line+1}
                )
        return retval
    def save(self, *args, **kwargs):
        instance = super(JuniorYearForm, self).save(*args, **kwargs)
        still_here = list()
        for first_name, last_name, points in self.competitor_data:
            c, created = Competitor.objects.get_or_create(
                first_name = first_name, 
                last_name = last_name,
                juniorattempt__year_class = instance)
            # print c, created
            if created:
                c.save()
            else:
                c.juniorattempt_set.all().delete()
            still_here.append(c.id)
            a = JuniorAttempt(year_class = self.instance, competitor = c)
            a.save()
        Competitor.objects.filter(
            juniorattempt__year_class = instance,
            profile=None).exclude(id__in=still_here).delete()
        return instance

class JuniorMentorshipForm(ModelForm):
    class Meta:
        model = JuniorMentorship
        fields = ()

class JuniorYearInline(InlineFormSet):
    model = JuniorYear
    form_class = JuniorYearForm
    can_delete = False
    extra = 0
    fields = ['raw_data']
