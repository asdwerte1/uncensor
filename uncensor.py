""" 
Someone has attempted to censor my strings by replacing 
every vowel with a *, l*k* th*s. Luckily, 
I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, 
return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
"""

def uncensor(txt, vowels):
    txt_list = list(txt)
    vowels_list = list(vowels)

    for char in range(len(txt) - 1, -1, -1):
        if txt[char] == "*":
            txt_list[char] = vowels_list.pop()
    return "".join(txt_list)
    
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))