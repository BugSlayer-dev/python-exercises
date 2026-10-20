import json
def load_text(name_file):
    try:
        with open(name_file,"r",encoding="utf-8") as file:
            texts = json.load(file)
    except FileNotFoundError:
        return []
    if not isinstance(texts,list):
        raise ValueError("باید لیست باشد.")
    if not all(isinstance(text,str) for text in texts):
        raise ValueError("همه ی اعضای لیست باید متن باشد .")
    return texts

def add_text(file_name,text):
    texts=load_text(file_name)
    texts.append(text)
    with open(file_name,"w",encoding="utf-8") as file:
        json.dump(texts,file,ensure_ascii=False,indent=2)
    print("متن ذخیره شد.")

def show_all(file_name):
    texts=load_text(file_name)
    if not texts:
        print("متنی هنوز ثبت نشده است.")
        return
    for number,text in enumerate(texts,start=1):
        print(f"{number},{text}")


while True:
    try:
        print("1 = افرودن متن \n")
        print("2 = نمایش همه \n")
        print("3 = خروج \n")
        number=input("انتخااب عدد مورد نظر : ").strip()
        if number not in ("1","2","3"):
            print("لطفا بین اعداد 1 تا 3 انتخاب کن .")
            continue
        if number == "3":
            break
        name_file=input("اسم فایل را انتخاب کنید( با پسوند ) = ").strip()
        if not name_file:
            print("باید اسم فایل مورد نظر را وارد کنی")
            continue
        if number=="1":
            text=input("متن مورد نظر را انتخاب کنید = ").strip()
            if not text:
                print("باید متن فایل مورد نظر را وارد کنی")
                continue
            add_text(name_file,text)
        else:
            show_all(name_file)
    except OSError as e:
        print(f"مشکل در خواندن یا نوشتن فایل: {e}")

    except json.JSONDecodeError:
        print("محتوای فایل JSON معتبر نیست؛ فایل را بررسی کن.")

    except ValueError as e:
        print(e)

