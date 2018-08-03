#########################################
## I2C Device Register/Address         ##
#########################################
SCL_PIN         = 5
SDA_PIN         = 4
I2C_FREQ        = 400000

#########################################
## MAG3110 Magnetometer Registers      ##
#########################################
MAG_ADDRESS     = 0x0E
DR_STATUS       = 0x00
OUT_X_MSB       = 0x01
OUT_X_LSB       = 0x02
OUT_Y_MSB       = 0x03
OUT_Y_LSB       = 0x04
OUT_Z_MSB       = 0x05
OUT_Z_LSB       = 0x06
WHO_AM_I        = 0x07
SYSMOD          = 0x08
OFF_X_MSB       = 0x09
OFF_X_LSB       = 0x0A
OFF_Y_MSB       = 0x0B
OFF_Y_LSB       = 0x0C
OFF_Z_MSB       = 0x0D
OFF_Z_LSB       = 0x0E
DIE_TEMP        = 0x0F
CTRL_REG1       = 0x10
CTRL_REG2       = 0x11

#########################################
## MAG3110 WHO_AM_I Response           ##
#########################################
WHO_AM_I_RESULT = 0xC4

#########################################
## MAG3110 Commands and Settings       ##
#########################################
MAG3110_DR_OS_80_16         = 0x00
MAG3110_DR_OS_40_32         = 0x08
MAG3110_DR_OS_20_64         = 0x10
MAG3110_DR_OS_10_128        = 0x18
MAG3110_DR_OS_40_16         = 0x20
MAG3110_DR_OS_20_32         = 0x28
MAG3110_DR_OS_10_64	        = 0x30
MAG3110_DR_OS_5_128	        = 0x38
MAG3110_DR_OS_20_16	        = 0x40
MAG3110_DR_OS_10_32	        = 0x48
MAG3110_DR_OS_5_64	        = 0x50
MAG3110_DR_OS_2_5_128	    = 0x58
MAG3110_DR_OS_10_16	        = 0x60
MAG3110_DR_OS_5_32	        = 0x68
MAG3110_DR_OS_2_5_64	    = 0x70
MAG3110_DR_OS_1_25_128	    = 0x78
MAG3110_DR_OS_5_16		    = 0x80
MAG3110_DR_OS_2_5_32	    = 0x88
MAG3110_DR_OS_1_25_64       = 0x90
MAG3110_DR_OS_0_63_128	    = 0x98
MAG3110_DR_OS_2_5_16	    = 0xA0
MAG3110_DR_OS_1_25_32	    = 0xA8
MAG3110_DR_OS_0_63_64	    = 0xB0
MAG3110_DR_OS_0_31_128	    = 0xB8
MAG3110_DR_OS_1_25_16	    = 0xC0
MAG3110_DR_OS_0_63_32	    = 0xC8
MAG3110_DR_OS_0_31_64	    = 0xD0
MAG3110_DR_OS_0_16_128	    = 0xD8
MAG3110_DR_OS_0_63_16	    = 0xE0
MAG3110_DR_OS_0_31_32	    = 0xE8
MAG3110_DR_OS_0_16_64	    = 0xF0
MAG3110_DR_OS_0_08_128  	= 0xF8

#########################################
## CTRL_REG1 Settings                  ##
#########################################
MAG3110_FAST_READ           = 0x04
MAG3110_TRIGGER_MEASUREMENT	= 0x02
MAG3110_ACTIVE_MODE			= 0x01
MAG3110_STANDBY_MODE		= 0x00

#########################################
## CTRL_REG2 Settings                  ##
#########################################
MAG3110_AUTO_MRST_EN		= 0x80
MAG3110_RAW_MODE			= 0x20
MAG3110_NORMAL_MODE			= 0x00
MAG3110_MAG_RST				= 0x10

#########################################
## SYSMOD Readings                     ##
#########################################
MAG3110_SYSMOD_STANDBY		= 0x00
MAG3110_SYSMOD_ACTIVE_RAW	= 0x01
MAG3110_SYSMOD_ACTIVE		= 0x02

#########################################
## MAG3110 Axis Indices                ##
#########################################
MAG3110_X_AXIS              = 1
MAG3110_Y_AXIS              = 3
MAG3110_Z_AXIS              = 5

#########################################
## MAG3110 SYSMOD Descriptions         ##
#########################################
sys_mode_descriptions = ["STANDBY mode", "ACTIVE MODE, RAW data", "ACTIVE MODE, non-RAW user-corrected data"]