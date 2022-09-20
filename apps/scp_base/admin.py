from django.contrib import admin
from apps.scp_base.models import SCP, SCPEuclid, SCPKetter


@admin.register(SCP)
class SCPAdmin(admin.ModelAdmin):
    pass


@admin.register(SCPEuclid)
class SCPAdmin(admin.ModelAdmin):
    pass


@admin.register(SCPKetter)
class SCPAdmin(admin.ModelAdmin):
    pass