import gameServer_pb2
import gameServer_pb2_grpc
import grpc
import logging
import time
import math
import copy
import random
import json
from concurrent import futures

 
class GameServiceServer(gameServer_pb2_grpc.GameServiceServicer):
    
    #pass a json file of monsters?
    enemy_list = {}
    
    #take request for which direction to move
    def Move(self, request, context):
        position = directions_to_move(request)
        #gameServer_pb2.Position() = gameServer_pb2.Position() + position
        if check_for_attack():
            return (position,1)
        return (position,0)

        


    
    def check_for_attack(self):
        #mod by 3 so there is not a 50/50 chance of encountering an enemy
        #return the result of this calculation
        return random.randrange(1,20,1) % 3 == 0
    
    def directions_to_move(self,request):
        position = gameServer_pb2.Position()
        switch_for_directions(request.x_direction, position.x_position)
        switch_for_directions(request.y_direction, position.y_position)
        return position    

    
    def switch_for_directions(self, direction_to_move, position):
        return {
        #North        
        'N': lambda position: position + 1,
        #South
        'S': lambda position: position - 1, 
        #East
        'E': lambda position: position + 1,
        #West
        'W': lambda position: position - 1
                
        }.get(direction_to_move)(position)


    def PhysicalAttack(self,request,context):
        player = copy.copy(request)
        player.Stats.STAMINA -= int(request.Stats.STAMINA / request.Stats.LEVEL) + request.Stats.DEFENSE
        if player.Stats.HEALTH == 0:
            print("RIP")
        return player

    def MagicAttack(self,request,context):
        player = copy.copy(request)
        player.Stats.MANA = int(math.sqrt(request.Stats.MANA) + (request.Stats.LEVEL / request.Stats.STAMINA)) 
        print("Damage done was - ", player.Stats.MANA, "!")
        return player
    
    
    #use magic, gain health
    def Heal(self,request,context):
        #print(dir(request))
        player = copy.copy(request)
        player.Stats.MANA -= int((request.Stats.MANA / request.LEVEL) + request.Stats.STAMINA)
        player.Stats.HEALTH += int(math.sqrt(player.Stats.LEVEL) + request.Stats.STAMINA)
        print("Restoring Health +++ ", player.Stats.HEALTH)
        return player



if __name__ == "__main__":
    logging.basicConfig()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gameServer_pb2_grpc.add_GameServiceServicer_to_server(GameServiceServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop()
        print("Server Killed - RIP")
