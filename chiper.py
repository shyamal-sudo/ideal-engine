without_shift = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
with_shift = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# number of shift

shift = int(input("enter the number of shifts: "))

# shift number of letters


for i in range(shift):
    with_shift.insert(0, with_shift.pop(25))

user_str = str(input("Enter your message to encode: "))
us = user_str.upper()
# 👇 takes letters one by one and return the index value of that letter from withOut_shift list

num = []
for j in us:
    if j == " ":
        continue
    else:
        num.append(without_shift.index(j))

outputStr = ""
for k in num:
    outputStr = outputStr + with_shift[k]

for l in range(len(us)):
    if us[l] == " ":
        outputStr = outputStr[:l] + ' ' + outputStr[l:]

print(outputStr)
