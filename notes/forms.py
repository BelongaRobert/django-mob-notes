from django.forms import ModelForm, Textarea
from .models import Note, Category

class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'db border-box hover-black w-100 measure ba b--black-20 pa2 br2 mv2'
        self.fields['title'].widget.attrs['class'] = 'input-reset ba b--black-20 pa2 mb2 db w-100'
        self.fields['categories'].widget.attrs['class'] = 'input-reset w-100 mv2 b--black-20'
    class Meta:
        model = Note
        fields = [
            'text',
            'title',
            'categories',
        ]






class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
