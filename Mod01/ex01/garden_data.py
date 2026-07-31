class Plant :
    def __init__(self, name : str, age : int, height : int)->None :
        self.name = name
        self.age = age
        self.height = height

    #=== Garden Plant Registry ===
    #Rose: 25cm, 30 days old
    #Sunflower: 80cm, 45 days old
    #Cactus: 15cm, 120 days old

def main() :
    Rose = Plant("Rose", 30, 25)
    Sunflower = Plant("Sunflower", 45, 80)
    Cactus = Plant("Cactus", 120, 15)
    print("=== Garden Plant Registry ===")
    print(Rose.name, ": ", Rose.height, "cm, ", Rose.age, "days old.")
    print(Sunflower.name, ": ", Sunflower.height, "cm, ", Sunflower.age, "days old.")
    print(Cactus.name, ": ", Cactus.height, "cm, ", Cactus.age, "days old.")



if __name__ == "__main__" :
    main()