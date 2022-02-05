# ScratchPY Online loader
import os
try:
    import pygame
except ImportError:
    os.system("pip install pygame")
    import pygame
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import pygame,json,_thread,os,io
filename = None
userdata = ["OverflowExceptionError","code"]
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen
code = {}
class FakeOpen:
  def __init__(self,useless):
    a = requests.get(useless)
    self.a = a
    pass
  def __enter__(self):
    return self
  def __exit__(self,u,r,s):
    print(u)
    print(self)
    print(r)
    print(s)
    pass
  def read(self):
    return self.a.text
with FakeOpen("http://overflowexceptionerror.github.io/Website/scratchpy/users/" + userdata[0] + "/" + userdata[1] + ".json") as f:
    data = json.load(f)
    code = data
class Image:
  def __init__(self,username,project,image):
    # a = requests.get(useless)
    b = urlopen("http://overflowexceptionerror.github.io/Website/scratchpy/users/" + username + "/" + project + "/" + image).read()
    file = io.BytesIO(b)
    self.a = file
    pass
  def __enter__(self):
    return self
  def __exit__(self,u,r,s):
    print(u)
    print(self)
    print(r)
    print(s)
    pass
  def read(self):
    return self.a
if code["showForeverWindowOnly"] == "false":
    window = pygame.display.set_mode((code["window"]["width"],code["window"]["height"]))
    pygame.display.set_caption("ScratchPY Client - " + code["name"] + " by " + code["publisher"])
sprimages = []
sprites = []
for sprite in code["sprites"]:
    sprimages.append(pygame.image.load(Image(code["user"],code["window"]["title"],code[sprite]["image"]).read()))
    sprites.append(sprite)
# move(X,Y)="move"
# goto(X,Y)="gotoPos"
# when flag clicked="flagclicked"
# when (x) happens="startgrp"
csx = 0
csy = 0
currentVersion = 3
if code["version"] < currentVersion:
    print("Warning: older code types may be incompatible with the current version.")
if code["version"] > currentVersion:
    print("Warning: newer scripts may use code objects incompatible with the current version.")
from time import time
cutime = time()
tickSpeed = 5
close = 0
ticksPassed = 0
waiting = 0
def otherWorld(host,sprite):
    if code[sprite]["script"][host]["version"] > currentVersion:
        print("Warning: newer scripts may use code objects incompatible with the current version.")
    if code["showForeverWindow"] == "true" or code["showForeverWindowOnly"] == "true":
        window2 = pygame.display.set_mode((code[sprite]["script"][host]["window"]["width"],code[sprite]["script"][host]["window"]["height"]),0,32)
        pygame.display.set_caption(code[sprite]["script"][host]["window"]["title"])
    while True:
        if code["showForeverWindow"] == "true" or code["showForeverWindowOnly"] == "true":
            window2.fill((255,255,255))
        for sprite in sprites:
            for thing in code[sprite]["script"][host]["script"]:
                if code[sprite]["script"][host]["script"][thing]['type'] == "startgrp" and waiting == 0:
                    pass
                if code[sprite]["script"][host]["script"][thing]['type'] == "flag" and waiting == 0:
                    pass
                if code[sprite]["script"][host]["script"][thing]['type'] == "moveto" and waiting == 0:
                    code[sprite]["pos"][0] = code[sprite]["script"][thing]["x"]
                    code[sprite]["pos"][1] = code[sprite]["script"][thing]["y"]
                if code[sprite]["script"][host]["script"][thing]['type'] == "goto" and waiting == 0:
                    print("GoTo is a depricated function.")
                if code[sprite]["script"][host]["script"][thing]['type'] == "forever" and waiting == 0:
                    print("Threading is not implemented yet. Are you running a newer version of code.json?")
                if code[sprite]["script"][host]["script"][thing]['type'] == "wait" and waiting == 0:
                    pygame.time.wait(code[sprite]["script"][host]["script"][thing]["seconds"])
                if code[sprite]["script"][host]["script"][thing]['type'] == "endgrp" and waiting == 0:
                    pass
            if code["showForeverWindow"] == "true" or code["showForeverWindowOnly"] == "true":
                for sprit in sprimages:
                    window2.blit(sprit,(code[sprite]["pos"][0],code[sprite]["pos"][1]))
        if code["showForeverWindow"] == "true" or code["showForeverWindowOnly"] == "true":
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    close = 1
                    exit()
            pygame.display.update()
for sprite in sprites:
    for thing in code[sprite]["script"]:
        if code[sprite]["script"][thing]["type"] == "startgrp" and waiting == 0:
            pass
        if code[sprite]["script"][thing]["type"] == "flag" and waiting == 0:
            pass
        if code[sprite]["script"][thing]["type"] == "moveto" and waiting == 0:
            code[sprite]["pos"][0] = code[sprite]["script"][thing]["x"]
            code[sprite]["pos"][1] = code[sprite]["script"][thing]["y"]
        if code[sprite]["script"][thing]["type"] == "goto" and waiting == 0:
            print("GoTo is a depricated function.")
        if code[sprite]["script"][thing]["type"] == "forever" and waiting == 0:
            try:
                _thread.start_new_thread(otherWorld,(thing,sprite),)
            except TypeError:
                print("A code mistake was made, and ScratchPy can't continue running this block.")
            # print("Threading is not implemented yet. Are you running a newer version of code.json?")
        if code[sprite]["script"][thing]["type"] == "wait" and waiting == 0:
            pygame.time.wait(code[sprite]["script"][thing]["seconds"])
        if code[sprite]["script"][thing]["type"] == "endgrp" and waiting == 0:
            pass
while True:
    if code["showForeverWindowOnly"] == "false":
        window.fill(code["window"]["background"])
        for sprite in sprites:
            for sprit in sprimages:
                window.blit(sprit,(code[sprite]["pos"][0],code[sprite]["pos"][1]))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        pygame.display.update()
    if close == 1:
        exit()
