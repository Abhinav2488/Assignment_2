# ------------------ Q 1 --------------------------

print("--------------------------------------------")

a1 =  8
a2 = 2

sum = a1 + a2
diff = a1 - a2
prod = a1 * a2
quo = a1//a2
print("Q1")
print(f"Sum = {sum} Difference = {diff} Product = {prod} Quotient = {quo}")

# ------------------ Q 2 --------------------------

a2 = 2
b2 = 3
a2 +=b2
# --------------
a3 = 8
b3 = 4
a3 -=b3
# --------------
a4 = 8
b4 = 4
a4 *=b4
# --------------
a5 = 8
b5 = 4
a5 /=b5
# --------------
a6 = 8
b6 = 4
a6 %=b6
# --------------
a7 = 8
b7 = 4
a7 //= b7

print("Q2")
print(f"Add = {a2} Subtraction = {a3} Multiplication = {a4} Division = {a5} Mode = {a6} Floor Division = {a7}")

#-------------------------- Q3 --------------------------------
print("Q3")

num1 = 8
num2 = 4

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# ------------------------ Q4 ---------------------------------

print("Q4")

if num1>num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")    

#--------------------------- Q5 ---------------------------------

print("Q5")    

p = 8
q = p


print(id(p))
print(id(q))

#------------------------- Q6 -----------------------------------
print("Q6")

x = 8
y = 4

print(x|y)
print(x&y)
print(x^y)
print(~x)

#---------------------------- Q7 ----------------------------------

print("Q7")

p1 = 8
p2 = -p1
print(p2)

#---------------------------- Q8 -----------------------------------

print('Q8')

num3, num4 = 8, 4
 
if num3 != num4:
    if num3 > num4:
        print(" Num 3 is greater than Num4")
    else:
        print("Num4 is greater than Num3")
else:
    print("Both Num3 and Num4 are equal")