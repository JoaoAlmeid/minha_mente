from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):

    due_date = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }
        ),
    )
    class Meta:
        model = TodoList
        fields = '__all__'
        exclude = ('status',)

    def __init__(self, *args, **kwargs):
        super(TodoListForm,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'