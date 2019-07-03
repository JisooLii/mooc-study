# Lecture

_Written in Italic: external reference_

Everything in Python is an object. (Even Python code itself is so.)

#### Object types

1. __Scalar__
    - Indivisible
    - _absence of matrix data structures or vector data structures like arrays or collections or lists, typles or dictionaries_
    - _Single Value_
    - Types:
        - Int
        - Float
            - caution: Float is not the same as real number. ( You can presume as the same, but be careful always)
                - float 2.4 != real number 2.4
        - Boolean : True, False
        - None
        - Char (Python doesn't have this though)

2. __Non-Scalar__
    - _Non-Singular Value_
    - _Types:_
        - _Array / List_
        - _Tuples_
        - _Dictionary_


#### Overloaded Operator

operand whose function depends on operands

- ex. +
    - 3 + 2 = 5 (calculation)
    - 'a' + '3' = 'a3' (concatenation)

#### Types of error (in Python)
- Syntax Error: Grammatical error.
    - ex: print(3 3)
- Type Error: Semantic error. (which does not make sense, while it is gramatically correct)
    - ex: print('b'/3)

#### Program?
A program(or, a script) is a sequence of commands

##### Variable
- Key concept of almost every programming language
- Each language has different notion on variable
- Python: simply a name of an object
- Assignment in Python: binds the name to an object

##### Straight Line Program
- Execute every command without making any deviation,
without going back with any loops to execute a command more than once
- Every command gets executed exactly once
- Running Time: Number of lines of codes

##### Conditional Statement
- if ... else ...
- for testing and making decisions.
- Every command gets executed at most once

##### Branching Program
- Program with conditional statement
- Running Time: Governed by the size of the program
- Not proportional in time to the input -> limited functionality

##### Looping Construct
- iteration
- Turing Complete : Any program that can be written, or any function that can be computed, rather, can be computed in a Turing Complete language.



#### Comment
- When writing comment, assume that readers can read the code.
- Don't have to explain programming language or semantics in comment
- Purpose of writing comment, is to make the program easier to read.
- Explains my thinking when I wrote the program
- What algorithm I've used for the program?

---
---


### Recitation

#### Syntax, Semantics
(1) Syntax (based on python syntax)
- Correct: var + var
- Incorrect: var var +

(2) Static Semantics
- Correct: 3/5
- Incorrect: 3/'bar'

(3) Semantic (meaningful enough, but breaks)
- Correct: 5/2
- Incorrect: 6/0


Every program is a sequence of _expressions_.
*Expressions* are made up with operators, operands and functions.
*Everything constituting expression* is object

Boolean-type operators: and, or, not
