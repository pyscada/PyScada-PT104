# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.models import Device, Variable
from pyscada.pt104.models import PT104Variable, PT104Device, ExtendedPT104Device, ExtendedPT104Variable

from django.dispatch import receiver
from django.db.models.signals import post_save

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=PT104Variable)
@receiver(post_save, sender=PT104Device)
@receiver(post_save, sender=ExtendedPT104Device)
@receiver(post_save, sender=ExtendedPT104Variable)
def _reinit_daq_daemons(sender, instance, **kwargs):
    """
    update the daq daemon configuration when changes be applied in the models
    """
    if type(instance) is PT104Device:
        post_save.send_robust(sender=Device, instance=instance.pt104_device)
    elif type(instance) is PT104Variable:
        post_save.send_robust(sender=Variable, instance=instance.pt104_variable)
    elif type(instance) is ExtendedPT104Variable:
        post_save.send_robust(sender=Variable, instance=Variable.objects.get(pk=instance.pk))
    elif type(instance) is ExtendedPT104Device:
        post_save.send_robust(sender=Device, instance=Device.objects.get(pk=instance.pk))
