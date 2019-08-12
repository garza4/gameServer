import gameServer_pb2
import gameServer_pb2_grpc
import logging
import grpc

#channel = grpc.insecure_channel('localhost:50051')
#stub = gameServer_pb2_grpc.GameServiceStub(channel)


def createPlayer(mana, health, stamina,level,exp,xVal,yVal):
    player = gameServer_pb2.Player()
    player.mana = mana
    player.health = health
    player.stamina = stamina
    player.level = level
    #print(player.level)
    player.exp = exp
    player.xVal = xVal
    player.yVal = yVal
    return player

def gameMagicAttack(stub,player,reqMagic):
    player.mana = stub.MagicAttack(player).mana
    return player



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gameServer_pb2_grpc.GameServiceStub(channel)
        magic = gameServer_pb2.Magic()
        magic.mana = 4
        player1 = createPlayer(10,10,20,1,0,0,0)
        #print(gameMagicAttack(stub,player1,magic))
        #print(stub.Heal(player1))
        direction = gameServer_pb2.Direction()
        direction.x_direction = "North"
        direction.y_direction = "North"
        position = stub.Move(direction)
        player1.xVal = position.x_position
        player1.yVal = position.y_position
        print(player1)
        spellbook = {"Fireball" : 5, "Regenerate":5}
        
        
if __name__ == "__main__":
    logging.basicConfig()
    run()


