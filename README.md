# uncensor
A simple solution for the following Edabit challenge:#

Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s.

Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

## Example
<pre>
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
</pre>

<hr>
The solution has time complexity and space complexity O(n+m) where n and m are the lengths of the two strings.
