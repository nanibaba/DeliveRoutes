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


def view(ID, name):
    print(f"Product ID: {ID}")
    print(f"Product Name: {name}", end="\n\n")


def view_expanded(ID, variant_name, country_of_origin, 
                  price, description, properties, name): 
    print(f"Variant ID: {ID}")
    print(f"Variant Name: {variant_name}")
    print(f"Variant Country of Origin: {country_of_origin}")
    print(f"Variant Price: {price}")
    print(f"Variant Description: {description}")
    print(f"Variant Properties: {properties}")
    print(f"Variant Type: {name}", end="\n\n")


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
    while command != '-1':

        if (command != 'view' and command != 'view-expanded' 
                and command != 'sort' and command != '-1'):
            print("Invalid command!", end="\n\n")
        else: 
            print("\n")
            with open(products_file, "r") as product_DB:
                reader = csv.reader(product_DB, delimiter=",")
                next(reader)
                for line in reader:
                    variants.append(map_variant(line, product_types))
                for type in product_types:
                    products.append(map_product(type, variants))
            if command == 'view':
                for product in products: 
                    view(product.ID, product.name)
            elif command == 'view-expanded':
                for product in products: 
                    for variant in product.variants:
                        view_expanded(variant.ID, variant.variant_name, 
                                      variant.country_of_origin, variant.price, 
                                      variant.description, variant.properties, 
                                      variant.name)
                        
        command = input("Command: ")


if __name__ == '__main__':
    main()