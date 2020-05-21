from django.http import HttpResponse
from django.template import loader
from .models import Note


def notes(request):
    notes_list = Note.objects.all()
    template = loader.get_template('note/notes.html')
    context = {
        'notes_list': notes_list,
    }
    return HttpResponse(template.render(context, request))


def note(request, note_id):
    return HttpResponse("This be note %s" % note_id)
