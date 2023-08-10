from django.contrib import admin
from audition.models import Audition

@admin.register(Audition)
class AuditionAdmin(admin.ModelAdmin):
    list_display=['cid', 'cname', 'place', 'img']
