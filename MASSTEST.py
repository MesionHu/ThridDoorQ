import Form
import Function
import ISORNOR

#不改变选择
def NOT_CHANGE_DOOR(N,DOOR_NUMBER):
    count=0
    for i in range(N):
        Doors=Form.INIT_Door(DOOR_NUMBER)#初始化门
        Function.SET_REWARD(Doors)#设置奖励门
        PLAYER_DOOR=Function.SET_PLAYER(DOOR_NUMBER)#玩家选择的门
        Function.SET_HOSTER(Doors,PLAYER_DOOR)#主持人排除的门
        result=ISORNOR.REWARD_MATCH(Doors,PLAYER_DOOR)#判断是否匹配
        count+=result
    return count
#改变选择
def CHANGE_DOOR(N,DOOR_NUMBER):
    count=0
    for i in range(N):
        Doors=Form.INIT_Door(DOOR_NUMBER)#初始化门
        Function.SET_REWARD(Doors)#设置奖励门
        PLAYER_DOOR=Function.SET_PLAYER(DOOR_NUMBER)#玩家选择的门
        Function.SET_HOSTER(Doors,PLAYER_DOOR)#主持人排除的门
        PLAYER_DOOR_2=Function.ChangeDoor(Doors,PLAYER_DOOR)#更换门的选项
        result=ISORNOR.REWARD_MATCH(Doors,PLAYER_DOOR_2)#判断是否匹配
        count+=result
    return count