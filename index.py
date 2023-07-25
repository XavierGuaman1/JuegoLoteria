lotery_ticket ={
    'animal':'lion',
    'winner_number':'6666'
}

boleto= input('ingresa tu boleto: ')


if boleto in lotery_ticket['animal']=='lion' and lotery_ticket['winner_number']== '6666':
    print('you winner')
elif boleto in lotery_ticket['animal']== 'lion' and not lotery_ticket['winner_number']== 6666:
    print('tienes otro chanse')
else:
    print('you lose')