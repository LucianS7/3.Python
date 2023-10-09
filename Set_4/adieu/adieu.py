import inflect

p = inflect.engine()

Names = []

while True:
    try:
        name = input ("Name: ")
        Names = Names + [name]
    except EOFError:
        break

print ("Adieu, adieu, to " + p.join(Names))


