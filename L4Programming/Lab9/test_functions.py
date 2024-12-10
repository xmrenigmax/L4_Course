import pytest
from functions import *

pytest.main()
' Exercise 1'
def test_add():
    assert add_two_numbers(1, 2) == 3
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(0, 1) == 1
    assert add_two_numbers(-1, -1) == -2
    assert add_two_numbers(0, -1) == -1

def test_product():
    assert product_two_numbers(3, 4) == 12
    assert product_two_numbers(-9,-4) == 36
    assert product_two_numbers(6, -3) == -18
    assert product_two_numbers(-4, 0) == 0
    assert product_two_numbers(0, 4) == 0

def test_sort():
    assert sorted_alphabetically("programming") == ["a", "g", "g", "i", "m", "m", "n", "o", "p", "r", "r"]
    assert sorted_alphabetically("civic") == ["c", "c", "i", "i", "v"]
    assert sorted_alphabetically("aabb") == ["a", "a", "b", "b"]
    assert sorted_alphabetically("PaBaBB") == ["a","a","B","B","B","P"]
    assert sorted_alphabetically("BaAaA") == ["A","A","a","a","B"]

def test_mode():
    assert commons_of_lists([1, 2, 3, 4], [3, 4, 19 ,21, 5]) == [3, 4]
    assert commons_of_lists([3, 3, 3], [4, 4, 4]) == []
    assert commons_of_lists([3, 4, 5], [3, 4, 5]) == [3, 4, 5]
    assert commons_of_lists([11, 10, 9, 23], [23, 11, 15]) == [11, 23]
    assert commons_of_lists([-11, 11, -9, 10, 8], [10, -3, 0, 14, 8, -9]) == [8, 10, -9]

def test_palindrome():
    assert palindrome("civic") == True
    assert palindrome("anna") == True
    assert palindrome("rotator") == True
    assert palindrome("week") == False
    assert palindrome("cciivv") == False

def movie_prices():
    assert movie_ticket_price(0,1,0,10) == 14.25
    assert movie_ticket_price(2,2,0,13) == 30
    assert movie_ticket_price(2,2,0,13) == 28.5
    assert movie_ticket_price(2,1,1,13) == 30.4
    assert 53.91 < movie_ticket_price(4,3,2,11) < 54.00
    assert movie_ticket_price(-2,-5,2,13) == None

def divisible_by():
    assert divisible_by_2_3_5(10) == [0,30,60,90,120,150,180,210,240,270]
    assert divisible_by_2_3_5(5) == [0,30,60,90,120]
    assert divisible_by_2_3_5(0) == []

' Exercise 2'
def test_fix_code():
    assert fix_code(2022) == "That's the past!"
    assert fix_code(2024) == "That's the present!"
    assert fix_code(2025) == "That's the future!"
    assert fix_code(2023) == "That's the past!"
    assert fix_code(2026) == "That's the future!"

def total_sum_fix():
    assert total_sum([1, 2, 3, 4]) == 10

def count_n_test():
    assert count_n(5) == [1, 2, 3, 4, 5] 

def sort_list_test():
    assert sort_list([3, 2, 1]) == [1, 2, 3]

def power_test():
    assert power(2, 3) == 8

def even_number():
    assert even_in_list([1, 2, 3, 4, 5]) == [2, 4]