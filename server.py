import grpc
import time
from test_pb2 import *
import test_pb2_grpc
from concurrent import futures


class TestServiceServicer(test_pb2_grpc.TestServiceServicer):
    def __init__(self):
        pass

    def ClientTest(self, request, context):
        return ServerTestResponseParam(
            reply_msg="A:" + str(request.flagA) + ":" + str(request.valA)
            + " B:" + str(request.flagB) + ":" + str(request.valB)
            + " C:" + str(request.flagC) + ":" + str(request.valC)
            + " D:" + str(request.flagD) + ":" + str(request.valD)
        )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
test_pb2_grpc.add_TestServiceServicer_to_server(TestServiceServicer(), server)
server.add_insecure_port('[::]:5051')
server.start()

try:
    while True:
        time.sleep(24 * 3600)
except KeyboardInterrupt:
    # stop server
    server.stop(0)
