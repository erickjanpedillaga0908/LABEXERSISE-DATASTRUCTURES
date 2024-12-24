basket = []
print ("Catch any of these fruits: ('apple', 'orange', 'mango', 'guava')")

x = int(input("How many fruits would you like to catch? "))

print("Choose a fruit to catch. Press A, O, M, or G.")

for i in range(x):
    i += 1
    fruits = input("Fruit " + str(i) + " of " + str(x) + ": ")
    
    if fruits.upper()=="A":
        basket.append("Apple")
    elif fruits.upper()=="O":
        basket.append("Orange")
    elif fruits.upper()=="M":
        basket.append("Mango")
    elif fruits.upper()=="G":
        basket.append("Guava")
    else:
        print("Invalid.")
    
print("Your basket now has: " + str(basket))

z = 0;

while z < len(basket):
    inp = input("Press E to eat a fruit. ")
    
    if (inp.upper() == "E"):
        basket.pop()
        print("Fruit(s) in the basket : " + str(basket))
print("No more fruits")
          

          



            
        

