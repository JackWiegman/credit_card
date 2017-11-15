import math

def count_digits(number):
	x = 1
	digits = 0
	for i in range(17):
		if (number / x) >= 1:
			x *= 10
			digits += 1
		else:
			return digits

def check_valid_number(credit_number):
	digits = count_digits(credit_number)
	credit_card = []
	for i in range(16):
		current_number = 0
		power = 0
		power = (16 - len(credit_card)) - 1
		current_number = credit_number / 10 ** power

		credit_card.append(current_number)

		digits -= 1

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

	if sum_num % 10 == 0:
		return True
	else:
		return False


def sum(numbers):
	total = 0
	for i in numbers:
		total += i

	return total



print check_valid_number(4024007199143941)
