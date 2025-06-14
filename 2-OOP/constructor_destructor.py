class ClassSchedule:
   
   def __init__(self,name,age,gmail):
       self.__name = name # private
       self._age = age # protected
       self.gmail = gmail # public 
       print("constructor called ")
  
   def __del__(self):
       print('Destructor called')
   def display(self):
       print(f"{self.__name},{self._age},{self.gmail}")
       

obj = ClassSchedule('anees','12','anees@gmail.com')

obj.display()

obj.gmail ="ikram@gmail.com" # can accees publically

obj.display()