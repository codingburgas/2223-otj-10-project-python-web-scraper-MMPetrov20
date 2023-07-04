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