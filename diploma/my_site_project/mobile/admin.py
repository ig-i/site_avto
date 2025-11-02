from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Mobile
        fields = "__all__"


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Mobile, BlogAdmin)
admin.site.register(UserForm, BlogAdmin)
admin.site.register(CarForm, BlogAdmin)






