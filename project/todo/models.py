from django.db import models
from django.db.models.fields import BooleanField, DateTimeField

class ToDo(models.Model):
    title = models.CharField('Titulo', max_length=50, null=False)
    description = models.TextField('Descrição', blank=True, null=True)
    done = BooleanField('Finalizada', default=False)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

