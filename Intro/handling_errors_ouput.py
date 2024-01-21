# try-except blocks
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid Error')
# This helps to let the exit code be 0 other than 1(crashing)
# classes


class Point:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name= last_name

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point('Martin','Maina')
print(point.first_name)
point.move()


class Person:
    def __init__(self, name):  # constructor method
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


person = Person('Martin Maina')
person.talk()
john = Person('John Gert')
john.talk()