from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "regno",
        "name",
        "dob",
        "department",
        "city",
        "phone",
    )


admin.site.register(Student, StudentAdmin)
