import os
import math
import h5py
import numpy as np
from DDB.Data import Reader
from DDB.Service import Query


#对10kHz采样的信号进行加工处理
def process_10kHz(data):
    processed_data = []
    section = math.ceil(len(data) / 10)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(10 * j) :(10 * j + 10)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(10 * j):])
            processed_data.append(mean)
    return processed_data


#对50kHz采样的信号进行加工处理
def process_50kHz(data):
    processed_data = []
    section = math.ceil(len(data) / 50)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(50 * j) :(50 * j + 50)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(50 * j):])
            processed_data.append(mean)
    return processed_data


#对250kHz采样的信号进行加工处理
def process_250kHz(data):
    processed_data = []
    section = math.ceil(len(data) / 250)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(250 * j):(250 * j + 250)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(250 * j):])
            processed_data.append(mean)
    return processed_data


#对500kHz采样的信号进行加工处理
def process_500kHz(data):
    processed_data = []
    section = math.ceil(len(data) / 500)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(500 * j):(500 * j + 500)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(500 * j):])
            processed_data.append(mean)
    return processed_data


#对2MHz采样的信号进行加工处理
def process_2MHz(data):
    processed_data = []
    section = math.ceil(len(data) / 2000)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(2000 * j):(2000 * j + 2000)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(2000 * j):])
            processed_data.append(mean)
    return processed_data


#对10MHz采样的信号进行加工处理
def process_10MHz(data):
    processed_data = []
    section = math.ceil(len(data) / 10000)
    for j in range(section):
        if j < (section - 1):
            mean = np.mean(data[(10000 * j):(10000 * j + 10000)])
            processed_data.append(mean)
        else:
            mean = np.mean(data[(10000 * j):])
            processed_data.append(mean)
    return processed_data


#训练信号
all_tags = [
                r'\ip',
                r'\Bt',
                r'\axuv_ca_01',
                r'\vs_c3_aa001',
                r'\vs_ha_aa001',
                r'\sxr_cb_024',
                r'\sxr_cc_049',
                r'\Ivfp', r'\Ihfp',
                r'\MA_POL_CA01T', r'\MA_POL_CA02T', r'\MA_POL_CA23T', r'\MA_POL_CA24T'
            ]



size = 65
#调取可训练的炮号
root_path = os.path.dirname(__file__) + os.sep + r"data"
TrainNormal = np.load(root_path + os.sep + r"TrainData" + os.sep + r"TrainNormal.npy")
TrainBreak = np.load(root_path + os.sep + r"TrainData" + os.sep + r"TrainBreak.npy")
TrainNormal = list(TrainNormal)
TrainBreak = list(TrainBreak)
print(len(TrainNormal))
print(len(TrainBreak))
TrainShot = TrainNormal + TrainBreak


save_path = root_path + os.sep + r"ReduceSampling"
if not os.path.exists(save_path):
    os.makedirs(save_path)


n = 1
mistake = []
reader = Reader()
db = Query()
for shot in TrainShot:
    print("Shot:{}  ".format(shot) + "No.{}".format(n))
    n += 1
    try:
        shot_info = db.tag(int(shot))
        file = h5py.File(save_path + os.sep + r"{}.hdf5".format(shot))
        if not shot_info["IsDisrupt"]:
            DownTime = shot_info["RampDownTime"]
            for shottag in all_tags:
                dataset = reader.read_one(int(shot), shottag)
                data = dataset[0]
                time = dataset[1]
                data = data[time <= DownTime]
                time = time[time <= DownTime]
                data = data[time > 0.2]
                time = time[time > 0.2]
                datatemp = data[time < 0.21]
                if len(datatemp) < 200:
                    processed_data = process_10kHz(data)
                elif len(datatemp) < 700:
                    processed_data = process_50kHz(data)
                elif len(datatemp) < 3000:
                    processed_data = process_250kHz(data)
                elif len(datatemp) < 7000:
                    processed_data = process_500kHz(data)
                elif len(datatemp) < 40000:
                    processed_data = process_2MHz(data)
                else:
                    processed_data = process_10MHz(data)
                if len(processed_data) > size:
                    file.create_dataset("{}".format(shottag[1:]), data=processed_data)
                else:
                    mistake.append(shot)
        else:
            DownTime = shot_info["CqTime"]
            for shottag in all_tags:
                dataset = reader.read_one(int(shot), shottag)
                data = dataset[0]
                time = dataset[1]
                data = data[time <= DownTime]
                time = time[time <= DownTime]
                data = data[time > 0.2]
                time = time[time > 0.2]
                datatemp = data[time < 0.21]
                if len(datatemp) < 200:
                    processed_data = process_10kHz(data)
                elif len(datatemp) < 700:
                    processed_data = process_50kHz(data)
                elif len(datatemp) < 3000:
                    processed_data = process_250kHz(data)
                elif len(datatemp) < 7000:
                    processed_data = process_500kHz(data)
                elif len(datatemp) < 40000:
                    processed_data = process_2MHz(data)
                else:
                    processed_data = process_10MHz(data)
                if len(processed_data) > size:
                    file.create_dataset("{}".format(shottag[1:]), data=processed_data)
                else:
                    mistake.append(shot)
        file.close()
    except Exception as err:
        mistake.append(shot)
        file.close()

print("Length of mistake: {}".format(len(mistake)))
np.save(root_path + os.sep + r"mistake.npy", mistake)



