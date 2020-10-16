from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from tkinter import messagebox


def makeImageEven(image):
    pixels = list(image.getdata())  # 得到一个这样的列表： [(r,g,b,t),(r,g,b,t)...]
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]  # 更改所有值为偶数（魔法般的移位）
    evenImage = Image.new(image.mode, image.size)  # 创建一个相同大小的图片副本
    evenImage.putdata(evenPixels)  # 把上面的像素放入到图片副本
    return evenImage


def constLenBin(int):
    binary = "0"*(8-(len(bin(int))-2))+bin(int).replace('0b','')
    return binary


"""
将字符串编码到图片中
"""
def encodeDataInImage():
    global image
    message1=input.get()
    if message1 == "":
        messagebox.showinfo('提示','隐藏信息未填写，请返回填写！')
        return
    evenImage = makeImageEven(image)
    binary = ''.join(map(constLenBin ,bytearray(message1, 'utf-8')))
    if len(binary) > len(image.getdata()) * 4:
        raise Exception("Error: Can't encode more than " + len(evenImage.getdata()) * 4 + " bits in this image. ")
    encodedPixels = [(r+int(binary[index*4+0]),g+int(binary[index*4+1]),b+int(binary[index*4+2]),t+int(binary[index*4+3])) if index*4 < len(binary) else (r,g,b,t) for index,(r,g,b,t) in enumerate(list(evenImage.getdata()))] # 将 binary 中的二进制字符串信息编码进像素里
    encodedImage = Image.new(evenImage.mode, evenImage.size)
    encodedImage.putdata(encodedPixels)
    encodedImage.save('encodeImage.png')
    messagebox.showinfo('提示', '添加信息成功！图片已保存到temp文件下')
    encodedImage.show()

#从二进制字符串转为 UTF-8 字符串


def binaryToString(binary):
    index = 0
    string = []
    rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
    fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
    while index + 1 < len(binary):
        chartype = binary[index:].index('0')
        length = chartype*8 if chartype else 8
        string.append(chr(int(fun(binary[index:index+length],chartype),2)))
        index +=length
    return ''.join(string)

def selectPath():
    path_ = askopenfilename()
    path.set(path_)
    global image
    image=Image.open(path_)

"""
解码隐藏数据
"""
def decodeImage():
    pixels = list(image.getdata())  # 获得像素列表
    binary = ''.join([str(int(r>>1<<1!=r))+str(int(g>>1<<1!=g))+str(int(b>>1<<1!=b))+str(int(t>>1<<1!=t)) for (r,g,b,t) in pixels]) # 提取图片中所有最低有效位中的数据
    # 找到数据截止处的索引
    locationDoubleNull = binary.find('0000000000000000')
    endIndex = locationDoubleNull+(8-(locationDoubleNull % 8)) if locationDoubleNull%8 != 0 else locationDoubleNull
    data = binaryToString(binary[0:endIndex])

    messageshow.set(data)


global image
root = Tk()
root.resizable(width = 100, height = 300)
root.title("图片处理")
path = StringVar()
strpath=" "
input = StringVar()
Label(root, text="目标文件:").grid(row=0, column=0)
Entry(root, textvariable=path,width=30).grid(row=0, column=1)
Button(root, text="文件选择", command=selectPath).grid(row = 0, column = 2)
filename = path
la = Label(root, text="请输入水印信息:", width=20, height=1).grid(row=1,column=0)
text2 = Entry(root, textvariable=input, width=30).grid(row=1,column=1)
message1 = input.get()
bt2 = Button(root, text="给图片添加水印", width=15,command=encodeDataInImage)
bt2.grid(row=3, column=0)
bt3 = Button(root, text="从图片中提取信息" ,width=15, height=1,command=decodeImage).grid(row=4, column=0)
messageshow=StringVar()
text3 = Entry(root, textvariable = messageshow, width="30").grid(row = 4 ,column = 1)
root.mainloop()
