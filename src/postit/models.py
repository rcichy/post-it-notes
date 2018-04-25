from django.conf import settings
from django.db import models

# Create your models here.

BOARD_TYPES = (
    ('columnal', 'Columnal board type'),
)


class BoardType(models.Model):
    code = models.CharField(max_length=40, choices=BOARD_TYPES)


class Board(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    type = models.ForeignKey(BoardType, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


class Column(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)


class Note(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=40000, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
