# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 21:29:02 2025

@author: abarc(
"""

import decimal

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

k = int(input_file.readline())
a_list = input_file.readline().split()
p_list = input_file.readline().split()
n = int(input_file.readline())

def binets_formula(n):
    r5 = 5**0.5
    phi = (1 + r5) / 2
    psi = (1 - r5) / 2
    return round((phi**n - psi**n) / r5)

def binets_formula_for_large_n(n):
    r5 = decimal.Decimal('5').sqrt()
    phi = (1+r5) / 2
    psi = (1-r5) / 2
    return round((pow(phi, n) - pow(psi, n)) / r5)

def fibonnaci_forloop(n):
    if n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    for i in range(n-2):
        c = a
        a += b
        b = c
    return a

def fibonnaci_efficient_recursive(n, a=0, b=1):
    if n == 0:  return a
    return fibonnaci_efficient_recursive(n-1, a+b, a)

def fibonnaci_intuitive_recursive(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    return fibonnaci_intuitive_recursive(n-1) + fibonnaci_intuitive_recursive(n-2)

def lucas(p1, p2, c1, c2, n):
    if n == 0:
        return p2 - p1
    if n == 1:
        return p1
    if n == 2:
        return p2
    return c1 * lucas(p1, p2, c1, c2, n-1) + c2 * lucas(p1, p2, c1, c2, n-2)

def tribonacci(p1, p2, p3, c1, c2, c3, n):
    if n == 0:
        return p3 - p2 - p1
    if n == 1:
        return p1
    if n == 2:
        return p2
    if n == 3:
        return p3
    return (c1 * tribonacci(p1, p2, p3, c1, c2, c3, n-1) + 
            c2 * tribonacci(p1, p2, p3, c1, c2, c3, n-2) +
            c3 * tribonacci(p1, p2, p3, c1, c2, c2, n-3))

def general_recurrence(k, a_list, p_list, n):
    current_list = p_list
    for i in range(n-k):
        new_number = 0
        for j in range(k):
            new_number += int(a_list[j]) * int(current_list[j])
            
        current_list.append(new_number)
        del(current_list[0])
    
    output_file.write(str(current_list[-1]))
    
    
general_recurrence(k, a_list, p_list, n)

input_file.close()
output_file.close()
