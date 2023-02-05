from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PublicPost
from django_summernote.admin import SummernoteModelAdmin

class PublicPostAdmin(SummernoteModelAdmin):
    # Apply summernote to content field of your model
    summernote_fields = ('content',)

admin.site.register(PublicPost, PublicPostAdmin)