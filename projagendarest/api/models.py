from django.db import models

class Agenda(models.Model):
    descricao = models.CharField(max_length=255, blank=False, unique=True)
    nomepai = models.CharField(max_length=255)
    nomemae = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.descricao)