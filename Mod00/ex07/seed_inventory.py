def seed_inventory(seed_type : str, quantity : int, unit : str) -> None:
    print(seed_type.capitalize(), " seeds : ", quantity, unit, "available")


seed_inventory("carrot", 8, "grams")