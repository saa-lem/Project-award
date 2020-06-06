# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='media/wards/', blank = True, null =True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    project_link = models.URLField(unique=True, blank = True, null =True)
 