class Plant :
    def __init__(self, name : str, age : int, height : float, grow_rate : float)->None :
        self.name = name
        self.age = age
        self.height = height
        self.grow_rate = grow_rate

    def print_info(self) :
        print(self.name, ": ", round(self.height, 1), "cm, ", self.age, "days old.")
    def grow(self):
        self.print_info()
        total = 0
        for i in range(1, 8) :
            print("=== Day ", i , " ===")
            self.height += self.grow_rate
            self.age += 1
            total += self.grow_rate
            self.print_info()
        print("Growth this week: ", round(total, 1), "cm")


def main() :
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose", 30, 25, 0.8)
    Sunflower = Plant("Sunflower", 45, 80, 0.6)
    Cactus = Plant("Cactus", 120, 15, 0.5)
    Rose.grow()



if __name__ == "__main__" :
    main()