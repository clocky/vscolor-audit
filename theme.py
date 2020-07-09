from collections import Counter
from tabulate import tabulate
from colour import Color
from colored import fg, bg, attr
from operator import itemgetter

# Read all the ARGB values from a text file
with open('colors.txt') as file:
    palette = file.read().splitlines()

# Count the frequency of the most common colours in the file
counter = Counter(palette).most_common()

# Create a table of data appending hex, hue and luminance values
table = []
for argb, count in counter:
    # Create color object from the RGB values in ARGB
    color = Color('#' + argb[3:10])
    table.append((count, bg(color.hex_l) + "        " +
                  attr('reset'), argb, color.hex_l, color.hue, color.luminance))

# Sort the table by hue, then luminance
by_hue = sorted(table, key=itemgetter(4, 5))

# Render it all nicely to the console
print(tabulate(by_hue, headers=[
      "Count", "Sample", "ARGB", "RGB", "Hue", "Luminance"]))
