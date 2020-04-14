import os
import h5py
import numpy as np

TimeWidth = 32                    #时间窗长度
BreakTime = 30
InvalidTime = 5
standard = {                      #归一化基准
            'ip': 220,
            'Bt': 2,
            'axuv_ca_01': 10,
            'sxr_cb_024': 1.5,
            'sxr_cc_049': 7,
            'vs_c3_aa001': 7,
            'vs_ha_aa001': 1,
            'exsad1': 6, 'exsad2': 2.5, 'exsad4': 1.3, 'exsad7': 4, 'exsad8': 1, 'exsad10': 6,
            'Ivfp': 3,
            'Ihfp': 1,
            'MA_POL_CA01T': 1, 'MA_POL_CA02T': 1, 'MA_POL_CA03T': 1, 'MA_POL_CA05T': 1, 'MA_POL_CA06T': 1,
            'MA_POL_CA07T': 1, 'MA_POL_CA19T': 1, 'MA_POL_CA20T': 1, 'MA_POL_CA21T': 1, 'MA_POL_CA22T': 1,
            'MA_POL_CA23T': 1, 'MA_POL_CA24T': 1,
            'Polaris_Den_Rt01': 5 , 'Polaris_Den_Rt02': 225,  'Polaris_Den_Rt03': 10, 'Polaris_Den_Rt04': 10,
            'Polaris_Den_Rt05': 10, 'Polaris_Den_Rt06': 10,  'Polaris_Den_Rt07': 5, 'Polaris_Den_Rt08': 10,
            'Polaris_Den_Rt09': 5, 'Polaris_Den_Rt10':10, 'Polaris_Den_Rt11':5
            }

print(len(standard))

#训练信号
# all_tags = [
#                 r'\ip',
#                 r'\Bt',
#                 r'\axuv_ca_01',
#                 r'\vs_c3_aa001',
#                 r'\vs_ha_aa001',
#                 r'\sxr_cc_049',
#                 r'\Polaris_Den_Rt01', r'\Polaris_Den_Rt03', r'\Polaris_Den_Rt04', r'\Polaris_Den_Rt05',
#                 r'\Polaris_Den_Rt06', r'\Polaris_Den_Rt08', r'\Polaris_Den_Rt09', r'\Polaris_Den_Rt10',
#                 r'\Polaris_Den_Rt11'
#             ]


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


for i in range(len(all_tags)):       #去掉\
    all_tags[i] = all_tags[i][1:]

root_path = os.path.dirname(__file__) + os.sep + r"data"
#训练集
TrainBreak = np.load(root_path + os.sep + r"TrainData" + os.sep + r"BreakTrain.npy")
TrainNormal = np.load(root_path + os.sep + r"TrainData" + os.sep + r"NormalTrain.npy")
#测试集
# TrainBreak = np.load(root_path + os.sep + r"TrainData" + os.sep + r"BreakTest.npy")
# TrainNormal = np.load(root_path + os.sep + r"TrainData" + os.sep + r"NormalTest.npy")


hdf5_path = root_path + os.sep + r"ReduceSampling"


n = 1
PositiveAllData = np.mat(np.ones((1, len(all_tags)*TimeWidth)))
for num in TrainNormal:
    print("Shot:{}  ".format(num) + "No.{}".format(n))
    n += 1
    g = h5py.File(hdf5_path + os.sep + r"{}.hdf5".format(num), 'r')
    data = g.get("ip")
    step = len(data) - TimeWidth + 1
    incident = np.mat(np.ones((step, 1)))
    for tag in all_tags:
        data = g.get(tag)
        data = (np.array(data)) / (standard[tag])
        chip = []
        for i in range(step):
            chip.append(data[i : (i + TimeWidth)])
        chip = np.mat(chip)
        incident = np.hstack((incident,chip))
    incident = np.delete(incident, 0, axis=1)
    print(incident.shape)
    g.close()
    PositiveAllData = np.vstack((PositiveAllData,incident))
PositiveAllData = np.delete(PositiveAllData, 0, axis=0)


NegativeAllData = np.mat(np.ones((1, len(all_tags)*TimeWidth)))
for num in TrainBreak:
    print("Shot:{}  ".format(num) + "No.{}".format(n))
    n += 1
    g = h5py.File(hdf5_path + os.sep + r"{}.hdf5".format(num), 'r')
    data = g.get("ip")
    StepNormal = len(data) - TimeWidth - BreakTime + 1
    incident = np.mat(np.ones((StepNormal, 1)))
    for tag in all_tags:
        data = g.get(tag)
        data = (np.array(data)) / (standard[tag])
        chip = []
        for i in range(StepNormal):
            chip.append(data[i : (i + TimeWidth)])
        chip = np.mat(chip)
        incident = np.hstack((incident,chip))
    incident = np.delete(incident, 0, axis=1)
    print(incident.shape)
    PositiveAllData = np.vstack((PositiveAllData,incident))
    StepInvalid = len(data) - TimeWidth - InvalidTime + 1
    NegativeIncident = np.mat(np.ones(((BreakTime - InvalidTime), 1)))
    for tag in all_tags:
        data = g.get(tag)
        data = (np.array(data)) / (standard[tag])
        chip = []
        for i in range(StepNormal,StepInvalid):
            chip.append(data[i : (i + TimeWidth)])
        chip = np.mat(chip)
        NegativeIncident = np.hstack((NegativeIncident, chip))
    NegativeIncident = np.delete(NegativeIncident, 0, axis=1)
    NegativeAllData = np.vstack((NegativeAllData,NegativeIncident))
    g.close()
NegativeAllData = np.delete(NegativeAllData, 0, axis=0)

PositiveAllData = np.array(PositiveAllData)
NegativeAllData = np.array(NegativeAllData)
print(PositiveAllData.shape)
print(NegativeAllData.shape)


#训练集
np.save(root_path + os.sep + r"TrainData" + os.sep + r"TrainPositive.npy",PositiveAllData)
np.save(root_path + os.sep + r"TrainData" + os.sep + r"TrainNegative.npy",NegativeAllData)
#测试集
# np.save(root_path + os.sep + r"TrainData" + os.sep + r"TestPositive.npy",PositiveAllData)
# np.save(root_path + os.sep + r"TrainData" + os.sep + r"TestNegative.npy",NegativeAllData)