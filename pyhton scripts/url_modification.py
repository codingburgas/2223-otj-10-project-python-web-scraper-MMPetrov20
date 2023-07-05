# Update page URL based on the the selected product category
def update_URL(str): 

    # Initial page URL
    path = "https://ardes.bg/"

    # Modify the URL 
    match str:
        case "gaming PCs":
            path += "kompyutri/nastolni-kompyutri/za-igri-gaming"

        case "all-in-one PCs":
            path += "kompyutri/nastolni-kompyutri/all-in-one"

        case "mouses":
            path += "periferiya/mishki"

        case "keyboards":
            path += "periferiya/klaviaturi"

        case "monitors":
            path += "periferiya/monitori"

        case "gaming laptops":
            path += "laptopi/laptopi/za-igri"

        case "portable laptops":
            path += "laptopi/laptopi/teglo-do-2"

        case "apple smartphones":
            path += "smartfoni/smartfoni/apple"

        case "samsung smartphones":
            path += "smartfoni/smartfoni/samsung"

        case "xiaomi smartphones":
            path += "smartfoni/smartfoni/xiaomi"

        case "asus smartphones":
            path += "smartfoni/smartfoni/asus"

        case "samsung TVs":
            path += "televizori-i-publichni-displei/televizori/samsung"

        case "sony TVs":
            path += "televizori-i-publichni-displei/televizori/sony"

        case "philips TVs":
            path += "televizori-i-publichni-displei/televizori/philips"

    # Return the modified URL
    return path

# Point URL to the next product subcategory page
def page_up(path, top_name_num):

    if top_name_num != 1:
        # Check if the URL already has a page number
        if 'page' in path:
            # Find the index of the last '/'
            symbol_index = path.rfind("/")

            if symbol_index != -1:
                # Seperate the page number from the URL
                page_num_str = path[(symbol_index + 1):]

                # Get the page number as an integer
                page_num_int = int(page_num_str)

                # Update the page number
                page_num_int += 1

                # Replace the old page number with the new one
                path = path.replace(page_num_str, str(page_num_int))
        else:
            # Update the URL with a page indicator
            path += "/page/2"
    else:
        return path

    # Return the updated URL
    return path
