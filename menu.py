""""
Name: Dehinde Shogbanmu

Software Development 1 
Product List Menu Driven Program
"""

option = 0

product_codes = []
product_names = []

product_list = []
product_dict = {}

while option != 9:
    print("""
1. Input Product Details
2. Populate a 2-D list from the 1-D lists
3. Populate a Dictionary with the product data
4. Lookup 2-D list by index
5. Lookup Dictionary by Key
9. Exit
    """)

    option = input("Select menu from option : ")
    option = int(option)

    if option == 1:
        prod_code = input("Enter product code : ")
        product_codes.append(prod_code.upper())
        prod_name = input("Enter product name : ")
        product_names.append(prod_name)
        print(product_codes)
        print(product_names)

    elif option == 2:
        product_list = []
        for product in range(len(product_codes)):
            prod_code = product_codes[product]
            prod_name = product_names[product]
            product_list.append([prod_code, prod_name])
        print(product_list)

    elif option == 3:
        product_dict = {}
        for product in product_list:
            prod_code = product[0]
            prod_name = product[1]
            product_dict[prod_code] = prod_name
        print(product_dict)

    elif option == 4:
        product_idx = int(input("Enter index : "))
        product = product_list[product_idx]
        prod_code = product[0]
        prod_name = product[1]
        print(f"Index:{product_idx}, Code:{prod_code}, Name:{prod_name}")

    elif option == 5:
        prod_code = input("Enter product code : ")
        prod_code = prod_code.upper()
        if prod_code in product_dict:
            prod_name = product_dict[prod_code]
            print(f"Code:{prod_code}, Name:{prod_name}")
        else:
            print(f"Invalid! Code:{prod_code} is not in Dictionary")
