import os
import numpy as np
from DDB.Eliminate import eliminater


root_path = os.path.dirname(__file__) + os.sep + r"data"
Break = np.load(root_path + os.sep + "BreakFilt.npy")

vp = eliminater()
breakvp = vp.Vpfiltshot(Shotlist=Break, Detail=True)

np.save(root_path + os.sep + "BreakVp.npy",breakvp)



