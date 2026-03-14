##Longest Substring Without Repeating Characters
##Sliding Window

class LongestLength:
    def findLengthofsubstring(s):
        left_corner = 0
        max_length  = 0
        seen = set()
        for right_corner in range(len(s)):
            while s[right_corner] in seen:
                seen.remove(s[left_corner])
                left_corner += 1

            seen.add(s[right_corner])
            max_length = max(max_length,(right_corner-left_corner)+1)

        return max_length        




if __name__ == "__main__":
    s = "abcbcaaabcd"

    ll=LongestLength
    print(ll.findLengthofsubstring(s))






# Similar problems
# Longest Repeating Character Replacement
# Minimum Window Substring
# Permutation in String