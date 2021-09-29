from PIL import Image
import os
lists=[]
new_list=[]
dir = os.getcwd() + "/image"
if os.path.isdir(dir) == False:
    os.mkdir(dir)

if len(os.listdir(dir)) == 0:
    exit

files=os.listdir(dir)
for i in range(len(files)):
    img=Image.open(dir+"/"+files[i])
    img=img.convert("RGB")
    lists.append(img)

img_1=lists[0]
if len(lists) != 1:
    for i in range(1,len(lists)):
        new_list.append(lists[i])

img_1.save(os.getcwd()+"/image.pdf", save_all=True,append_images=new_list)
