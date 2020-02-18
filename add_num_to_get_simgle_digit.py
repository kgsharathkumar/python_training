def add_digits(num):
         if num > 0:
            return (num - 1) % 9 + 1
         else:
             return 0

print(add_digits(int(input("num"))))
print(add_digits(int(input("2nd num"))))
