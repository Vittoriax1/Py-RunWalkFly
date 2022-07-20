# Created by Jennifer Souvannasing, SEC290, Chap 3 Exercise, 07/11/22 updated 07/18/22

# Intro banner
intro = '|      Walk, Drive or Fly Calculator      |'
text_len = len(intro)
print('{}'.format('=' * text_len))
print(intro)
print('{}'.format('=' * text_len))

# Getting user input
miles = float(input('How many miles are you traveling? '))

# Conditions
if miles < 3:
    transport_mode = 'walking'

elif miles < 300:
    transport_mode = 'driving'

else:
    transport_mode = 'flying'

# Display the result
print('Calculating..')

print('I suggest {} to your destination.'.format(transport_mode))

if transport_mode == 'driving':
    print('With the price of gas, you might want to \nreconsider your trip!')
else:
    print('Have a great trip.')
