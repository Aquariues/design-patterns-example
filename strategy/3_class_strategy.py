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

class LocateSeatStrategy(ABC):
    """
    Abstract base class for seat locating strategies.

    Subclasses of `LocateSeatStrategy` must implement the `process_located_seat` method.
    """

    @abstractmethod
    def process_located_seat(self, located_seat: list) -> list:
        """
        Process the located seat information.

        Args:
            located_seat (list): A list of located seat information.

        Returns:
            list: A list of processed seat information.
        """
        pass

class FIFOLocate(LocateSeatStrategy):
    """
    A class that implements the First-In-First-Out (FIFO) strategy for locating seats.

    This strategy simply returns the located seats in the order they were found.

    Attributes:
        None

    Methods:
        process_located_seat: Processes the located seats and returns them in the same order.

    """

    def process_located_seat(self, located_seat: list) -> list:
        """
        Processes the located seats and returns them in the same order.

        Args:
            located_seat (list): A list of located seats.

        Returns:
            list: The located seats in the same order.

        """
        return located_seat
    
class FILOLocate(LocateSeatStrategy):
    """
    A strategy class that implements the First-In-Last-Out (FILO) strategy for locating seats.

    This strategy reverses the order of the located seats.

    Args:
        LocateSeatStrategy (class): The base class for all seat locating strategies.

    Methods:
        process_located_seat(located_seat: list) -> list:
            Reverses the order of the located seats.

    Returns:
        list: The located seats in reverse order.
    """

    def process_located_seat(self, located_seat: list) -> list:
        """
        Reverses the order of the located seats.

        Args:
            located_seat (list): The list of located seats.

        Returns:
            list: The located seats in reverse order.
        """
        return list(reversed(located_seat))

class RANDOMLocate(LocateSeatStrategy):
    """
    A strategy class that randomly shuffles the located seats.

    This class implements the `LocateSeatStrategy` interface and provides a strategy
    for processing located seats by randomly shuffling them.

    Attributes:
        None

    Methods:
        process_located_seat: Randomly shuffles the located seats.

    """

    def process_located_seat(self, located_seat: list) -> list:
        """
        Randomly shuffles the located seats.

        Args:
            located_seat (list): The list of located seats.

        Returns:
            list: The list of located seats after being randomly shuffled.

        """
        random.shuffle(located_seat)
        
        return located_seat
    
class WAITINGLocate(LocateSeatStrategy):
    """
    A strategy class for locating seats when the user is in the waiting state.
    """

    def process_located_seat(self, located_seat: list) -> list:
        """
        Process the located seat and return an empty list.

        Returns:
            list: An empty list.
        """
        print(f"Please wait :)")

        return []

class Seat:
    """init Seat"""

    class MyClass:
        def __init__(self, place: LocateSeatStrategy):
            """
            Initializes an instance of MyClass.

            Args:
                place (LocateSeatStrategy): The strategy object used to locate seats.

            Attributes:
                located_seat (list): A list to store located seats.
                place (LocateSeatStrategy): The strategy object used to locate seats.
            """
            self.located_seat = []
            self.place = place

    def create_seat(self, name) -> None:
        """
        Creates a new seat for a student with the given name.

        Args:
            name (str): The name of the student.

        Returns:
            None
        """
        self.located_seat.append(Student(name))

    def process_located_seat(self) -> None: 
        """
        Process the located seats for students.

        This method processes the located seats for students and prints the seat number and student details.

        Returns:
            None
        """
        if len(self.located_seat) == 0:
            print("There are no located_seat to process. Well done!")
        
            return

        students = self.place.process_located_seat(self.located_seat)
        
        for i, student in enumerate(students, 1):
            self.print_seat(i, student)
        
            return

        print(f"Notthing happened.")

        return
        
    def print_seat(self, num, student: Student) -> None:
        """
        Prints the seat number, student ID, and student name.

        Args:
            num (int): The seat number.
            student (Student): The student object containing the ID and name.

        Returns:
            None
        """
        print(f"Seat number [{num}]: \t ID: {student.id} \t NAME: {student.name} \n")

seat = Seat(WAITINGLocate())

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
for student in students:
    seat.create_seat(student)

print("==================================")
print(f"List of students: {students}")
print(f"Place type: {seat.place}")
print("==================================")

seat.process_located_seat()
