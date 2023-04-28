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

########################################################################
def replace(guess, x, y):
    return guess[:x] + y + guess[x+1:]

def dfs(n, nx):
    checked = set()

    def helper(cc):
        if cc.empty() == True:
            return strcon_nil()
        else:
            n1 = cc.get()
            for n2 in reversed(nx(n1)):
                if (not n2 in checked):
                    cc.put(n2)
                    checked.add(n2)
                    return strcon_cons(n1, lambda: helper(cc))
    cnx = queue.LifoQueue()
    for n0 in n:
        cnx.put(n0)
        checked.add(n0)

def wordle_guess(hints):
    guess = "_" * len(hints[0])
    still_check_count = []
    still_check = set()
    dict = list("abcdefghijklmnopqrstuvwxyz")
    
    for hint in hints:
        for x,y in enumerate(hint):
            if y[0] == 1:
                guess = replace(guess, x, y[1])
            elif y[0] == 2:
                still_check.add((x, y[1]))
                still_check_count += y[1]
            else:
                if y[1] in dict:
                    dict.remove(y[1])
    def result_check(word):
        wordlist = list(word)
        def check1(i):
            return foreach_to_iforall(string_foreach)(i,lambda n,x: (not(n,x) in i))
        def check2(i):
            result = True
            for cc in still_check_count:
                if (cc in i):
                    i.remove(cc)
                else:
                    result = False
                    break
                return result
            return check1(word) and check2(wordlist) and (not '_' in word)
        def next(nxt1):
            try:
                i = nxt1.index('_')
                return string_imap_pylist(dict, lambda _,c: replace(nxt1, i, c))
            except ValueError:
                return []
    if '_' in guess:
        g1 = stream_make_filter(dfs([guess], next), lambda s: result_check(s))
        return stream_get_at(g1, 0)
    else:
        return guess
########################################################################
