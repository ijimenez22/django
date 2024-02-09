from django import forms

class CreateNewFormTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    
class CreateNewFormProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=200)