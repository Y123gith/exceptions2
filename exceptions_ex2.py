# אם מחלקים ב־0 – החזר None + סטטוס מתאים במקום קריסה
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_div(10, 0))


# אם האינדקס מחוץ לטווח – החזר את האיבר האחרון, ואם הרשימה ריקה החזר None
def get_item(items, i):
    try:
        return items[i]
    except IndexError:
        return None

print(get_item([5, 6, 7], 10))


# אם הקלט אינו מחרוזת – החזר "Unknown" במקום קריסה
def normalize_name(name):
    try:
        return name.strip().title()
    except ValueError:
        return "Unkown"

print(normalize_name(None))


# אם אחד המפתחות חסר – התייחס אליו כ־0 והמשך לחשב ציון
def calc_score(stats):
    try:
        return stats["kills"] * 10 + stats["assists"] * 5 - stats["deaths"] * 3
    except KeyError:
        if not "kills" in stats.keys():
            return  stats["assists"] * 5 - stats["deaths"] * 3
        elif not "assists" in stats.key():
            return stats["kills"] * 10 - stats["deaths"] * 3
        else:
            return stats["kills"] * 10 + stats["assists"] * 5

print(calc_score({"kills": 2, "deaths": 1}))


# אם הפורמט אינו "מספר:מספר" – נסה לפצל לפי "-" ואם לא מצליח החזר 0
def area(spec):
    try:
        w, h = spec.split(":")
        return int(w) * int(h)
    except ValueError:
        try:
            w,h = spec.split("-")
            return int(w) * int(h)
        except ValueError:
            return 0
    
print(area("10-5"))


# אם הביטים מכילים תווים לא חוקיים – נסה לנקות אותם, ואם לא מצליח החזר None
def binary_to_int(bits):
    for i in range(2):
        try:
            return int(bits, 2)
        except ValueError:
            for i,bit in enumerate(bits):
                if bit == "1" or bit == "0":
                    if i == 0:
                        bits = bit
                    else:
                        bits = bits+bit
    return None

print(binary_to_int("10 01"))


# חשב ממוצע רק לערכים שניתן להמיר ל־float. אם אין – החזר None
def avg(nums):
    count = 0
    for i,value in enumerate(nums):
        try: 
            nums[i] = float(value)
        except TypeError:
            nums.pop(i)
            count += 1
    if len(nums)==count:
        return None 
    else:
        return sum(nums) / len(nums)

print(avg([10, "20", None, 30]))


# אם חסר מידע במבנה המקונן – החזר "NO_CITY" במקום קריסה
def get_city(user):
    try:
        return user["profile"]["address"]["city"].upper()
    except ValueError, KeyError:
        return "NO_CITY"

print(get_city({"profile": {"address": {}}}))


# אם הסכום אינו מספר או גדול מהיתרה – החזר את היתרה המקורית
def withdraw(balance, amount_text):
    try:
        amount = int(amount_text)
        if amount > balance:
            raise ValueError
        return balance - amount
    except ValueError:
        return balance
    
print(withdraw(100, "fifty"))


# אם האינדקס מחוץ לטווח – בחר איבר בצורה מחזורית. אם הרשימה ריקה – החזר None
def pick_code(codes, idx):
    if not codes:
        return None
    try:
        return codes[idx]
    except IndexError:
       return idx % len(codes)

print(pick_code(["A1", "B2", "C3"], 5))
