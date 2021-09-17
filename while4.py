welkedag = input("geef hier de dag van de week op? \n").lower
maandag ="maandag"
dinsdag ="maandag dinsdag"
woensdag ="maandag dinsdag woensdag"
donderdag ='maandag dinsdag woensdag donderdag'
vrijdag ='maandag dinsdag woensdag donderdag vrijdag'
zaterdag ='maandag dinsdag woensdag donderdag vrijdag zaterdag'
zondag ='maandag dinsdag woensdag donderdag vrijdag zaterdag zondag'

while welkedag == "maandag":
    print(maandag)
    break
while welkedag =='dinsdag':
    print(dinsdag)
    break
while welkedag =='woensdag':
    print(woensdag)
    break
while welkedag =='donderdag':
    print(donderdag)
    break
while welkedag =='vrijdag':
    print(vrijdag)
    break
while welkedag =='zaterdag':
    print(zaterdag)
    break
while welkedag =='zondag':
    print(zondag)
    break