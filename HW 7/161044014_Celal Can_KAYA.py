def member():
    members = ['celal', 'emre', 'tuğba', 'aynur', 'kadir', 'sevgi', 'oktay', 'emine', 'hanife', 'necati']
    print("Members of the family: " + str(members) + "\nWrite the 2 members of this family for see their relationship.\n" )

def get_input_1():
    x=input("First:")

    return x

def get_input_2():
    y=input("Second Member:")

    return y


def relation():
    relations = {"celal emre" : "brother", "celal aynur": "son", "celal tuğba": "brother", "celal kadir": "son", "celal emine": "nephew", "celal sevgi": "nephew",
                 "celal oktay": "nephew", "celal necati": "grandson", "celal hanife": "grandson", "emre celal": "brother", "emre tuğba": "brother",
                 "emre aynur": "son", "emre kadir": "son", "emre sevgi": "nephew", "emre emine": "nephew", "emre oktay": "nephew", "emre necati": "grandson",
                 "emre hanife": "grandson", "tuğba celal": "sister", "tuğba emre": "sister", "tuğba aynur": "daughter", "tuğba kadir": "daughter",
                 "tuğba sevgi": "nephew", "tuğba emine": "nephew", "tuğba oktay" : "nephew", "tuğba necati" : "granddaughter", "tuğba hanife": "granddaughter",
                 "aynur celal": "mother", "aynur emre": "mother", "aynur tuğba": "mother", "aynur kadir": "wife", "aynur sevgi": "sister", "aynur emine":"sister",
                 "aynur oktay": "sister", "aynur hanife": "daughter", "aynur necati": "daughter", "kadir celal": "father", "kadir tuğba": "father",
                 "kadir emre": "father", "kadir aynur": "husband", "kadir sevgi": "brother in law", "kadir emine": "brother in law", "kadir oktay": "brother in law",
                 "kadir necati": "son in law", "kadir hanife": "son in law", "sevgi celal": "aunt", "sevgi tuğba": "aunt", "sevgi emre": "aunt",
                 "sevgi kadir": "sister in law", "sevgi emine": "sister", "sevgi aynur": "sister", "sevgi oktay": "sister", "sevgi hanife": "daughter",
                 "sevgi necati": "daughter", "emine celal": "aunt", "emine tuğba": "aunt", "emine emre": "aunt", "emine kadir": "sister in law",
                 "emine aynur": "sister", "emine sevgi": "sister", "emine oktay": "sister", "emine hanife": "daughter", "emine necati": "daughter",
                 "oktay celal": "uncle", "oktay emre": "uncle", "oktay tuğba": "uncle", "oktay kadir": "brother in law", "oktay aynur": "brother",
                 "oktay sevgi": "brother", "oktay emine": "brother", "oktay hanife": "son", "oktay necati": "son", "hanife celal": "grandmother",
                 "hanife emre": "grandmother", "hanife tuğba": "grandmother", "hanife aynur": "mother", "hanife kadir": "mother in law", "hanife sevgi": "mother",
                 "hanife oktay": "mother", "hanife emine": "mother", "hanife necati": "wife", "necati celal": "grandfather", "necati emre": "grandfather",
                 "necati tuğba": "grandfather", "necati aynur": "father", "necati kadir": "father in law", "necati sevgi": "father", "necati emine": "father",
                 "necati oktay": "father", "necati hanife": "husband"}
                 
                 

    return relations

def main():
    member()
    x=get_input_1()
    y=get_input_2()
    relations=relation()

    z = str(x) + " " + str(y)
    v = str(y) + " " + str(x)

    if z in relations:
        print("\n" + x + " is " + relations[z] + " of " + y + ".")
        if v in relations:
            print(y + " is " + relations[v] + " of " + x + ".")
    else:
        print("Not Found!")

main()

