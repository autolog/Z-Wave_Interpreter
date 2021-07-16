#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_BASIC_COMMAND_SET = 0x01
ZW_BASIC_COMMAND_GET = 0x02
ZW_BASIC_COMMAND_REPORT = 0x03


class ZwaveBasicCommand:
    """
    Z-Wave Command Class: Basic Command "0x20" [Decimal 32]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_BASIC_COMMAND] = dict()
            self.command_classes[ZW_BASIC_COMMAND][ZW_IDENTIFIER] = u"Basic Command"
            self.command_classes[ZW_BASIC_COMMAND][ZW_COMMANDS] = dict()
            self.command_classes[ZW_BASIC_COMMAND][ZW_COMMANDS][ZW_BASIC_COMMAND_SET] = u"Set"
            self.command_classes[ZW_BASIC_COMMAND][ZW_COMMANDS][ZW_BASIC_COMMAND_GET] = u"Get"
            self.command_classes[ZW_BASIC_COMMAND][ZW_COMMANDS][ZW_BASIC_COMMAND_REPORT] = u"Report"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBasicCommand' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_BASIC_COMMAND_SET:
                self._interpret_set()
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BASIC_COMMAND_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BASIC_COMMAND_REPORT:
                self._interpret_report()
                return

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBasicCommand' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_set(self):
        try:
            value, value_bool, value_ui = self.utility.evaluate_value(self.zw_interpretation[ZW_COMMAND_DETAIL][0])

            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', value: '{3}' | {4} | '{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_VALUE],
                                                                    self.zw_interpretation[ZW_VALUE_BOOL],
                                                                    self.zw_interpretation[ZW_VALUE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBasicCommand' Class, '_interpret_set' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            value, value_bool, value_ui = self.utility.evaluate_value(self.zw_interpretation[ZW_COMMAND_DETAIL][0])

            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', value: '{3}' | {4} | '{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_VALUE],
                                                                    self.zw_interpretation[ZW_VALUE_BOOL],
                                                                    self.zw_interpretation[ZW_VALUE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveBasicCommand' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
