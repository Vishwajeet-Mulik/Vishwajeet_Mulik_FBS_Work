def emp(**data): 
    for key, val in data.items(): # key or val is not mandatory but data.items is mandatory
        print(key,':',val)

emp(id=101, name='vishwajeet',age=21, sal=85000)