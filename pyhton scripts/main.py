from menu import select_category
from url_modification import update_URL
from scraper import collect_data, print_data

# Get the target product category
target_category = select_category()

# Update the URL to point to the target product category
URL = update_URL(target_category)

# Collect data from the URL
collected_data = collect_data(URL, target_category)

# Print the collectted data
print_data(collected_data)