import gameServer_pb2
import gameServer_pb2_grpc
import logging
import grpc

#channel = grpc.insecure_channel('localhost:50051')
#stub = gameServer_pb2_grpc.GameServiceStub(channel)


def createPlayer(stub,mana, health, stamina):
    player = gameServer_pb2.Player()
    player.mana = mana
    player.health = health
    player.stamina = stamina
    return player

def gameMagicAttack(stub,player,reqMagic):
    player.mana -= stub.MagicAttack(reqMagic).mana
    #player.mana -= magic 
    return player



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gameServer_pb2_grpc.GameServiceStub(channel)
        magic = gameServer_pb2.Magic()
        magic.mana = 4
        player1 = createPlayer(stub,10,10,10)
        print(gameMagicAttack(stub,player1,magic))
        spellbook = {"Fireball" : 5, "Regenerate":5}
        
        
if __name__ == "__main__":
    logging.basicConfig()
    run()

    print("Cooper")

