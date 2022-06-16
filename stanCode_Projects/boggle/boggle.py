"""
File: boggle.py
Name: 林志叡
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	DIC = read_dictionary()
	lst = input_check()
	# test case: lst = ['f', 'y', 'c', 'l', 'i', 'o', 'm', 'g', 'o', 'r', 'i', 'l', 'h', 'j', 'h', 'u']
	if lst != 0:
		# if return 0 then print illegal input
		number = find_words_in_dic(DIC, lst, '', [], [])
		print('There are ' + str(number) + ' words in total.')
	else:
		print('Illegal input')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words_in_dic(dic, lst, changing_s, ans_lst, index):
	if len(changing_s) >= 4 and changing_s in dic:
		#  base case: make sure words over 4 alphabet in the dic
		if changing_s not in ans_lst:
			#  make sure every answer is unique
			ans_lst.append(changing_s)
			print("Found: " + str(changing_s))
			dic.remove(changing_s)
			# remove the answer from dic and check if there's same substring in the dic
			if has_prefix(changing_s):
				find_words_in_dic(dic, lst, changing_s, ans_lst, index)
	else:
		for i in range(16):
			# check if the choosing alphabet is near the last-selected alphabet
			if i not in index and len(index) > 0 and (i+1) in check_around(index[-1]+1):
				changing_s += lst[i]
				index.append(i)
				if has_prefix(changing_s):
					find_words_in_dic(dic, lst, changing_s, ans_lst, index)
					# un-choose both index and changing_s
				changing_s = changing_s[:len(changing_s) - 1]
				index.remove(i)
			elif i not in index and len(index) == 0:
				# if there's no alphabet in changing_s, then it's an initial situation
				changing_s += lst[i]
				index.append(i)
				if has_prefix(changing_s):
					find_words_in_dic(dic, lst, changing_s, ans_lst, index)
					# un-choose both index and changing_s
				changing_s = changing_s[:len(changing_s) - 1]
				index.remove(i)
	return len(ans_lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	DIC = []
	with open('dictionary.txt', 'r') as f:
		for line in f:
			line = line.strip()
			DIC.append(line)
	return DIC


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	DIC = read_dictionary()
	for word in DIC:
		if word.startswith(sub_s):
			return True


def input_check():
	lst = []
	count = 1
	b = input(str(count) + ' row of letters: ')
	# the number of alphabets in a row need to equal to 4
	# input must be 4 alphabet
	# every input must can be split by /n
	while True:
		b_split = b.split()
		if len(b_split) != 4:
			return 0
		for i in b_split:
			if not i.isalpha():
				return 0
			if not len(i) == 1:
				return 0
			lst.append(i)
		# if can satisfies every rules, then add alphabet in a list
		if count == 4:
			return lst
		count += 1
		b = input(str(count) + ' row of letters: ')


def check_around(i):
	"""
	:param i: position of last-selected alphabet
	:return: available position in input
	set the position of the alphabet from 1~16 and arrange like an array below
	1 2 3 4
	5 6 7 8
	9 10 11 12
	13 14 15 16
	"""
	if i == 1:
		return [2, 5, 6]
	elif i == 4:
		return [3, 7, 8]
	elif i == 13:
		return [9, 10, 14]
	elif i == 16:
		return [11, 12, 15]
	elif i in [5, 9]:
		return [i-4, i+4, i-3, i+5, i+1]
	elif i in [8, 12]:
		return [i-4, i+4, i-5, i+3, i-1]
	elif i in [2, 3]:
		return [i-1, i+1, i+3, i+4, i+5]
	elif i in [14, 15]:
		return [i-1, i+1, i-3, i-4, i-5]
	elif i in [6, 7, 10, 11]:
		return [i+1, i-1, i+3, i-3, i+4, i-4, i+5, i-5]


if __name__ == '__main__':
	main()


"""
lst= [f, y, c, l, i, o, m, g, o, r, i, l, h, j, h, u]

"""