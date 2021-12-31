import mysql.connector
import dbconfig as cfg
class carsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host= cfg.mysql['host'],
        user= cfg.mysql['user'],
        password= cfg.mysql['password'],
        database= cfg.mysql['database']
        )
    def create(self, car):
        cursor = self.db.cursor()
        sql="insert into cars (plate, model, year, fuel) values (%s,%s,%s,%s)"
        values = [
            car['plate'],
            car['model'], 
            car['year'], 
            car['fuel']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, car):
        cursor = self.db.cursor()
        sql="select * from cars where plate = %s"
        values = [car['plate']]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, car):
        cursor = self.db.cursor()
        sql="update cars set plate = %s, model= %s, year=%s, fuel=%s  where plate = %s"
        values = [
            car['plate'],
            car['model'], 
            car['year'], 
            car['fuel'], 
            car['plate']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return car
    
    def delete(self, car):
        cursor = self.db.cursor()
        sql="delete from cars where plate = %s"
        values = [car['plate']]

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")
        return {}
    
    def convertToDictionary(self, result):
        colnames=['id','plate','model','year','fuel']
        car = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        
        return car

carsDAO = carsDAO()

