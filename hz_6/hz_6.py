import random as rmd
from datetime import datetime, timedelta

def txt_gen():
    start_date = datetime(2025, 10, 24)
    end_date = datetime(2025, 11, 24)
    days = (end_date - start_date).days + 1

    # felülírjuk a fájlt, hogy mindig tiszta legyen
    with open("i.txt", "w", encoding="utf-8") as txt_file:
        for plus_days in range(days):
            rmd_c = round(float(rmd.randint(0, 20)) + rmd.random(), 1)
            rmd_present = rmd.randint(0, 100)
            idojaras = rmd.choice(["szeles", "napos", "semillen", "ködös", "esős"])
            txt_file.writelines(
                f"Dátum: {start_date + timedelta(days=plus_days)}\n"
                f"Időjárás: {idojaras}\n"
                f"Hőmérséklet: {rmd_c}C\n"
                f"Várható eső: {rmd_present}%\n"
            )

def get_file_data(filename="i.txt"):
    records = []
    with open(filename, "r", encoding="utf-8") as f:
        block = {}
        for line in f:
            line = line.strip()

            if line.startswith("Dátum:"):
                if block:
                    records.append(block)
                    block = {}
                block["date"] = line.replace("Dátum:", "").strip()

            elif line.startswith("Időjárás:"):
                block["idojaras"] = line.replace("Időjárás:", "").strip()

            elif line.startswith("Hőmérséklet:"):
                temp = line.replace("Hőmérséklet:", "").strip()
                if temp.endswith("C"):
                    temp = temp[:-1]
                block["temp"] = temp.strip()

            elif line.startswith("Várható eső:"):
                rain = line.replace("Várható eső:", "").strip()
                if rain.endswith("%"):
                    rain = rain[:-1]
                block["esik_present"] = rain.strip()

        if block:
            records.append(block)

    return records


def find_first(date):
    for rec in get_file_data("i.txt"):
        if rec.get("date") == date:
            return rec
    return None


def ketto_ido_kozt(date_1, date_2):
    data = get_file_data("i.txt")
    ind_1 = None
    ind_2 = None

    for i, rec in enumerate(data):
        if rec.get("date") == date_1:
            ind_1 = i
            break

    for i, rec in enumerate(data):
        if rec.get("date") == date_2:
            ind_2 = i
            break

    if ind_1 is None or ind_2 is None:
        return []

    result = []
    for i in range(ind_1, ind_2 + 1):
        result.append(data[i])
    return result


def get_avg_temp(filename="i.txt"):
    data = get_file_data(filename)
    if not data:
        return 0.0

    total = 0.0
    count = 0

    for rec in data:
        if "temp" in rec:
            total += float(rec["temp"])
            count += 1

    if count == 0:
        return 0.0

    return round(total / count, 1)


def max_temp(filename="i.txt"):
    data = get_file_data(filename)
    if not data:
        return None

    max_rec = data[0]
    max_val = float(max_rec["temp"])

    for rec in data[1:]:
        if "temp" in rec:
            val = float(rec["temp"])
            if val > max_val:
                max_val = val
                max_rec = rec

    return max_rec


def list_of_esos_day(filename="i.txt"):
    data = get_file_data(filename)
    result = []
    for rec in data:
        if rec.get("idojaras") == "esős":
            result.append(rec)
    return result


def list_of_semillen_day(filename="i.txt"):
    data = get_file_data(filename)
    result = []
    for rec in data:
        if rec.get("idojaras") == "semillen":
            result.append(rec)
    return result



txt_gen()  
data = get_file_data()
print(f"beolvasott rekordok: {len(data)}")
print(f"első rekord: {data[0]}")
avg = get_avg_temp()
print(f"{avg} C")
mx = max_temp()
print(f"[max_temp]{mx}")
esos = list_of_esos_day()
print(f"{len(esos)}")
semi = list_of_semillen_day()
print(f"{len(semi)}")

first_date = data[0]["date"]
third_date = data[2]["date"]
between = ketto_ido_kozt(first_date, third_date)
print(f"[ketto_ido_kozt] {first_date} → {third_date} között: {len(between)} rekord")
for r in between:
    print("   ", r)
