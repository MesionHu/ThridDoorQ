import random
def SET_REWARD(Doors):
    Reward_number=random.randint(0,len(Doors)-1)
    Doors[Reward_number]=1

def SET_PLAYER(NUMBER):
    return random.randint(0,NUMBER-1)

def SET_HOSTER(Doors,NUMBER):
    Host_number=random.randint(0,len(Doors)-1)
    if Host_number==NUMBER:
        Host_number=random.randint(0,len(Doors)-1)
    if Doors[Host_number]!=1:
        Doors[Host_number]=2
    else:
        SET_HOSTER(Doors)