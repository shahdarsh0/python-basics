color='blue'
user_input=' '
attempt=0
while user_input!=color:
    user_input=input('Enter the color')
    attempt+=1
if attempt<2:
    print('Total attempt made',attempt)
else:
    print('Total attempts made',attempt)
