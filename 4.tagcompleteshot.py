import os
import numpy as np
from DDB.Eliminate import eliminater

#训练的信号名
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
print(len(all_tags))
root_path = os.path.dirname(__file__) + os.sep + r"data"
Break = np.load(root_path + os.sep + "Break.npy")
Normal = np.load(root_path + os.sep + "Normal.npy")


tc = eliminater()
breaklist = tc.TCShotlist(Taglist=all_tags, Shotlist=Break, Detail=True)
normallist = tc.TCShotlist(Taglist=all_tags, Shotlist=Normal, Detail=True)
print(len(breaklist))
print(len(normallist))

np.save(root_path + os.sep + "BreakFilt.npy", breaklist)
np.save(root_path + os.sep + "NormalFilt.npy", normallist)