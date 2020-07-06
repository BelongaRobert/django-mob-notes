from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_notes(request):
    user = request.user
    notes = user.notes.all()
    return render(request,  'notes/list_notes.html', {'notes': notes})


def show_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/show_note.html', {'note': note})


def add_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(data= request.POST)
        if form.is_valid():
            note = form.save()
            note.save()
            return redirect('show_note, pk=note.pk')
    else:
        form= NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})
