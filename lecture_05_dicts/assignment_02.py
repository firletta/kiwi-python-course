eur_amount = float(input("Enter an amount in EUR: "))

convertor = {
	"GBP": 0.84 * eur_amount,
	"CZK": 24.57 * eur_amount,
    "USD": 1.02 * eur_amount,
}

print(convertor)

