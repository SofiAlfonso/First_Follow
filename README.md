## First and Follow Set Calculator <br>
This project was created by David Ramírez and Ana Sofía Alfonso.    A Python project to compute the First and Follow sets of a specific grammar.

# Table of Contents
- Introduction
- Usage
- Examples
- Features

# Introduction

This Python project, developed by David Ramírez and Ana Sofía Alfonso, helps users compute First and Follow sets for context-free grammars. It's handy for students and pros working on compiler design and syntax analysis. It's a great tool for grasping grammars, creating parsing methods, and improving compilers.

# Usage
Instructions on how to use the project to compute First and Follow sets.

python "main.py"
When prompted, enter the number of cases, the number of nonterminals, and the productions in the following format:

#### Enter the number of cases: 1
#### Enter the number of nonterminals: 3
```
- S -> A B
- A -> a B c | ε
- B -> b
```
# Example of grammar input
```
grammar = Grammar()
grammar.add_production('S', 'A B')
grammar.add_production('A', 'a B c | ε')
grammar.add_production('B', 'b')
grammar.compute_first()
grammar.compute_follow()
grammar.print_first_and_follow()
```

# Expected output
```
 First(S) = {a, b, ε}
 First(A) = {a, ε}
 First(B) = {b}
 Follow(S) = {$}
 Follow(A) = {b, c}
 Follow(B) = {c, $}
```
# Features

1. Calculate First sets: The project computes First sets for context-free grammars, crucial for predicting symbols in parsing algorithms like LL and LR parsers. It's based on established algorithms, ensuring accurate results.
2. Calculate Follow sets: The project also computes Follow sets, essential for predictive parsing methods such as LL(1) parsing. Follow sets aid in constructing parsing tables and resolving parsing conflicts.
3. Handles epsilon (ε) productions: The implementation effectively manages epsilon productions, ensuring accurate computation of First and Follow sets. It appropriately incorporates epsilon transitions for comprehensive analysis of grammar predictability.


