import os
import numpy as np
from DDB.Plot import Ploter


# 训练的信号名
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


#调取可训练的炮号
root_path = os.path.dirname(__file__) + os.sep + r"data" + os.sep + r"TrainData"
TrainNormal = np.load(root_path + os.sep + r"TrainNormal.npy")
TrainBreak = np.load(root_path + os.sep + r"TrainBreak.npy")
TrainNormal = list(TrainNormal)
TrainBreak = list(TrainBreak)
TrainShot = TrainNormal + TrainBreak
print(len(TrainShot))


save_path = os.path.dirname(__file__) + os.sep + r"plot"
if not os.path.exists(save_path):
    os.makedirs(save_path)
all_save = save_path + os.sep + r"all"
if not os.path.exists(all_save):
    os.makedirs(all_save)


pl = Ploter()
pl.plot_much(Taglist=all_tags, Shotlist=TrainShot, Savepath=all_save, ShowDownTime=True, ShowIpFlat=True)