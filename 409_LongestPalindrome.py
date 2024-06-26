"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        turn_into_list = list(s)
        different_letters_present = []

        for i in range(len(turn_into_list)):
            get_letter = turn_into_list[i]
            if get_letter not in different_letters_present:
                different_letters_present.append(get_letter)

        empty_dict = {}

        for j in range(len(different_letters_present)):
            get_actual_letter = different_letters_present[j]
            times_the_letter_appered = 0
            for k in range(len(turn_into_list)):
                get_another_letter_to_compare = turn_into_list[k]
                if get_actual_letter == get_another_letter_to_compare:
                    times_the_letter_appered += 1
                    empty_dict[get_actual_letter] = times_the_letter_appered

        length_of_palindrome = 0
        odd_found = False

        for key in empty_dict:
            count = empty_dict[key]
            if count % 2 == 0:
                length_of_palindrome += count
            else:
                length_of_palindrome += count - 1
                odd_found = True

        if odd_found:
            length_of_palindrome += 1

        return length_of_palindrome