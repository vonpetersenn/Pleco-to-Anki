from numerical_pinyin_converter import convert_from_numerical_pinyin

print("Welcome to the numerical pinyin converter.")

print("")

print("Input numerical pinyin (tai4 kong1) and get back pinyin with tone marks (tài kōng).")
print("Examples of valid numerical pinyin: huang1 miu4, lve4 duo2, tai4 tai5, xian4 r5")

print("")

while True:
    pinyin = input("Enter numerical pinyin: ")
    try:
        print(convert_from_numerical_pinyin(pinyin))
    except Exception as e:
        print("Sorry, please enter valid pinyin (ex: huang1 miu4, lve4 duo2, tai4 tai5, xian4 r5)")
       # print(e)
