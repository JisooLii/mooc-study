

### Knowledge?

#### Declarative Knowledge

- Composed of statements of fact
    - ex1. A good health care plan improves the quality of medical care while saving money.
    - ex2. y is the square root of x if and only if y*y=x

- Says something true. (if it's not, then it's 'misinformation')
- Doesn't tell you how to do it.

#### Imperative Knowledge
- tells you how to solve problem
    - ex1. Cookbook, Recipes.
    - ex2. Approximation Algorithm (11:08)
- Algorithm ?
    - description of how to perform a computation. 
    - Set of instructions/steps that can be executed & a flow of control.
    - When we reach pretty close approximation result, we say that the algorithm is converged (which means halted).
    - Termination condition is important
    
### Computer
#### Fixed Program Computer
- Initial computer
- ex) Atanasoff and Berry, 1941, Artillery Trajectory Plotting Computer.
- ex2. Alan Turing, WW2, German Engima Code Breaking Computer
- Only do 'one thing'. Cannot run multiple kinds of programs

#### Stored Program Computer
- Algorithm(Program) are the same as data
- Enables to run multiple kinds of programs
- Became to be thought as 'Program' (Interpreter)

![Computer Structure](https://github.com/JisooLii/mooc-study/blob/master/MIT/6.00SC_2011/class-notes/unit1/1/computer_structure.png)

(Image from lecture slide)


- Memory: Only one memory exists. Is not separated into like (1)memory for program and (2)memory for data.
- Control Unit: tells memory what to do
    - ex1. fetch some data from memory
    - ex2. put some data in memory
    - ex3. send some output to a screen
    - etc...
- Arithmetic Logic Unit: Brains of computer. Do the computation
- Accumulator: Part of ALU. stores results.
- Input & Output devices
- Only have small set of instructions, but combined them to make a complex program. 


### Interpreter vs  Compiler
#### Interpreter
- Program that can execute any legal set of instructions.
- Can tell error in the source code's language

#### Compiler
- Translate source code into object code - language closer to the hardware / computer interpretation method.
- Tell error into object code, not the source code's language. Developer is unable to see it.
- More efficient, because of less running time due to translation.

### Language 
#### What distinguishes one language from another

- What are your instructions?

- What of your flow of control?

- How do you combine them?

- What are the combining mechanisms?


### Syntax and Semantics
Will compare human language and computer language
#### Syntax
- Tells us which sequences of characters and symbols constitute a well-formed string
- Syntactically correct sentences don't have to be 'meaningful'
#### Static Semantics
- Which well-formed strings have a meaning?
#### Semantics
- What the meanings are?
- Semantics of language: looks only at the strings that are both 1.syntactically and 2.static semantically correct, and then assigns real meaning to them.

| Language | Sentences| Syntax| Static Semantics|
|:---:|:---:| :---:| :---: |
| Human | I are big | O | X |
| | Susan is building | O | X | 
| Computer | x = 3 + 4 | O | O |
| | x = 3 4 | X | X |
| | '3' / 'abc' | O | X |

#### Difference between Human & Computer Language
- Human language can be ambiguous.
- Computer Language doesn't allow ambiguity.
    - Every well-formed program has exactly one meaning.
    - Doesn't have semantic error only.