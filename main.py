from variant import Variant


def main():
    print("Welcome to DeliveRoutes")
    properties = {
        "sizes": ["L", "M", "S", "XS"],
        "colors": ["Lucky Green", "White", "Black"],
        "fit": None
    }
    variant = Variant("Sneaker", "Air Jordan 1 Mid", 
                      "Indonesia", 259.99, 
                      "Inspired by the original AJ1", 
                      properties)
    print(variant.properties)


if __name__ == '__main__':
    main()