from django.contrib import admin

from api.models import Specialization, Patient, Visit, Doctor, Service


admin.site.register(Specialization)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Service)
admin.site.register(Doctor)
