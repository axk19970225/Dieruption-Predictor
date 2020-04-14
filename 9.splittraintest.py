import os
import numpy as np


root_path = os.path.dirname(__file__) + os.sep + r"data" + os.sep + r"TrainData"
NormalShot = np.load(root_path + os.sep + r"TrainNormal.npy")
BreakShot = np.load(root_path + os.sep + r"TrainBreak.npy")
NormalShot = list(NormalShot)
BreakShot = list(BreakShot)
print(len(NormalShot))
print(len(BreakShot))


np.random.seed(42)
BreakTest = np.random.choice(BreakShot, 50, replace = False)
NormalTest = np.random.choice(NormalShot, 50, replace = False)
BreakTest = list(BreakTest)
NormalTest = list(NormalTest)


for i in BreakTest:
    BreakShot.remove(i)
BreakTrain = BreakShot

for i in NormalTest:
    NormalShot.remove(i)
NormalTrain = NormalShot

print("NormalTrain : {}".format(len(NormalTrain)))
print("BreakTrain  : {}".format(len(BreakTrain)))
print("NormalTest  : {}".format(len(NormalTest)))
print("BreakTest   : {}".format(len(BreakTest)))

np.save(root_path + os.sep + r"NormalTest.npy", NormalTest)
np.save(root_path + os.sep + r"BreakTest.npy",BreakTest)
np.save(root_path + os.sep + r"NormalTrain.npy",NormalTrain)
np.save(root_path + os.sep + r"BreakTrain.npy",BreakTrain)
