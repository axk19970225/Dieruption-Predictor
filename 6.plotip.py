import os
import numpy as np
from DDB.Plot import Ploter


#训练的信号名
# all_tags = [
#                 r'\ip',
#                 r'\Bt',
#                 r'\axuv_ca_01',
#                 r'\vs_c3_aa001',
#                 r'\vs_ha_aa001',
#                 r'\sxr_cb_024',
#                 r'\sxr_cc_049',
#                 r'\Ivfp', r'\Ihfp',
#                 r'\MA_POL_CA01T', r'\MA_POL_CA02T', r'\MA_POL_CA23T', r'\MA_POL_CA24T'
#             ]


root_path = os.path.dirname(__file__) + os.sep + r"data"
breakshot = np.load(root_path + os.sep + "BreakVp.npy")
normalshot = np.load(root_path + os.sep + "NormalFilt.npy")
print(len(breakshot))
print(len(normalshot))


save_path = os.path.dirname(__file__) + os.sep + r"plot"
if not os.path.exists(save_path):
    os.makedirs(save_path)
break_save = save_path + os.sep + r"break"
normal_save = save_path + os.sep + r"normal"
if not os.path.exists(break_save):
    os.makedirs(break_save)
if not os.path.exists(normal_save):
    os.makedirs(normal_save)


pl = Ploter()
pl.plot_much(Taglist=[r"\ip"], Shotlist=breakshot, Savepath=break_save, ShowDownTime=True)
pl.plot_much(Taglist=[r"\ip"], Shotlist=normalshot, Savepath=normal_save, ShowDownTime=True)