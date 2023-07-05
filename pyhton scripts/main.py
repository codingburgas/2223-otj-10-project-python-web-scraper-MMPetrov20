import os
import requests
from bs4 import BeautifulSoup
from menu import select_category
from url_modification import update_URL, page_up
from scraper import collect_data, print_data, get_top_page_num

def main():
    # Get the target product category
    target_category = select_category()

    # Update the URL to point to the target product category
    URL = update_URL(target_category)

    # Collect data from the URL
    page_data = []
    page_num = 1

    # Clear the terminal
    os.system("cls")

    while(True):
        # Collect date from a page
        page_data = collect_data(URL, target_category, page_num)

        # Check if top page has been reached
        if page_data != None:
            # Print the data collected from the page
            print_data(page_data, page_num)

            if page_num != get_top_page_num():
                # Update the URL to point to the next page
                URL = page_up(URL, get_top_page_num())

                # Update the page number
                page_num += 1
            else:
                break
        else:
            break

# Run main function
if __name__ == "__main__":
    main()
