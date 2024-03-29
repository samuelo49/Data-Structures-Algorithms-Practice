'''
Tax Calculator

You are given a list of tax brackets, each defined by a range of taxable income and a marginal tax rate. Your task is to write a function that takes in a taxable income and returns the amount of tax payable on that income based on the given tax brackets.

Write a function that takes the following parameters:

taxable_income: a float representing the amount of taxable income
brackets: a list of tuples, where each tuple contains three floats: the lower limit of the bracket (exclusive), the upper limit (inclusive), and the marginal tax rate for that bracket. The first tuple should represent the lowest bracket with a lower limit of 0 and an upper one greater than 0.

The function should return the total amount of tax payable on the taxable_income, calculated as the sum of the tax payable for each bracket.

[Optional]: How would you account for deductions? What about tax credits?

Further reading: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
 

EXAMPLE(S)
If the taxable income is $80,000 and the tax brackets are:
[(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]

The function should return 18500 because of the following calculation:

The first $10,000 is taxed at 10%, which is $1,000
The next $20,000 is taxed at 15%, which is $3,000
The next $30,000 is taxed at 25%, which is $7,500
The remaining $20,000 is taxed at 35%, which is $7,000
The total tax payable is $1,000 + $3,000 + $7,500 + $7,000 = $18,500
 

FUNCTION SIGNATURE
function calculate_tax(taxable_income, brackets) {
def calculate_tax(taxable_income: float, brackets: List[Tuple[float, float, float]]) -> float:
'''
from typing import List, Tuple

def calculate_tax(taxable_income: float, brackets: List[Tuple[float, float, float]]) -> float:
    tax = 0
    for bracket in brackets:
        lower, upper, rate = bracket
        if taxable_income <= lower:
            break
        elif taxable_income <= upper:
            tax += (taxable_income - lower) * rate
            break
        else:
            tax += (upper - lower) * rate
    return round(tax, 2)