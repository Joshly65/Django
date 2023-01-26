from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class categorias(models.Model):
    name = models.ChatField(_MAX_LENGTH=100)