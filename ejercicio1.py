print("Hello, world")

for num in range(10):
    print(num)
    
letras=["a","e","i","o","u"]
for letra in letras:
    print(letra)
    
    
suma = 2 + 2
print(suma)

multiplicar = 2 * 2
print(multiplicar)

dividir = 4 / 2
print(dividir)

potencia = 4 ** 2
print(potencia)

modulo = 4 % 2
print(modulo)

print("Python has three numeric types: int, float, and complex")

myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

valor = 3.14
print(valor)
print(type(valor))
print(str(valor) + " is of the data type " + str(type(valor)))

valor2 = 5j
print(valor2)
print(type(valor2))
print(str(valor2) + " is of the data type " + str(type(valor2)))

valor3 = True
print(valor3)
print(type(valor3))
print(str(valor3) + " is of the data type " + str(type(valor3)))

valor4 = False
print(valor4)
print(type(valor4))
print(str(valor4) + " is of the data type " + str(type(valor4)))

myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


"""
name = input("What is your name? \n")
print(name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
"""

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

