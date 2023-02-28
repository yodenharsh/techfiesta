import seaborn as sns
import database_operations as dbOps
import matplotlib.pyplot as plt
import numpy as np

db_conn = dbOps.dbOps("localhost", "root", "root", "techfiesta")
LOW_RISK = db_conn.selectByRiskAndConfidence(risk="LOW")


HIGH_RISK = db_conn.selectByRiskAndConfidence(risk="HIGH")


MEDIUM_RISK = db_conn.selectByRiskAndConfidence(risk="MEDIUM")

potholes = db_conn.fetchAll()
print(db_conn.fetchAll())
risk_list = []
for x in LOW_RISK:
    risk_list.append(x[3])

for x in MEDIUM_RISK:
    risk_list.append(x[3])

for x in HIGH_RISK:
    risk_list.append(x[3])

area_list = []
for x in potholes:
    area_list.append(x[1]*x[2])

print(area_list)

sns.set_style("whitegrid")
sns.kdeplot(np.array(area_list), bw_method=0.5, fill=True)

plt.xlabel("Area (in cm^2)")
plt.show()
