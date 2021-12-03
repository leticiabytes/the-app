from django import forms

from .models import Post

class ToDoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Post
        fields = ('description', )
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Adicione uma tarefa', 'autofocus': True, 'class': 'input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
