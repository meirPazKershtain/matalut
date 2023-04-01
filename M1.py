

## tirgul
def my_func(x1,x2,x3) :
    a,b,c=type(x1)is float, type(x2) is float ,type(x3)is float
    if (a !=True or b !=True or c !=True ):
        a,b,c= type(x1)is int, type(x2) is int ,type(x3)is int
        if ( a ==True or b == True or c == True ): 
            return  'Error: parameters should be float'
        else :
            return 'None' 
    try :
        a=((x1+x2+x3)*((x2+x3)*x3))/(x1+x2+x3)
    except  :
            return  'Not a number – denominator equals zero' 
                
    return float(a)


print(my_func("1.0",1.0,1))

#Q2
def reword (word:str):
    new_word =word[len(word)-1]
    for i in range((len(word)-2),-1,-1):
        char = word[i]
        new_word = new_word + char
    return new_word        

def countword():
    word= None
    count = 0
    fh = open("text.txt",'r')
    for line in fh:
        if word is None:
            word = line.rsplit(' ' )[0].lower().strip()
            continue
        l=line.lower().rsplit(' ')
        for w in l:
            new_w=reword(w).strip()
            if (str(new_w) == str(word)):
                count=count+1
    return (count+1)
    
print(countword())
