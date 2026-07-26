def recursion(i, days):
    if (i > days):
        print("Harvest Time!")
        return
    print("Day ", i)
    recursion(i + 1, days)

def harvest_recursive():
    days = input("Days untill harvest : ")
    i = 1
    recursion(i, int(days))

harvest_recursive()