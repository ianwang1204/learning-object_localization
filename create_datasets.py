#把要用的引入
from PIL import Image, ImageColor, ImageDraw as D
import os,sys,random



#得知顏色
c=ImageColor.colormap
c_map=list()
for a, b in enumerate(c):
    t=ImageColor.getrgb(b)
    if(b=="ivory" or b=="oldlace" or b=="cornsilk" or t[0]+t[1]+t[2]>600):
        continue
    if len(b)>=5 and b[-5:] != "white" and b[:5]!="white" and b!="lightgoldenrodyellow" and b!="linen" and b!="seashell":
        c_map.append(b)


#創資料夾、文件
www=open("train.csv","w")
www.writelines("img_path,xmin,ymin,xmax,ymax,width,height,label\n")
image_path = "train_images"
if image_path not in os.listdir():
    os.mkdir(image_path)
    print("folder created")
    



#畫
for ind in range(1600):
    #畫布
    i=Image.new('RGB', (200,200),(255,255,255))
    draw=D.Draw(i)
    #大小、顏色
    left=max(0,random.randint(-5,150))
    right = min(200,random.randint(left+10,205))
    up=max(0,random.randint(-5,150))
    down = min(200,random.randint(up+10,205))
    cc=random.choice(c_map)
    ccc=''.join(str(ImageColor.getrgb(cc)).split(' '))
    s=f"{image_path}/{ind}.jpg,{left},{up},{right},{down},200,200" #名字
    #label
    if min(right-left, down-up)>20 and random.randint(1,10)<=6:
        w=random.randint(3,min(right-left, down-up)//2-2)
        draw.rectangle([(left,up),(right,down)],outline=cc,width=w)
        s+=",filled"
    else:
        draw.rectangle([(left,up),(right,down)],outline=cc,fill=cc)
        s+=",0"
    #存檔
    www.writelines(s+"\n")
    i.save(f"{image_path}/{ind}.jpg",'JPEG')


www.close()
