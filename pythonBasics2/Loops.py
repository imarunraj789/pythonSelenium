greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
    print("Second Line")
else:
    print("Condition do not match")
print("If else condition code is completed")

# FOR lOOP

obj = [2,3,5,6,89]

for i in obj :
    print(i*2)

# Sum of first 5 Natural Number 1+2+3+4+5 = 15

# range(i, j) - starts from i and ends at j-1

sumValue = 0
for j in range(1,6):
    sumValue = sumValue + j
print(sumValue)
print("*********************")

for k in range(1,10,2):
    print(k)
print("*********************")
print("Skipping first index")
for m in range(10):
    print(m)