# gallons to cups

# 1 gallon = 4 quarts
# 1 quart = 2 pints
# 1 pint = 2 cups

def convert_gallons_to_cups(gallons):
    def gallons_tp_quarts(gallons):
        print(f"Converting {gallons} to quarts")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"COnverting {quarts} to pints")
        return quarts * 2

    def pints_to_cups(pints):
        print(f"COnverting {pints} to cups")
        return pints * 2

    quarts = gallons_tp_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)

    return cups

print(convert_gallons_to_cups(3))