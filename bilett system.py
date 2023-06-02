from datetime import datetime, time

current_time = datetime.now().time()
rush_hour_time = (
    (time(14, 00), time(16, 59)),
    (time(0, 30), time(8, 59))
)

pricelist = {
    "1": {"name": "Barnebillett", "rush_hour_price": 20, "non_rush_hour_price": 20},
    "2": {"name": "Voksenbillett", "rush_hour_price": 39, "non_rush_hour_price": 25},
    "3": {"name": "Ung Voksenbillett", "rush_hour_price": 39, "non_rush_hour_price": 25},
    "4": {"name": "Honnør(67+)", "rush_hour_price": 20, "non_rush_hour_price": 20},
    "5": {"name": "Militære", "rush_hour_price": 20, "non_rush_hour_price": 20},
}

print("Alternativer:\n 1. Barnebilett (20kr-20kr)\n 2. Voksenbilett (25kr-39kr)\n 3. Ung voksenbilett (25kr-39kr)\n 4. Honnør (20kr-20kr)\n 5. Militære (20kr-20kr)")

ticket = input("Hvilken billett ønsker du å kjøpe? ")

if ticket not in pricelist:
    print("Ugyldig billettvalg.")
else:
    is_rush_hour = any(start <= current_time <= end for start, end in rush_hour_time)
    selected_ticket = pricelist[ticket]

    if is_rush_hour:
        price = selected_ticket["rush_hour_price"]
    else:
        price = selected_ticket["non_rush_hour_price"]

    hund_sykkel = input("Har du hund eller sykkel? '1' for nei og '2' for ja: ")

    if hund_sykkel == "1":
        hund_sykkel_price = 0
    elif hund_sykkel == "2":
        hund_sykkel_price = 20
    else:
        print("Ugyldig valg for hund eller sykkel.")
        exit()

    total_price = price + hund_sykkel_price
    print("Det vil koste deg", total_price, "kr.")
