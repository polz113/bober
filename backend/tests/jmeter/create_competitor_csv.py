#!/usr/bin/env python
import csv

if __name__ == '__main__':
    names = []
    surnames = []
    with open('roman_gods.txt') as f:
        names = [i.strip() for i in f.readlines() ]
    with open('slavic_gods.txt') as f:
        midnames = [i.strip() + 'ic' for i in f.readlines()]
    with open('greek_gods.txt') as f:
        surnames = [i.strip() for i in f.readlines()]
    with open('data.csv', 'wb') as f:
        w = csv.writer(f)
        for surname in surnames:
            for midname in midnames:
                for name in names:
                    w.writerow([name, midname +" "+ surname])
