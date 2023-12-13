# 10. Write a program for the word break problem using dynamic programming.

# The word break problem involves determining whether a given string can be segmented 
# into space-separated words from a given dictionary.

# In this implementation, the word_break function uses dynamic programming to build a boolean table dp, 
# where dp[i] represents whether the substring s[0:i] can be segmented into words from the dictionary. 
# It iterates through the input string and checks if any substring can be formed by combining valid substrings 
# from earlier positions.

# The example usage demonstrates checking whether the input string "leetcode" can be segmented 
# into words "leet" and "code" from the given dictionary. You can replace input_string and word_dictionary with your own values.

def word_break(s, word_dict):
    """
    Solve the Word Break problem using dynamic programming.

    Parameters:
    - s: The input string.
    - word_dict: A set of words in the dictionary.

    Returns:
    - True if the input string can be segmented into words from the dictionary, False otherwise.
    """
    n = len(s)

    # Create a table to store the results of subproblems
    dp = [False] * (n + 1)
    dp[0] = True  # An empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            # Check if the substring s[j:i] is in the word dictionary and if dp[j] is True
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Example usage:
input_string = "leetcode"
word_dictionary = {"leet", "code"}

result = word_break(input_string, word_dictionary)

if result:
    print("The input string can be segmented.")
else:
    print("The input string cannot be segmented.")
