class ClassSchedule:
    # constructor will call automatically when object is created
   def __init__(self):
       print("constructor called ")
    
    # destructor will call when object is destroyed
   def __del__(self):
       print('Destructor called')
       
obj = ClassSchedule()