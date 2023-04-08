
BALBOA_DEFAULT_PORT = 4257

M_STARTEND = 0x7E

C_PUMP1 = 0x04
C_PUMP2 = 0x05
C_PUMP3 = 0x06
C_PUMP4 = 0x07
C_PUMP5 = 0x08
C_PUMP6 = 0x09
C_LIGHT1 = 0x11
C_LIGHT2 = 0x12
C_MISTER = 0x0E
C_AUX1 = 0x16
C_AUX2 = 0x17
C_BLOWER = 0x0C
C_TEMPRANGE = 0x50
C_HEATMODE = 0x51

MAX_PUMPS = 6

NROF_BMT = 14

(
    BMTR_STATUS_UPDATE,
    BMTR_FILTER_INFO_RESP,
    BMTS_CONFIG_REQ,
    BMTR_MOD_IDENT_RESP,
    BMTS_FILTER_REQ,
    BMTS_CONTROL_REQ,
    BMTS_SET_TEMP,
    BMTS_SET_TIME,
    BMTS_SET_WIFI,
    BMTS_PANEL_REQ,
    BMTS_SET_TSCALE,
    BMTR_DEVICE_CONFIG_RESP,
    BMTR_SYS_INFO_RESP,
    BMTR_SETUP_PARAMS_RESP,
) = range(0, NROF_BMT)

mtypes = [
    [0xFF, 0xAF, 0x13],  # BMTR_STATUS_UPDATE
    [0x0A, 0xBF, 0x23],  # BMTR_FILTER_INFO_RESP
    [0x0A, 0xBF, 0x04],  # BMTS_CONFIG_REQ
    [0x0A, 0xBF, 0x94],  # BMTR_MOD_IDENT_RESP
    [0x0A, 0xBF, 0x22],  # BMTS_FILTER_REQ
    [0x0A, 0xBF, 0x11],  # BMTS_CONTROL_REQ
    [0x0A, 0xBF, 0x20],  # BMTS_SET_TEMP
    [0x0A, 0xBF, 0x21],  # BMTS_SET_TIME
    [0x0A, 0xBF, 0x92],  # BMTS_SET_WIFI
    [0x0A, 0xBF, 0x22],  # BMTS_PANEL_REQ
    [0x0A, 0xBF, 0x27],  # BMTS_SET_TSCALE
    [0x0A, 0xBF, 0x2E],  # BMTR_DEVICE_CONFIG_RESP
    [0x0A, 0xBF, 0x24],  # BMTR_SYS_INFO_RESP
    [0x0A, 0xBF, 0x25],  # BMTR_SETUP_PARAMS_RESP
]

text_heatmode = ["Ready", "Rest", "Ready in Rest"]
text_heatstate = ["Idle", "Heating", "Heat Waiting"]
text_tscale = ["Fahrenheit", "Celcius"]
text_timescale = ["12h", "24h"]
text_pump = ["Off", "Low", "High"]
text_temprange = ["Low", "High"]
text_blower = ["Off", "Low", "Medium", "High"]
text_switch = ["Off", "On"]
text_filter = ["Off", "Cycle 1", "Cycle 2", "Cycle 1 and 2"]

"""	
The CRC is annoying.  Doing CRC's in python is even more annoying than it	
should be.  I hate it.	
 * Generated on Sun Apr  2 10:09:58 2017,	
 * by pycrc v0.9, https://pycrc.org	
 * using the configuration:	
 *    Width         = 8	
 *    Poly          = 0x07	
 *    Xor_In        = 0x02	
 *    ReflectIn     = False	
 *    Xor_Out       = 0x02	
 *    ReflectOut    = False	
 *    Algorithm     = bit-by-bit	
https://github.com/garbled1/gnhast/blob/master/balboacoll/collector.c	
"""
