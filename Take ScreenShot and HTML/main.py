from selenium_mod.content_downloader import download_content
import io
# import os
from PIL import Image

target_url = r"C:\Users\Ehtisham Ali\OneDrive\Desktop\Take ScreenShot and HTML\URLs.txt"
with open(target_url, 'r') as file:
    mylist = file.read().splitlines()
i=0
for line in mylist:
    if line:
        i = i+1
        html_code,screenshot_file,res = download_content("https://"+line)
        print(res)
        if res == "success":
                screenshot = io.BytesIO(screenshot_file)
                im = Image.open(screenshot)
                im.save(f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\image{i}.png")

# for i in range(1,75):
#     print(i)
#     respo = os.path.isfile(f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\image{i}.png")
#     if not respo:
#         to_try = mylist[i-1]
#         html_code,screenshot_file,res = download_content("https://"+to_try)
#         print(res)
#         if res == "success":
#                 screenshot = io.BytesIO(screenshot_file)
#                 im = Image.open(screenshot)
#                 im.save(f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\image{i}.png")
#     else:
#         print(f"image{i} already exists...")

# respo = os.path.isfile(f"C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Take ScreenShot and HTML\\image4.png")
# print(respo)

