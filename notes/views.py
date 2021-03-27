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
        deleteid = request.POST.get('delete_note_id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        #Check if tag is None, and if i"t has a '#'
        if request.POST.get('tags') == None:
            tag = request.POST.get('tags')
        else:
            if request.POST.get('tags')[0] == "#":
                tag = request.POST.get('tags').lower()
            else:
                tag = "#" + request.POST.get('tags').lower()    

        #Delete note
        if deleteid != None and deleteid != "None" and deleteid != '':
            deleteNote(deleteid)
        
        #Edit note
        elif noteid != None and noteid != "None" and noteid != '':
            editNote(noteid, title, content, tag)
        
        #Create note
        else:
            Note(title=title, content=content, tag=tag).save()
    
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})