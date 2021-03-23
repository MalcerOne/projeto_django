from django.shortcuts import render, redirect
from .models import Note

def editNote(identif, titulo, content, tag):
    note = Note.objects.get(id=identif)
    note.title = titulo
    note.content = content
    note.tag = tag
    note.save()

def deleteNote(identif):
    note = Note.objects.get(id=identif)
    note.delete()


def index(request):
    if request.method == 'POST':
        noteid = request.POST.get('edit_note')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tags')

        deleteid = request.POST.get('delete_id')

        #Delete note
        if deleteid != None:
            deleteNote(deleteid)
        
        #Edit note
        elif noteid != None:
            editNote(noteid, title, content, tag)
        
        #Create note
        else:
            Note(title=title, content=content, tag=tag).save()
    
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})