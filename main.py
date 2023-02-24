from PotholesVBIT import camera_video
import os
import database_operations
os.chdir("../PotholesVBIT")


def riskCalculation(x, y):
    area = int(x) * int(y)
    if area < 10100:
        return "LOW"
    elif area >= 10100 and area < 20200:
        return "MEDIUM"
    else:
        return "HIGH"


_, _, files = next(os.walk("./pothole_size"))
file_count = len(files)

for i in range(0, file_count):
    try:
        file = open("./pothole_size/pothole" + str(i)+'.txt', 'r')
        line = file.readline()
        param_list = line.split(',')

        values = {
            'x': param_list[0],
            'y': param_list[1],
            'confidence': param_list[2],
            'risk': riskCalculation(param_list[0], param_list[1])
        }

        dbOpsObj = database_operations.dbOps(
            "localhost", "root", "root", "techfiesta")
        dbOpsObj.save(values=values)
        file.close()
    except FileNotFoundError:
        pass
