import requests
print('DOWNLOADING VERSION LIST')
print(requests.get('http://overflowexceptionerror.github.io/Website/list.txt').text)
a = input('CHOOSE: ')
b = requests.get("http://overflowexceptionerror.github.io/Website/hcarchives/" + a + ".pck", stream=True)
handle = open("versions/" + a + '.pck', "wb")
for chunk in b.iter_content(chunk_size=512):
    if chunk:  # filter out keep-alive new chunks
        handle.write(chunk)
handle.close()
handle = open("launcher.pck","wb")
handles = open("versions/" + a + '.pck', "rb")
handle.write(handles.read())
handle.close()
handles.close()
import os
os.system('launcher.exe')
os.remove('launcher.pck')
print('THANK YOU FOR USING HOUSECRAFT LEGACY ARCHIVES')