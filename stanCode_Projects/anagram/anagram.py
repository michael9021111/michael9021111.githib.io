"""
File: anagram.py
Name: 林志叡
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
SHORT_DIC = []
DIC = []


def main():
    """
    The program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant
    """
    # ####################
    read_dictionary()
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    s = input('Find anagrams for: ')
    while True:
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            s = input('Find anagrams for: ')
    # ####################


def read_dictionary():
    # establish dic list as global variable
    with open('dictionary.txt', 'r') as f:
        for line in f:
            line = line.strip()
            DIC.append(line)


def find_anagrams(s):
    """
    :param s: input word
    :return: answer list
    """
    # pick out words with same length in DIC
    # fist alphabet in each word must match least one alphabet in target string
    for i in DIC:
        if len(s) == len(i) and i[0] in s:
            SHORT_DIC.append(i)
    ans = find_anagrams_helper(s, '', [], SHORT_DIC, [])
    print(str(len(ans))+" anagrams: ", end='')
    print(ans)


def find_anagrams_helper(s, changing_s, ans_lst, short_dic, index):
    if len(changing_s) == len(s) and changing_s in short_dic:
        # make sure every anagram in the ans_lst is unique
        if changing_s not in ans_lst:
            ans_lst.append(changing_s)
            print("Searching.........")
            print("Found: " + changing_s)
    else:
        if len(changing_s) < len(s):
            for i in range(len(s)):
                if i not in index:
                    # choose
                    changing_s += s[i]
                    index.append(i)
                    # explore
                    if has_prefix(changing_s):
                        find_anagrams_helper(s, changing_s, ans_lst, short_dic, index)
                    # un-choose both index and changing_s
                    changing_s = changing_s[:len(changing_s) - 1]
                    index.remove(i)

    return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s: the sub-string of the anagram word
    :return: if sub_s in target list , return True
    """
    for word in SHORT_DIC:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
