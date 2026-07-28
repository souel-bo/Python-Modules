# Python Module 00 - Fundamentals

## Overview

This module introduces the core concepts of the Python programming language.

The goal is not only to learn Python syntax, but also to understand how Python executes programs, how objects behave, and how to write clean, readable code.

This repository contains my personal solutions together with notes explaining every concept introduced throughout the module.

---

# Learning Objectives

By the end of this module, You should understand:

- Python function definitions
- User input and program output
- Variables and object references
- Basic data types
- Type conversion
- Arithmetic operations
- Conditional statements
- Iteration using loops
- Recursion
- Type annotations
- String methods
- Writing readable Python code

---

# Concepts Covered

| Exercise | Topic |
|----------|-----------------------------|
| ex00 | Functions & print() |
| ex01 | User input & variables |
| ex02 | Type conversion & arithmetic |
| ex03 | Calculations |
| ex04 | Conditional statements |
| ex05 | Multiple conditions |
| ex06 | Loops & recursion |
| ex07 | Type hints & string methods |

---

# Skills Developed

Throughout this module You practice:

- Reading specifications carefully
- Writing small reusable functions
- Thinking algorithmically
- Breaking problems into smaller steps
- Producing clean and readable code
- Following Python conventions

---

# Python Concepts Learned

## Functions

Functions group instructions into reusable blocks.

Topics:

- `def`
- Parameters
- Function calls
- Return values

---

## Variables

Variables in Python are names that reference objects.

Unlike C, variables do not directly store values.

---

## Objects

Everything in Python is an object.

Examples:

- integers
- strings
- functions
- lists

Each object has:

- Identity
- Type
- Value

---

## Mutable vs Immutable Objects

Immutable:

- int
- float
- bool
- str
- tuple

Mutable:

- list
- dict
- set

---

## Decision Making

Python provides:

- `if`
- `elif`
- `else`

to execute code conditionally.

---

## Loops

Iteration allows repeating instructions.

Topics:

- `while`
- loop variables
- stopping conditions

---

## Recursion

A recursive function solves a problem by calling itself.

Every recursive function requires:

- Base case
- Recursive case
ME 
---

## Type Hints

Example:

```python
def add(a: int, b: int) -> int:
```

Type hints improve readability and can be checked using `mypy`.

---

## String Methods

Strings provide useful methods such as:

- `capitalize()`
- `upper()`
- `lower()`
- `strip()`

Strings are immutable, so these methods return new string objects.

---

# Repository Structure

```
Mod00/
│
├── README.md
│
├── ex00/
├── ex01/
├── ex02/
├── ex03/
├── ex04/
├── ex05/
├── ex06/
└── ex07/
```

Each exercise contains:

- the Python solution
- a dedicated README explaining the concepts introduced
- implementation notes

---

# What You Learned

This module help you understand that Python is more than just a simpler syntax than C or C++.

Key takeaways include:

- Everything is an object.
- Variables are references to objects.
- Functions are first-class objects.
- Python emphasizes readability and simplicity.
- Type hints improve maintainability without changing runtime behavior.

---

# Next Module

The next module will build on these fundamentals by introducing more advanced Python features such as data structures, object-oriented programming, exception handling, modules, and additional standard library tools.