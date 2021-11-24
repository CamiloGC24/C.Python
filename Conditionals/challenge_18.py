print('\n Welcome to voter registration app!')
name = input('\n Enter your name please : ')
age = int(input('\n Please enter your age: '))

parties = ['democrates', 'republicans', 'independents', 'green']

if age > 17:
    print(f'\n Congratulations! {name} You are old enough to vote.')

    print('\n Available parties :')
    for i in parties:
         print(f'\n {i}')

    user_choice = input('\n Pick a party to join : ').lower()
    if user_choice == 'democrates':    
        print(f'\n Congratulations {name} you\'ve joined the {user_choice} party, that is a major party of.')
    elif user_choice == 'republicans':    
        print(f'\n Congratulations {name} you\'ve joined the {user_choice} party, that is a major party of.')    
    elif user_choice == 'independents':    
        print(f'\n Congratulations {name} you\'ve joined the {user_choice} party, that is a individual part.')
    elif user_choice == 'green':    
        print(f'\n Congratulations {name} you\'ve joined the {user_choice} party, that is a minor party of.')    
    else:
        print(f'\n Such party doesn\'t exists!')    
else:
    print(f'\n Sorry! {name}, you are not old enough to vote')        