class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0]+last_name+birth_year


ip1 = input()
ip2 = input()
ip3 = input()

student1 = Student(ip1, ip2, ip3)
print(student1.id)