lines = [
    "AVS",
    "# ADSADA",
    "      ",
    "ASDASDAS",
    "'''sdasdasd'''"
]
line_counter = 0
for line in lines:
    if line.lstrip().startswith("#") == False and len(line.strip()) > 0:
        line_counter += 1
print (f"Number of lines of code in the file = {line_counter}")
