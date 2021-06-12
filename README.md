# simplesite-testcases

Write a set of tests that will ensure that the combination of sorting and filtering works correctly.
However there's a catch: you need to write your tests in such a way that if I modify the data on the website (if I remove some rows or add new ones), your tests still correctly verify the functionality. For the sorting part, you can choose 2 fields that you will validate (instead of doing all 4). Here's additional information that can help you:
* capital letters are ignored by both filtering and sorting (it works as if all letters were small letters)
* sorting works only in one direction: from low to high, from A to Z, sorting by complexity sorts from low to high
* number of cases uses special formatting, thousands might be expressed as letter "k" (5000 = 5k), millions as M (1200000 = 1.2M), billions as "B" (1580000000 = 1.58B)In order to write the tests you can use any programming language and framework of your choice as long as it is possible to run your tests in UNIX-like environment. 
