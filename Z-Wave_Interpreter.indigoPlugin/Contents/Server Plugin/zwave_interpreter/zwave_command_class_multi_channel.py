#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *
from .zwave_interpreter import *

# ### Multi Channel Command Class ###

ZW_MULTI_CHANNEL_END_POINT_GET = 0x07
ZW_MULTI_CHANNEL_END_POINT_REPORT = 0x08
ZW_MULTI_CHANNEL_CAPABILITY_GET = 0x09
ZW_MULTI_CHANNEL_CAPABILITY_REPORT = 0x0A
ZW_MULTI_CHANNEL_END_POINT_FIND = 0x0B
ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT = 0x0C
ZW_MULTI_CHANNEL_CMD_ENCAP = 0x0D
ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET = 0x0E
ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT = 0x0F


class ZwaveMultiChannel():
    """
    Z-Wave Command Class: Multi Channel "0x60" [Decimal 96]

    """

    def __init__(self, parent):
        try:
            self.parent = parent
            self.logger = parent.logger
            self.utility = parent.utility
            self.command_classes = parent.zw_command_classes
            self.zw_interpretation = parent.zw_interpretation

            self.command_classes[ZW_MULTI_CHANNEL] = dict()
            self.command_classes[ZW_MULTI_CHANNEL][ZW_IDENTIFIER] = u"Multi Channel"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS] = dict()
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_END_POINT_GET] = u"End Point Get"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_END_POINT_REPORT] = u"End Point Report"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_CAPABILITY_GET] = u"Capability Get"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_CAPABILITY_REPORT] = u"Capability Report"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_END_POINT_FIND] = u"End Point Find"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT] = u"End Point Find Report"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_CMD_ENCAP] = u"Command Encapsulation"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET] = u"Aggregated Members get"
            self.command_classes[ZW_MULTI_CHANNEL][ZW_COMMANDS][ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT] = u"Aggregated Members Report"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMultiChannel' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:

            if self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_END_POINT_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_END_POINT_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_CAPABILITY_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_CAPABILITY_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_END_POINT_FIND:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_CMD_ENCAP:
                self._interpret_cmd_encap()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT:
                pass
            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMultiChannel' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_cmd_encap(self):
        try:
            source_end_point = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b01111111  # Clear high order bit [RES]
            bit_address = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b10000000  # 1 = bit mask, 0 = Endpoint
            destination_end_point = 0
            if bit_address:
                bit_mask = self.zw_interpretation[ZW_COMMAND_DETAIL][1] & 0b01111111
                loop = 0
                for i in [1,2,4,8,16,32,64,128]:
                    loop += 1
                    if bit_mask & i == 1:
                        destination_end_point = loop
                        break
            else:
                destination_end_point = self.zw_interpretation[ZW_COMMAND_DETAIL][1] & 0b01111111

            # Destination Fix to set main device?
            if destination_end_point == 1:
                destination_end_point = 0

            node = self.zw_interpretation[ZW_NODE_ID]

            source_end_point_ui = "Source Device Name"
            destination_end_point_ui = "Destination Device Name"

            source_end_point_ui = self.parent.node_to_indigo_device[node][source_end_point][ZW_INDIGO_DEVICE_NAME]
            destination_end_point_ui = self.parent.node_to_indigo_device[node][destination_end_point][ZW_INDIGO_DEVICE_NAME]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Source: '{3}' [End Point {4}], Destination: '{5}' [End Point {6}]"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    source_end_point_ui,
                                                                    source_end_point,
                                                                    destination_end_point_ui,
                                                                    destination_end_point))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMultiChannel' Class, '_interpret_cmd_encap' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

