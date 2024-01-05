from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):
    
    class Meta:
        model = TodoList
        fields = ('title', 'due_date') 
        exclude = ('status',)
        labels = {
            'title': 'Título',
            'due_date': 'Data Limite', 
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'