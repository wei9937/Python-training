import itertools, random

aa=(1,2,3);
sub=[1,3,5]

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

#print(aa);
random.shuffle(deck)

#print(deck[1][0], "of", deck[1][1])


pi = 3.1415926

di=4;

ans=(di/2)**2*pi
print ("ans="+str(ans));
