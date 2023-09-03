## 0x07. Python - Test-driven development

## Resources FOR THIS TASK
	
	https://docs.python.org/3.4/library/doctest.html
	https://pymotw.com/3/doctest/
	https://www.youtube.com/watch?v=1Lfv5tUGsn8
	https://www.youtube.com/watch?v=6tNS--WetLI
	https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/

## Requirements

	Python Scripts
	Allowed editors: vi, vim, emacs
	All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	All your files should end with a new line
	The first line of all your files should be exactly #!/usr/bin/python3
	A README.md file, at the root of the folder of the project, is mandatory
	Your code should use the pycodestyle (version 2.8.*)
	All your files must be executable
	The length of your files will be tested using wc

## Python Test Cases

	Allowed editors: vi, vim, emacs
	All your files should end with a new line
	All your test files should be inside a folder tests
	All your test files should be text files (extension: .txt)
	All your tests should be executed by using this command: python3 -m doctest ./tests/*
	All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
	We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

## TASKS

## 0-add_integer.py, tests/0-add_integer.txt

+ Write a function that adds 2 integers.

	- Prototype: def add_integer(a, b=98):
	- a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
	- a and b must be first casted to integers if they are float
	- Returns an integer: the addition of a and b
	- You are not allowed to import any module

## 2-matrix_divided.py, tests/2-matrix_divided.txt

> Write a function that divides all elements of a matrix.

	- Prototype: def matrix_divided(matrix, div):
	- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
	- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
	# div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
	- div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
	> All elements of the matrix should be divided by div, rounded to 2 decimal places
	* Returns a new matrix
	+ You are not allowed to import any module