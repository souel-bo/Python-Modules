def harvest_recursive(current_day, total_days):
    days = input("Days untill harvest : ")
    i = 1
    if i > int(days):
        return
    print("Day ", i)
    harvest_recursive()
    print("Harvest Time!")
