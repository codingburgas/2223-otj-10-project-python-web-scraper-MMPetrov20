import requests
from bs4 import BeautifulSoup

# Define specific product parameters
specific_product_parameters = { 
    'gaming PCs' : ['CPU', 'GPU', 'RAM', 'Storage', 'Warranty period'],
    'all-in-one PCs' : ['Monitor', 'CPU', 'GPU', 'RAM', 'Storage', 'Warranty period'],
    'mouses' : ['Connectivity', 'Sensor', 'Sensitivity', 'Number of buttons', 'Interface', 'Warranty period'],
    'keyboards' : ['Technology', 'Interface', 'Backlight', 'BDS Cyrillic', 'Kit', 'Warranty'],
    'monitors' : ['Size', 'Resolution', 'Matrix type', 'Viewing angle', 'Refresh rate', 'Brightness', 'Interfaces'],
    'gaming laptops' : ['CPU', 'GPU', 'RAM', 'Storage','Monitor', 'Refresh rate', 'Warranty period'],
    'portable laptops' : ['CPU', 'GPU', 'RAM', 'Storage','Monitor', 'Warranty period'],
    'apple smartphones' : ['Operating system', 'Display', 'Refresh rate', 'Chipset', 'RAM', 'Built-in memory', 'Camera', 'Warranty period'],
    'samsung smartphones' : ['Operating system', 'Display', 'Refresh rate', 'Chipset', 'RAM', 'Built-in memory', 'Camera', 'Warranty period'],
    'xiaomi smartphones' : ['Operating system', 'Display', 'Refresh rate', 'Chipset', 'RAM', 'Built-in memory', 'Camera', 'Warranty period'],
    'asus smartphones' : ['Operating system', 'Display', 'Refresh rate', 'Chipset', 'RAM', 'Built-in memory', 'Camera', 'Warranty period'],
    'samsung TVs' : ['Screen size', 'Resolution', 'Warranty period'],
    'sony TVs' : ['Screen size', 'Matrix type', 'Resolution', 'Scan rate', 'Warranty period'],
    'philips TVs' : ['Screen size', 'Matrix type', 'Resolution', 'Scan rate', 'Warranty period']
}

# Define page variables
page = None
page_content = None
   
# Get the top page number
def get_top_page_num():
    page_numbing = page_content.find("ul", class_="pagination")
    numbers = []

    if page_numbing != None:
        for li in page_numbing.find_all("li", class_="number"):  
            #  Cast the li(type: Any) to int
            edited_li = int(li.text.strip())

            # Append the processed item to the list
            numbers.append(edited_li)
    else:
        return 1

    return max(numbers)
    
# Web scraper
def collect_data(URL, selected_category, page_num):
    global page, page_content
    page = requests.get(URL)
    page_content = BeautifulSoup(page.content, "html.parser")
    products = page_content.find_all("div", class_="product")
    product_info = []

    # Iterate through the scraped products
    for i in products:
        # Build a list with the product's parameters
        parameters = i.find("ul", class_="parameters")
        
        # Process the product's parameters
        list_items = []
        for li in parameters.find_all("li"):  
            #  Cast the li(type: Any) to string
            edited_li = str(li.text.strip())

            # Check for and edit odd list items
            if(edited_li.find(':') > 0):
                edited_li = edited_li.split(':', 1)[1]
                edited_li = edited_li[1:]

            # Append the processed item to the list
            list_items.append(edited_li)

        # Check if a product has enough listed parameters
        if(len(list_items) == len(specific_product_parameters[selected_category])):
            # Get the product's listed name
            product_name = i.find("div", class_="isTruncated").text.strip()

            # Get the product's listed price
            product_price = str(i.find("div", class_="prices").find("div", class_="price").find("span").text.strip())
            product_price = product_price.replace("00", "") # Format out the extra zeros

            # Build a dictionary from the product parameters and their values 
            parameter_package = dict(zip(specific_product_parameters[selected_category], list_items))

            # Join the dictionary of parameters with the product's name and price
            product_package = {'Name': product_name, **parameter_package, 'Price' : product_price}

            # Append the complete product package to the list
            product_info.append(product_package)

    # Return the finished list of product packages
    return product_info

# Print collected data
def print_data(product_info):

    # Iterate throught the product
    for dictionary in product_info:

        # Print data from the product packages
        for key, value in dictionary.items():
            print(f"{key}: {value}")
            
        # Print a blank line between the product packages
        print()