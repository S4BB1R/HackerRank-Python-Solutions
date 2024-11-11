"""
Problem: [String Validators]
Difficulty: [Easy]
Category: [String]
URL: [https://www.hackerrank.com/challenges/string-validators/problem]

Description:
[Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.]

"""

def stringValidators():
    def stringValidators():
        validateString = input()
    
        has_alnum = any(character.isalnum() for character in validateString)
        has_alpha = any(character.isalpha() for character in validateString)
        has_digit = any(character.isdigit() for character in validateString)
        has_lower = any(character.islower() for character in validateString)
        has_upper = any(character.isupper() for character in validateString)
    
        print(has_alnum)
        print(has_alpha)
        print(has_digit)
        print(has_lower)
        print(has_upper)

if __name__ == '__main__':
    # Sample test case
    stringValidators()
