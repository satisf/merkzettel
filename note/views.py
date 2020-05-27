from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Note, Memo
import logging

logger = logging.getLogger("views")


def notes(request):
    notes_list = Note.objects.all()
    template = loader.get_template('note/notes.html')
    context = {
        'notes_list': notes_list,
    }
    logger.debug(notes_list)
    return HttpResponse(template.render(context, request))


def note(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
        memos = Memo.objects.filter(note_id=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'note/note.html', {'note': note, 'memos': memos})


def add_note(request):
    txt = request.POST.get('note_title', '')
    if txt:
        new_note = Note(title=txt)
        new_note.save()
    return HttpResponseRedirect(reverse('note:notes'))


def add_memo(request, note_id):
    txt = request.POST.get('memo_text', '')
    if txt:
        corresponding_note = Note.objects.get(pk=note_id)
        new_memo = Memo(note=corresponding_note, memo_text=txt, is_active=True)
        new_memo.save()
    return HttpResponseRedirect(reverse('note:note', args=(note_id,)))


def deactivate_memo(request, note_id, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.is_active = False
    memo.save()
    return HttpResponseRedirect(reverse('note:note', args=(note_id,)))
