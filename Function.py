import random
#无奖励门：0，奖励门：1，主持人选门：2，玩家选门：数字
def SET_REWARD(Doors):
    Reward_number=random.randint(0,len(Doors)-1)
    Doors[Reward_number]=1

def SET_PLAYER(NUMBER):
    return random.randint(0,NUMBER-1)

def SET_HOSTER(Doors,NUMBER):
    Host_number=random.randint(0,len(Doors)-1)
    if Host_number==NUMBER:
        SET_HOSTER(Doors,NUMBER)
    elif Doors[Host_number]==2:
        SET_HOSTER(Doors,NUMBER)
    elif Doors[Host_number]!=1:
        Doors[Host_number]=2
    else:
        SET_HOSTER(Doors,NUMBER)

def ChangeDoor(Doors,NUMBER):
    PLAYER_NUMBER=random.randint(0,len(Doors)-1)
    
    if PLAYER_NUMBER!=NUMBER and Doors[PLAYER_NUMBER]!=2:
        return PLAYER_NUMBER
    
    else:
        return ChangeDoor(Doors,NUMBER)
        