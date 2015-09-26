import random
pairsSet=set(["Leah","Lucy Roberts","JJW","Jowita","Leila","Anna","Lucy Cross","Eleanor","Lucy Harris","Nina","Dani","Aidan","Eddie","Nicole"])
pairs=[]
while len(pairsSet)>1:
	newPair = random.sample(pairsSet,2)
	pairs.append(newPair)
	pairsSet.remove(newPair[0]);pairsSet.remove(newPair[1])

week = 0
for pair in pairs:
	week+=1
	print("In week " + str(week) + ' ' + pair[0] + " is paired with " + pair[1])

for remainder in pairsSet: # Will only run for 1 or 0 people remaining
	print("Unfortunately " + remainder + " is on his/her own :(")
