# Task 1.3

message = "    🚨🔍📱🔑secret_code✌️"

print(message[message.find("🔑") + 1 :].upper())

# Task 1.2

flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

original = flipped_message[::-1]

result_message = original[0:6] + "🗡️ " + original[12:20] + "🌸"

print(result_message.lower())

# Task 1.1

secret_message = "    Programming in Python is not only powerful but also fun!    "

first_index = secret_message.upper().find("PYTHON")
second_index = secret_message.upper().find("POWERFUL")
result_message = (
    secret_message[first_index : first_index + 6]
    + "-"
    + secret_message[second_index : second_index + 8]
)

print(result_message.upper())
