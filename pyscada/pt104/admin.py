# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.admin import admin_site
from pyscada.models import Device, DeviceProtocol

from pyscada.pt104 import PROTOCOL_ID
from pyscada.pt104.models import PT104Variable, PT104Device, ExtendedPT104Device, ExtendedPT104Variable
from pyscada.admin import DeviceAdmin
from pyscada.admin import VariableAdmin
from django.contrib import admin
import logging

logger = logging.getLogger(__name__)



class PT104DeviceAdminInline(admin.StackedInline):
    model = PT104Device


class PT104DeviceAdmin(DeviceAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'protocol':
            kwargs['queryset'] = DeviceProtocol.objects.filter(pk=PROTOCOL_ID)
            db_field.default = PROTOCOL_ID
        return super(PT104DeviceAdmin,self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(PT104DeviceAdmin, self).get_queryset(request)
        return qs.filter(protocol_id=PROTOCOL_ID)

    inlines = [
        PT104DeviceAdminInline
    ]


class PT104VariableAdminInline(admin.StackedInline):
    model = PT104Variable


class PT104VariableAdmin(VariableAdmin):
    def name(self, instance):
        return instance.pt104_variable.name

    def value_class(self, instance):
        return instance.pt104_variable.value_class

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'device':
            kwargs['queryset'] = Device.objects.filter(protocol=PROTOCOL_ID)
        return super(PT104VariableAdmin,self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(PT104VariableAdmin, self).get_queryset(request)
        return qs.filter(device__protocol_id=PROTOCOL_ID)

    inlines = [
        PT104VariableAdminInline
    ]

admin_site.register(ExtendedPT104Variable, PT104VariableAdmin)
admin_site.register(ExtendedPT104Device,PT104DeviceAdmin)
