import logging
import grpc
import gameServer_pb2
import gameServer_pb2_grcp

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        gameStub = gamerServer_pb2_grcp.GameServiceStub(channel)
        response = stub.Move(gameServer_pb2.Direction(direction="north"))

if __name__ = "__main__":
    logging.basicConfig()
    run()

