# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada import core

__version__ = core.__version__
__author__ = core.__author__

default_app_config = 'pyscada.pt104.apps.PyScadaPT104Config'

PROTOCOL_ID = 11

parent_process_list = [{'pk':PROTOCOL_ID,
                        'label': 'pyscada.pt104',
                        'process_class': 'pyscada.pt104.worker.Process',
                        'process_class_kwargs': '{"dt_set":30}',
                        'enabled': True}]
