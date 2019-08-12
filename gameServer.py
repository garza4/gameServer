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
        position = gameServer_pb2.Position()
        if request.x_direction == "North":
            position.x_position += 1
        if request.x_direction == "South":
            position.x_direction -= 1
        if request.x_direction == "East":
            position.x_direction += 1
        if request.x_direction == "West":
            position.x_direction -= 1
        
        if request.y_direction == "North":
            position.y_position += 1
        if request.y_direction == "South":
            position.y_direction -= 1
        if request.y_direction == "East":
            position.y_direction += 1
        if request.y_direction == "West":
            position.y_direction -= 1
        print(position)
        return position


    def PhysicalAttack(self,request,context):
        player  = copy,copy(request)
        player.stamina -= int(request.stamina / request.level)
        return player

    def MagicAttack(self,request,context):
        player = copy.copy(request)
        player.mana = int(math.sqrt(request.mana) + (request.level / request.stamina)) 
        print("Damage done was - ", player.mana, "!")
        return player
    
    
    #use magic, gain health
    def Heal(self,request,context):
        print(dir(request))
        player = copy.copy(request)
        player.mana -= int((request.mana / request.level) + request.stamina)
        player.health += int(math.sqrt(player.level) + request.stamina)
        return player
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
