'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1: # Not possible for "th" to exist
        return 0
    elif (word[0] == 't') and (word[1] == 'h'):  # Check if value of 0th index and 1st index equal "th"
        return 1 + count_th(word[1:]) # return 1 plus recursive call of list minus the first item
    else:
        return count_th(word[1:]) # return recursive call of list minus the first item
