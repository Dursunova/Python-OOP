class Person:
    first_name="Nergiz"
    last_name="Dursunova"
    age=19
    def speak(self):
        print("Hello")
     
person1=Person()
print(person1.first_name)
person1.speak()

class Animal:
    def __init__(self,name1,color1,age1):
        self.name=name1
        self.color=color1
        self.age=age1

    def sound(self):
        print(f"{self.name} makes a sound")

# dog=Animal("Dog","Black",8)
# dog.sound()

class Dog(Animal): #inheritance
    pass

# dog=Dog("Tommy","Black",9)
# print(dog.name,dog.color,dog.age)

class Cat(Animal):
    def __init__(self,hair,name1,color1,age1):
        self.hair=hair
        super().__init__(name1,color1,age1)

cat=Cat("Black","Mesy","White",4)
print(cat.hair)