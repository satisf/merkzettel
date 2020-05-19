from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    note_id = models.UUIDField
    active = models.BooleanField
    mod_date = models.DateTimeField('date modified')

class Memo(models.Model):
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    memo_id = models.UUIDField
    memo_text = models.TextField(max_length=200)
    active = models.BooleanField