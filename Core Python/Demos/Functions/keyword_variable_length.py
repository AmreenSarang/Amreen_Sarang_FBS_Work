def emp(**data):
    for key , val in data.items():
        print(key , ':' , val)
emp(id = 101 , name = 'ABC' , dept = 'IT' , sal = 35000)