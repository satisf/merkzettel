from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    mod_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Memo(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    memo_text = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.memo_text
