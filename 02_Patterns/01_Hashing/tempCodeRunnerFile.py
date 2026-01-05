#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:47:33 2026

@author: Rishabh_Tyagi

codebasics YT
Hash Table - Data Structures & Algorithms Tutorials In Python #5
https://www.youtube.com/watch?v=ea8BRGxGmlA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5

"""

"""
Write a program that can give price based on a day from the csv
99_data/stock_prices.csv
"""

# Using Array/List
stock_prices = []
with open('99_data/stock_prices.csv', 'r') as f:
    for line in f:
        day, price = line.split(',')
        stock_prices.append((day, float(price)))

print(stock_prices)