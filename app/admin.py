from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "regno",
        "name",
        "dob",
        "department",
        "address",
        "phone",
    )


admin.site.register(Student, StudentAdmin)
