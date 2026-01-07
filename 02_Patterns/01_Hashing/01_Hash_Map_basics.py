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

"""
hashtable and hashmap are two terms used for that same datastrucutre and dictionary is the pyton implementation of this datastructure.

in hashtable/hashmap, we use a hash function to get a 

Lookup by key is O(1) in hashmap
Insertion/Deletion is O(1) in hashmap

"""

#####
# Using Array/List

stock_prices = []

with open('99_data/stock_prices.csv', 'r', encoding="utf-8-sig") as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_prices.append([day,price])

stock_prices # its a list of lists, each sub list has two elements, date and price

for element in stock_prices:
    if element[0] == '06-Mar': # get price on 06-Mar
        print(element[1])



#####
# Using Dictionary

stock_price_dict = {}

with open('99_data/stock_prices.csv', 'r', encoding="utf-8-sig") as fl:
    for line in fl:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_price_dict[day] = price

stock_price_dict # dict with day as key, price as value

stock_price_dict['06-Mar']
stock_price_dict['11-Mar']





