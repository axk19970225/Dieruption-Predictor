from MDSplus import connection
import numpy as np
import h5py
from DDB.Data import Exporter

#取1s内的数据
def fetch_data(tag):
    data = np.array(c.get(tag))     # diagnostic data
    time = np.array(c.get(r'DIM_OF(BUILD_PATH({}))'.format(tag)))    # DIM_OF(tag), time axis
    data = data[time >= 0]
    time = time[time >= 0]
    data = data[time <= 1]
    time = time[time <= 1]
    return data, time

#训练的信号名
all_tags = [
                r'\ip',
                r'\Bt',
                r'\axuv_ca_01',
                r'\sxr_cb_024',
                r'\vs_c3_aa001',
                r'\vs_ha_aa001',
                r'\sxr_cc_049',
                r'\exsad1', r'\exsad2', r'\exsad4', r'\exsad7', r'\exsad8', r'\exsad10',
                r'\Ivfp', r'\Ihfp',
                r'\MA_POL_CA01T', r'\MA_POL_CA02T', r'\MA_POL_CA03T', r'\MA_POL_CA04T', r'\MA_POL_CA05T', r'\MA_POL_CA06T',
                r'\MA_POL_CA07T', r'\MA_POL_CA08T', r'\MA_POL_CA09T', r'\MA_POL_CA10T', r'\MA_POL_CA11T', r'\MA_POL_CA12T',
                r'\MA_POL_CA13T', r'\MA_POL_CA14T', r'\MA_POL_CA15T', r'\MA_POL_CA16T', r'\MA_POL_CA17T', r'\MA_POL_CA18T',
                r'\MA_POL_CA19T', r'\MA_POL_CA20T', r'\MA_POL_CA21T', r'\MA_POL_CA22T', r'\MA_POL_CA23T', r'\MA_POL_CA24T',
                r'\vp', r'\vp2',
                r'\Polaris_Den_Rt01', r'\Polaris_Den_Rt02', r'\Polaris_Den_Rt03', r'\Polaris_Den_Rt04', r'\Polaris_Den_Rt05', r'\Polaris_Den_Rt06',
                r'\Polaris_Den_Rt07', r'\Polaris_Den_Rt08', r'\Polaris_Den_Rt09', r'\Polaris_Den_Rt10', r'\Polaris_Den_Rt11', r'\Polaris_Den_Rt12',
                r'\Polaris_Den_Rt13', r'\Polaris_Den_Rt14', r'\Polaris_Den_Rt15', r'\Polaris_Den_Rt16', r'\Polaris_Den_Rt17'
            ]
print(len(all_tags))


#shot_start = 1064014
shot_start = 1066648
shot_end = 1064034


exporter = Exporter(root_path=r'/nas/axk/data')
i = 0
while True:
    shot = shot_start - i
    if shot < shot_end:
        break
    print("第{}个".format(i+1) + "    炮号：{}".format(shot))
    i += 1
    c = connection.Connection('211.67.27.245')
    try:
        c.openTree('jtext', shot=shot)
        for tag in all_tags:
            try:
                data, time = fetch_data(tag)
                exporter.save(data, time, shot, tag)
            except Exception as err:
                pass
        c.closeAllTrees()
    except Exception as err:
        print(err)