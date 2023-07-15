import random

N_CHANCES = 5
WORDS = ["aleksandra", "mortadela", "orzeszek", "salceson", "arystoteles"]

n_guess = 0
answer = random.choice(WORDS)

#TWORZENIE LISTY WYŚWIETLANEJ GRACZOWI
printed_answer = ["_" for _ in range(len(answer))] # Lista składana

print()
print(*printed_answer) # * przed listą powoduje wydrukowanie listy ze spacją jako separatorem

while n_guess < N_CHANCES:
	guess=input("Podaj literę: ").lower()

	#Sprawdzanie czy podano jeden znak
	if len(guess) != 1:
		print("Nie podano jednej litery\n")
		print(*printed_answer)
		continue

	#JEŻELI LITERA WYSTĘPUJE W ROZWIĄZANIU I NIE POWTARZA SIĘ
	if guess in answer and guess not in printed_answer:

		for i in range(len(answer)):
			if answer[i] == guess:
				printed_answer[i] = guess

		print()
		print(*printed_answer)

		if "_" not in printed_answer:
			print("\nWygrana")
			break
	else:
		n_guess += 1

		#JEŻELI PRZEKROCZONO LICZBĘ SZANS - KONIEC
		if n_guess == N_CHANCES:
			print("\nPrzegrana :(")
			break
		#JEŻELI LITERA JUŻ BYŁA WCZEŚNIEJ ZGADNIĘTA
		elif guess in answer:
			print(f"Powtórzono literę. Liczba szans: {N_CHANCES - n_guess}.")
		#JEŻELI PODANO ZŁĄ LITERĘ NIE BĘDĄCĄ W ROZWIĄZANIU
		else:
			print(f"Nie trafiono. Liczba szans: {N_CHANCES - n_guess}.")
		print()
		print(*printed_answer)