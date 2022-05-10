#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#


from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_SENSOR_BINARY_GET = 0x02
ZW_SENSOR_BINARY_REPORT = 0x03
ZW_SENSOR_BINARY_SUPPORTED_GET_SENSOR = 0x01
ZW_SENSOR_BINARY_SUPPORTED_SENSOR_REPORT = 0x04


class ZwaveSensorBinary:
    """
    Z-Wave Command Class: Sensor Binary "0x30" [Decimal 48]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_SENSOR_BINARY] = dict()
            self.command_classes[ZW_SENSOR_BINARY][ZW_IDENTIFIER] = "Binary Sensor"
            self.command_classes[ZW_SENSOR_BINARY][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SENSOR_BINARY][ZW_COMMANDS][ZW_SENSOR_BINARY_GET] = "Get"
            self.command_classes[ZW_SENSOR_BINARY][ZW_COMMANDS][ZW_SENSOR_BINARY_REPORT] = "Report"
            self.command_classes[ZW_SENSOR_BINARY][ZW_COMMANDS][ZW_SENSOR_BINARY_SUPPORTED_GET_SENSOR] = "Get Supported Sensor"
            self.command_classes[ZW_SENSOR_BINARY][ZW_COMMANDS][ZW_SENSOR_BINARY_SUPPORTED_SENSOR_REPORT] = "Supported Sensor Report"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_BINARY_GET:  # noqa [Duplicated code fragment!]
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_BINARY_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_BINARY_SUPPORTED_GET_SENSOR:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_BINARY_SUPPORTED_SENSOR_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self):
        try:
            value, value_bool, value_ui = self.utility.evaluate_value(self.zw_interpretation[ZW_COMMAND_DETAIL][0])  # noqa [Duplicated code fragment!]

            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', value: '{self.zw_interpretation[ZW_VALUE]}' | {self.zw_interpretation[ZW_VALUE_BOOL]} | '{self.zw_interpretation[ZW_VALUE_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
