import os
import time
from PIL import Image

path = 'D:/DCIM/100CLOUD/'
l = os.listdir(path)
for f in l:
    print(f)
    ext = f.split('.')[1]
    print(os.path.getmtime(path+str(f)))
    a = os.path.getmtime(path+str(f))
    b = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(a))
    print(b)
    target = ''
    try:
        target = Image.open(path+str(f))._getexif()[36867]
        target = target.replace(':', '-')
    except:
        target = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(a))
    print(target)

    
    try:
        os.rename(path+str(f), path+target+'.'+ext)
    except:
        os.rename(path+str(f), path+target+f+'.'+ext)


