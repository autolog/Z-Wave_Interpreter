#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
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

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_SENSOR_ALARM] = dict()
            self.command_classes[ZW_SENSOR_ALARM][ZW_IDENTIFIER] = u"Thermostat Mode"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_GET] = u"Get"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_REPORT] = u"Report"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_SENSOR_ALARM][ZW_COMMANDS][ZW_SENSOR_ALARM_SUPPORTED_REPORT] = u"Supported Report"

            self.zw_sensor_alarm_types = dict()
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_GENERAL_PURPOSE] = u"General Purpose"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_SMOKE] = u"Smoke"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_CO] = u"CO"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_CO2] = u"CO2"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_HEAT] = u"Heat"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_WATER_LEAK] = u"Water Leak"
            self.zw_sensor_alarm_types[ZW_SENSOR_ALARM_RETURN_FIRST_ALARM_ON_SUPPORTED_LIST] = u"Return first alarm on supported list"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorAlarm' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_SENSOR_ALARM_GET:
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

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorAlarm' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

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
                self.zw_interpretation[ZW_SENSOR_ALARM_TYPE_UI] = u"Unknown Alarm Sensor Type"

            value, value_bool, value_ui = self.utility.evaluate_sensor_state(sensor_state)

            self.zw_interpretation[ZW_SECONDS] = seconds
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Sensor Type: {3}, value: '{4}' | {5} | '{6}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_SENSOR_ALARM_TYPE_UI],
                                                                    self.zw_interpretation[ZW_VALUE],
                                                                    self.zw_interpretation[ZW_VALUE_BOOL],
                                                                    self.zw_interpretation[ZW_VALUE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorAlarm' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
