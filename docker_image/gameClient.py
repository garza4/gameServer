import gameServer_pb2
import gameServer_pb2_grpc
import logging
import grpc

#channel = grpc.insecure_channel('localhost:50051')
#stub = gameServer_pb2_grpc.GameServiceStub(channel)


def createPlayer(mana, health, stamina,level,exp,xVal,yVal,name):
    player = gameServer_pb2.Player()
    player.mana = mana
    player.health = health
    player.stamina = stamina
    player.level = level
    #print(player.level)
    player.exp = exp
    player.xVal = xVal
    player.yVal = yVal
    player.name = name
    return player

def gameMagicAttack(stub,player,reqMagic):
    player.mana = stub.MagicAttack(player).mana
    return player

def playerMovement(player,stub):
    while True:
        controllerInput = input("Enter a direction to move : North South East West \n")
        direction = gameServer_pb2.Direction()
        direction.x_direction = controllerInput
        direction.y_direction = controllerInput
        print(direction)
        position = stub.Move(direction)
        player.xVal = position.x_position 
        player.yVal = position.y_position


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gameServer_pb2_grpc.GameServiceStub(channel)
        magic = gameServer_pb2.Magic()
        magic.mana = 4
        player1 = createPlayer(10,10,20,1,0,0,0,"Cooper")
        playerMovement(player1,stub)
        print(player1)
        spellbook = {"Fireball" : 5, "Regenerate":5}
        
        
if __name__ == "__main__":
    logging.basicConfig()
    run()


