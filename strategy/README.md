# TRATEGY PATTERNS 
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

## Problem:
We have a list of 10 students waiting in line to go to the classroom. The teacher wants to assign seats to the students using the following methods: `first in - first out, first in - last out, random, or waiting.`

The expected output should show the teacher which student goes to which seat.

## Solution:
...

## Code example

### 1_normal.py
- Basic code

### 2_refactory.py
Simple refactor code from 1_normal.py

- Change hard coded text to constant
- Add func description
- Handle undefined value when init Seat

### 3_class_strategy.py
Apply Strategy pattern for class

- The `generate_id` function generates a random ID of a specified length using uppercase ASCII characters. The default length is 8.

- The `Student` class represents a student with an ID and a name. The ID is generated using the generate_id function.

- The `LocateSeatStrategy` class is an abstract base class (ABC) that defines a common interface for all strategies. 
    - This class has an abstract method `process_located_seat` that expects a list of located seats and returns a list of processed seat information. This method must be implemented by all subclasses of LocateSeatStrategy.

- There are four concrete strategy classes: `FIFOLocate`, `FILOLocate`, `RANDOMLocate`, and `WAITINGLocate`. Each of these classes implements the process_located_seat method in a different way according to the specific strategy:

- `FIFOLocate` returns the located seats in the order they were found.
- `FILOLocate` reverses the order of the located seats.
- `RANDOMLocate` randomly shuffles the located seats.
- `WAITINGLocate` returns an empty list and prints a "Please wait" message.
- The `Seat` class represents a seat in the classroom. It has a place attribute that holds the current seat locating strategy, and a located_seat attribute that is a list of students who have been assigned a seat. 
    - The `create_seat` method adds a new student to the located_seat list. 
    - The `process_located_seat` method processes the located seats using the current strategy and prints the seat number and student details.

- Finally, the code creates a `Seat` object with the `FIFOLocate` strategy, adds ten students to it, and processes the located seats.

### 4_func_strategy.py
Apply Strategy pattern with func programming

- The `generate_id` function is used to create a random ID for each student. It uses the random.choices function to select random characters from the uppercase ASCII letters. The number of characters is determined by the length parameter, which defaults to 8.

- The `Student` class represents a student. Each student has an ID, which is generated using the `generate_id` function, and a name, which is passed to the constructor.

- The `fifo_locate_seat`, `filo_locate_seat`, `random_locate_seat`, and `waiting_locate_seat` functions are strategies for processing the seats. 
    - The `fifo_locate_seat` function returns the seats in the order they were added. 
    - The `filo_locate_seat` function returns the seats in reverse order. 
    - The `random_locate_seat` function shuffles the seats and returns them in a random order. 
    - The `waiting_locate_seat` function clears the seats and returns an empty list.

- The Seat class represents the seating system. It has a list of located seats, which are instances of the Student class. 
    - The `create_seat` method adds a new student to the list of located seats.
    - The `process_located_seat` method processes the located seats based on a specified strategy. If the list of located seats is empty, it prints a message and returns. Otherwise, it prints the seats in the order determined by the strategy. 
    - The `print_seat` method prints the seat number, student ID, and student name.

- The script then creates an instance of the `Seat` class, adds some students to it, and processes the seats using the FIFO strategy.

## Reference
- [Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
- [Wiki pedia](https://en.wikipedia.org/wiki/Strategy_pattern)
- [FreeCodeCamp](https://www.freecodecamp.org/news/a-beginners-guide-to-the-strategy-design-pattern/)
- [Refactoring Guru Github](https://github.com/RefactoringGuru)
- [Sourcemaking](https://sourcemaking.com/design_patterns)