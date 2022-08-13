from django.contrib import admin
from .models import Manifest


@admin.register(Manifest)
class ManifestAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)
