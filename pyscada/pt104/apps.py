# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PyScadaPT104Config(AppConfig):
    name = 'pyscada.pt104'
    verbose_name = _("PyScada PT104")

    def ready(self):
        import pyscada.pt104.signals
