while True:

    try:

        x=input('Enter a value: ')
        y=input('Enter a value: ')
        count=0

        while True:

            if int(x)==int(y):
                print(len(x),' digits matches from the rightmost digit.'
)
                break
    
            if int(x)==0 :
                if int(x)==(int(y)%10):
                    print(len(x),' digits matches from the rightmost digit.')
                    break
                else:
                    print(count,' digits matches from the rightmost digit.')
                    break

                if int(y)==0:
                    if int(y)==(int(x)%10):
                        print(len(y),' digits matches from the rightmost digit.')
                        break
                else:
                    print(count,' digits matches from the rightmost digit.')
                    break
    
            if (int(x)%10)==(int(y)%10):
                if (int(x)%10)==int(x):
                    if int(x)==(int(y)%10):
                        print(len(x),' digits matches from the rightmost digit.')
                        break
                    else:
                        print(count,' digits matches from the rightmost digit.')
                        break
                elif (int(y)%10)==int(y):
                    if int(y)==(int(x)%10):
                        print(len(y),' digits matches from the rightmost digit.')
                        break
                    else:
                        print(count,' digits matches from the rightmost digit.')
                        break


            while True:

                if (int(x)%10)==(int(y)%10):
                    count += 1
                    x=(int(x)/10)
                    y=(int(y)/10)
                    continue
                else :
                    print(count,' digits matches from the rightmost digit.')
                    break

            break

    except:
        print('Enter Only Numbers!\n')
        continue

    break

    
   
