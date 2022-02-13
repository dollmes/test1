from asyncio.windows_events import NULL
import tkinter as tk
import grpc
from test_pb2 import *
import test_pb2_grpc


def number_validation(before_word, after_word):
    return (after_word.isdecimal()) and (len(after_word) <= 6)


def btn_send_clicked():
    response = stub.ClientTest(
        ClientTestSendParam(
            flagA=1 if chkvalA.get() else 0,
            flagB=1 if chkvalB.get() else 0,
            flagC=1 if chkvalC.get() else 0,
            flagD=1 if chkvalD.get() else 0,
            valA=int(text_BoxA.get()),
            valB=int(text_BoxB.get()),
            valC=int(text_BoxC.get()),
            valD=int(text_BoxD.get())
        )
    )
    print(response)


def on_closing():
    global channel
    channel.close()
    app.destroy()


app = tk.Tk()
app.geometry("200x200")
app.title('test')
app.protocol("WM_DELETE_WINDOW", on_closing)

test_frame = tk.Frame(app)
test_frame.pack(anchor="center", expand=True)

text_labelFlag = tk.Label(test_frame, text="flag")
text_labelFlag.grid(row=0, column=1)
text_labelVal = tk.Label(test_frame, text="val")
text_labelVal.grid(row=0, column=2)

text_labelA = tk.Label(test_frame, text="[A]")
text_labelA.grid(row=1, column=0)
chkvalA = tk.BooleanVar(value=True)
chkA = tk.Checkbutton(test_frame, text='', variable=chkvalA)
chkA.grid(row=1, column=1)
text_BoxA = tk.Entry(test_frame, width=6)
vcmdA = (text_BoxA.register(number_validation), '%s', '%P')
text_BoxA.configure(validate='key', vcmd=vcmdA)
text_BoxA.insert(0, "10")
text_BoxA.grid(row=1, column=2)

text_labelB = tk.Label(test_frame, text="[B]")
text_labelB.grid(row=2, column=0)
chkvalB = tk.BooleanVar(value=True)
chkB = tk.Checkbutton(test_frame, text='', variable=chkvalB)
chkB.grid(row=2, column=1)
text_BoxB = tk.Entry(test_frame, width=6)
vcmdB = (text_BoxA.register(number_validation), '%s', '%P')
text_BoxB.configure(validate='key', vcmd=vcmdB)
text_BoxB.insert(0, "10")
text_BoxB.grid(row=2, column=2)

text_labelC = tk.Label(test_frame, text="[C]")
text_labelC.grid(row=3, column=0)
chkvalC = tk.BooleanVar(value=True)
chkC = tk.Checkbutton(test_frame, text='', variable=chkvalC)
chkC.grid(row=3, column=1)
text_BoxC = tk.Entry(test_frame, width=6)
vcmdC = (text_BoxC.register(number_validation), '%s', '%P')
text_BoxC.configure(validate='key', vcmd=vcmdC)
text_BoxC.insert(0, "10")
text_BoxC.grid(row=3, column=2)

text_labelD = tk.Label(test_frame, text="[D]")
text_labelD.grid(row=4, column=0)
chkvalD = tk.BooleanVar(value=True)
chkD = tk.Checkbutton(test_frame, text='', variable=chkvalD)
chkD.grid(row=4, column=1)
text_BoxD = tk.Entry(test_frame, width=6)
vcmdD = (text_BoxD.register(number_validation), '%s', '%P')
text_BoxD.configure(validate='key', vcmd=vcmdD)
text_BoxD.insert(0, "10")
text_BoxD.grid(row=4, column=2)


btn_send = tk.Button(test_frame, text="送信", command=btn_send_clicked)
btn_send.grid(row=5, column=3, padx=(6, 0), pady=(4, 0))

channel = grpc.insecure_channel('localhost:5051')
stub = test_pb2_grpc.TestServiceStub(channel)

app.mainloop()
