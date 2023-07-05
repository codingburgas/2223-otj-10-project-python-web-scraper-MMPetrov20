import os

""""
1 PCs
    gaming PCs
    all-in-One PCs
2 PC periferals
    mouses
    keyboards
    monitors
3 laptops
    gaming laptops
    portable laptops
4 smartphones
    apple
    samsung
    xiaomi
    ASUS
5 TVs
    samsung
    sony
    philips
"""

# First layer menu options
menu_options = ["PCs", "PC periferals", "Laptops", "Smartphones", "TVs"]

# Second layer menu options
menu_suboptions = [
    ["gaming PCs", "all-in-one PCs"], 
    ["mouses", "keyboards", "monitors"],
    ["gaming laptops", "portable laptops"],
    ["apple smartphones", "samsung smartphones", "xiaomi smartphones", "asus smartphones"],
    ["samsung TVs", "sony TVs", "philips TVs"]
]

# Display first menu layer
def display_first_menu_layer():
    
    row_num = 1
    for x in menu_options:
        print(f'{row_num}. {x}')
        row_num += 1

# Display second menu layer
def display_second_menu_layer(user_input):

    # Clear the terminal
    os.system("cls")

    row_num = 1
    for y in menu_suboptions[user_input-1]:
        print(f'{row_num}. {y}')
        row_num += 1

# Select category of products for data scraping 
def select_category():
    first_layer_input = 0
    second_layer_input = 0

    display_first_menu_layer()
    first_layer_input = int(input())

    display_second_menu_layer(first_layer_input)
    second_layer_input = int(input())

    return menu_suboptions[first_layer_input-1][second_layer_input-1]