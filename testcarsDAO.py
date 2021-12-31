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
    'plate' : 11112,
    'model' : 'Ferrari',
    'year' : 2021,
    'fuel' : 'Diesel'
}
car2 = {
    'plate' : 1223,
    'model' : 'F',
    'year' : 2022,
    'fuel' : 'Petrol'
}
# delete
returnvalue = carsDAO.create(car)
#print(returnvalue)
#returnvalue = carsDAO.findByID(car2)
#print("find by Id: ")
#print(returnvalue)
#returnvalue = carsDAO.getAll()
#print(returnvalue)
#returnvalue = carsDAO.findByID('1')
#print(returnvalue)
#returnvalue = carsDAO.update(car2)
#print(returnvalue)
#returnvalue = carsDAO.findByID(car2)
#print(returnvalue)
#returnvalue = carsDAO.delete(car)
#print(returnvalue)
#returnvalue = carsDAO.getAll()
#print(returnvalue)