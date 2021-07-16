#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_WAKE_UP_INTERVAL_SET = 0x04
ZW_WAKE_UP_INTERVAL_GET = 0x05
ZW_WAKE_UP_INTERVAL_REPORT = 0x06
ZW_WAKE_UP_NOTIFICATION = 0x07
ZW_WAKE_UP_NO_MORE_INFORMATION = 0x08
ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET = 0x09
ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT = 0x0A


class ZwaveWakeUp:
    """
    Z-Wave Command Class: Wake Up "0x84" [Decimal 132]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_WAKE_UP] = dict()
            self.command_classes[ZW_WAKE_UP][ZW_IDENTIFIER] = u"Wakeup"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS] = dict()
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_SET] = u"Interval Set"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_GET] = u"Interval Get"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_REPORT] = u"Interval Report"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_NOTIFICATION] = u"Notification"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_NO_MORE_INFORMATION] = u"No More Information"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET] = u"Interval Capabilities Get"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT] = u"Interval Capabilities Report"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveWakeUp' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_SET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_NOTIFICATION:
                self._interpret_wake_up_notification()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_NO_MORE_INFORMATION:
                self._interpret_wake_up_no_more_information()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveWakeUp' Class, 'process_class_wake_up' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_wake_up_no_more_information(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveWakeUp' Class, '_interpret_wake_up_no_more_information' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_wake_up_notification(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveWakeUp' Class, '_interpret_wake_up_notification' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
