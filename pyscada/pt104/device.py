# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import time
driver_ok = True
try:
    from PT104 import PT104, Channels, DataTypes, Wires
    driver_ok = True
except ImportError:
    driver_ok = False

import logging

logger = logging.getLogger(__name__)


class Device:
    def __init__(self, device):
        self.variables = []
        self.device = device
        if not driver_ok:
            logger.debug('not driver_ok')
            return
        self.unit = PT104()
        self.unit.connect(device.pt104device.serial_nb)
        if not self.unit.is_connected:
            logger.debug('not connected')
            return
        for item in device.variable_set.filter(active=1):
            if not hasattr(item, 'pt104variable'):
                continue
            self.variables.append(item)
            self.unit.set_channel(int(item.pt104variable.channel), int(item.pt104variable.data_type), int(item.pt104variable.wires))

    def request_data(self):
        """

        """
        if not driver_ok:
            return []

        output = []
        for item in self.variables:
            value = None
            timeout = time() + 2  # 2 seconds timeout
            while value is None:
                value = self.unit.get_value(int(item.pt104variable.channel))
                timestamp = time()
                if time() > timeout:
                    break
            # update variable
            if value is not None and item.update_value(value, timestamp):
                output.append(item.create_recorded_data_element())
        return output
