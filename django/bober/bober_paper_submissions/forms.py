#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, HiddenInput, Textarea, CharField
from django.utils.translation import ugettext_lazy as _
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, JuniorAttempt, Competitor, parse_competitor_data
from extra_views import InlineFormSet
from django.core.exceptions import ValidationError
import re

class JuniorYearForm(ModelForm):
    class Meta:
        model = JuniorYear
        widgets = {
            'raw_data': Textarea(attrs={'rows': 20, 'cols': 20})
        }
        labels = {
            'raw_data': ''
        }
        fields = ['raw_data']

    def clean(self):
        retval = super(JuniorYearForm, self).clean()
        self.competitor_data = parse_competitor_data(
            self.cleaned_data['raw_data'])
        return retval

    def save(self, *args, **kwargs):
        instance = super(JuniorYearForm, self).save(*args, **kwargs)
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
