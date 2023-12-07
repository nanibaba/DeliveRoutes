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

    print("Welcome to DeliveRoutes!", end="\n\n")

    with open(products_file, "r") as product_DB:
        reader = csv.reader(product_DB, delimiter=",")
        next(reader)
        for line in reader:
            variants.append(map_variant(line, product_types))
        for type in product_types:
            products.append(map_product(type, variants))
        
        for product in products: 
            print(f"Product ID: {product.ID}")
            print(f"Product Name: {product.name}", end="\n\n")


if __name__ == '__main__':
    main()