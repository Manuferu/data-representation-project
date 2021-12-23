from carsDAO import carsDAO

#create
#latestid = carsDAO.create(('123Limerick', 'Ford',2002,'Diesel'))
# find by id
#result = carsDAO.findByID(latestid);
#print (result)

#update
#carsDAO.update(('123Dublin','Ferrari',2010,'Petrol',latestid))
#result = carsDAO.findByID(latestid);
#print (result)

# get all 
#allCars = carsDAO.getAll()
#for cars in allCars:
#  print(cars)
car = {
    'plate' : 11111,
    'model' : 'Ford',
    'year' : 2021,
    'fuel' : 'Diesel'
}
car2 = {
    'plate' : 1222,
    'model' : 'Ford',
    'year' : 2021,
    'fuel' : 'Petrol'
}
# delete
#returnvalue = carsDAO.create(car2)
#print(returnvalue)
#returnvalue = carsDAO.findByID(car2['plate'])
#print("find by Id: ")
#print(returnvalue)
#returnvalue = carsDAO.getAll()
#print(returnvalue)
#returnvalue = carsDAO.findByID(car2['plate'])
#print(returnvalue)
#returnvalue = carsDAO.update(car)
#print(returnvalue)
#returnvalue = carsDAO.findByID(car2['plate'])
#print(returnvalue)
#returnvalue = carsDAO.delete(car2['plate'])
#print(returnvalue)
#returnvalue = carsDAO.getAll()
#print(returnvalue)