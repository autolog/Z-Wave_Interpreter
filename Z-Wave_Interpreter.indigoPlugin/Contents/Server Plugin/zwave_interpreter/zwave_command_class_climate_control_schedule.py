#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_CLIMATE_CONTROL_SCHEDULE_SET = 0x01
ZW_CLIMATE_CONTROL_SCHEDULE_GET = 0x02
ZW_CLIMATE_CONTROL_SCHEDULE_REPORT = 0x03
ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_GET = 0x04
ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_REPORT = 0x05
ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_SET = 0x06
ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_GET = 0x07
ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_REPORT = 0x08


class ZwaveClimateControlSchedule:
    """
    Z-Wave Command Class: Climate Control Schedule "0x46" [Decimal 70]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE] = dict()
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_IDENTIFIER] = u"Climate Control Schedule"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_SET] = u"Set"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_GET] = u"Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_REPORT] = u"Report"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_GET] = u"Changed Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_REPORT] = u"Changed Report"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_SET] = u"Override Set"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_GET] = u"Override Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_REPORT] = u"Override Report"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveClimateControlSchedule' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveClimateControlSchedule' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
