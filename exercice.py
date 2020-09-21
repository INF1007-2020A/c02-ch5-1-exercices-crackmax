#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	TAX_RATE = 0.15
# Calculer le sous total
	sum = 0
	for item in data:
		sum += item[INDEX_QUANTITY] * item[INDEX_PRICE]
# Calculer les taxes et total
	taxes = TAX_RATE * sum
	total = sum + taxes
# Retourner la facture formater (sous-total, taxes, total)

	bill_data = [
		("SOUS TOTAL", sum),
		("TAXES     ", taxes),
		("TOTAL     ",total)
	]
	result = name
	for d in bill_data:
		result += "\n" + f"{d[0]} {d[1] : >10.2f} $"

	#result += "\n" + f"SOUS-TOTAL {sum : >10.2f} $"
	#result += "\n" + f"TAXES      {taxes : >10.2f} $"
	#result += "\n" + f"TOTAL      {total : >10.2f} $"
	return result


def format_number(number, num_decimal_digits):
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))

	#Approche plus automagique : f"{decimal_part :.{num_decimal_digits}f}"[1:]
	decimal_str ="." + str(int(round( decimal_part * 10**num_decimal_digits)))
	whole_part_str=""
	while whole_part >= 100:
		three_digits = whole_part % 1000
		digits_str = f" {three_digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part//= 1000
	whole_part_str = str(whole_part) + whole_part_str


	return ("-" if number < 0 else "") + whole_part_str + decimal_str

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	triangle_width = 1 + 2 * (num_rows - 1)

	border_row = BORDER_CHAR * (triangle_width + 2)

	result = border_row

	for i in range(num_rows):
		num_triangle_char = i * 2 + 1
		triangle_chars = TRIANGLE_CHAR * num_triangle_char
		triangle_line = f"{triangle_chars : ^{triangle_width}}"
		result += "\n" + BORDER_CHAR + triangle_line + BORDER_CHAR
	result += "\n" + border_row
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
