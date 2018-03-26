print('AREA CALCULATOR\n')        #Description of program

while True:         #I used while loop because if there is a runtime error i want to turn back to starting part

    try :           #If the input is not integer jump to the except part 

        import math     #Imported math module because i need to use pi value
        x = input('Enter a value: ')        #Take a input from user
        print('Area of Circle: ', float(math.pi)*(float(x)*float(x)))   #Calculate area of circle and print it
        print('Area of Equilateral Triangle: ', ((float(3)**float(1/2))/4)*(float(x)*float(x)))     #Calculate are of equilateral triangle and print it
        print('Area of Square: ', float(x)*float(x), '\n')      #Calculate area of square and print it
        break       #Everything is OK so we need to break while loop

    except :        #If the error occurs this part will print an error message
        print('Oops!There was an error.Please try again.')      #Print the error message    
        continue    #Something went wrong so we need to continue to loop     
    


#BONUS PART (ONLY SQUARE)

y=0     
print('Here is the', str(x),'*',str(x), 'square.\n')

while True:
    y += 1      #This is the variable for counting lines
    print('*' * int(x))     #Printing a line of shape

    if int(y) == int(x):        #If printed lines are equal to users input break the loop
        break       #The shape is OK, so break the loop
    else:   
        continue        #The shape isn't OK, 
