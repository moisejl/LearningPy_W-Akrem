#these funciton has to be called first to adress dependency of even_or_odd function
def Sum_of_List(List_of_number):
  total = 0
  for number in List_of_number:
    total += number
  return total

def CountList(ListToCount):
  compteur = 0
  for _ in ListToCount:
    compteur += 1
  return compteur

# We played arount alot with this function in order to learn dependencies.
# Calling Functions within functions
# Understanding what pre-programmed functions do and how it works
def Even_or_odd(numbers):
    Outliers = []
    EvenNumbers = []
    OddNumbers = []
    for number in numbers:
        if number >= 100 or number == 0:
            print(f"{number} an outlier")
            Outliers.append(number)
        elif number % 2 != 0:
            print(f"{number} is an odd number")
            OddNumbers.append(number)
        else:
            print(f"{number} is an even number")
            EvenNumbers.append(number)
    print(Sum_of_List(Outliers))
    print(Sum_of_List(EvenNumbers))
    print(Sum_of_List(OddNumbers))
    print(Outliers)
    print(EvenNumbers)
    print(OddNumbers)
    print(len(EvenNumbers))
    print(CountList(EvenNumbers))
    all_lists = Outliers + EvenNumbers + OddNumbers
    print(sum(all_lists))

numberlist = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
Even_or_odd(numberlist)
print(Sum_of_List(numberlist))
