# Python, JavaScript interview practise.

## Table of Content
- [Author](#author)
- [Description](#description)
___

- [Island Perimeter](0x09-island_perimeter/README.md)
- [Lockboxes](0x01-lockboxes/README.md)
- [Log Parsing](0x03-log_parsing/README.md)
- [Making Change](0x08-making_change/README.md)
- [Minimum Operations](0x02-minimum_operations/README.md)
- [N-Queens](0x05-nqueens/README.md)
- [Pascal Triangle](0x00-pascal_triangle/README.md)
- [Rotate 2D Matrix](0x07-rotate_2d_matrix/README.md)
- [Star Wars API](0x06-starwars_api/README.md)
- [UTF8 Validation](0x04-utf8_validation/README.md)
___

- [Requirements](#requirements)

## Description
___

1. # Pascal's Triangle

## Resources

- [What is Pascal’s triangle](https://www.cuemath.com/algebra/pascals-triangle/)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=0iMtlus-afo)
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)

## Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=1qw5ITr3k9E)

### *Must Know*

To successfully complete this project, you should revise the following Python concepts:

### Concepts Needed:

1. **Lists and List Comprehensions:**

    - Understand how to create, access, modify, and iterate over lists.
    - Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.

2. **Functions:**

    - Know how to define and call functions.
    - Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.

3. **Loops:**

    - Use `for` and `while` loops to iterate through sequences.
    - Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

4. **Conditional Statements:**

    - Apply `if`, `elif`, and `else` conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

5. **Recursion (Optional):**

    - While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
    - Recognize base cases and recursive cases for a function that generates the triangle’s rows.

6. **Arithmetic Operations:**

    - Perform addition, a fundamental operation for calculating each element of - - Pascal’s Triangle as the sum of the two elements directly above it.

7. **Indexing and Slicing:**

    - Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.

8. **Memory Management:**

    - Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.

9. **Error and Exception Handling (Optional):**

    - Use try-except blocks as needed to handle potential errors, such as invalid input types or values.

10. **Efficiency and Optimization:**

    -Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
    - Evaluate and apply optimizations to improve the performance of the solution.

By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.
___

2. # Lockboxes

### *Must Know*

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

## Concepts Needed:

1. **Lists and List Manipulation:**

    - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
    - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

2. **Graph Theory Basics:**

    - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
    - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

3. **Algorithmic Complexity:**

    - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
    - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

4. **Recursion:**

    - Some solutions might require a recursive approach to traverse through the boxes and keys.
    - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

5. **Queue and Stack:**

    - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
    - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

6. **Set Operations:**

    - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
    - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

## Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)
___

3. # Minimum Operations

For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:

# Concepts Needed:

1. **Dynamic Programming:**
    - Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
    - [Dynamic Programming (GeeksforGeeks)](https://intranet.alxswe.com/rltoken/l3JYgicNQw2Ue1Kg9jV80Q)

2. **Prime Factorization:**
    - Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.
    - [Prime Factorization (Khan Academy)](https://intranet.alxswe.com/rltoken/cFcADpVYRCl5pdut-Lemmg)

3. **Code Optimization:**
    - Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
    - [How to optimize Python code](https://intranet.alxswe.com/rltoken/98ZF5bRckUKror6pGJQlHQ)

4. **Greedy Algorithms:**
    - The problem can also be approached with greedy algorithms, choosing the best option at each step.
    - [Greedy Algorithms (GeeksforGeeks)](https://intranet.alxswe.com/rltoken/k6-mba0b4nayJi0VqYhKjQ)

5. **Basic Python Programming:**
    - Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
    - [Python Functions (Python Official Documentation)](https://intranet.alxswe.com/rltoken/ao3SJVl4yY1SfugfVa3anw)

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

# Additional Resources
- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/HX0vuVl1V-9T4vvh8NDCyw)

# Requirements

## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version `3.4.3`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable

4. # Log Parsing

For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

# Concepts Needed:

1. **File I/O in Python:**
    - Understand how to read from `sys.stdin` line by line.
    - [Python Input and Output](https://intranet.alxswe.com/rltoken/f7U2MDsBT_rd9AfUUaqVnQ)

2. **Signal Handling in Python:**
    - Handling keyboard interruption (CTRL + C) using signal handling in Python.
    - [Python Signal Handling](https://intranet.alxswe.com/rltoken/1nDqPJe80rSD-NMulzjJBw)

3. **Data Processing:**
    - Parsing strings to extract specific data points.
    - Aggregating data to compute summaries.

4. **Regular Expressions:**
    - Using regular expressions to validate the format of each line.
    - [Python Regular Expressions](https://intranet.alxswe.com/rltoken/ZsD-YLisfaHFeMT_sZxX1Q)

5. **Dictionaries in Python:**
    - Using dictionaries to count occurrences of status codes and accumulate file sizes.
    - [Python Dictionaries](https://intranet.alxswe.com/rltoken/JM-RpavKkb8yanxWEnNYJw)

6. **Exception Handling:**
    - Handling possible exceptions that may arise during file reading and data processing.
    - [Python Exceptions](https://intranet.alxswe.com/rltoken/OA2PlryrYA2gyCCKIsdgUw)

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

# Additional Resources
- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/VlOaXKkbecRYdnTLaLU1lg)
____

5. # UTF-8 Validation

For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:

## Concepts Needed:

1. **Bitwise Operations in Python:**
    - Understanding how to manipulate bits in Python, including operations like AND ( `&` ), OR ( `|` ), XOR ( `^` ), NOT ( `~` ), shifts ( `<<` , `>>` ).
    - [Python Bitwise Operators](https://intranet.alxswe.com/rltoken/BslyYNZlXdyxW3_b0WNOcg)

2. **UTF-8 Encoding Scheme:**
    - Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
    - Understanding the patterns that represent a valid UTF-8 encoded character.
    - [UTF-8 Wikipedia](https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ)
    - [Characters, Symbols, and the Unicode Miracle](https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw)
    - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://intranet.alxswe.com/rltoken/9EwaXVds22dSK3IvF5nNCA)

3. **Data Representation:**
    - How to represent and work with data at the byte level.
    - Handling the least significant bits (LSB) of integers to simulate byte data.

4. **List Manipulation in Python:**
    - Iterating through lists, accessing list elements, and understanding list comprehensions.
    - [Python Lists](https://intranet.alxswe.com/rltoken/TaN91MgmOL80GeOGvmldIw)

5. **Boolean Logic:**
    - Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Additional Resource
- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/X1lZqipeyegt8pbQ9aXSFQ)
___

6. # N Queens

The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

# Concepts Needed:

1. **Backtracking Algorithms:**

    - Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
    - [Backtracking Introduction](https://intranet.alxswe.com/rltoken/Gbaz9HkwvR9FX4zjBt9dSw)

2. **Recursion:**

    - Using recursive functions to implement backtracking algorithms.
    - [Recursion in Python](https://intranet.alxswe.com/rltoken/X1vaNXgy_pPyvKfOJm90XQ)

3. **List Manipulations in Python:**

    - Creating and manipulating lists, especially to store the positions of queens on the board.
    - [Python Lists](https://intranet.alxswe.com/rltoken/P3KbYxmdtSeoJvVfr9Iv0w)

4. **Python Command Line Arguments:**

    - Handling command-line arguments with the `sys` module.
    - [Command Line Arguments in Python](https://intranet.alxswe.com/rltoken/2IF4V6xsY_Nq-xcGDK3Bhw)

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

# Additional Resources
- [Mock Interview](https://intranet.alxswe.com/rltoken/aQ3uJmGVeZa-R6B1jYTjXg)
___

7. # Star Wars API

The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display
information about Star Wars characters based on the movie ID provided as an argument. To successfully
complete this project, you need to be familiar with several key concepts related to web programming, API
interaction, and asynchronous programming in JavaScript.

# Concepts Needed:

1. **HTTP Requests in JavaScript:**

    - Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
    - [A Complete Guide to Making HTTP Requests in Node.js](https://intranet.alxswe.com/rltoken/iRse23lnV4gAsD9JJTJMMQ)

2. **Working with APIs:**

    - Understanding the basics of RESTful APIs and how to interact with them.
    - Parsing JSON data returned by APIs.
    - [Working with APIs in JavaScript](https://intranet.alxswe.com/rltoken/KyGS_uB68mLaP5irrH8JVA)

3. **Asynchronous Programming:**

    - Managing asynchronous operations with callbacks, promises, and async/await syntax.
    - Handling API response data asynchronously.
    - [Asynchronous Programming in JavaScript](https://intranet.alxswe.com/rltoken/tdKMGJrRstCkXSReNfRFpQ)

4. **Command Line Arguments in Node.js:**

    - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
    - [How to Parse Command Line Arguments in Node.js](https://intranet.alxswe.com/rltoken/oWBOWJZLF_D9GfOydPz6Kg)

5. **Array Manipulation and Iteration:**

    - Iterating over arrays and manipulating data structures to format and display character names.
    - [JavaScript Array Methods](https://intranet.alxswe.com/rltoken/8zdG036OYYvVco_AZTExoA)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

# Additional Resources
- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/du6hlPQm6qi4A7eEursNhQ)
___

8. # Rotate 2D Matrix

For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.

# Concepts Needed:

1. **Matrix Representation in Python:**

    - Understanding how 2D matrices are represented using lists of lists in Python.
    - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations:**

    - Performing operations on data without creating a copy of the data structure.
    - The importance of minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition:**

    - Understanding the concept of transposing a matrix (swapping rows and columns).
    - Implementing matrix transposition as a step in the rotation process.

4. **Reversing Rows in a Matrix:**

    - Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. **Nested Loops:**

    - Using nested loops to iterate through 2D data structures like matrices.
    - Modifying elements within nested loops to achieve the desired rotation.

# Resources:

- **Python Official Documentation:**

    - [Data Structures (list comprehensions, nested list comprehension)](https://intranet.alxswe.com/rltoken/eZc_ELGxUgkuc4kkE_fd7Q)
    - [More on Lists](https://intranet.alxswe.com/rltoken/0ORj179giGhGe8jpcxBkXg)

- **GeeksforGeeks Articles:**

    - [Inplace rotate square matrix by 90 degrees](https://intranet.alxswe.com/rltoken/9T8w4mtiIIRDtfLSmEmrLA)
    - [Transpose a matrix in Single line in Python](https://intranet.alxswe.com/rltoken/JdIFvtej2hMW-Wd9ABHMOA)

- **TutorialsPoint:**

    - [Python Lists](https://intranet.alxswe.com/rltoken/rFmzUTpaLGqDXjGA6D9eYw) for basics of list manipulation in Python.

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.

# Additional Resources
- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/4GPWA9C2AJHtpdGxuIHEPA)
___

9. # Making Change

For the “0. Change comes from within” project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.

## Concepts Needed:

1. **Greedy Algorithms:**

    - Understanding how greedy algorithms work and why they are suitable for the coin change problem.
    - Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.

2. **Dynamic Programming:**

    - Basic principles of dynamic programming as a method to solve optimization problems.
    - The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

3. **Algorithmic Complexity:**

    - Analyzing the time and space complexity of algorithms.
    - Striving for solutions with lower complexity to meet runtime constraints.

4. **Problem-Solving Strategies:**

    - Breaking down the problem into smaller, manageable sub-problems.
    - Iterative vs recursive approaches to dynamic programming.

5. **Python Programming:**

    - Manipulating lists and using list comprehensions.
    - Implementing functions with efficient looping and conditional statements.

# Resources:

- **Python Official Documentation:**

    - [More Control Flow Tools(for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)

- **GeeksforGeeks Articles:**

    - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
    - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **YouTube Tutorials:**

    - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw) for a visual and step-by-step explanation of the dynamic programming approach.

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

# Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=9BSSIsJ-fWg)
___

## Requirements

## Python

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version `3.4.3`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable

10. # Island Perimeter

For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

## Concepts Needed:

1. **2D Arrays (Matrices):**

    - Accessing and iterating over elements in a 2D array.
    - Understanding how to navigate through adjacent cells (horizontally and vertically).

2. **Conditional Logic:**

    - Applying conditions to determine whether a cell contributes to the perimeter of the island.

3. **Counting Techniques:**

    - Developing a method to count the edges that contribute to the island’s perimeter.

4. **Problem-Solving Strategies:**

    - Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

5. **Python Programming:**

    - Nested loops for iterating over grid cells.
    - Conditional statements to check the status of adjacent cells.

# Resources:

- **Python Official Documentation:**

    - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists
within lists in Python.

- **GeeksforGeeks Articles:**

    - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.

- **TutorialsPoint:**

    - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

- **YouTube Tutorials:**

    - [Python 2D arrays and lists](https://www.youtube.com/watch?v=aNzepGawwCI)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

# Additional Resources
- [Mock Technical Interviews](https://www.youtube.com/watch?v=fFgEM6CMQc4)

# Requirements

## General
- Allowed editors: `vi` , `vim` , `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version `3.4.3`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version `1.7`)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## JavaScript

## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version `10.14.x`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://intranet.alxswe.com/rltoken/9P3gH5mVdJCEKL87E-IMaA) + [semicolons on top](https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw). Also as reference: [AirBnB style](https://intranet.alxswe.com/rltoken/Xp81RT-Sfi7uE_kNCSXunw)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

# More Info

**Install Node 10**

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**

[Documentation](https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw)

```bash
$ sudo npm install semistandard --global
```

**Install `request` module and use it**

[Documentation](https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw)

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Author

**Tafara Nyamhunga  - [Github](https://github.com/tafara-n) / [Twitter](https://twitter.com/tafaranyamhunga)**
