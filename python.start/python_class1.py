# 定義類別IO 兩個屬性 supportedSrcs,read

class IO:
    supportedSrcs= ["copnsole", 'file']
    def read(src):
        if src not in IO.supportedSrcs:
            print("not supproted")
        else:
            print("Read from", src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")