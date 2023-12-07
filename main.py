from decimal import Decimal
from variant import Variant
from product import Product
import csv
import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def map_properties(sizes, colors, fit):
    return {
        "sizes": sizes,
        "colors": colors,
        "fit": fit
    }


def map_variant(line, product_types):
    name = line[7]
    variant_name = line[0]
    country = line[1]
    price = Decimal(line[2])
    descriprion = line[3]
    sizes = line[4].split('/')
    colors = line[5].split('/')
    fit = None if line[6] == "None" else line[6]
    properties = map_properties(sizes, colors, fit)

    if name not in product_types: 
        product_types.append(name)
            
    return Variant(name, variant_name, country, 
                   price, descriprion, properties)


def map_product(type, variants):
    product = Product(type) 
    product.variants = list(
        filter(lambda variant: 
               variant.name == type, 
               variants))
    return product


def main():
    variants = []
    products = []
    product_types = []
    config = read_config()
    products_file = config['Files']['products_file']

    print("Welcome to DeliveRoutes!")
    print("What would you like to do?")
    print("Enter 'view' to view the list of products.")
    print("Enter 'view-expanded' to view the expanded list of products.")
    print("Enter 'sort' to sort the expanded list of products", end=" ")
    print("by a selected property.")
    print("Enter 'order' to create a sales order.")
    print("Enter '-1' to quit the program.", end="\n\n")

    command = input("Command: ")
    print("\n")
    while command != '-1':

        if (command != 'view' and command != 'view-expanded' 
                and command != 'sort' and command != '-1'):
            print("Invalid command!", end="\n\n")
        else: 
            with open(products_file, "r") as product_DB:
                reader = csv.reader(product_DB, delimiter=",")
                next(reader)
                for line in reader:
                    variants.append(map_variant(line, product_types))
                for type in product_types:
                    products.append(map_product(type, variants))
            if command == 'view':
                for product in products: 
                    print(f"Product ID: {product.ID}")
                    print(f"Product Name: {product.name}", end="\n\n")
            elif command == 'view-expanded':
                for product in products: 
                    for variant in product.variants:
                        print(f"Variant ID: {variant.ID}")
                        print(f"Variant Name: {variant.variant_name}")
                        print(f"Variant Country: {variant.country_of_origin}")
                        print(f"Variant Price: {variant.price}")
                        print(f"Variant Description: {variant.description}")
                        print(f"Variant Properties: {variant.properties}")
                        print(f"Variant Type: {variant.name}", end="\n\n")
        command = input("Command: ")
        print("\n")


if __name__ == '__main__':
    main()