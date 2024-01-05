from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,
                               related_name='status', to_field='id', default='1')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    due_date = models.DateField(null=True, blank=True, verbose_name='Data Limite')
    
    def time_remaining(self):
        if self.due_date:
            now = timezone.now().date()
            remaining_days = (self.due_date - now).days
            return remaining_days if remaining_days >= 0 else 0
        return self.due_date

    def __str__(self): 
        return self.title
    