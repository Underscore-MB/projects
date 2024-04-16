#IMPORT
import time
import random
#SPEL
print('blackjack zonder aas')
print('--------------------------------------------------------------------------------------------------------------------------------------')
time.sleep(1)

#geef een random kaart en vertel de kaart aan de speler
Spelerkaart1 = random.randint(2,10)
print('je eerste kaart heeft een waarde van', Spelerkaart1, '.')
time.sleep(2)
Spelerkaart2 = random.randint(2,10)
print('je tweede kaart heeft een waarde van', Spelerkaart2, '.')
time.sleep(2)

#bereken en vertel het totaal
totaal = Spelerkaart1 + Spelerkaart2
print('je totaal is', totaal, '.')
time.sleep(2)

#zeg of je verloren hebt of blackjack hebt
if totaal == 21:
    print('Blackjack! (gewonnen)')
    exit()
elif totaal > 21:
    print('je hebt verloren, dealer had', '!dealer had nog geen kaarten!' ,'jij had',totaal,'.')
    exit()

#Bepaal dealers kaarten
else:
    Dealerkaart1 = random.randint(2,10)
    print('De dealers eerste kaart heeft een waarde van', Dealerkaart1, '.')
    time.sleep(2)
    Dealerkaart2 = random.randint(2,10)
    print('de tweede kaart mag je niet zien.')
    time.sleep(2)
    dealertotaal = Dealerkaart1 + Dealerkaart2
    if dealertotaal == 21:
        print('Dealer heeft Blackjack, dealer wint')
        exit()
    if dealertotaal < 17:
        Dealerkaart3 = random.randint(2,10)
        print('De dealers derde kaart heeft een waarde van', Dealerkaart3, '.')
        dealertotaal += Dealerkaart3

if dealertotaal > 21:
    print('de dealer heeft te hoog getrokken, je wint. dealer had', dealertotaal)
    exit()

if dealertotaal < 17:
    Dealerkaart4 = random.randint(2,10)
    print('De dealers vierde kaart heeft een waarde van', Dealerkaart4, '.')
    dealertotaal += Dealerkaart4
if dealertotaal == 21:
    print('Dealer heeft Blackjack, dealer wint')
    exit()

if dealertotaal > 21:
    print('de dealer heeft te hoog getrokken, je wint. dealer had', dealertotaal)
    exit()

print('--------------------------------------------------------------------------------------------------------------------------------------')
#de code voor hit of stand nummer 3
time.sleep(2)
print('Typ hit om nog een kaart te nemen, typ stand om te stoppen.')
h1 = str(input())
if h1 == 'hit':
    Spelerkaart3 = random.randint(2,10)
    print('je derde kaart heeft een waarde van', Spelerkaart3, '.')
    time.sleep(2)
    totaal += Spelerkaart3
    if totaal > 21:
        print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
        exit()
if h1 == 'stand':
    if totaal > dealertotaal and totaal < 21:
        print('je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
    else:
        print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
        exit()
print('je totaal is', totaal, '.')

#zeg of je verloren hebt of blackjack hebt
if totaal == 21:
    print('Blackjack! je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
    exit()
elif totaal > 21:
    print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
    exit()
print('--------------------------------------------------------------------------------------------------------------------------------------')

#de code voor hit of stand nummer 4
time.sleep(2)
print('Typ hit om nog een kaart te nemen, typ stand om te stoppen.')
h1 = str(input())
if h1 == 'hit':
    Spelerkaart4 = random.randint(2,10)
    print('je vierde kaart heeft een waarde van', Spelerkaart4, '.')
    time.wait(2)
    totaal += Spelerkaart4
    print('je totaal is', totaal, '.')
    if totaal > 21:
        print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
        exit()
if h1 =='stand':
    if totaal > dealertotaal and totaal < 21:
        print('je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
        exit()
    else:
        print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
        exit()
    
#zeg of je verloren hebt of blackjack hebt
if totaal == 21:
    print('Blackjack! je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
    exit()
elif totaal > 21:
    print('je totaal is',totaal,'je hebt verloren.')
    exit()

print('--------------------------------------------------------------------------------------------------------------------------------------')

#de code voor hit of stand nummer 5
time.sleep(2)
print('Typ hit om nog een kaart te nemen, typ stand om te stoppen.')
h1 = str(input())
if h1 == 'hit':
    Spelerkaart5 = random.randint(2,10)
    print('je vierde kaart heeft een waarde van', Spelerkaart5, '.')
    totaal += Spelerkaart5
    print('je totaal is', totaal, '.')

if h1 == 'stand':
    if totaal > dealertotaal and totaal < 21:
        print('je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
        exit()
    else:
        print('je hebt verloren, dealer had', dealertotaal,'jij hebt',totaal)
        exit()
#zeg of je verloren hebt of blackjack hebt
if totaal == 21:
    print('Blackjack! je hebt gewonnen met een totaal van', totaal, 'de dealer had een totaal van', dealertotaal, '.')
    exit()
elif totaal > 21:
    print('je totaal is',totaal,'je hebt verloren.')
    exit()
