class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resStr = ''

        '''
        Initial idea is to check every possible substring to see if it is a palindrome
        if it is a palindrome and its length is > resLen, update resLen and resStr

        Every possible substring is O(n^2) operation, not very time efficient
        the part to check palindrome, can be done in O(n) time using pointers

        In total this idea would be O(n^3) time, I think we can do better than this

        The creating every substring part is very inefficient,
        I think a better could be to still iterate over each letter, but
        instead of creating a substring each time, from that letter we treat it
        as the center of the palindrome

        ababd
        for example on our first iteration, this a is the center, we check its left and right
        to see if it is a palindrome, we will go until either the left or the right hit 0 or len(s) - 1
        respectively

        now that I think about it, there's an edge case to this approach, that is for even length
        palindromes, in this case, the only idea that comes to mind right now is
        that for each letter we check for the case of odd and even length palindromes,

        and since we are treating the current letter(s) as the center of our palindrome,
        we will expand outwards so for example:
        ababd

        this approach still loops over the string but doesn't get every possible substring
        so that is O(n), the part to check whether it is a palindrome is O(n)
        2n since we check for even and odd case which is still n

        Total time is O(n^2)
        Space: O(n)
        '''

        for i in range(len(s)):
            left = i
            right = i

            # odd palindrome case
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    resStr = s[left:right + 1]
                left -= 1
                right += 1
            
            # even palindrome case
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    resStr = s[left:right + 1]
                left -= 1
                right += 1
            
        return resStr
        '''
        ababd
        01234
        
        l = 0, r = 0
        len = 1, str = 'a'
        l = -1, r = 1

        l = 1, r = 1
        l = 0, r = 2
        len = 3, str = 'aba'
        l = -1, r = 3

        l = 2, r = 2
        l = 1, r = 3
        l = 0, r = 4
        l = -1, r = 5

        l = 3, r = 3
        l = 2, r = 4

        l = 4, r = 4
        l = 3, r = 5

        return 'aba'
        '''