
import mysql.connector


class dbOps:
    def __init__(self, host, user, password, databaseName):
        self.conn = mysql.connector.connect(
            host=host, user=user, passwd=password, database=databaseName)
        self.cursor = self.conn.cursor()

    def save(self, values: dict):
        x = values.get("x")
        y = values.get("y")
        risk = values.get("risk")
        confidence = values.get("confidence")
        query = "INSERT INTO pothole_list (id,x_len,y_len,risk,confidence,fixed) VALUES (%s,%s,%s,%s,%s,false)"
        val = (0, x, y, risk, confidence)
        self.cursor.execute(query, val)
        self.conn.commit()

    def fetchAll(self):
        self.cursor.execute("SELECT * from pothole_list")
        return self.cursor.fetchall()

    def selectByRiskAndConfidence(self, risk="*", confidence_thresh=0):
        if (risk == "*"):
            self.cursor.execute(
                f"SELECT * from pothole_list where confidence={confidence_thresh}")
        else:
            self.cursor.execute(
                f"SELECT * from pothole_list where risk='{risk}' AND confidence>={confidence_thresh}")

        return self.cursor.fetchall()

    def selectByFixedOrNot(self, fixed):
        self.cursor.execute(f"SELECT * from pothole_list where fixed={fixed}")
        return self.cursor.fetchall()


# dbOpsObject = dbOps("localhost", "root", "root", "techfiesta")

# # values = {
# #     "x": 4,
# #     "y": 11,
# #     "risk": "HIGH",
# #     "confidence": 34
# # }

# # dbOpsObject.save(values=values)

# print(dbOpsObject.fetchAll())
# print(dbOpsObject.selectByRiskAndConfidence())
# print(dbOpsObject.selectByFixedOrNot(True))
