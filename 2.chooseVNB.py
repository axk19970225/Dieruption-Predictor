import os
import numpy as np
from DDB.Service import Query

# IsValidShot
db = Query()
valid_query = {'IsValidShot':True, 'IpFlat':{'$gt':100}, "$or": [{'CqTime':{'$gt':0.2}}, {'RampDownTime':{'$gt':0.2}}]}
break_query = {'IsValidShot':True, 'IsDisrupt': True, 'IpFlat':{'$gt':100}, 'CqTime':{'$gt':0.2}}
normal_query = {'IsValidShot':True, 'IsDisrupt': False, 'IpFlat':{'$gt':100}, 'RampDownTime':{'$gt':0.2}}
validshot = db.query(valid_query)
breakshot = db.query(break_query)
normalshot = db.query(normal_query)

root_path = os.path.dirname(__file__) + os.sep + "data"
if not os.path.exists(root_path):
    os.makedirs(root_path)
np.save(root_path + os.sep + r"Valid.npy", validshot)
np.save(root_path + os.sep + r"Break.npy", breakshot)
np.save(root_path + os.sep + r"Normal.npy", normalshot)

