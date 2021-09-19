# name of student: Anthony van de leuv 
# number of student:
# purpose of program: change options
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # hoeveel je moet betalen 
payed = int(float(input('Payed amount: ')) * 100) # hoeveel hij heeft betaalt
change = payed - toPay # hier berekent hij het wisselgeld uit

if change > 0: # bij wisselgeld reageert hij pas op de if
  coinValue = 500 # dit bepaalt hoeveel de munt waard is maar hier hebben we het in centen 
  
  while change > 0 and coinValue > 0: # hij blijft loops maken totdat hij zegmaar geen wisselgeld meer heeft of die coins op zijn 
    nrCoins = change // coinValue # hoeveel coins hij kan gebruiken van een bepaalde munteenheid dat doet hij door te delen 

    if nrCoins > 0: # als de uitkomst hoger is dan null gaat hij antwoorden geven 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # dit loopt hij totdat hij nr coin niet meer kan runnen
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hier print hij netjes de uitkomsten
      change -= nrCoinsReturned * coinValue # hier wordt nogmaals het wisselgeld berekent mocht er een fout komen dan wordt hij naar beneden door verstuurd 

# comment on code below: 
    if coinValue ==500:
      coinValue = 300
    if coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100

    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als je geen coinvalue meer hebt dan is dit het andere einde
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')