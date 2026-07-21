colours = ("red", "green", "blue", "yellow", "purple")

print("The third colour in the tuple is:", colours[2])

print("\nThe colours in the tuple are:")
for colour in colours:
    print(colour)

print("\nThe length of the tuple colours is:", len(colours))

( a, b, c, d, e) = colours
print("\nThe fourth colour in the tuple is:", d)

del colours
print("\nThe tuple has been deleted.")