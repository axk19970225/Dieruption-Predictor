import os
import pprint
import numpy as np
from DDB.Eliminate import eliminater
import matplotlib.pyplot as plt


#训练的信号名
# lf_tags = [
#             r'\ip',
#             r'\Bt',
#             r'\axuv_ca_01',
#             r'\sxr_cb_024',
#             r'\vs_c3_aa001',
#             r'\vs_ha_aa001',
#             r'\sxr_cc_049',
#             r'\exsad1', r'\exsad2', r'\exsad4', r'\exsad7', r'\exsad8', r'\exsad10',
#             r'\Ivfp', r'\Ihfp'
#         ]
#
# hf_tags = [
#             r'\MA_POL_CA01T', r'\MA_POL_CA02T', r'\MA_POL_CA03T', r'\MA_POL_CA04T', r'\MA_POL_CA05T', r'\MA_POL_CA06T',
#             r'\MA_POL_CA07T', r'\MA_POL_CA08T', r'\MA_POL_CA09T', r'\MA_POL_CA10T', r'\MA_POL_CA11T', r'\MA_POL_CA12T',
#             r'\MA_POL_CA13T', r'\MA_POL_CA14T', r'\MA_POL_CA15T', r'\MA_POL_CA16T', r'\MA_POL_CA17T', r'\MA_POL_CA18T',
#             r'\MA_POL_CA19T', r'\MA_POL_CA20T', r'\MA_POL_CA21T', r'\MA_POL_CA22T', r'\MA_POL_CA23T', r'\MA_POL_CA24T'
#         ]
# all_tags =  lf_tags + hf_tags


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


root_path = os.path.dirname(__file__) + os.sep + r"data"
validshot = np.load(root_path + os.sep + "Valid.npy")

tc = eliminater()
tc.TagNum(Taglist=all_tags, Shotlist=validshot)

"""
可用诊断：

all_tags = [
                r'\ip',
                r'\Bt',
                r'\axuv_ca_01',
                r'\vs_c3_aa001',
                r'\vs_ha_aa001',
                r'\sxr_cc_049',
                r'\Polaris_Den_Rt01', r'\Polaris_Den_Rt02', r'\Polaris_Den_Rt03', r'\Polaris_Den_Rt04', r'\Polaris_Den_Rt05',
                r'\Polaris_Den_Rt06', r'\Polaris_Den_Rt07', r'\Polaris_Den_Rt08', r'\Polaris_Den_Rt09', r'\Polaris_Den_Rt10',
                r'\Polaris_Den_Rt11'
            ]
"""



