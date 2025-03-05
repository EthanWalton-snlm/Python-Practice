# Assignment:
# Write a comparison in terms of scope on keywords
# global vs nonlocal
# with examples


global color
color = "blue"


def sky_color():
    color = "green"
    global colour
    return f"The sky is {color}"


print(sky_color())
