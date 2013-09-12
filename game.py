import pygame.camera
import pygame.image
import sys
import cv2
import time
from VideoCapture import Device

cam = Device()
cam.saveSnapshot('image.jpg')
cam.setResolution(160,120)

# grab first frame
colorimg = cam.getImage()
img = colorimg.convert('L')
WIDTH = img.size[0]
HEIGHT = img.size[1]
screen = pygame.display.set_mode( ( WIDTH*2, HEIGHT*2 ) )
pygame.display.set_caption("pyGame Camera View")
average = img
diff = img


while True :
    time.sleep(0.05)
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            sys.exit()
    rgbimg = img.convert("RGB")
    mode = rgbimg.mode
    size = rgbimg.size
    data = rgbimg.tostring()
    #print mode
    #assert mode in "RGB", "RGBA"
    surface = pygame.image.fromstring(data, size, mode)
    
    rgbimg = average.convert("RGB")
    mode = rgbimg.mode
    size = rgbimg.size
    data = rgbimg.tostring()
    #print mode
    #assert mode in "RGB", "RGBA"
    surface2 = pygame.image.fromstring(data, size, mode)

    rgbimg = diff.convert("RGB")
    mode = rgbimg.mode
    size = rgbimg.size
    data = rgbimg.tostring()
    #print mode
    #assert mode in "RGB", "RGBA"
    surface3 = pygame.image.fromstring(data, size, mode)

    rgbimg = colorimg
    mode = rgbimg.mode
    size = rgbimg.size
    data = rgbimg.tostring()
    #print mode
    #assert mode in "RGB", "RGBA"
    surface4 = pygame.image.fromstring(data, size, mode)

    # draw frame
    screen.blit(surface, (0,0))
    screen.blit(surface2, (WIDTH,HEIGHT))
    screen.blit(surface3, (0,HEIGHT))
    screen.blit(surface4, (WIDTH,0))

    pygame.display.flip()
    # grab next frame
    lastimg = img
    diff = lastimg
    colorimg = cam.getImage()
    img = colorimg.convert('L')
    for x in range(0, WIDTH):
        for y in range(0,HEIGHT):
            average.putpixel((x,y),(average.getpixel((x,y))*8 +  img.getpixel((x,y))*2)/10.0)

    for x in range(0, WIDTH):
        for y in range(0,HEIGHT):
            diff.putpixel( (x,y),  abs(lastimg.getpixel((x,y)) - img.getpixel((x,y))))

