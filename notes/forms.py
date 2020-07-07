from django.forms import ModelForm, Textarea
from .models import Note, Category

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'text',
            'title',
            'categories',
        ]

        widgets = {
            'text': Textarea(attrs={'class': 'note-text'}),
        }




class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
