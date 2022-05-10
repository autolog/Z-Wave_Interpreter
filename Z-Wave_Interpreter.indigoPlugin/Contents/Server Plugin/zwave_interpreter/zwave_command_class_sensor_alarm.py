#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_SENSOR_ALARM_GET = 0x01
ZW_SENSOR_ALARM_REPORT = 0x02
ZW_SENSOR_ALARM_SUPPORTED_GET = 0x03
ZW_SENSOR_ALARM_SUPPORTED_REPORT = 0x04

ZW_SENSOR_ALARM_GENERAL_PURPOSE = 0x00
ZW_SENSOR_ALARM_SMOKE = 0x01
ZW_SENSOR_ALARM_CO = 0x02
ZW_SENSOR_ALARM_CO2 = 0x03
ZW_SENSOR_ALARM_HEAT = 0x04
ZW_SENSOR_ALARM_WATER_LEAK = 0x05
ZW_SENSOR_ALARM_RETURN_FIRST_ALARM_ON_SUPPORTED_LIST = 0xFF


class ZwaveSensorAlarm:
    """
    Z-Wave Command Class: Sensor Alarm "0x9C" [Decimal 67]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_SENSOR_ALARM] = dict()
            self.command_classes[ZW_SENSOR_ALARM][ZW_IDENTIFIER] = "Thermostat Mode"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_GET] = "Get"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_REPORT] = "Report"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_SUPPORTED_REPORT] = "Supported Report"

            self.zw_sensor_alarm_types = dict()
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_GENERAL_PURPOSE] = "General Purpose"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_SMOKE] = "Smoke"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_CO] = "CO"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_CO2] = "CO2"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_HEAT] = "Heat"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_WATER_LEAK] = "Water Leak"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_RETURN_FIRST_ALARM_ON_SUPPORTED_LIST] = "Return first alarm on supported list"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_ALARM_GET:  # noqa [Duplicated code fragment!]
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_ALARM_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_ALARM_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_ALARM_SUPPORTED_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self):
        try:
            # source_node_id = self.zw_interpretation[ZW_COMMAND_DETAIL][0]  # Not relevant for Indigo as it already knows the source node
            sensor_type = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
            sensor_state = self.zw_interpretation[ZW_COMMAND_DETAIL][2]
            seconds = (self.zw_interpretation[ZW_COMMAND_DETAIL][3] * 256) + self.zw_interpretation[ZW_COMMAND_DETAIL][4]

            self.zw_interpretation[ZW_SENSOR_ALARM_TYPE] = sensor_type
            if sensor_type in self.zw_sensor_alarm_types:
                self.zw_interpretation[ZW_SENSOR_ALARM_TYPE_UI] = self.zw_sensor_alarm_types[sensor_type]
            else:
                self.zw_interpretation[ZW_SENSOR_ALARM_TYPE_UI] = "Unknown Alarm Sensor Type"

            value, value_bool, value_ui = self.utility.evaluate_sensor_state(sensor_state)

            self.zw_interpretation[ZW_SECONDS] = seconds
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Sensor Type: {self.zw_interpretation[ZW_SENSOR_ALARM_TYPE_UI]}, value: '{self.zw_interpretation[ZW_VALUE]}' | {self.zw_interpretation[ZW_VALUE_BOOL]} | '{self.zw_interpretation[ZW_VALUE_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
