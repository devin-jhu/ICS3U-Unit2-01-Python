#!/usr/bin/env python3

# Created by Devin Jhu
# Created on February 2022
# The area and perimeter calculator
# Currently calculating for 15mm radius circle

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15 mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 15**2))
    print("Perimeter is {} mm.".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()
