class PreciousStone:
    def __init__(self, carats=0.0, price=0.0, name="Unknown"):
        self.__carats = carats
        self.__price = price
        self.__name = name

    def get_carats(self):
        return self.__carats
    
    def set_carats(self, carats):
        self.__carats = carats

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"PreciousStone(name={self.__name}, carats={self.__carats}, price={self.__price})"
    
    def __repr__(self):
        return f"PreciousStone({self.__name}, {self.__carats}, {self.__price})"
    
    def details(self):
        return f"{self}"

def main():
    diamond = PreciousStone(1.5, 5000, "Diamond")
    ruby = PreciousStone(2.0, 10000, "Ruby")
    sapphire = PreciousStone(0.8, 2000, "Sapphire")

    stones = [diamond, ruby, sapphire]
    for stone in stones:
        print(stone.details())
        print()

if __name__ == "__main__":
    main()
