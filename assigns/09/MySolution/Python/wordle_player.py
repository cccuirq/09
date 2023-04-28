########################
# HX-2023-04-15: 20 points
########################
"""
Given a history of wordle hints, this function returns a
word as the player's guess.
"""
import queue
import sys
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
import nltk
nltk.download('words')
from nltk.corpus import words
########################################################################
def dfs(n, nx):
    checked = set()
    stack = []
    results =[]
    
    for n1 in n:
        stack.append(n1)
        checked.add(n1)
    
    while stack:
        current = stack.pop()
        results.append(current)

        for next in reversed(nx(current)):
            if next not in checked:
                stack.append(next)
                checked.add(next)
    return results

def next(nxt1, still_check_count):
            results = []
            try:
                index = nxt1.index("_")
                for l in still_check_count:
                    results.append(nxt1[:index] + l + nxt1[index+1:])
                return results
            except ValueError:
                return []
            
def wordle_guess(hints):
    guess = "_" * len(hints[0])
    still_check_count = []
    still_check = set()
    dict = list("abcdefghijklmnopqrstuvwxyz")
    
    for hint in hints:
        for x,y in enumerate(hint):
            if y[0] == 1:
                guess = guess[:x] + y[1] + guess[x+1:]
            elif y[0] == 2:
                still_check.add((x, y[1]))
                still_check_count += y[1]
            else:
                if y[1] in dict:
                    dict.remove(y[1])
    def result_check(word, wrong, included):
        for i, l in enumerate(word):
            if (i,l) in wrong:
                return False
        for l in included:
            if l not in word:
                return False
        return "_" not in word and word in words.words()
    if "_" in guess:
        valid_guesses = dfs([guess], lambda x: next(x, still_check_count))
        for word in valid_guesses:
            if result_check(word, still_check, still_check_count):
                return word
    else:
        return guess
########################################################################
