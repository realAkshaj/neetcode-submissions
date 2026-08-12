class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = "".join(char.lower() for char in s if char.isalnum())
        print(st)
        n = len(st)
        i = 0
        j = len(st) - 1
        
        while i < j:

            if st[i] == st[j]:

                i += 1
                j -= 1
            
            else:
                return False
        
        return True