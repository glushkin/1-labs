#Glushkin Alexander PS-22
import urllib2
import re
import urllib



list_extensions = ['gif', 'bmp', 'jpg', 'jpeg', 'png']
url = 'http://lenta.ru/'
contents = urllib2.urlopen(url) 
contents = contents.read()
img_urls = re.findall('img .*?src="(.*?)"', contents)  
for i in range(len(img_urls)):
     address = img_urls[i]
     if address[address.rfind('.') + 1:] in list_extensions:  
         name_img = address[address.rfind('/') + 1:]
         urllib.urlretrieve(address, name_img)