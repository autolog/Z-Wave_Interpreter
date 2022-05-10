#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

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

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE] = dict()
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_IDENTIFIER] = "Climate Control Schedule"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_SET] = "Set"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_GET] = "Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_REPORT] = "Report"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_GET] = "Changed Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_CHANGED_REPORT] = "Changed Report"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_SET] = "Override Set"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_GET] = "Override Get"
            self.command_classes[ZW_CLIMATE_CONTROL_SCHEDULE][ZW_COMMANDS][ZW_CLIMATE_CONTROL_SCHEDULE_OVERRIDE_REPORT] = "Override Report"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
