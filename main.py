import MASSTEST

DOOR_NUMBER=3
HOST_NUMBER=1
N=100000
CHANGE=MASSTEST.CHANGE_DOOR(N,DOOR_NUMBER)
NOT_CHANGE=MASSTEST.NOT_CHANGE_DOOR(N,DOOR_NUMBER)

print("进行更换的概率:",CHANGE/N)
print("进行不更换的概率:",NOT_CHANGE/N)