def try_me():
    x = int(input("how many minutes since the lecture started? (typr in a number)"))
    if x >= 40:
        print ('Alibot: We need a break!')
        return True
    else:
        print (f'Alibot: Bravo! only {40-x} till our break')
        return False 