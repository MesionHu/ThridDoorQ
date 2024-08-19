import Form
import Function

DOOR_NUMBER=3

Doors=Form.INIT_Door(DOOR_NUMBER)
Function.SET_REWARD(Doors)
Function.SET_HOSTER(Doors)
PLAYER_DOOR=Function.SET_PLAYER(DOOR_NUMBER)
print(Doors)
print(PLAYER_DOOR)