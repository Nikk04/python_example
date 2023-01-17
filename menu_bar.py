print("Benvenuto, hai fame?")

bevande = ["acqua", "vino", "birra", "coca", "fanta"]
cibo=["hamburger", "pizza", "piadina", "aperitivo", "focaccia", "dolce"]
print("Il cibo disponibile è ", cibo)
mangiare = input("Cosa vuoi mangiare?")
print("Le bevande disponibili sono", bevande)

bere = input("Cosa vuoi bere?")
if bere not in bevande:
    print("non disponibile")
else:
    print("certo porto subito")
if mangiare not in cibo:
    print("non disponibile")
else:
    print("certo porto subito")
altro = input("altro?")
if altro not in bevande and cibo:
    print("ciao")
else:
    print("certo, paga con bamcomat?")