import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException




# Load Values
def load_dictionary(list):
    df = pd.read_excel (r'D:\profiles\echoi.guest\Documents\GitHub\C-S-\lush_ingredients_list.xlsx')
    for ind in df.index:
        temp = (df['List'][ind])
        list.append(temp)

base_url= 'https://www.lush.ca'

table_data=["https://www.lush.ca/en/new/new-products/","https://www.lush.ca/en/new/spring","https://www.lush.ca/en/new/easter","https://www.lush.ca/en/new/mothers-day/",
            "https://www.lush.ca/en/discover/bestsellers/","https://www.lush.ca/en/discover/vegan/","https://www.lush.ca/en/discover/naked/","https://www.lush.ca/en/discover/collections/",
            "https://www.lush.ca/en/discover/online-exclusives/","https://www.lush.ca/en/discover/valentines-day/","https://www.lush.ca/en/bath/bath-bombs/","https://www.lush.ca/en/bath/bubble-bars/",
            "https://www.lush.ca/en/bath/bath-oils/","https://www.lush.ca/en/bath/kids-faves/","https://www.lush.ca/en/shower/bar-soap/","https://www.lush.ca/en/shower/shower-gels-jellies/","https://www.lush.ca/en/shower/naked-shower-gels/",
            "https://www.lush.ca/en/shower/body-scrubs","https://www.lush.ca/en/shower/shower-bombs/","https://www.lush.ca/en/shower/shaving-creams/","https://www.lush.ca/en/shower/body-cleansers/","https://www.lush.ca/en/shower/body-butters-conditioners/",
            "https://www.lush.ca/en/bath-shower/citrus/","https://www.lush.ca/en/bath-shower/floral/","https://www.lush.ca/en/bath-shower/herbal/","https://www.lush.ca/en/bath-shower/sweet/",
            "https://www.lush.ca/en/hair/shampoo-bars/","https://www.lush.ca/en/hair/shampoo/","https://www.lush.ca/en/hair/conditioners/","https://www.lush.ca/en/hair/hair-treatments/","https://www.lush.ca/en/hair/styling/","https://www.lush.ca/en/hair/pressed-conditioners/",
            "https://www.lush.ca/en/hair/henna-hair-dyes/","https://www.lush.ca/en/hair/moisturizing/","https://www.lush.ca/en/hair/shine-enhancing/","https://www.lush.ca/en/hair/volumizing/",
            "https://www.lush.ca/en/face/cleansers-scrubs/","https://www.lush.ca/en/face/moisturizers/","https://www.lush.ca/en/face/toners-and-steamers/","https://www.lush.ca/en/face/masks/","https://www.lush.ca/en/face/makeup/","https://www.lush.ca/en/face/lip-scrubs-and-balms/","https://www.lush.ca/en/face/teeth/","https://www.lush.ca/en/face/shaving/",
            "https://www.lush.ca/en/face/balancing/","https://www.lush.ca/en/face/exfoliating/","https://www.lush.ca/en/face/moisturizing/","https://www.lush.ca/en/face/soothing/",
            "https://www.lush.ca/en/body/body-lotions/","https://www.lush.ca/en/body/massage-bars/","https://www.lush.ca/en/body/handcare/","https://www.lush.ca/en/body/footcare/","https://www.lush.ca/en/body/shaving-creams/","https://www.lush.ca/en/body/body-cleansers/","https://www.lush.ca/en/body/deodorants-and-dusting-powders/",
            "https://www.lush.ca/en/fragrances/perfume/","https://www.lush.ca/en/fragrances/body-sprays/","https://www.lush.ca/en/fragrances/perfume-library/","https://www.lush.ca/en/fragrances/perfume-library/","https://www.lush.ca/en/fragrances/solid-perfume/",
            "https://www.lush.ca/en/gifts/gift-sets/","https://www.lush.ca/en/gifts/knot-wraps/","https://www.lush.ca/en/gifts/accessories/"]

options = webdriver.ChromeOptions()
# Save on processing time, no GUI and other chrome options
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Scraping Method to find product links
def findProducts(url,products,driver):
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script('window.stop();')
    parent = driver.find_elements_by_class_name('link')
    for block in parent:
        element = block.get_attribute('href')
        products.append(element)
    print("Completed Scraping: " + url)

# Only add ingredients
def matchIngredients (url,palm_oil_derivatives,palm_oil_products,driver):
    specific_product_ingredients=[]
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script('window.stop();')

    parent = driver.find_elements_by_class_name('ingredient-link-wrapper')
    for block in parent:
        elements = block.find_elements_by_tag_name('a')
        specific_product_ingredients.append(block.text)
        print(block.text)
    for item in specific_product_ingredients:
        print ("comparing item:"+item)
        if item in palm_oil_derivatives:
            palm_oil_products.add(url)
            break

if __name__=='__main__':
    chrome_install = webdriver.remote
    driver =webdriver.Chrome(chrome_install , options=options)
    palm_oil_ingredients=[]
    load_dictionary(palm_oil_ingredients)
    print(palm_oil_ingredients)
    palm_oil_products = set()
    products_url=[]
    for product_category in table_data:
        findProducts(product_category, products_url,driver)
    print(products_url)
    for product_url in products_url:
        matchIngredients(product_url,palm_oil_ingredients,palm_oil_products,driver)
    print(palm_oil_products)





