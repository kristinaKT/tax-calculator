# after entering net price, program will calculate tax prices for different countries


def tax_calculator():
        
    vat_rates = {
    "Germany": 1.19,
    "Austria": 1.20,
    "Netherlands": 1.21,
    "Belgium": 1.21,
    "Finland": 1.24,
    "France": 1.20,
    "Greece": 1.23,
    "Croatia": 1.25,
    "Italy": 1.22,
    "Slovenia": 1.22,
    "Slovakia": 1.20,
    "Poland": 1.23,
    "Bulgaria": 1.20,
    "Czechia": 1.21,
    "Hungary": 1.27,
    "Romania": 1.19,
    "Sweden": 1.25
}
    print("________________________________")
    print("")
    net_price = input("Enter net price: " + "€")
    print("")

    for country, vat_rate in vat_rates.items():
        result = (vat_rate) * int(net_price)
        print("VAT price - " + country + ": " + str(round(result)) + " €")
()

for i in range(100):
    tax_calculator()