import gameServer_pb2
import gameServer_pb2_grpc
import logging
import grpc

#channel = grpc.insecure_channel('localhost:50051')
#stub = gameServer_pb2_grpc.GameServiceStub(channel)


def createPlayer(mana, health, stamina,level,exp,xVal,yVal,name,attack,defense):
    
    player = gameServer_pb2.Player()
    player.Stats.MANA = mana
    player.Stats.HEALTH = health
    player.Stats.STAMINA = stamina
    player.Stats.LEVEL = level
    #print(player.level)
    player.Stats.EXP = exp
    player.Stats.XVAL = xVal
    player.Stats.YVAL = yVal
    player.Stats.NAME = name
    player.Stats.ATTACK = attack
    player.Stats.DEFENSE = defense
    return player

def gameMagicAttack(stub,player,reqMagic):
    player.stats.mana = stub.MagicAttack(player).stats.mana
    return player

def playerMovement(player,stub):
    #while True:
    controllerInput = input("Enter a direction to move : North South East West \n")
    direction = gameServer_pb2.Direction()
    direction.x_direction = controllerInput
    direction.y_direction = controllerInput
    print(direction)
    position = stub.Move(direction)
    player.Stats.XVAL = position.x_position 
    player.Stats.YVAL = position.y_position
        
def gameHeal(stub, player):
    return stub.Heal(player).Stats.HEALTH


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gameServer_pb2_grpc.GameServiceStub(channel)
        player1 = createPlayer(10,10,20,1,0,0,0,"Cooper",10,10)
        playerMovement(player1,stub)
        player1.Stats.HEALTH = gameHeal(stub,player1)
        print(player1)
        spellbook = {"Fireball" : 5, "Regenerate":5}
        
        
if __name__ == "__main__":
    logging.basicConfig()
    run()


