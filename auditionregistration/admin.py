# from django.contrib import admin
# from auditionregistration.models import AuditionRegistrationModel

# @admin.register(AuditionRegistrationModel)
# class AuditionRegiAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'place', 'date', 'regimg']


from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id', 'cid', 'name', 'nimg']
