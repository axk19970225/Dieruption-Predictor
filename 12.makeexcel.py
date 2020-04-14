import os
import xlsxwriter


root_path = os.path.dirname(__file__) + os.sep + r"data"
if not os.path.exists(root_path):
    os.makedirs(root_path)
workbook = xlsxwriter.Workbook(root_path + os.sep + r"result.xlsx")
worksheet = workbook.add_worksheet('1')
head = ["gamma vs nu","accury","precision","recall","FPR","conf[0,0]","conf[0,1]","conf[1,0]","conf[1,1]","AUC","cross_val_score"]
worksheet.write_row('A1',head)
count = 1
# for gamma in [0.00001,0.0001,0.001,0.01,0.1,1,10,100]:
#     for C in [0.00001,0.0001,0.001,0.01,0.1,1,10,100,1000,10000,100000]:
#         temp = str(gamma) + "vs" +str(C)
#         worksheet.write(count,0,temp)
#         count += 1


for gamma in [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
    for nu in [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        temp = str(gamma) + "vs" + str(nu)
        worksheet.write(count, 0, temp)
        count += 1


# count = 1
# for C in [0.00001,0.0001,0.001,0.01,0.1,1,10,100,1000,10000,100000]:
#     temp = "C : " + str(C)
#     worksheet.write(count,0,temp)
#     count += 1
workbook.close()




