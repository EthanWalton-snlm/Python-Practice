# Task 1.1

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
letters = []

for i in avengers:
    word = i.replace(" ", "")
    letters.append(len(word))

print(letters)
