#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter - Plugin © Autolog 2020
#


# noinspection PyUnresolvedReferences
# ============================== Native Imports ===============================
from datetime import datetime
import logging
import os
import platform

# ============================== Custom Imports ===============================
try:
    # noinspection PyUnresolvedReferences
    import indigo
except ImportError:
    pass

from constants import *
from zwave_interpreter.zwave_interpreter import *
from zwave_interpreter.zwave_constants_interpretation import *

# ================================== Header ===================================
__author__    = u"Autolog"
__copyright__ = u""
__license__   = u"MIT"
__build__     = u"unused"
__title__     = u"Z-Wave Interpreter Plugin for Indigo"
__version__   = u"unused"

kDefaultPluginPrefs = {
    u"zwaveInterpretationMode": u"S",
    u"zwaveLogToIndigoEventLogOption": False,
    u"zwaveLogToPluginLogOption": False,
    u"zwaveLogToStandAloneFileOption": False,
    u"standAloneZwaveLogFolderPath": u"",
    u"standAloneZwaveLogFileName": u""
}


class Plugin(indigo.PluginBase):

    def __init__(self, plugin_id, plugin_display_name, plugin_version, plugin_prefs):
        super(Plugin, self).__init__(plugin_id, plugin_display_name, plugin_version, plugin_prefs)

        self.zwave_available_devices = dict()
        self.zwave_interpreted_devices = dict()

        # Initialise dictionary to store plugin Globals
        self.globals = dict()

        self.needToSavePrefs = True
        # if True:  # when adding a pref
        #     self.needToSavePrefs = True

        # Initialise Indigo plugin info
        self.globals[K_PLUGIN_INFO] = {}
        self.globals[K_PLUGIN_INFO][K_PLUGIN_ID] = plugin_id
        self.globals[K_PLUGIN_INFO][K_PLUGIN_DISPLAY_NAME] = plugin_display_name
        self.globals[K_PLUGIN_INFO][K_PLUGIN_VERSION] = plugin_version
        self.globals[K_PLUGIN_INFO][K_PATH] = indigo.server.getInstallFolderPath()
        self.globals[K_PLUGIN_INFO][K_API_VERSION] = indigo.server.apiVersion
        self.globals[K_PLUGIN_INFO][K_ADDRESS] = indigo.server.address

        log_format = logging.Formatter("%(asctime)s.%(msecs)03d\t%(levelname)-12s\t%(name)s.%(funcName)-25s %(msg)s", datefmt="%Y-%m-%d %H:%M:%S")
        self.plugin_file_handler.setFormatter(log_format)
        self.plugin_file_handler.setLevel(K_LOG_LEVEL_INFO)  # Logging Level for plugin log file
        self.indigo_log_handler.setLevel(K_LOG_LEVEL_INFO)   # Logging level for Indigo Event Log

        self.logger = logging.getLogger(u"Plugin.ZWI")

        # Now logging is set-up, output Initialising Message
        startup_message_ui = "\n"  # Start with a line break
        startup_message_ui += u"{0:={1}130}\n".format(u" Initialising Z-Wave Interpreter Plugin ", u"^")
        startup_message_ui += u"{0:<31} {1}\n".format(u"Plugin Name:", self.globals[K_PLUGIN_INFO][K_PLUGIN_DISPLAY_NAME])
        startup_message_ui += u"{0:<31} {1}\n".format(u"Plugin Version:", self.globals[K_PLUGIN_INFO][K_PLUGIN_VERSION])
        startup_message_ui += u"{0:<31} {1}\n".format(u"Plugin ID:", self.globals[K_PLUGIN_INFO][K_PLUGIN_ID])
        startup_message_ui += u"{0:<31} {1}\n".format(u"Indigo Version:", indigo.server.version)
        if self.versGreaterThanOrEq(indigo.server.apiVersion, u"2.5"):
            startup_message_ui += u"{0:<31} {1}\n".format(u"Indigo License:", indigo.server.licenseStatus)
        startup_message_ui += u"{0:<31} {1}\n".format(u"Indigo API Version:", indigo.server.apiVersion)
        startup_message_ui += u"{0:<31} {1}\n".format(u"Python Version:", sys.version.replace(u"\n", u""))
        startup_message_ui += u"{0:<31} {1}\n".format(u"Mac OS Version:", platform.mac_ver()[0])
        startup_message_ui += u"{0:={1}130}\n".format(u"", u"^")
        self.logger.info(startup_message_ui)

        # Set Plugin Config Values
        self.initialise_closedPrefsConfigUi = True
        self.closedPrefsConfigUi(plugin_prefs, False)

    def closedPrefsConfigUi(self, values_dict=None, user_cancelled=False):
        """
        Indigo method invoked after plugin configuration dialog is closed.

        -----
        :param values_dict:
        :param user_cancelled:
        :return:
        """

        try:
            if user_cancelled:
                return

            # Get required Event Log and Plugin Log logging levels
            self.event_log_level = int(values_dict.get(u"eventLogLevel", K_LOG_LEVEL_ZWAVE))
            self.plugin_log_level = int(values_dict.get(u"pluginLogLevel", K_LOG_LEVEL_ZWAVE))

            # Set initial required logging levels
            self.indigo_log_handler.setLevel(self.event_log_level)
            self.plugin_file_handler.setLevel( self.plugin_log_level)

            # Modify Logging levels dependant on Z-Wave Interpretations Requested

            if bool(values_dict.get(u"indigoEventLogDebug", False)):
                self.event_log_level = K_LOG_LEVEL_DEBUGGING
                self.indigo_log_handler.setLevel(self.event_log_level)

            zwave_log_to_indigo_event_log = bool(values_dict.get(u"zwaveLogToIndigoEventLogOption", False))
            if self.event_log_level != K_LOG_LEVEL_DEBUGGING:  # Check Debug not in process
                if self.initialise_closedPrefsConfigUi:
                    if zwave_log_to_indigo_event_log:
                        self.event_log_level = K_LOG_LEVEL_ZWAVE
                        self.indigo_log_handler.setLevel(self.event_log_level)
                    else:
                        self.event_log_level = K_LOG_LEVEL_INFO
                        self.indigo_log_handler.setLevel(self.event_log_level)
                    self.pluginPrefs[u"eventLogLevel"] = u"{0}".format(self.event_log_level)
                    indigo.server.savePluginPrefs()
            self.logger.info(u"Indigo Event Log set to '{0}'".format(K_LOG_LEVEL_TRANSLATION[self.event_log_level]))

            if bool(values_dict.get(u"pluginLogDebug", False)):
                self.plugin_log_level = K_LOG_LEVEL_DEBUGGING
                self.indigo_log_handler.setLevel(self.plugin_log_level)

            zwave_log_to_plugin_log = bool(self.pluginPrefs.get(u"zwaveLogToPluginLogOption", False))
            if self.plugin_log_level != K_LOG_LEVEL_DEBUGGING:  # Check Debug not in process
                if self.initialise_closedPrefsConfigUi:
                    if zwave_log_to_plugin_log:
                        self.plugin_log_level = K_LOG_LEVEL_ZWAVE
                        self.plugin_file_handler.setLevel(self.plugin_log_level)
                    else:
                        self.plugin_log_level = K_LOG_LEVEL_INFO
                        self.plugin_file_handler.setLevel(self.plugin_log_level)
                    self.pluginPrefs[u"pluginLogLevel"] = u"{0}".format(self.plugin_log_level)
                    indigo.server.savePluginPrefs()
            self.logger.info(u"Plugin Log set to '{0}'".format(K_LOG_LEVEL_TRANSLATION[self.plugin_log_level]))

            self.initialise_closedPrefsConfigUi = False

            if self.event_log_level <= K_LOG_LEVEL_ZWAVE:
                self.pluginPrefs[u"zwaveLogToIndigoEventLogOption"] = True
            else:
                self.pluginPrefs[u"zwaveLogToIndigoEventLogOption"] = False
            if self.plugin_log_level <= K_LOG_LEVEL_ZWAVE:
                self.pluginPrefs[u"zwaveLogToPluginLogOption"] = True
            else:
                self.pluginPrefs[u"zwaveLogToPluginLogOption"] = False
            indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'closedPrefsConfigUi' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

            return True

    def getMenuActionConfigUiValues(self, menu_id=0):

        # Indigo method called to pre-populate menu config dialogs.

        try:
            values_dict = indigo.Dict()

            values_dict[u"zwaveLogToIndigoEventLogOption"] = bool(self.pluginPrefs.get(u"zwaveLogToIndigoEventLogOption", False))
            values_dict[u"zwaveLogToPluginLogOption"] = bool(self.pluginPrefs.get(u"zwaveLogToPluginLogOption", False))
            values_dict[u"zwaveLogToStandAloneFileOption"] = bool(self.pluginPrefs.get(u"zwaveLogToStandAloneFileOption", False))

            stand_alone_zwave_log_folder_path = self.pluginPrefs.get(u"standAloneZwaveLogFolderPath", u"")
            if stand_alone_zwave_log_folder_path == u"":
                stand_alone_zwave_log_folder_path = u"{0}/Logs/com.autologplugin.indigoplugin.zwaveinterpreter/zwave_log".format(self.globals[K_PLUGIN_INFO][K_PATH])
                self.pluginPrefs[u"standAloneZwaveLogFolderPath"] = stand_alone_zwave_log_folder_path
                indigo.server.savePluginPrefs()
            values_dict[u"standAloneZwaveLogFolderPath"] = stand_alone_zwave_log_folder_path

            stand_alone_zwave_log_file_name = self.pluginPrefs.get(u"standAloneZwaveLogFileName", u"")
            if stand_alone_zwave_log_file_name == u"":
                stand_alone_zwave_log_file_name = u"zwave_interpreter_log.txt"
                self.pluginPrefs[u"standAloneZwaveLogFileName"] = stand_alone_zwave_log_file_name
                indigo.server.savePluginPrefs()
            values_dict[u"standAloneZwaveLogFileName"] = stand_alone_zwave_log_file_name

            self.zwave_available_devices = dict()
            self.zwave_interpreted_devices = dict()

            for zwave_dev in indigo.devices.iter(u"indigo.zwave"):
                zwave_dev_name = u"{0}".format(zwave_dev.name)
                zwave_props = zwave_dev.pluginProps
                if u"zwave_interpretation" in zwave_props and bool(zwave_props[u"zwave_interpretation"]):
                    self.zwave_interpreted_devices[zwave_dev.id] = zwave_dev_name
                else:
                    self.zwave_available_devices[zwave_dev.id] = zwave_dev_name

            values_dict[u"zwaveInterpretationMode"] = self.pluginPrefs[u"zwaveInterpretationMode"]

            errors_dict = indigo.Dict()

            return values_dict, errors_dict

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'getMenuActionConfigUiValues' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def evaluateZwaveInterpretationMode(self, values_dict, type_id):
        try:

            saved_zwave_interpretation_mode = self.pluginPrefs.get(u"zwaveInterpretationMode", u"S")
            updated_zwave_interpretation_mode = values_dict.get(u"zwaveInterpretationMode", u"S")
            # self.logger.warning(u"evaluateZwaveInterpretationMode: Saved='{0}', Updated='{1}'".format(saved_zwave_interpretation_mode, updated_zwave_interpretation_mode))
            if updated_zwave_interpretation_mode != saved_zwave_interpretation_mode:
                self.pluginPrefs[u"zwaveInterpretationMode"] = updated_zwave_interpretation_mode

                if updated_zwave_interpretation_mode == u"S":  # Selected Z-Wave devices only
                    interpreted_zwave_devices_list = list()
                    for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.iteritems():
                        interpreted_zwave_devices_list.append(int(zwave_dev_id))
                    self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)
                else:
                    # All Z-Wave devices
                    self.zwave_interpreter_class_instance.interpret_list(True, None)

                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'evaluateZwaveInterpretationMode' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def setZwaveLogToIndigoEventLogOption(self, values_dict, type_id):
        try:
            saved_zwave_log_to_indigo_event_log = bool(self.pluginPrefs.get(u"zwaveLogToIndigoEventLogOption", False))
            updated_zwave_log_to_indigo_event_log = bool(values_dict.get(u"zwaveLogToIndigoEventLogOption", False))
            if updated_zwave_log_to_indigo_event_log != saved_zwave_log_to_indigo_event_log:
                self.pluginPrefs[u"zwaveLogToIndigoEventLogOption"] = updated_zwave_log_to_indigo_event_log
                indigo.server.savePluginPrefs()

            if self.event_log_level != 5:  # Check Debug not in process
                if updated_zwave_log_to_indigo_event_log:
                    self.event_log_level = K_LOG_LEVEL_ZWAVE
                    self.indigo_log_handler.setLevel(self.event_log_level)
                else:
                    self.event_log_level = K_LOG_LEVEL_INFO
                    self.indigo_log_handler.setLevel(self.event_log_level)
                self.pluginPrefs[u"eventLogLevel"] = u"{0}".format(self.event_log_level)
                self.logger.info(u"Indigo Event Log set to '{0}'".format(K_LOG_LEVEL_TRANSLATION[self.event_log_level]))
                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'setZwaveLogToIndigoEventLogOption' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def setZwaveLogToPluginLogOption(self, values_dict, type_id):
        try:
            saved_zwave_log_to_plugin_log = bool(self.pluginPrefs.get(u"zwaveLogToPluginLogOption", False))
            updated_zwave_log_to_plugin_log = bool(values_dict.get(u"zwaveLogToPluginLogOption", False))
            if updated_zwave_log_to_plugin_log != saved_zwave_log_to_plugin_log:
                self.pluginPrefs[u"zwaveLogToPluginLogOption"] = updated_zwave_log_to_plugin_log
                indigo.server.savePluginPrefs()

            if self.plugin_log_level != 5:  # Check Debug not in process
                if updated_zwave_log_to_plugin_log:
                    self.plugin_log_level = K_LOG_LEVEL_ZWAVE
                    self.plugin_file_handler.setLevel(self.plugin_log_level)
                else:
                    self.plugin_log_level = K_LOG_LEVEL_INFO
                    self.plugin_file_handler.setLevel(self.plugin_log_level)
                self.pluginPrefs[u"pluginLogLevel"] = u"{0}".format(self.plugin_log_level)
                self.logger.info(u"Plugin Log set to '{0}'".format(K_LOG_LEVEL_TRANSLATION[self.plugin_log_level]))
                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'setZwaveLogToPluginLogOption' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def setZwaveLogToStandAloneLogOption(self, values_dict, type_id):
        try:
            saved_zwave_log_to_stand_alone_log = bool(self.pluginPrefs.get(u"zwaveLogToStandAloneFileOption", False))
            updated_zwave_log_to_stand_alone_log = bool(values_dict.get(u"zwaveLogToStandAloneFileOption", False))
            if updated_zwave_log_to_stand_alone_log != saved_zwave_log_to_stand_alone_log:
                self.pluginPrefs[u"zwaveLogToStandAloneFileOption"] = updated_zwave_log_to_stand_alone_log
                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'setZwaveLogToPluginLogOption' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def setZwaveLogToStandAloneLogFolderPath(self, values_dict, type_id):
        try:
            saved_zwave_log_to_stand_alone_log_folder_path = self.pluginPrefs.get(u"standAloneZwaveLogFolderPath", u"")
            updated_zwave_log_to_stand_alone_log_folder_path = values_dict.get(u"standAloneZwaveLogFolderPath", u"")
            if updated_zwave_log_to_stand_alone_log_folder_path != saved_zwave_log_to_stand_alone_log_folder_path:
                self.pluginPrefs[u"standAloneZwaveLogFolderPath"] = updated_zwave_log_to_stand_alone_log_folder_path
                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'setZwaveLogToStandAloneLogFolderPath' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def setZwaveLogToStandAloneLogFileName(self, values_dict, type_id):
        try:
            saved_zwave_log_to_stand_alone_log_file_name = self.pluginPrefs.get(u"standAloneZwaveLogFileName", u"")
            updated_zwave_log_to_stand_alone_log_file_name = values_dict.get(u"standAloneZwaveLogFileName", u"")
            if updated_zwave_log_to_stand_alone_log_file_name != saved_zwave_log_to_stand_alone_log_file_name:
                self.pluginPrefs[u"standAloneZwaveLogFileName"] = updated_zwave_log_to_stand_alone_log_file_name
                indigo.server.savePluginPrefs()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'setZwaveLogToStandAloneLogFilerName' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def getPrefsConfigUiValues(self):
        try:
            prefs_config_ui_values = self.pluginPrefs

            if "zwave_log_file_path" not in prefs_config_ui_values:
                prefs_config_ui_values["zwave_log_file_path"] = u"{0}/Logs/com.autologplugin.indigoplugin.zwaveinterpreter/zwave_logs".format(self.globals[K_PLUGIN_INFO][K_PATH])
            if "zwave_log_file_name" not in prefs_config_ui_values:
                prefs_config_ui_values["zwave_log_file_name"] = u"zwave_interpreter_log.txt"

            return prefs_config_ui_values

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'getPrefsConfigUiValues' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def shutdown(self):
        self.logger.threaddebug(u"shutdown called")

    def startup(self):
        try:
            if self.needToSavePrefs:
                indigo.server.savePluginPrefs()

            self.zwave_available_devices = dict()
            self.zwave_interpreted_devices = dict()

            for zwave_dev in indigo.devices.iter(u"indigo.zwave"):
                zwave_dev_name = u"{0}".format(zwave_dev.name)
                zwave_props = zwave_dev.pluginProps
                if u"zwave_interpretation" in zwave_props and bool(zwave_props[u"zwave_interpretation"]):
                    self.zwave_interpreted_devices[zwave_dev.id] = zwave_dev_name
                else:
                    self.zwave_available_devices[zwave_dev.id] = zwave_dev_name

            self.zwave_interpreter_class_instance = ZwaveInterpreter(self.logger, indigo.devices)  # Instantiate and initialise Z-Wave Interpreter Object

            # Having instantiated the Z-Wave Interpreter Object, determine what Z-Wave devices should be logged for it.
            zwave_interpretation_mode = self.pluginPrefs.get(u"zwaveInterpretationMode", u"S")
            if zwave_interpretation_mode == u"S":  # Selected Z-Wave devices only
                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.iteritems():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)
            else:
                # All Z-Wave devices
                self.zwave_interpreter_class_instance.interpret_list(True, None)

            # Intercept incoming and outgoing Z-Wave messages
            indigo.zwave.subscribeToIncoming()
            indigo.zwave.subscribeToOutgoing()

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'startup' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def zwaveCommandReceived(self, zwave_command):
        try:
            self.process_zwave_interpretation(ZW_RECEIVED, zwave_command)

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'zwaveCommandReceived' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def zwaveCommandSent(self, zwave_command):
        try:
            self.process_zwave_interpretation(ZW_SENT, zwave_command)

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'zwaveCommandSent' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    #################################
    #
    # Start of bespoke plugin methods
    #
    #################################

    def add_interpreted_zwave_devices(self, values_dict, type_iId):
        try:
            for dev_id in values_dict[u"available_zwave_devices_list"]:
                zwave_dev_id = int(dev_id)
                zwave_dev_name = self.zwave_available_devices.pop(zwave_dev_id)

                zwave_dev = indigo.devices[zwave_dev_id]
                props = zwave_dev.pluginProps
                props[u"zwave_interpretation"] = True
                zwave_dev.replacePluginPropsOnServer(props)

                self.zwave_interpreted_devices[zwave_dev_id] = zwave_dev_name

                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.iteritems():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)

            return values_dict

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'add_interpreted_zwave_devices' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def build_interpreted_zwave_devices_list(self, filter="", values_dict=None, type_id="", target_id=0):
        try:
            interpreted_zwave_devices_list = list()
            for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.iteritems():
                interpreted_zwave_devices_list.append((zwave_dev_id, zwave_dev_name))

            return sorted(interpreted_zwave_devices_list, key=lambda item: item[1])  # Sort list by Device Name

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'build_interpreted_zwave_devices_list' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def build_available_zwave_devices_list(self, filter="", values_dict=None, type_id="", target_id=0):
        try:
            available_zwave_devices_list = list()
            for zwave_dev_id, zwave_dev_name in self.zwave_available_devices.iteritems():
                available_zwave_devices_list.append((zwave_dev_id, zwave_dev_name))

            return sorted(available_zwave_devices_list, key=lambda item: item[1])  # Sort list by Device Name

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'build_available_zwave_devices_list' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def mkdir_with_mode(self, directory):
        try:
            # Forces Read | Write on creation so that the plugin can delete the folder id required
            if not os.path.isdir(directory):
                oldmask = os.umask(000)
                os.makedirs(directory, 0o777)
                os.umask(oldmask)
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'mkdir_with_mode' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def process_zwave_interpretation(self, send_receive_option, zwave_command):
        try:
            zw_interpretation = self.zwave_interpreter_class_instance.interpret_zwave(send_receive_option, zwave_command)
            if zw_interpretation[ZW_INTERPRETATION_ATTEMPTED]:
                # self.logger.warning(u"Z-Wave Interpreted")
                self.zwave_log(zw_interpretation[ZW_INTERPRETATION_OVERVIEW_UI], zw_interpretation[ZW_INTERPRETATION_DETAIL_UI])

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'process_zwave_interpretation' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def remove_interpreted_zwave_devices(self, values_dict, type_id):
        try:
            for dev_id in values_dict[u"interpreted_zwave_devices_list"]:
                zwave_dev_id = int(dev_id)
                zwave_dev_name = self.zwave_interpreted_devices.pop(zwave_dev_id)

                zwave_dev = indigo.devices[zwave_dev_id]
                props = zwave_dev.pluginProps
                props[u"zwave_interpretation"] = False
                zwave_dev.replacePluginPropsOnServer(props)

                self.zwave_available_devices[zwave_dev_id] = zwave_dev_name

                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.iteritems():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)

            return values_dict

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'remove_interpreted_zwave_devices' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def zwave_log(self, overview, detail):
        try:
            def zwave_log_to_file(overview, detail, logfile_path_and_name):
                try:
                    f = open(logfile_path_and_name, "ab")
                    f.write(overview)
                    f.write("\n")
                    f.write(detail)
                    f.write("\n\n")
                    f.close()
                except IOError as io_error_message:
                    self.logger.error(u"Z-wave Logging error: {0}".format(io_error_message))

            now = datetime.now()  # current date and time
            logged_date_time = (now.strftime("%Y-%m-%d %H:%M:%S.%f"))[:-3]  # e.g. '2020-11-03 00:00:11.688'
            output_overview = (u"{0} {1}".format(logged_date_time, overview)).encode("utf8")
            output_detail = (u"                              {0}".format(detail)).encode("utf8")

            if bool(self.pluginPrefs.get(u"zwaveLogToStandAloneFileOption", False)):
                if not os.path.exists(self.pluginPrefs[u"standAloneZwaveLogFolderPath"]):
                    self.mkdir_with_mode(self.pluginPrefs[u"standAloneZwaveLogFolderPath"])

                logfile_name = u"{0}/{1}".format(self.pluginPrefs[u"standAloneZwaveLogFolderPath"], self.pluginPrefs[u"standAloneZwaveLogFileName"])
                zwave_log_to_file(output_overview, output_detail, logfile_name)

            if self.logger.getEffectiveLevel() <= 10:
                self.logger.debug(u"{0} {1}\n                                   {2}\n".format(logged_date_time, overview, detail))

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'zwave_log' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
