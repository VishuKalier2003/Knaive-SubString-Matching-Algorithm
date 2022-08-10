#Implementing Naive SubString Matching Algorithm... where we match the substring present at how many locations in the parent string...

# Creating the parent string...
a = int(input("Enter the number of characters in the string : "))
array = ['a'] * a;
for i in range(0, a):
    array[i] = input("Enter the position character : ")

#Creating the Substring...
x = int(input("Enter size of the substring : "))
sub = ['a'] * x;
for i in range(0, x):
    sub[i] = input("Enter the substring character : ")

# Print Operations...
print("Array : ")
for i in range(0, a):
    print(array[i], end=", ")
print()
print("SubString : ")
for i in range(0, x):
    print(sub[i], end=", ")
print()

# <--- Algorithm Begins --->
match = 0;     # Variable declaration
t = 0;
for i in range(0, a-x+1):      # Outer loop variable for the parent string... O(n) time...
    if(array[i] == sub[0]):       # If the first characters of the parent string and the substring match...
        t = i;
        for j in range(0, x):           # Inner loop for the substring... O(n) time...
            if(array[t] == sub[j]):    # If characters match at the given location...
                match = match + 1     # Increment the value...
            t = t + 1;     # Increase the index by +1...
    if(match == x):      # If the total matches are equal to the length of the substring then the substring is present at the given location...
        print("Substring at ",i," th location in the array !!")
    match = 0
# <--- Algorithm Ends --->