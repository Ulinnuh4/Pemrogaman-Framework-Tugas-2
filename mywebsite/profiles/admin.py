from django.contrib import admin

# Register your models here.
from .models import Profile, Resume

admin.site.register(Profile)
admin.site.register(Resume)
