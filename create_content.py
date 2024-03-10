import json
from slugify import slugify
from datetime import datetime


from datetime import datetime, timedelta
import random

def get_random_date_last_3_months():
    now = datetime.now()
    three_months_ago = now - timedelta(days=90)  # Approximation of 3 months
    random_days = random.randint(0, 90)  # Generate a random number of days within the last 3 months
    random_date = three_months_ago + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

images={
        'Beauty':"/images/Beauty.webp", 
        'St. Lawrence Market':"/images/market.webp", 
        'Restaurants':"/images/Restaurant.webp", 
        'Retail':"/images/Retail.webp", 
        'Service':"/images/service.webp", 
        'Fitness':"/images/fitness.webp", 
        ' Health':"/images/fit.webp", 
        ' Service':"/images/service.webp", 
        'Health':"/images/fit.webp", 
        'Coffee Shops':"/images/Coffee.webp", 
        ' Restaurants':"/images/Restaurant.webp", 
        'Grocery / Convenience Store':"/images/grocery.webp", 
        'Art/Theatre':"/images/Theatre.webp", 
        ' Retail':"/images/Retail.webp", 
        ' St. Lawrence Market':"/images/market.webp", 
        'General':"/images/General.webp", 
        'Hotels / Accomodation':"/images/Hotel.webp", 
        'Historical Landmarks':"/images/HL.webp", 
        'Education':"/images/education.webp", 
        ' Hotels / Accomodation':"/images/Hotel.webp",
        
    }
# Load the enhanced business listings from the JSON file
with open('enhanced_business_listings.json', 'r') as f:
    businesses = json.load(f)

for business in businesses:
    # Generate a slug from the business name
    slug = slugify(business['name'])
    filename = f'{slug}.md'

    # Format the current date and time for the markdown template
    now = get_random_date_last_3_months()

    # Define categories if available, or default to an empty list
    data_all = []
    try:
        keywords = business.get("genre").split(",")
        for k in keywords:
            data_all.append(k.strip())
    except:
        pass
    categories = business.get('categories', data_all)

    choose_image =images.get('General',"/images/General.webp")
    if categories:
        choose_image=images.get(categories[0],"/images/General.webp")
    # Convert categories list to a string representation
    categories_str = ', '.join([f'"{category}"' for category in categories])

    description_str = ""
    try:
        description_str = business.get('meta_description', '').strip()
    except:
        pass
    
    if "Error" in description_str:
        description_str = ""

    # Prepare the content of the markdown file using the provided template
    content = f"""+++
title = "Toronto Business Directory - {business['name']}"
date = {now}
draft = false
description = "{description_str}"
image = "{choose_image}"
imageBig = "{choose_image}"
categories = [{categories_str}]
authors = ["CplsIT"]
avatar = "/images/avatar.webp"
featured = false
+++


* **URL** :  {business.get('website', 'N/A')}
* **Description** : {business.get('meta_description', 'No description available')}
* **Telephone** : {business.get('phone_number', 'N/A')}
* **Address** : {business.get('address', 'N/A')}"""

    # Write the content to the markdown file
    with open("content/posts/"+filename, 'w') as f:
        f.write(content)

print("Markdown files have been created for each business.")

"""
data_all = []
for data in json_data:
    print(data.get("genre"))
    try:
        keywords = data.get("genre").split(",")
        for k in keywords:
            data_all.append(k.strip())
    except:
        pass

list(dict.fromkeys(data_all))

"""

"""
[
    {
        'Beauty':"/images/Beauty.webp", 
        'St. Lawrence Market':"/images/market.webp", 
        'Restaurants':"/images/Restaurant.webp", 
        'Retail':"/images/Retail.webp", 
        'Service':"/images/service.webp", 
        'Fitness':"/images/fitness.webp", 
        ' Health':"/images/fit.webp", 
        ' Service':"/images/service.webp", 
        'Health':"/images/fit.webp", 
        'Coffee Shops':"/images/Coffee.webp", 
        ' Restaurants':"/images/Restaurant.webp", 
        'Grocery / Convenience Store':"/images/grocery.webp", 
        'Art/Theatre':"/images/Theatre.webp", 
        ' Retail':"/images/Retail.webp", 
        ' St. Lawrence Market':"/images/market.webp", 
        'General':"/images/General.webp", 
        'Hotels / Accomodation':"/images/Hotel.webp", 
        'Historical Landmarks':"/images/HL.webp", 
        'Education':"/images/education.webp", 
        ' Hotels / Accomodation:"/images/Hotel.webp"'
        
    }
        
        ]
"""