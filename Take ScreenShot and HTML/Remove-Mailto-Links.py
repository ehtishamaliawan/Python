lines = []
with open(r"C:\Users\Ehtisham Ali\OneDrive\Desktop\Take ScreenShot and HTML\URLs.txt", 'r') as fp:
    lines = fp.readlines()
with open(r"C:\Users\Ehtisham Ali\OneDrive\Desktop\Take ScreenShot and HTML\newURLs.txt", 'w') as fp:
    for line in lines:
        if 'drive' not in line:
            fp.write(line)