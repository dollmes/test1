from bdb import Breakpoint
import grpc
import os
from filesendtest_pb2 import *
import filesendtest_pb2_grpc

limitsendsize = 2 * 1024 * 1024
#limitsendsize = 1024

channel = grpc.insecure_channel('localhost:5051')
stub = filesendtest_pb2_grpc.FileSendTestServiceStub(channel)

def send(sendfile):
    readsize = 0
    filesize = os.path.getsize(sendfile)
    datas = []
    with open(sendfile, 'rb') as f:
        while readsize < filesize:
            f.seek(readsize)
            data = f.read(limitsendsize)
            datas.append(data)
            readsize += len(data)
    def stream():
        sendindex = 0
        fname=os.path.basename(sendfile)
        for d in datas:
            yield FileSendTestParam(
                name = fname,
                filesize = filesize,
                index = sendindex,
                data = d)
            sendindex += 1
    respose = stub.FileSendTest(stream())
    while 1:
        ite = next(respose, None)
        if ite is None:
            break
        #print(ite.reply + ":index=" + str(ite.index) + ":recved=" + str(ite.recvedsize))
    print("end")

send("./input/test_small.jpg")
send("./input/test_middle.jpg")
