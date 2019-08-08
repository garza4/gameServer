import gameServer_pb2
import gameServer_pb2_grpc
import logging
import grpc

#channel = grpc.insecure_channel('localhost:50051')
#stub = gameServer_pb2_grpc.GameServiceStub(channel)

#def gameMagicAttack(stub):
    #stub.MagicAttack()



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gameServer_pb2_grpc.GameServiceStub(channel)
        gameMagicAttack(stub)

if __name__ == "__main__":
    logging.basicConfig()
    run()
    print()

