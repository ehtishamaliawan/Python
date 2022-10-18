from fileinput import filename
import os
import hashlib

if __name__ == '__main__':
    unique = []
    for i in range(0,506):
        respo = os.path.isfile(f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\images\\image{i}.png")
        if respo:
            filename = f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\images\\image{i}.png"
            with open(filename,"rb") as f:
                bytes = f.read()
                filehash = hashlib.md5(bytes).hexdigest();
                if filehash not in unique: 
                    unique.append(filehash)
                else:
                    f.close()
                    os.remove(filename)
                    print(f"image{i} removed!")
        else:
            print(f"No Image{i}")