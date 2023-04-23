#!/usr/bin/python3

char2abjad = {'ا': 1, 'ب': 2, 'ج': 3, 'د': 4,
              'ه': 5, 'و': 6, 'ز': 7, 'ح': 8,
              'ط': 9, 'ی': 10, 'ک': 20, 'ل': 30,
              'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
              'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400,
              'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}

# abjad2char = {v: k for k, v in char2abjad.items()}

abjad2char = {1: 'ا', 2: 'ب', 3: 'ج', 4: 'د', 5: 'ه',
              6: 'و', 7: 'ز', 8: 'ح', 9: 'ط', 10: 'ی',
              20: 'ک', 30: 'ل', 40: 'م', 50: 'ن', 60: 'س',
              70: 'ع', 80: 'ف', 90: 'ص', 100: 'ق', 200: 'ر',
              300: 'ش', 400: 'ت', 500: 'ث', 600: 'خ', 700: 'ذ',
              800: 'ض', 900: 'ظ', 1000: 'غ'}


def abjad_sum(input):
	"""
	calculates Jomal sum
	"""
	abjad_code = sum(list(char2abjad[item] for item in input))
	return abjad_code

def remove_a_char(name, char_index: int) -> str:
	return ''.join([name[:char_index], name[char_index + 1:]])


def encrypt(name: str) -> str:
	"""
	encrypt using Kashkul algorithm
	اگر خواستی اسم پنهانی را از کسی بشناسی، از او بخواه که حرف اول آن را بیندازد
	و جمع ابجدی بقیه حروف را نگه دارد، سپس حرف بعدی را بیندازد و جمع عددی بقیه حروف را نگه دارد
	و همین طور، سپس آنچه نگه داشته با هم جمع کند و حاصل جمع را پس از انداختن عدد اول، بر باقیمانده تقسیم کند
	و سپس خارج قسمت را از جمع اول کم نماید، باقیمانده عدد حرف اول است،
	باز هم خارج قسمت را از جمع کسر کند، باقیمانده عدد حرف دوم است. و همینطور.
	- کشکول #شیخ_بهایی
	"""

	# TODO: normalize name.
	
	sums_with_char_removed = list()
	for i, removed_char in enumerate(name):
		name_with_removed_char = remove_a_char(name, i)
		sums_with_char_removed.append(abjad_sum(name_with_removed_char))
	
	sum_of_sums = sum(sums_with_char_removed)