import random
range1=input("Guess Number GAME !! , BOOM range 1- ? :");
range1=int(range1);
boom=random.randrange(0,range1);

GG=False;
rangefloor=1;
rangesky=range1;

while (GG==False):
    number = input("Guess Number "+str(rangefloor)+"-"+str(rangesky) +" :" );
    number = int(number);
    if (number==boom):
        print("BOOM !!  GAME OVER!!");
        GG=True;
    elif (number>boom and number<rangesky):
        print("number is too big !");
        rangesky=number;
    elif (number<boom and number>rangefloor):
        print("number is too small !");
        rangefloor=number;
    else :
        print("number is Out of range !");


print(boom);