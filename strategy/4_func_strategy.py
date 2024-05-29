import string
import random
from abc import ABC, abstractmethod

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

def fifo_locate_seat(located_seat: list) -> list:
    """
    Process the located seats and return them in the same order.

    Args:
        located_seat (list): A list of located seat information.

    Returns:
        list: The located seats in the same order.
    """
    return located_seat

def filo_locate_seat(located_seat: list) -> list:
    """
    Process the located seats and return them in reverse order.

    Args:
        located_seat (list): A list of located seat information.

    Returns:
        list: The located seats in reverse order.
    """
    return list(reversed(located_seat))

def random_locate_seat(located_seat: list) -> list:
    """
    Process the located seats and return them in random order.

    Args:
        located_seat (list): A list of located seat information.

    Returns:
        list: The located seats in random order.
    """
    random.shuffle(located_seat)
    return located_seat

def waiting_locate_seat(located_seat: list) -> list:
    """
    Process the located seats and return an empty list.

    Args:
        located_seat (list): A list of located seat information.

    Returns:
        list: An empty list.
    """
    return []

class Seat:
    """init Seat"""

    def __init__(self):
        self.located_seat = []

    def create_seat(self, name):
        """
        Creates a new seat for a student with the given name.

        Args:
            name (str): The name of the student.

        Returns:
            None
        """
        self.located_seat.append(Student(name))

    def process_located_seat(self, place_type): 
        """
        Process the located seats based on the specified place.

        If the located_seat list is empty, it prints a message and returns.
        If the place is "fifo", it prints the seats in the order they were added.
        If the place is "filo", it prints the seats in reverse order.
        If the place is "random", it shuffles the located_seat list and prints the seats.
        If the place is "waiting", it clears the located_seat list and prints a message.

        Returns:
            None
        """
        students = place_type(self.located_seat)
        
        if len(self.located_seat) == 0:
            print("There are no located_seat to process. Well done!")
            
            return
        
        for i, student in enumerate(students, 1):
            self.print_seat(i, student)

            return
        
        print(f"Notthing happened.")
        
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

seat = Seat()

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
for student in students:
    seat.create_seat(student)

print("==================================")
print(f"List of students: {students}")
print("==================================")

seat.process_located_seat(fifo_locate_seat)
