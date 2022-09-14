from django.contrib import admin
from .models import Contact, Qa


@admin.register(Qa)
class QaAdmin(admin.ModelAdmin):
    list_display = ('question', 'publish')
    list_filter = ('publish',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
