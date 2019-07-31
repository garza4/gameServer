import gameServicer.gameServer_pb2 as pb
import gameServicer.gameServer_pb2_grpc as pb2
class gameServer(gameServer_pb2_grpc.GameServiceServer):
   
    

    def Move(self, request, context):
        print(self.North)
    
    def PhysicalAttack(self,request,context):
        print("attack!")

    def MagicAttack(self,request,context):
        print("magic attack!")
    
    def Heal(self,request,context):
        print("Restoring Health ---")


