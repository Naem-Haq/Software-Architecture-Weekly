import json
import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

countries = sorted(set(
    eva.get("country")
    for eva in eva_data
    if eva.get("country")
))

print("Available countries:")
for country in countries:
    print("-", country)

country_input = input("Enter a country: ").strip()

selected_country = None

for country in countries:
    if country.lower() == country_input.lower():
        selected_country = country
        break

if selected_country is None:
    print("Country not found.")
    exit()

records = []
country_total_hours = 0

for eva in eva_data:
    duration_text = eva.get("duration")

    if not duration_text:
        continue

    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    country = eva.get("country")

    if country and country.lower() == selected_country.lower():
        country_total_hours += duration_hours

    date_text = eva.get("date")

    if not date_text:
        continue

    date = datetime.fromisoformat(date_text)

    records.append((date, duration_hours))

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

for date, duration_hours in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)

print("\nCountry EVA Statistics:")
print(f"{selected_country}: {country_total_hours:.2f} hours")

with open(
    "country_statistics.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)

    writer.writerow([
        "Country",
        "Total EVA Duration (hours)"
    ])

    writer.writerow([
        selected_country,
        f"{country_total_hours:.2f}"
    ])

print("\nCountry statistics saved to country_statistics.csv")

plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()