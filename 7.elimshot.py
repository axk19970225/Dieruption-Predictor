import os
import numpy as np
from DDB.Eliminate import eliminater


#训练的信号名
# all_tags = [
#                 r'\ip',
#                 r'\Bt',
#                 r'\axuv_ca_01',
#                 r'\vs_c3_aa001',
#                 r'\sxr_cb_024',
#                 r'\vs_ha_aa001',
#                 r'\sxr_cc_049',
#                 r'\Ivfp', r'\Ihfp',
#                 r'\MA_POL_CA01T', r'\MA_POL_CA02T', r'\MA_POL_CA23T', r'\MA_POL_CA24T'
#             ]


root_path = os.path.dirname(__file__) + os.sep + r"data"
breakshot = np.load(root_path + os.sep + "BreakVp.npy")
normalshot = np.load(root_path + os.sep + "NormalFilt.npy")
mistake = np.load(root_path + os.sep + r"mistake.npy")
print("Length of original break shots : {}".format(len(breakshot)))
print("Length of original normal shots: {}".format(len(normalshot)))

break_error =  [1065225,1065398,1065524,1065539,1065540,1065541,1065543,1065549,1065553,1065831,1066236,1066237,1066254,
                1066375,1066376,1066442,1066478,1066552,1066574] + list(mistake)
normal_error = [1064921,1064922,1065235,1065387,1065538,1065544,1065561,1065562,1065565,1065566,1065896,1065897,1065917,
                1066339,1066340,1066498,1066499,1066501,1066503,1066550,1066555,] + list(mistake)
print("Length of error break shots    : {}".format(len(break_error)))
print("Length of error normal shots   : {}".format(len(normal_error)))


el = eliminater()
TrainBreak = el.Elimshot(Biglist=breakshot, Smalllist=break_error)
TrainNormal = el.Elimshot(Biglist=normalshot, Smalllist=normal_error)
print("Length of break shots          : {}".format(len(TrainBreak)))
print("Length of normal shots         : {}".format(len(TrainNormal)))


save_path = root_path + os.sep + r"TrainData"
if not os.path.exists(save_path):
    os.makedirs(save_path)
np.save(save_path + os.sep + r"TrainBreak.npy", TrainBreak)
np.save(save_path + os.sep + r"TrainNormal", TrainNormal)