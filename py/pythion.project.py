

# This is a sample Python script conservasion convert int to roman number.
def intToRoman(num):
    m=["","M","MM","MMM",]
    c=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    x=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    i=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    #converting to roman
    thousands=m[num//1000]
    hundreds=c[(num%1000)//100]
    tens=x[(num%100)//10]
    ones=i[num%10]

    ans=(thousands+hundreds+tens+ones)

    return ans
while True:
    print('''1.Conversion from int to roman
2.Exit'''
    )
    a=int(input('Enter your choice :- '))
    if a==1:
        number=int(input("Write  the number here:"))
        print("The nummber in roman is:",intToRoman(number))
    elif a==2:
        break
    else:
        print('Invalid')
    

    
    
    

