from math import pi, cos  # Inbuilt
from datetime import datetime  # Imports on top of the file

print(pi)
print(cos(pi / 2))
print(cos(0))

now = datetime.now()
print(now)


print(f"The Current date is: {now:%d-%m-%Y}")
print(f"The Current date is: {now:%d/%m/%Y}")
print(f"The Current date is: {now:%d %m %Y}")
print(f"The Current date is: {now:%d %B %Y}")
print(f"The Current date is: {now:%d %b %Y}")

# 2025-12-28 # Dev
