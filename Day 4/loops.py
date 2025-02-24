# Task 1.1 (While loop)
i = 1
while i <= 5:
    print("🔥" * i)
    i += 1


# Task 1.2 (Refactoring with for Loop)
for i in range(1, 6):
    print("🔥" * i)

# Task 1.3 (with while loop)
rows = int(input("Please tell the no of rows?: ").strip())
pattern = input("Please tell the pattern?: ").strip()

i = 1

while i <= rows:
    print(f"{pattern}" * i)
    i += 1


# Task 1.4 (Refactor with for loop)
rows = int(input("Please tell the no of rows?: ").strip())
pattern = input("Please tell the pattern?: ").strip()

for i in range(1, rows + 1):
    print(f"{pattern}" * i)

###

# Easy way
# for i in range(1, 51, 2):
#    print(i)

# Hard way
# for i in range(1, 51):
#    if i % 2 == 0:
#        continue
#    print(i)
