import string
import random

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Student:
    """init Student"""
    def __init__(self, name):
        self.id = generate_id()
        self.name = name

class Seat:
    """init Seat"""
    def __init__(self, place: str = "fifo"):
        self.located_seat = []
        self.place = place

    def create_seat(self, name):
        self.located_seat.append(Student(name))

    def process_located_seat(self): 
        if len(self.located_seat) == 0:
            print("There are no located_seat to process. Well done!")
            return
        
        if self.place == "fifo":
            num = 1
            for seat in self.located_seat:
                self.print_seat(num, seat)
                num += 1

        elif self.place == "filo":
            num = 1
            for seat in reversed(self.located_seat):
                self.print_seat(num, seat)
                num += 1

        elif self.place == "random":
            list_copy = self.located_seat.copy()
            random.shuffle(list_copy)
            num = 1
            for seat in list_copy:
                self.print_seat(num, seat)
                num += 1

        elif self.place == "waiting":
            self.located_seat = []
            print("Please wait :)")

    def print_seat(self, num, student: Student):
        print(f"Seat number [{num}]: \t ID: {student.id} \t NAME: {student.name} \n")

seat = Seat("fifo")

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
for student in students:
    seat.create_seat(student)

print("==================================")
print(f"List of students: {students}")
print(f"Place type: {seat.place}")
print("==================================")

seat.process_located_seat()
