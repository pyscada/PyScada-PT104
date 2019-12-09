# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.models import Variable, Device

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import logging

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class PT104Variable(models.Model):
    pt104_variable = models.OneToOneField(Variable)
    channel_choices = (('1', 'CH1'),
                       ('2', 'CH2'),
                       ('3', 'CH3'),
                       ('4', 'CH4'),
                       ('5', 'CH5'),
                       ('6', 'CH6'),
                       ('7', 'CH7'),
                       ('8', 'CH8'),)
    channel = models.CharField(default='', max_length=10, choices=channel_choices)
    wires_choices = (('2', '2 Wires'),('3', '3 Wires'),('4', '4 Wires'),)
    wires = models.CharField(default='', max_length=10, choices=wires_choices)
    data_type_choices = (('0', 'OFF'),
                         ('1', 'PT100'),
                         ('2','PT1000'),
                         ('3', 'RESISTANCE_TO_375R'),
                         ('4', 'RESISTANCE_TO_10K'),
                         ('5', 'DIFFERENTIAL_TO_115MV'),
                         ('6', 'DIFFERENTIAL_TO_2500MV'),
                         ('7', 'SINGLE_ENDED_TO_115MV'),
                         ('8', 'SINGLE_ENDED_TO_2500MV'),)
    data_type = models.CharField(default='', max_length=10, choices=data_type_choices)

    def __str__(self):
        return self.pt104_variable.name


@python_2_unicode_compatible
class PT104Device(models.Model):
    pt104_device = models.OneToOneField(Device)
    serial_nb = models.CharField(default='', max_length=15)
    def __str__(self):
        return self.pt104_device.short_name


class ExtendedPT104Device(Device):
    class Meta:
        proxy = True
        verbose_name = 'PT104 Device'
        verbose_name_plural = 'PT104 Devices'


class ExtendedPT104Variable(Variable):
    class Meta:
        proxy = True
        verbose_name = 'PT104 Variable'
        verbose_name_plural = 'PT104 Variable'

