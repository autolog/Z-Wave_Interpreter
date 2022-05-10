#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR = 0x01
ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT = 0x02
ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE = 0x03
ZW_SENSOR_MULTILEVEL_GET = 0x04
ZW_SENSOR_MULTILEVEL_REPORT = 0x05
ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT = 0x06

ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE = 0x01  # noqa [Duplicated code fragment!]
ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE = 0x02
ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE = 0x03
ZW_SENSOR_MULTILEVEL_TYPE_POWER = 0x04
ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY = 0x05

ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY = 0x06
ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION = 0x07
ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE = 0x08
ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE = 0x09
ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION = 0x0A

ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT = 0x0B

ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE = 0x0C
ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL = 0x0D
ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT = 0x0E
ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE = 0x0F
ZW_SENSOR_MULTILEVEL_TYPE_CURRENT = 0x10
ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL = 0x11
ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW = 0x12
ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY = 0x13
ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE = 0x14
ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION = 0x15
ZW_SENSOR_MULTILEVEL_TYPE_ROTATION = 0x16
ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE = 0x17
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE = 0x18
ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY = 0x19
ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE = 0x1A

ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET = 0x1B

ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY = 0x1C
ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY = 0x1D
ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS = 0x1E
ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE = 0x1F

ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY = 0x20
ZW_SENSOR_MULTILEVEL_TYPE_TIME = 0x21
ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE = 0x22
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5 = 0x23
ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL = 0x24
ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION = 0x25
ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY = 0x26
ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL = 0x27
ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL = 0x28
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY = 0x29
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY = 0x2A
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY = 0x2B
ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE = 0x2C
ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE = 0x2D
ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS = 0x2E
ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS = 0x2F

ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS = 0x30
ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW = 0x31
ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR = 0x32
ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI = 0x33
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS = 0x34
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS = 0x35
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS = 0x36
ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY = 0x37
ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW = 0x38
ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE = 0x39
ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH = 0x3A
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10 = 0x3B
ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE = 0x3C
ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL = 0x3D
ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE = 0x3E
ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE = 0x3F

ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE = 0x40
ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE = 0x41
ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL = 0x42
ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY = 0x43
ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA = 0x44
ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO = 0x45
ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION = 0x46
ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR = 0x47
ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE = 0x48
ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE = 0x49
ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE = 0x4A
ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE = 0x4B
ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE = 0x4C
ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE = 0x4D
ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE = 0x4E
ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE = 0x4F

ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST = 0x50
ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3 = 0x51
ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2 = 0x52
ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2 = 0x53
ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3 = 0x54
ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB = 0x55
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1 = 0x56

ZW_SCALE_CELSIUS = 0x00
ZW_SCALE_FAHRENHEIT = 0x01
ZW_SCALE_PERCENTAGE = 0x00
ZW_SCALE_LUX = 0x01
ZW_SCALE_HUMIDITY = 0x01
ZW_SCALE_DIMENSIONLESS_VALUE = 0x01
ZW_SCALE_WATT = 0x00
ZW_SCALE_BTU_H = 0x01
ZW_SCALE_UV_INDEX = 0x00


class ZwaveSensorMultilevel:
    """
    Z-Wave Command Class: Thermostat Multilevel "0x31" [Decimal 49]

    """

    #     def __init__(self, logger, utility, command_classes, zw_interpretation):
    def __init__(self, parent):
        try:
            self.exception_handler = parent.exception_handler
            self.logger = parent.logger
            self.utility = parent.utility
            self.command_classes = parent.zw_command_classes
            self.zw_interpretation = parent.zw_interpretation

            self.command_classes[ZW_SENSOR_MULTILEVEL] = dict()
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_IDENTIFIER] = "Multilevel Sensor"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR] = "Get Supported Sensor"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT] = "Supported Sensor Report"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE] = "Get Supported Scale"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_GET] = "Get"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_REPORT] = "Report"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT] = "Supported Scale Report"

            self.zw_sensor_multilevel_types = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_IDENTIFIER] = "Air Temperature"  # 0x01
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_IDENTIFIER] = "General Purpose"  # 0x02
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES][ZW_SCALE_PERCENTAGE] = ("Percentage Value (%)", "%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES][ZW_SCALE_DIMENSIONLESS_VALUE] = ("Dimensionless", " Dimensionless")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_IDENTIFIER] = "Illuminance"  # 0x03
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES][ZW_SCALE_PERCENTAGE] = ("Percentage Value (%)", "%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES][ZW_SCALE_LUX] = ("Lux", " Lux")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_IDENTIFIER] = "Power"  # 0x04
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES][ZW_SCALE_WATT] = ("Watt (W)", " W")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES][ZW_SCALE_BTU_H] = ("Btu/h", " Btu/h")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_IDENTIFIER] = "Humidity"  # 0x05
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES][ZW_SCALE_PERCENTAGE] = ("Percentage Value (%)", "%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES][ZW_SCALE_HUMIDITY] = ("Absolute humidity (g/m3)", " g/m3")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY][ZW_IDENTIFIER] = "Velocity"  # 0x06

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION][ZW_IDENTIFIER] = "Direction"  # 0x07

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE][ZW_IDENTIFIER] = "Atmospheric pressure"  # 0x08

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE][ZW_IDENTIFIER] = "Barometric pressure"  # 0x09

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION][ZW_IDENTIFIER] = "Solar radiation"  # 0x0A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_IDENTIFIER] = "Dew Point"  # 0x0B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE][ZW_IDENTIFIER] = "Rain Rate"  # 0x0C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL][ZW_IDENTIFIER] = "Tide Level"  # 0x0D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT][ZW_IDENTIFIER] = "Weight"  # 0x0E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE][ZW_IDENTIFIER] = "Voltage"  # 0x0F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CURRENT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CURRENT][ZW_IDENTIFIER] = "Current"  # 0x10

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL][ZW_IDENTIFIER] = "Carbon Dioxide [CO2] Level"  # 0x11

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW][ZW_IDENTIFIER] = "Air Flow"  # 0x12

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY][ZW_IDENTIFIER] = "Tank Capacity"  # 0x13

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE][ZW_IDENTIFIER] = "Distance"  # 0x14

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION][ZW_IDENTIFIER] = "Angle Position"  # 0x15

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ROTATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ROTATION][ZW_IDENTIFIER] = "Rotation"  # 0x16

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_IDENTIFIER] = "Water Temperature"  # 0x17
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_IDENTIFIER] = "Soil Temperature"  # 0x18
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY][ZW_IDENTIFIER] = "Seismic Intensity"  # 0x19

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE][ZW_IDENTIFIER] = "Seismic Magnitude"  # 0x1A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_IDENTIFIER] = "Ultraviolet"  # 0x1B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_SCALES][ZW_SCALE_UV_INDEX] = ("UV Index", " UV Index")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY][ZW_IDENTIFIER] = "Electrical Resistivity"  # 0x1C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY][ZW_IDENTIFIER] = "Electrical Conductivity"  # 0x1D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS][ZW_IDENTIFIER] = "Loudness"  # 0x1E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE][ZW_IDENTIFIER] = "Moisture"  # 0x1F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY][ZW_IDENTIFIER] = "Frequency"  # 0x20

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIME] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIME][ZW_IDENTIFIER] = "Time"  # 0x21

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_IDENTIFIER] = "Target Temperature"  # 0x22
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5][ZW_IDENTIFIER] = "Particulate Matter 2.5"  # 0x23

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL][ZW_IDENTIFIER] = "Formaldehyde [CH2O] Level"  # 0x24

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION][ZW_IDENTIFIER] = "Radon Concentration"  # 0x25

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY][ZW_IDENTIFIER] = "Methane [CH4] Density"  # 0x26

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL][ZW_IDENTIFIER] = "Volatile Organic Compound Level"  # 0x27

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL][ZW_IDENTIFIER] = "Carbon Monoxide [CO] Level"  # 0x28

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY][ZW_IDENTIFIER] = "Soil Humidity"  # 0x29

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY][ZW_IDENTIFIER] = "Soil Reactivity"  # 0x2A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY][ZW_IDENTIFIER] = "Soil Salinity"  # 0x2B

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE][ZW_IDENTIFIER] = "Heart Rate"  # 0x2C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE][ZW_IDENTIFIER] = "Blood Pressure"  # 0x2D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS][ZW_IDENTIFIER] = "Muscle Mass"  # 0x2E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS][ZW_IDENTIFIER] = "Fat Mass"  # 0x2F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS][ZW_IDENTIFIER] = "Bone Mass"  # 0x30

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW][ZW_IDENTIFIER] = "Total Body Water [TBW]"  # 0x31

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR][ZW_IDENTIFIER] = "Basis Metabolic Rate [BMR]"  # 0x32

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI][ZW_IDENTIFIER] = "Body Mass Index [BMI]"  # 0x33

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS][ZW_IDENTIFIER] = "Acceleration X-Axis"  # 0x34

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS][ZW_IDENTIFIER] = "Acceleration Y-Axis"  # 0x35

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS][ZW_IDENTIFIER] = "Acceleration Z-Axis"  # 0x36

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY][ZW_IDENTIFIER] = "Smoke Density"  # 0x37

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW][ZW_IDENTIFIER] = "Water Flow"  # 0x38

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE][ZW_IDENTIFIER] = "Water Pressure"  # 0x39

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH][ZW_IDENTIFIER] = "RF Signal Strength"  # 0x3A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10][ZW_IDENTIFIER] = "Particulate Matter 10"  # 0x3B

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE][ZW_IDENTIFIER] = "Respiratory Rate"  # 0x3C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL][ZW_IDENTIFIER] = "Relative Modulation Level"  # 0x3D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_IDENTIFIER] = "Boiler Water Temperature"  # 0x3E
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_IDENTIFIER] = "Domestic Hot Water [DHW] Temperature"  # 0x3F
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_IDENTIFIER] = "Outside Temperature"  # 0x40
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_IDENTIFIER] = "Exhaust Temperature"  # 0x41
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL][ZW_IDENTIFIER] = "Water Chlorine Level"  # 0x42

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY][ZW_IDENTIFIER] = "Water Acidity"  # 0x43

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA][ZW_IDENTIFIER] = "Water Oxidation Reduction Potential"  # 0x44

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO][ZW_IDENTIFIER] = "Heart Rate LF/HF Ratio"  # 0x45

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION][ZW_IDENTIFIER] = "Motion Direction"  # 0x46

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR][ZW_IDENTIFIER] = "Applied Force On The Sensor"  # 0x47

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_IDENTIFIER] = "Return Air Temperature"  # 0x48
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_IDENTIFIER] = "Supply Air Temperature"  # 0x49
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_IDENTIFIER] = "Condenser Coil Temperature"  # 0x4A
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_IDENTIFIER] = "Evaporator Coil Temperature"  # 0x4B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_IDENTIFIER] = "Liquid Line Temperature"  # 0x4C
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_IDENTIFIER] = "Discharge Line Temperature"  # 0x4D
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE][ZW_IDENTIFIER] = "Suction [Input Pump/Compressor] Pressure"  # 0x4E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE][ZW_IDENTIFIER] = "Discharge (output Pump/compressor) Pressure"  # 0x4F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_IDENTIFIER] = "Defrost Temperature [Sensor Used To Decide When To Defrost]"  # 0x50
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES][ZW_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3][ZW_IDENTIFIER] = "Ozone (o3)"  # 0x51

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2][ZW_IDENTIFIER] = "Sulfur Dioxide (so2)"  # 0x52

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2][ZW_IDENTIFIER] = "XXXNitrogen Dioxide (no2)XXXXXXX"  # 0x53

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3][ZW_IDENTIFIER] = "Ammonia (nh)"  # 0x54

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB][ZW_IDENTIFIER] = "Lead (pb)"  # 0x55

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1][ZW_IDENTIFIER] = "Particulate Matter 1"  # 0x56

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self, zw_command, zw_command_detail):
        try:
            if zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_GET:
                self._interpret_get(zw_command_detail)
                return
            elif zw_command == ZW_SENSOR_MULTILEVEL_REPORT:
                self._interpret_report(zw_command_detail)
                return
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_get(self, zw_command_detail):  # noqa [Unused local symbols]
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self, zw_command_detail):
        try:
            # sensor_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0]
            # precision_scale_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
            sensor_type = zw_command_detail[0]
            precision_scale_size = zw_command_detail[1]
            precision = (precision_scale_size & 0b11100000) >> 5
            scale = (precision_scale_size & 0b00011000) >> 3
            if sensor_type in self.zw_sensor_multilevel_types:
                if scale in self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES]:
                    scale_ui = self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES][scale][0]
                    scale_ui_compact = self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES][scale][1]
                else:
                    scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
            else:
                scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
            size = precision_scale_size & 0b00000111
            end_value = 2 + size
            # value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            # if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
            value = self.utility.bytes_to_int(zw_command_detail[2:end_value])
            if zw_command_detail[2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = f"{{:.{precision}f}}"
            value_ui = value_ui_format.format(float(value) / 10 ** precision)

            self.zw_interpretation[ZW_SENSOR_TYPE] = sensor_type
            if sensor_type in self.zw_sensor_multilevel_types:
                self.zw_interpretation[ZW_SENSOR_TYPE_UI] = self.zw_sensor_multilevel_types[sensor_type][ZW_IDENTIFIER]
            else:
                self.zw_interpretation[ZW_SENSOR_TYPE_UI] = f"Sensor Type {sensor_type} unknown"
            self.zw_interpretation[ZW_PRECISION] = precision  # noqa [Duplicated code fragment!]
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            zw_interpretation_ui = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Sensor: '{self.zw_interpretation[ZW_SENSOR_TYPE_UI]}', Value: '{self.zw_interpretation[ZW_VALUE_UI]}{self.zw_interpretation[ZW_SCALE_UI_COMPACT]}'")

            self.zw_interpretation[ZW_INTERPRETATION_UI] = zw_interpretation_ui

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
