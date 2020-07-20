
try:
    print("resource open")
    a = int(input("enter numerator: "))
    b = int(input("enter denominator: "))
    res = a/b
    print(res)
except ZeroDivisionError as ze:
    print("Oopsss: ", ze)
except ValueError as ve:
    print("Unable to parse: ", ve)
finally:
    print("resource close")
