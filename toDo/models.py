from django.db import models

class Post(models.Model):
    description = models.CharField('descrição', max_length=30)
    complete = models.BooleanField('completo', default=False)

    class Meta:
        ordering = ('description',)
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return self.description

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'complete': self.complete,
        }
