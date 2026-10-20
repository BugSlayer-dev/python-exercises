import json

expenses={
    "کاپشن":3500000,
    "گوشی":15000000,
    "کفش":4900000,
    "شارژ":150000,
    "نوشابه":120000,
    "نان":75000,
}

try:
    with open("new.json" , "w" , encoding="utf-8") as file :
        json.dump(expenses , file , ensure_ascii=False)
    with open("new.json" , "r" , encoding="utf-8") as file :
        loaded_expenses = json.load(file)
except OSError as e:
    print(f"مشکل در خواندن یا نوشتن فایل: {e}")
except json.JSONDecodeError as e:
    print(f"محتوای فایل JSON معتبر نیست: {e}")
else:
    total=0
    for title in loaded_expenses :
        total += loaded_expenses[title]
    print(f"Total Costs = {total:,}")
