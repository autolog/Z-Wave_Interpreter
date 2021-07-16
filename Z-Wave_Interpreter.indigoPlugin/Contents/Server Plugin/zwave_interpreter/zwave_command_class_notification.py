#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

# Basic Command Class "0x20" [32]

# ### Notification Class ### Note that this overloads the Alarm Class

ZW_NOTIFICATION = 0x71
ZW_NOTIFICATION_EVENT_SUPPORTED_GET = 0x01
ZW_NOTIFICATION_EVENT_SUPPORTED_REPORT = 0x02
ZW_NOTIFICATION_NOTIFICATION_GET = 0x04
ZW_NOTIFICATION_NOTIFICATION_REPORT = 0x05
ZW_NOTIFICATION_NOTIFICATION_SET = 0x06
ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_GET = 0x07
ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_REPORT = 0x08

ZW_NOTIFICATION_TYPE_SMOKE_ALARM = 0X01
ZW_NOTIFICATION_TYPE_CO_ALARM = 0X02
ZW_NOTIFICATION_TYPE_CO2_ALARM = 0X03
ZW_NOTIFICATION_TYPE_HEAT_ALARM = 0X04
ZW_NOTIFICATION_TYPE_WATER_ALARM = 0X05
ZW_NOTIFICATION_TYPE_ACCESS_CONTROL = 0X06
ZW_NOTIFICATION_TYPE_HOME_SECURITY = 0X07
ZW_NOTIFICATION_TYPE_POWER_MANAGEMENT = 0X08
ZW_NOTIFICATION_TYPE_SYSTEM = 0X09
ZW_NOTIFICATION_TYPE_EMERGENCY_ALARM = 0X0A
ZW_NOTIFICATION_TYPE_CLOCK = 0X0B
ZW_NOTIFICATION_TYPE_APPLIANCE = 0X0C
ZW_NOTIFICATION_TYPE_HOME_HEALTH = 0X0D
ZW_NOTIFICATION_TYPE_SIREN = 0X0E
ZW_NOTIFICATION_TYPE_WATER_VALVE = 0X0F
ZW_NOTIFICATION_TYPE_WEATHER_ALARM = 0X10
ZW_NOTIFICATION_TYPE_IRRIGATION = 0X11
ZW_NOTIFICATION_TYPE_GAS_ALARM = 0X12
ZW_NOTIFICATION_TYPE_PEST_CONTROL = 0X13
ZW_NOTIFICATION_TYPE_LIGHT_SENSOR = 0X14
ZW_NOTIFICATION_TYPE_WATER_QUALITY_MONITORING = 0X15
ZW_NOTIFICATION_TYPE_HOME_MONITORING = 0X16
ZW_NOTIFICATION_TYPE_REQUEST_PENDING_NOTIFICATION = 0XFF

ZW_STATE_HOME_SECURITY_IDLE = 0x00
ZW_STATE_HOME_SECURITY_INTRUSION_LOCATION_PROVIDED = 0x01
ZW_STATE_HOME_SECURITY_INTRUSION = 0x02
ZW_STATE_HOME_SECURITY_TAMPERING_PRODUCT_COVER_REMOVED = 0x03
ZW_STATE_HOME_SECURITY_TAMPERING_INVALID_CODE = 0x04
ZW_STATE_HOME_SECURITY_GLASS_BREAKAGE_LOCATION_PROVIDED = 0x05
ZW_STATE_HOME_SECURITY_GLASS_BREAKAGE = 0x06
ZW_STATE_HOME_SECURITY_MOTION_DETECTION_LOCATION_PROVIDED = 0x07
ZW_STATE_HOME_SECURITY_MOTION_DETECTION = 0x08
ZW_STATE_HOME_SECURITY_TAMPERING_PRODUCT_MOVED = 0x09
ZW_STATE_HOME_SECURITY_IMPACT_DETECTED = 0x0A
ZW_STATE_HOME_SECURITY_MAGNETIC_FIELD_INTERFERENCE_DETECTED = 0x0B
ZW_STATE_HOME_SECURITY_RF_JAMMING_DETECTED = 0x0C
ZW_STATE_HOME_SECURITY_UNKNOWN_EVENT_STATE = 0xFE

ZW_STATE_ACCESS_CONTROL_DOOR_WINDOW_OPEN = 0x16
ZW_STATE_ACCESS_CONTROL_DOOR_WINDOW_CLOSED = 0x17

class ZwaveNotification:
    """
    Z-Wave Command Class: Notification "0x71" [Decimal 113]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_NOTIFICATION] = dict()
            self.command_classes[ZW_NOTIFICATION][ZW_IDENTIFIER] = u"Notification"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS] = dict()
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_EVENT_SUPPORTED_GET] = u"Event Supported Get"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_EVENT_SUPPORTED_REPORT] = u"Event Supported Report"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_NOTIFICATION_GET] = u"Get"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_NOTIFICATION_REPORT] = u"Report"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_NOTIFICATION_SET] = u"Set"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_NOTIFICATION][ZW_COMMANDS][ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_REPORT] = u"Supported Report"

            self.notification_types = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_SMOKE_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_SMOKE_ALARM][ZW_IDENTIFIER] = u"Smoke Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_SMOKE_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_CO_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_CO_ALARM][ZW_IDENTIFIER] = u"CO Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_CO_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_CO2_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_CO2_ALARM][ZW_IDENTIFIER] = u"CO2 Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_CO2_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_HEAT_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_HEAT_ALARM][ZW_IDENTIFIER] = u"Heat Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_HEAT_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_ALARM][ZW_IDENTIFIER] = u"Water Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_ACCESS_CONTROL] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_ACCESS_CONTROL][ZW_IDENTIFIER] = u"Access Control"
            self.notification_types[ZW_NOTIFICATION_TYPE_ACCESS_CONTROL][ZW_TYPES] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_ACCESS_CONTROL][ZW_TYPES][ZW_STATE_ACCESS_CONTROL_DOOR_WINDOW_OPEN] = u"Door/Window Is Open"
            self.notification_types[ZW_NOTIFICATION_TYPE_ACCESS_CONTROL][ZW_TYPES][ZW_STATE_ACCESS_CONTROL_DOOR_WINDOW_CLOSED] = u"Door/Window Is Closed"

            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_IDENTIFIER] = u"Home Security"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_IDLE] = u"Idle"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_INTRUSION_LOCATION_PROVIDED] = u"Intrusion [Location Provided]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_INTRUSION] = u"Intrusion"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_TAMPERING_PRODUCT_COVER_REMOVED] = u"Tampering [Product Cover Removed]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_TAMPERING_INVALID_CODE] = u"Tampering [Invalid Code]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_GLASS_BREAKAGE_LOCATION_PROVIDED] = u"Glass Breakage [Location Provided]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_GLASS_BREAKAGE] = u"Glass Breakage"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_MOTION_DETECTION_LOCATION_PROVIDED] = u"Motion Detection [Location Provided]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_MOTION_DETECTION] = u"Motion Detection"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_TAMPERING_PRODUCT_MOVED] = u"Tampering [Product Moved]"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_IMPACT_DETECTED] = u"Impact Detected"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_MAGNETIC_FIELD_INTERFERENCE_DETECTED] = u"Magnetic Field Interference Detected"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_RF_JAMMING_DETECTED] = u"RF Jamming Detected"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_SECURITY][ZW_TYPES][ZW_STATE_HOME_SECURITY_UNKNOWN_EVENT_STATE] = u"Unknown Event/State"

            self.notification_types[ZW_NOTIFICATION_TYPE_POWER_MANAGEMENT] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_POWER_MANAGEMENT][ZW_IDENTIFIER] = u"Power Management"
            self.notification_types[ZW_NOTIFICATION_TYPE_POWER_MANAGEMENT][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_SYSTEM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_SYSTEM][ZW_IDENTIFIER] = u"System"
            self.notification_types[ZW_NOTIFICATION_TYPE_SYSTEM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_EMERGENCY_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_EMERGENCY_ALARM][ZW_IDENTIFIER] = u"Emergency Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_EMERGENCY_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_CLOCK] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_CLOCK][ZW_IDENTIFIER] = u"Clock"
            self.notification_types[ZW_NOTIFICATION_TYPE_CLOCK][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_APPLIANCE] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_APPLIANCE][ZW_IDENTIFIER] = u"Appliance"
            self.notification_types[ZW_NOTIFICATION_TYPE_APPLIANCE][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_HEALTH] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_HEALTH][ZW_IDENTIFIER] = u"Home Health"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_HEALTH][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_SIREN] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_SIREN][ZW_IDENTIFIER] = u"Siren"
            self.notification_types[ZW_NOTIFICATION_TYPE_SIREN][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_VALVE] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_VALVE][ZW_IDENTIFIER] = u"Water Valve"
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_VALVE][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_WEATHER_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_WEATHER_ALARM][ZW_IDENTIFIER] = u"Weather Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_WEATHER_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_IRRIGATION] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_IRRIGATION][ZW_IDENTIFIER] = u"Irrigation"
            self.notification_types[ZW_NOTIFICATION_TYPE_IRRIGATION][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_GAS_ALARM] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_GAS_ALARM][ZW_IDENTIFIER] = u"Gas Alarm"
            self.notification_types[ZW_NOTIFICATION_TYPE_GAS_ALARM][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_PEST_CONTROL] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_PEST_CONTROL][ZW_IDENTIFIER] = u"Pest Control"
            self.notification_types[ZW_NOTIFICATION_TYPE_PEST_CONTROL][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_LIGHT_SENSOR] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_LIGHT_SENSOR][ZW_IDENTIFIER] = u"Light Sensor"
            self.notification_types[ZW_NOTIFICATION_TYPE_LIGHT_SENSOR][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_QUALITY_MONITORING] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_QUALITY_MONITORING][ZW_IDENTIFIER] = u"Water Quality mMnitoring"
            self.notification_types[ZW_NOTIFICATION_TYPE_WATER_QUALITY_MONITORING][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_MONITORING] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_MONITORING][ZW_IDENTIFIER] = u"Home Monitoring"
            self.notification_types[ZW_NOTIFICATION_TYPE_HOME_MONITORING][ZW_TYPES] = dict()

            self.notification_types[ZW_NOTIFICATION_TYPE_REQUEST_PENDING_NOTIFICATION] = dict()
            self.notification_types[ZW_NOTIFICATION_TYPE_REQUEST_PENDING_NOTIFICATION][ZW_IDENTIFIER] = u"Request Pending Notification"
            self.notification_types[ZW_NOTIFICATION_TYPE_REQUEST_PENDING_NOTIFICATION][ZW_TYPES] = dict()



        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveNotification' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_EVENT_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_EVENT_SUPPORTED_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_NOTIFICATION_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_NOTIFICATION_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_NOTIFICATION_SET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_NOTIFICATION_NOTIFICATION_SUPPORTED_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveNotification' Class, 'process_class_notification' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            if self.zw_interpretation[ZW_COMMAND_PACKET_LENGTH] >= 9:
                # Assume Version 8 of Notification Command

                v1_alarm_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0]
                v1_alarm_level = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
                # reserved
                notification_status = self.zw_interpretation[ZW_COMMAND_DETAIL][3]
                notification_type = self.zw_interpretation[ZW_COMMAND_DETAIL][4]
                notification_status_event = self.zw_interpretation[ZW_COMMAND_DETAIL][5]

                if notification_type in self.notification_types:
                    notification_type_ui = self.notification_types[notification_type][ZW_IDENTIFIER]
                    if notification_status_event in self.notification_types[notification_type][ZW_TYPES]:
                        notification_status_event_ui = self.notification_types[notification_type][ZW_TYPES][notification_status_event]
                    else:
                        notification_status_event_ui = u"{0} Unknown".format(hex(notification_status_event))
                else:
                    notification_type_ui = u"{0} Unknown".format(hex(notification_type))
                    notification_status_event_ui = u"{0} Unknown".format(hex(notification_status_event))

                self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Type: '{3}', Event/State: '{4}'"
                                                                .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_UI],
                                                                        notification_type_ui,
                                                                        notification_status_event_ui))

                self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveNotification' Class, 'process_command_notification_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
