import math
from random import randint

def count_digits(number):
	x = 1
	digits = 0
	for i in range(17):
		if (number / x) >= 1:
			x *= 10
			digits += 1
		else:
			return digits

def sum_credit_number(credit_number):
	digits = count_digits(credit_number)
	credit_card = []
	for i in range(16):
		current_number = 0
		power = 0
		power = (16 - len(credit_card)) - 1
		current_number = credit_number / 10 ** power

		credit_card.append(current_number)

	separated_credit_card = []
	for i in range(16):
		new_number = credit_card[i] % 10

		if (i + 1) % 2 == 1:
			new_number *= 2

		separated_credit_card.append(new_number)

	final_sum_numbers = []
	for i in separated_credit_card:
		x = (i / 10) + (i % 10)
		if count_digits(i) > 1:
			final_sum_numbers.append(x)
		else:
			final_sum_numbers.append(i)

	sum_num = sum(final_sum_numbers)
	return sum_num

def check_valid_number(credit_number):
	sum_num = sum_credit_number(credit_number)
	if sum_num % 10 == 0:
		return True
	else:
		return False

def sum(numbers):
	total = 0
	for i in numbers:
		total += i

	return total

def generate_card_number(num):
	while check_valid_number(num) == False:
		num = randint(1000000000000000, 9999999999999999)

	return num

def generate_card_number_better(rand_15_digit_number):
	num = rand_15_digit_number * 10
	added_nums = sum_credit_number(num)
	last_digit_pre = added_nums % 10
	last_digit = 10 - last_digit_pre
	valid_num = num + last_digit
	return valid_num

def sum_digits(number):
	n = 0
	while n:
		n += number % 10
		number //= 10
	return n


print sum_digits(126)
print check_valid_number(9444386154094054)
print generate_card_number(randint(1000000000000000, 9999999999999999))
print generate_card_number_better(randint(100000000000000, 999999999999999))