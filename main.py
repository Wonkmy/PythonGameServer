#from PIL import Image
#im=Image.open("down.png")
#out=im.convert("L")
#a,b=100
#a,b=out.size
#im.rotate(45).show()
#print(im.getpixel((100,100)))

# asciis="@%#*+=-. "
# texts=""

# for col in range(a):
#     for row in range(b):
#         gray=out.getpixel((col,row))
#         texts+=asciis[int(gray/255*8)]
#     texts+="\n"

 #with open("down.txt","w") as file:
 #    file.write(texts)

# from captcha.image import ImageCaptcha
# imgcap= ImageCaptcha()
# imgcap.write('wonkmy','captcha.png')

# f=open('notes.txt')
# print(f.read())
# f.close()
# f=open('notes.txt','a')
# f.write("write a content!!\n")
# f.close()

# class Ball:
#     def __init__(self,name='任意球'):
#         self.name=name

#     def kick(self):
#         print("我是 %s 谁在踢我?" %self.name)



# a = Ball('足球')
# print(a.__dict__)

import urllib.request

url='https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh'
data
res=urllib.request.urlopen("http://placekitten.com/g/500/600")
cat_img=res.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
