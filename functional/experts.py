"""
Contains functions related to Expert selection
and validation
"""

# pylint: disable=unnecessary-lambda-assignment

EXPERTS = ('Radford', 'Matt', 'Alireza',)
COMPANIES = ('com1', 'com2',)
DISCIPLINES = ('Engineer',)
POSITIONS = ('SMTS', 'Fellow', 'Senior',)
MATH_OF_INTERESTS = ('Prime', 'Factorial', 'Fibonacci',)

are_experts = lambda person: person in EXPERTS
are_companies = lambda company: company in COMPANIES
are_disciplines = lambda discipline: discipline in DISCIPLINES
are_positions = lambda position: position in POSITIONS
are_math_of_interest = lambda math_of_interest: math_of_interest in MATH_OF_INTERESTS

are_panel = (lambda name, company, discipline, position, math_of_interest:
             are_experts(name) and are_companies(company) and
             are_disciplines(discipline) and are_positions(position) and
             are_math_of_interest(math_of_interest))
