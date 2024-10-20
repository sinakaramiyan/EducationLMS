from django.contrib import admin
from .models import Role, CoursePermission, RolePermission, RoleAssignment, StudentMoreDetails, ManagerMoreDetails, RALevel

admin.site.register(Role)

admin.site.register(CoursePermission)

admin.site.register(RolePermission)

admin.site.register(RoleAssignment)

admin.site.register(StudentMoreDetails)

admin.site.register(ManagerMoreDetails)

admin.site.register(RALevel)