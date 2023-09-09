def convert(number):
    # BLAZINGLY FAST GRAAAAAAAH 
    return ''.join(text for divisor, text in {3:"Pling", 5:"Plang", 7:"Plong"}.items() if not number % divisor) or str(number)


print(convert(30))