import json
from datetime import datetime

import matplotlib.pyplot as plt

selected_country = input("Enter a country: ").strip().casefold()

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []
country_total_hours = 0

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not duration_text:
        continue

    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    if eva.get("country", "").strip().casefold() == selected_country:
        country_total_hours += duration_hours

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

print(f"Total EVA duration for {selected_country.upper()}: {country_total_hours:.2f} hours")

plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
