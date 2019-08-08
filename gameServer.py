import gameServer_pb2
import gameServer_pb2_grpc
import grpc
import logging
from concurrent import futures

def updateMagic(player,magic):
    magicOutput = gameServer_pb2_grpc.MagicAttack(magic)
    player.mana -= magicOutput
    return player.mana
 


class GameServiceServer(gameServer_pb2_grpc.GameServiceServicer):
    
    def __init__(self):
        self.db = gameServer

    def Move(self, request, context):
        #North
        if self.Direction == 1:
            self.Position.yval += 1
        #South
        if self.Direction == -1:
            self.Position.yval -= 1
        #East
        if self.Directions == 3:
            self.Direction.xval += 1
        #West
        if self.Direction == 4:
            self.Position -= 1
             

    def PhysicalAttack(self,request,context):
        request.stamina -= request.Stamina

    def MagicAttack(self,request,context):
        self.Player.mana -= request.Mana
        print("magic attack!")
    
    #use magic, gain health
    def Heal(self,request,context):
        self.Player.mana -= self.Mana
        self.Player.health += self.Health
        print("Restoring Health ---")
    #do damage to a given player
    def DamageCalculation(self,request,context):
        self.Player.health -= request.Attack

def serve():
    server = grpc.server(futures.ThreadPoolExeccutor(max_workers=10))
    gameServer_pb2_grpc.add_gameServiceServicer_to_server(GameServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == "main":
    logging.basicConfig()
    serve()
