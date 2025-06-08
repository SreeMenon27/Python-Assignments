import numpy as np
import json

# Load the JSON data
with open('nobelprize.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

prizes = data["prizes"]

#### --------------  Basic Summary Statistics ----------

# Total years present
years = np.array([prize["year"] for prize in prizes])
unique_years, years_count = np.unique(years, return_counts = True)

print("\n" + "-" * 45)
print("🔁  Basic Summary Statistics")
print("-" * 45)
print(f"🗓️   {'Total years present :':<30} {len(unique_years):<15}")

# Total prizes awarded (combination of year and category)
no_of_prizes = np.array([prize["year"]+prize["category"] for prize in prizes])
#print(len(np.unique(no_of_prizes)))
print(f"🏆  {'Total prizes awarded :':<30} {len(np.unique(no_of_prizes)):<15}")


# Total laureates honoured
laureates = [l["firstname"] for prize in prizes if "laureates" in prize for l in prize["laureates"]]
print(f"🎖️   {'Total laureates honoured :':<30} {len(laureates):<15}")


# Total unique categories
categories = np.array([prize["category"] for prize in prizes ])
unique_categories = np.unique(categories)
print(f"🗂️   {'Total unique categories :':<30} {len(unique_categories):<15}")

#### --------------  Group Summary Statistics ----------

print("-" * 45)
print("📊  Group Summary Statistics")
print("-" * 45)

# Laureates per category
print("-------- Laureates per category -------------")
cat_dict = {}
for prize in prizes:
    category = prize["category"]
    if "laureates" in prize:
        laureates_count = len(prize["laureates"])        
        if category not in cat_dict:
            cat_dict[category] = laureates_count
        else:
            cat_dict[category]+=laureates_count

total_category_laureates = len(laureates)

for key,values in sorted(cat_dict.items()):
    print(f"📚   {key:<30} : {values:<15}")

# Laureates % per category
print("-------- Laureates % per category -----------")

for key,values in sorted(cat_dict.items()):
    print(f"📈   {key:<30} : {int((values / total_category_laureates) * 100)} %")

# Laureates per year
print("-------- Laureates per year -----------------")
year_dict = {}
for prize in prizes:
    year = prize["year"]
    if "laureates" in prize:
        laureates_count = len(prize["laureates"])        
        if year not in year_dict:
            year_dict[year] = laureates_count
        else:
            year_dict[year]+=laureates_count

for key,values in sorted(year_dict.items()):
    print(f"📚   {key:<30} : {values:<15}")



