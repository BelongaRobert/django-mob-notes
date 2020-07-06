from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm

# Create your views here.
def list_notes(request):
    pass