# https://studygyaan.com/django/django-crud-create-retrieve-update-delete-function-based-views

from django import forms
from .models import Details


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"
