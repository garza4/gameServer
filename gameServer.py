import gameServer_pb2
import gameServer_pb2_grpc
import grpc
import logging
from concurrent import futures

class GameServiceServer(gameServer_pb2_grpc.GameServiceServer):
    print("something")
    

    def Move(self, request, context):
        print(self.North)
    
    def PhysicalAttack(self,request,context):
        print("attack!")

    def MagicAttack(self,request,context):
        print("magic attack!")
    
    def Heal(self,request,context):
        print("Restoring Health ---")

def serve():
    server = grpc.server(futures.ThreadPoolExeccutor(max_workers=10))
    gameServer_pb2_grpc.add_gameServiceServicer_to_server(GameServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == "main":
    print(GameServer())
    logging.basicConfig()
    serve()
