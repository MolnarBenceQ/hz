import random
import math
import datetime
import statistics

def mai_datum_info():
    today = datetime.date.today()
    weekday_name = today.strftime("%A")
    day_of_year = today.timetuple().tm_yday
    return today, weekday_name, day_of_year

def rmd_nummer_gen(count=10, low=1, high=100):
    return [random.randint(low, high) for _ in range(count)]


def statisztikak(numbers):
    avg = statistics.mean(numbers)
    stdev = statistics.stdev(numbers)    
    mx = max(numbers)
    mn = min(numbers)
    sum_ = sum(numbers)
    s_sqrt = math.sqrt(sum_)
    return {
        "average": avg,
        "stdev": stdev,
        "max": mx,
        "min": mn,
        "sum": sum_,
        "sum_sqrt": s_sqrt
    }


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def first_main():
    # hetes kiírás
    nap,het_napja,hanyadik_nap = mai_datum_info()

    print(f"""ez a mai nap {nap}
    ez a hét napja {het_napja}
    ez a hanyadik nap az évben {hanyadik_nap}\n
    """)

    #random samok 
    rmd_number_list = rmd_nummer_gen()
    rmd_number_choise = random.choice(rmd_nummer_gen())
    print(f"""ez a rmd lista {rmd_number_list}
    és ez a kivalsztot szam {rmd_number_choise}\n""")

    #static
    static = statisztikak(rmd_number_list)
    print(f"""=== STATISZTIKÁK ===
    Átlag: {static['average']}
    Szórásminta): {static['stdev']}
    Maximum: {static['max']}
    Minimum: {static['min']}
    Összeg: {static['sum']}
    Összeg gyöke (√összeg): {static['sum_sqrt']}\n""")

    #prime check 
    if isPrime(rmd_number_choise):
        print(f"yippe prime szam {rmd_number_choise}")
        
# 2 rész 

    


def many_days_to_b_day():
    today = datetime.date.today()
    print(f"Mai dátum: {today.strftime('%Y-%m-%d')}")

    month = int(input("Add meg a szuli hónapod (1-12): "))
    day = int(input("Add meg a szuli napod (1-31): "))

    birthday_this_year = datetime.date(today.year, month, day)

    if birthday_this_year < today:
        birthday_next = datetime.date(today.year + 1, month, day)
    else:
        birthday_next = birthday_this_year

    remaining_days = (birthday_next - today).days

    print(f"{remaining_days} nap van hátra a következő születésnapodig!")

#many_days_to_b_day()





