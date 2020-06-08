# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Review, Vote
# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Vote)

admin.site.site_header="Project Voter Administration"
admin.site.site_title="Project Voter App"