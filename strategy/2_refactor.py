import string
import random

def generate_id(length=8):
    """
    Generates a random ID of the specified length.
    
    Parameters:
        length (int): The length of the generated ID. Default is 8.
        
    Returns:
        str: The randomly generated ID.
    """
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Student:
    """init Student"""
    def __init__(self, name):
        self.id = generate_id()
        self.name = name

class SeatPlaceType:
    FIFO = "First In First Out"
    FILO = "First In Last Out"
    RANDOM = "Random"
    WAITING = "Waiting"

class Seat:
    """init Seat"""

    def __init__(self, place: str = SeatPlaceType.FIFO):
        self.located_seat = []
        self.place = place

    def create_seat(self, name):
        """
        Creates a new seat for a student with the given name.

        Args:
            name (str): The name of the student.

        Returns:
            None
        """
        self.located_seat.append(Student(name))

    def process_located_seat(self): 
        """
        Process the located seats based on the specified seat placement type.

        If there are no located seats to process, a message will be printed and the method will return.

        If the seat placement type is FIFO (First In First Out), the located seats will be processed in the order they were added.

        If the seat placement type is FILO (First In Last Out), the located seats will be processed in the reverse order they were added.

        If the seat placement type is RANDOM, the located seats will be processed in a random order.

        If the seat placement type is WAITING, the located seats will be cleared and a message will be printed.

        Returns:
            None
        """
        if len(self.located_seat) == 0:
            print("There are no located seats to process. Well done!")
            return
        
        if self.place == SeatPlaceType.FIFO:
            for i, seat in enumerate(self.located_seat, 1):
                self.print_seat(i, seat)

            return

        elif self.place == SeatPlaceType.FILO:
            list_copy = reversed(self.located_seat)
            for i, seat in enumerate(list_copy, 1):
                self.print_seat(i, seat)

            return

        elif self.place == SeatPlaceType.RANDOM:
            list_copy = self.located_seat.copy()
            random.shuffle(list_copy)
            for i, seat in enumerate(list_copy, 1):
                self.print_seat(i, seat)

            return

        elif self.place == SeatPlaceType.WAITING:
            self.located_seat = []
            print("Please wait :)")

            return
        
        print(f"Notthing happened. The seat placement type '{self.place}' is not recognized.")

        return

    def print_seat(self, num, student: Student):
        """
        Prints the seat number, student ID, and student name.

        Args:
            num (int): The seat number.
            student (Student): The student object containing the ID and name.

        Returns:
            None
        """
        print(f"Seat number [{num}]: \t ID: {student.id} \t NAME: {student.name} \n")

seat = Seat(SeatPlaceType.FIFO)

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
for student in students:
    seat.create_seat(student)

print("==================================")
print(f"List of students: {students}")
print(f"Place type: {seat.place}")
print("==================================")

seat.process_located_seat()
