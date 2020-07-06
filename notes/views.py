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



    