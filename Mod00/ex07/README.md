# Exercise 07 - Seed Inventory

## Learning Objectives

- Learn Python type annotations.
- Learn string methods.
- Practice writing readable functions.

## Concepts Introduced

- Type hints
- Function signatures
- String methods
- `capitalize()`

## What is Required

Implement:

```python
def seed_inventory(
    seed_type: str,
    quantity: int,
    unit: str
) -> None:
```

Support the following units:

- packets
- grams
- area

Print "Unknown unit type" for any unsupported unit.

## What You Need to Implement

- Add type annotations.
- Use `capitalize()` on the seed name.
- Use `if`, `elif`, and `else`.
- Print the exact required output.

## Key Takeaways

- Type hints improve readability.
- They are checked by tools such as `mypy`.
- String methods belong to string objects.
- `capitalize()` returns a new string because strings are immutable.