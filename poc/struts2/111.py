error_3 = ['.js']
error_4 = ['.mp4', '.mp3', '.gif', '.php', '.asp', '.htm', '.doc', '.swf', '.dox', '.cgi', '.txt', '.png', '.exe',
           '.jpg', '.zip', '.css']
error_5 = ['.docx', '.html', '.aspx']
urls = []

with open('1.txt', 'r')as f:
    url_list = f.readlines()

for line in url_list:
    line = line.strip()
    if 'http://' in line:
        url = line.strip("?")
        if url[-3:] in error_3:
            pass
        elif url[-4:] in error_4:
            pass
        elif url[-5:] in error_5:
            pass
        else:
            urls.append(url)
urls = sorted(list(set(urls)))
for i in urls:
    with open('2.txt','a')as w:
        w.write(i+'\n')