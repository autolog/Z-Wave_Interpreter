#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_BATTERY_GET = 0x02
ZW_BATTERY_REPORT = 0x03
ZW_BATTERY_HEALTH_GET = 0x04
ZW_BATTERY_HEALTH_REPORT = 0x05


class ZwaveBattery:
    """
    Z-Wave Command Class: Battery "0x80" [Decimal 128]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_BATTERY] = dict()
            self.command_classes[ZW_BATTERY][ZW_IDENTIFIER] = u"Battery"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS] = dict()
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_GET] = u"Get"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_REPORT] = u"Report"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_HEALTH_GET] = u"Health Get Command"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_HEALTH_REPORT] = u"Report Command"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBattery' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_HEALTH_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_HEALTH_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBattery' Class, 'process_class_battery' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBattery' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            battery_level = int(self.zw_interpretation[ZW_COMMAND_DETAIL][0])
            if battery_level > 100:
                battery_level = 255
            self.zw_interpretation[ZW_BATTERY_LEVEL] = battery_level
            if battery_level == 255:
                self.zw_interpretation[ZW_BATTERY_LEVEL_UI] = u"Low"
            else:
                self.zw_interpretation[ZW_BATTERY_LEVEL_UI] = u"{0}%".format(battery_level)
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Battery Level: {3}"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_BATTERY_LEVEL_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBattery' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
