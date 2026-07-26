def water_reminder():
    last = input("Days since last watering : ")
    if int(last) > 2:
        print("Water the plants!")
    elif int(last) < 1 :
        print("wrong number")
    else:
        print("Plants are fine")

water_reminder()