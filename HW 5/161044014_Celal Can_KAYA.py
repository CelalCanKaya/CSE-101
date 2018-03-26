def digit_multiplier(number):
        result=1 # you should initiliaze the final result
        if int(number)==0:
                result=0
        for x in str(number):
                if int(x) > 0:
                        z=int(x)
                        result=int(z)*int(result)
                        

	
        return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert digit_multiplier(123405) == 120
    assert digit_multiplier(999) == 729
    assert digit_multiplier(1000) == 1
    assert digit_multiplier(1111) == 1
