import numpy as np
import json

# Reading the json file
with open("nobelprize.json","r",encoding="utf-8") as f:
    data = json.load(f)

prizes = data["prizes"]

#### --------------  Basic Summary Statistics ----------

# Total years present
years = np.array([prize["year"] for prize in prizes])
unique_years, years_count = np.unique(years, return_counts= True )

print("\n" + "-" * 45)
print("🔁  Basic Summary Statistics")
print("-" * 45)
print(f"🗓️   {'Total years present ':<30}  : {len(unique_years):<15}")

# Total prizes awarded (combination of year and category)
no_of_prizes = np.array([prize["year"]+prize["category"] for prize in prizes])
print(f"🏆  {'Total prizes awarded ':<30}  : {len(np.unique(no_of_prizes)):<15}")

# Total laureates honoured
all_laureates = np.array([l["id"] for prize in prizes if "laureates" in prize for l in prize["laureates"]])
print(f"🎖️   {'Total laureates honoured ':<30}  : {len(all_laureates):<15}")

# Total unique categories
all_categories = np.array([prize["category"] for prize in prizes])
unique_categories = np.unique(all_categories)
print(f"🗂️   {'Total unique categories ':<30}  : {len(unique_categories):<15}")

# Year with max no of laureates
all_entries = []

for prize in prizes:
    year = prize["year"]
    if "laureates" in prize:
        no_of_laureates = len(prize["laureates"])
        all_entries.extend([year]*no_of_laureates)

np_all_entries = np.array(all_entries)
np_laureates_year, counts = np.unique(all_entries,return_counts = True)

max_index = np.argmax(counts) # finding index with highest count
print(f"📅  {'Year with the most laureates ':<30}  : {np_laureates_year[max_index]:<15}")

# Least laureates awarded year
min_index = np.argmin(counts) # finding index with highest count
print(f"📅  {'Year with the least laureates ':<30}  : {np_laureates_year[min_index]:<15}")

#### --------------  Group Summary Statistics ----------
print("-" * 45)
print("📊  Group Summary Statistics")
print("-" * 45)

# Laureates per category
print("-------- Laureates per category -------------")
all_entries = []

for prize in prizes:
    category = prize["category"]
    if "laureates" in prize:
        no_of_laureates = len(prize["laureates"])
        all_entries.extend([category] * no_of_laureates)

np_all_entries = np.array(all_entries)
np_laureates_category, counts = np.unique(np_all_entries, return_counts=True)

for category, count in zip(np_laureates_category, counts):
    print(f"📚   {category:<30} : {count:<15}")


# Laureates % per category
print("-------- Laureates % per category -----------")
for category,count in zip(np_laureates_category, counts):
    percent = (int(count)/int(len(all_laureates))) * 100
    print(f"📈   {category:<30} : {percent:.1f} %")




