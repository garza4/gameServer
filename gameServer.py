import gameServer_pb2
import gameServer_pb2_grpc
import grpc
import logging
import time
import math
import copy
from concurrent import futures

 
class GameServiceServer(gameServer_pb2_grpc.GameServiceServicer):
    

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
        player = copy.copy(request)
        print(request.level)
        player.mana = int(math.sqrt(request.mana) + (request.level / request.stamina)) 
        print("Damage done was - ", player.mana, "!")
        return player
    
    
    #use magic, gain health
    def Heal(self,request,context):
        request.Player.mana -= request.Mana
        request.Player.health += request.Health
        print("Restoring Health ---")
    #do damage to a given player
    def DamageCalculation(self,request,context):
        request.Player.health -= request.Attack

def serve():
    print("server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gameServer_pb2_grpc.add_GameServiceServicer_to_server(GameServiceServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            print(server)
            print("server running")
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
    print("somethign")
