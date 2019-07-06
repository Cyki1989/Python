'''
    W tym zadaniu liczymy pole koła
'''
WartoscPi = 3.14
PromienOkregu = 5
PoleKola = WartoscPi * PromienOkregu**2
print("Pole kola wynosi",PoleKola)
# a tu liczymy obwód
ObwodOkregu = 2 * WartoscPi * PromienOkregu
print("Obwód okręgu wynosi",ObwodOkregu)
# a tu liczymy pole prostokąta
DlugoscKrawedziA = 6
DlugoscKrawedziB = 3
PoleProstokata = DlugoscKrawedziA * DlugoscKrawedziB
print("Pole prostokąta wynosi",PoleProstokata)
# a teraz pole trapezu
Wysokosc = 4
PoleTrapezu = (DlugoscKrawedziA+DlugoscKrawedziB)*Wysokosc/2
print("Pole trapezu wynosi",PoleTrapezu)
