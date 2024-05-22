from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new Task...'}))
    class Meta:
        model=Task
        fields='__all__'

