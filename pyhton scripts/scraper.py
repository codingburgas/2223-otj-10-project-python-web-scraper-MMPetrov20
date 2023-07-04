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