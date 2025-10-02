# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def nameofdog(self):
        print(f"name of dog is : {self.name}.")

# Child class
class Dog(Animal):
    def __init__(self,name,breed): 
        # Call the parent class constructor
        super().__init__(name=name)
        self.breed = breed

    def dog_detail(self):
        super().nameofdog()  # Call the parent class's speak method
        print(f"Breed of dog is : {self.breed}")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.dog_detail()

# Output:
# Buddy makes a sound.
# Buddy barks.
