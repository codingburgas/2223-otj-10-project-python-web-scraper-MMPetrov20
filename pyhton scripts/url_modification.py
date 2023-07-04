# Update page URL based on the the selected product category
def update_URL(str): 

    # Initial page URL
    path = "https://ardes.bg/"

    # Modify the URL 
    match str:
        case "gaming PC":
            path += "kompyutri/nastolni-kompyutri/za-igri-gaming"

        case "mini PC":
            path += "kompyutri/nastolni-kompyutri/mini-pc"

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

        case "Apple smartphones":
            path += "smartfoni/smartfoni/apple"

        case "Samsung smartphones":
            path += "smartfoni/smartfoni/samsung"

        case "Xiaomi smartphones":
            path += "smartfoni/smartfoni/xiaomi"

        case "ASUS smartphones":
            path += "smartfoni/smartfoni/asus"

        case "Samsung TVs":
            path += "televizori-i-publichni-displei/televizori/samsung"

        case "Sony TVs":
            path += "televizori-i-publichni-displei/televizori/sony"

        case "Philips TVs":
            path += "televizori-i-publichni-displei/televizori/philips"

    # Return the modified URL
    return path