fruit=input("what type of fruit are you sorting?")

if(fruit)== "apple" or "Apple" or "apples" or "Apples" or "aples" or "apels" or "apel":
    print("Apples go in bin 1!")

elif(fruit) == "oranges" or "orange" or "Oranges" or "Orange":
    print("Oranges go in bin 2!")
elif(fruit) == "Banana" or "Bananas" or "banana" or "bananas":
    print("Bananas go in bin 3!")

else:
    print("Error: I do NOT recognize that fruit.")
