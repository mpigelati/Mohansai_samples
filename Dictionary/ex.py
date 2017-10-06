import datetime
import time
json_list = [
    {
        "Id": "dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4",
        "Created": "2017-07-11T15:07:58.990959648Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "exited",
            "Running": "false",
            "Paused": "false",
            "Restarting": "false",
            "OOMKilled": "false",
            "Dead": "false",
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2017-07-11T15:07:59.869672233Z",
            "FinishedAt": "2017-07-11T15:08:00.169576836Z"
        }
    }
]

start_time = json_list[0]["State"]["StartedAt"]
print (start_time)
#start_datetime = my_date_time_mod.convert_docker_date_time_to_datetime(start_time)
#print start_datetime

finish_time = json_list[0]["State"]["FinishedAt"]
#finish_datetime = my_date_time_mod.convert_docker_date_time_to_datetime(finish_time)
#print finish_datetime

data=[{
    "Image_Build_IDs": {
        "adsp": "ADSP.HT.3.0-00374-CB8998-1",
        "apps": "LA.UM.6.4-27202-8x98.1-1",
        "boot": "BOOT.XF.1.2.2.c1-00023-M8998LAB-1",
        "btfm": "BTFM.CHE.2.1.1-00130-QCACHROM-1",
        "common": "MSM8998.LA.2.0.1.1-21029-INT-1",
        "cpev2": "CPE.TSF.2.0-00006-W9335AAAAAAAAQ-1",
        "glue": "GLUE.MSM8998_LA.2.0.1.1-00009-NOOP_TEST-1",
        "modem": "MPSS.AT.2.5.c1-00090-8998_GEN_TEST-1",
        "rpm": "RPM.BF.1.7-00128-M8998AAAAANAAR-1",
        "slpi": "SLPI.HB.2.0-00167-M8998AAL-1",
        "spss": "SPSS.A1.1.0-00027-M8998AAAAANAAS-1",
        "tz": "TZ.BF.4.0.6-00130-M8998AAAAANAAT-1",
        "video": "VIDEO.VE.4.4-00026-PROD-1",
        "wapi": "WLAN_ADDON.HL.1.0-00006-CNSS_RMZ_WAPI-1",
        "wdsp": "WDSP.9340.1.0.c1-00008-W9340AAAAAAAAQ-1",
        "wgig": "WIGIG.SPR.5.2-00009-WIGIGSW-5",
        "wlan": "WLAN.HL.1.1-00592-QCAHLSW8998MTPL-1"
    },
    "Metabuild_Info": {
        "Meta_Build_ID": "MSM8998.LA.2.0.1.1-21029-INT-1",
        "Product_Flavor": "asic",
        "Time_Stamp": "2017-08-31 04:56:34"
    },
    "Version": "1.0"
}]


print (data[0]["Metabuild_Info"]["Meta_Build_ID"])
#print ("Metabuild_Info"[5])