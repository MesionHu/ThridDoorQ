import random
def SET_REWARD(Doors):
    Reward_number=random.randint(0,len(Doors)-1)
    Doors[Reward_number]=1
