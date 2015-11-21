from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class AddProjectForm(forms.Form):
    title = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title here...'}))
    shortname = forms.CharField(max_length=32,  
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter shortname/alias for project...'}))
    description = forms.CharField(max_length=2048, 
            widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter project description here...'}))

class AddTaskForm(forms.Form):
    TASK_TYPES = (('Feature', 'Feature'), 
            ('Bug', 'Bug'), 
            ('Enhancement', 'Enhancement'))

    title = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title here...'}))
    description = forms.CharField(max_length=2048, 
            widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description here...'}))
    type = forms.ChoiceField(choices=TASK_TYPES, required=True, label='Type')

class AddTodoForm(forms.Form):
    note = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note...'}))
