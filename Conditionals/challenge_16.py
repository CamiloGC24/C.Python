import uuid
def print_shipping_prices():
    print('\n Current shipping prices are as follows: ')
    print('\Shipping orders 0 to 100: \t\t $5.10 each')
    print('\nShipping orders 100 to 500: \t\t $5.00 each')
    print('\nShipping orders 500 to 1000: \t\t $4.95 each')
    print('\nShipping orders over 1000: \t\t $4.80 each')



def print_quotation(items:int):
    if items > 0 and items <= 100:
        print(f'\n To ship {items} items will cost you ${round(5.10 * items,2)}, at $5.10 per item.')
    elif items > 100 and items <=500:
        print(f'\n To ship {items} items will cost you ${round(5.00 * items,2)}, at $5.00 per item.')
    elif items > 500 and items <= 1000:
        print(f'\n To ship {items} items will cost you ${round(4.95 * items,2)}, at $4.95 per item.')
    elif items > 1000: 
        print(f'\n To ship {items} items will cost you ${round(4.80 * items,2)}, at $4.80 per item.')


print(f'\n Welcome to the Shipping account program.')

user_list = ['Camilo', 'footea', 'davisv', 'papinukt', 'allenj']

name=input('\n Hello, what is your username: ').title().strip()

if name in user_list:
    print(f'\n Hello {name} Welcome back to your account.')
    print_shipping_prices()
    items_to_be_shipped = int(input('\n How many items do you want to ship : '))
    print_quotation(items_to_be_shipped)
    place_order = input('\nWould you like to place the order ? [Y/N} ').lower()
    if place_order == 'y':
        print(f'\n Okay. Shipping your {items_to_be_shipped}  items.')
    elif place_order == 'n':
        print(f'\n Okay, no order is being placed at this time.')
    else:
        print('\n Invalid Input.')

else:
    print('\n Sorry, you do not have an account with us. Goodbye.')  