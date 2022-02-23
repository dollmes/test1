import grpc
from filesendtest_pb2 import *
import filesendtest_pb2_grpc
from concurrent import futures

class FileSendTestServiceServicer(filesendtest_pb2_grpc.FileSendTestServiceServicer):
    def __init__(self):
        pass
    def FileSendTest(self, request_iterator, context):
        size = 0
        name = ""
        def stream():
            while 1:
                yield next(request_iterator)
        output_stream = stream()
        while 1:
            ite = next(output_stream)
            #print(ite.name + ":index=" + str(ite.index) + ":" + str(len(ite.data)) + "byte")
            name = ite.name
            size += len(ite.data)
            index = ite.index
            yield FileSendTestResponseParam(
                reply = name,
                index = index,
                recvedsize = size
            )
            if size >= ite.filesize:
                break
        print("[" + name + "] recv end : " + str(size) + "byte")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
filesendtest_pb2_grpc.add_FileSendTestServiceServicer_to_server(FileSendTestServiceServicer(), server)
server.add_insecure_port('[::]:5051')
server.start()

try:
    server.wait_for_termination()
except KeyboardInterrupt:
    # stop server
    server.stop(0)
