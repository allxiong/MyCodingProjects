#Advanced image manipulation. Image collage
#problem 1
def pyCopy():
   pic = makePicture( pickAFile())
   w = getWidth(pic)
   h = getHeight(pic)
   myCanvas = makeEmptyPicture(w+600, h+600)
   for x in range(0, w):
     for y in range(0, h):
       p = getPixel(pic, x, y)
       setColor(getPixel(myCanvas, x+100, y+100), getColor(p))
   show(myCanvas)
   return myCanvas  

def pyCopy(source,target,targetX,targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      c = getColor(getPixel(source, x, y))
      setColor(getPixel(target, targetX + x, targetY + y), c)
  show(target)
  return target

#problem 2
def copyToCollage():
  width = 2550
  height = 3000
  curX = 0
  curY = 0
  rowMaxY = 0
  myCanvas = makeEmptyPicture(2550, 3000)
  
  for i in range(0, 8):
    #select image and copy to canvas. Recalculate the curX and curY to stay in boundary
    pic = makePicture( pickAFile())
    w = getWidth(pic)
    h = getHeight(pic)
    endX = curX + w
    if h > rowMaxY:
      rowMaxY = h
    if endX > 2550:
      curX = 0
      curY = curY + rowMaxY
    myCanvas = pyCopyTo(myCanvas, pic,  curX, curY)
    curX = curX + w
    
  show(myCanvas)
  writePictureTo(myCanvas, 'C:\\Users\\allie\\PythonCode\\images\\8by11collage.jpg')
  return myCanvas    

def shrink(picture):
  newpic = makeEmptyPicture(getWidth(picture)/2 + 1, getHeight(picture)/2)
  for x in range(0, getWidth(picture), 2):
    for y in range(0, getHeight(picture), 2):
      setColor(getPixel(newpic, x/2, y/2), getColor(getPixel(picture, x, y)))
  return newpic


def getPic():
  return makePicture(pickAFile())

"""Problem 1"""   
"""This version creates a large empty image and coppies the image to the desired x and y coordinates""" 

def simplecopyTo():
   source = getPic()
   target =  makeEmptyPicture(getWidth(source)+100, getHeight(source)+100)
   newpic = pyCopy(source, target, 50, 50)
   show(newpic)
   writePictureTo(newpic,'C:\\Users\\allie\\PythonCode\\images\\copiednewPic.jpg') 
   
def pyCopy(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      tP = getPixel(target, targetX+x-1, targetY+y-1)
      setColor(tP, color)
  return target
  
"""Problem 2"""
def vertical_mirror(pic):
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, getWidth(pic) - (x + 1), y)
      setColor(pixel2, color)
  return pic
  
  
def horizontal_mirror_ttb(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      setColor(pixel2, color)
  return pic
  
def horizontal_mirror_btt(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      color = getColor(pixel2)
      setColor(pixel, color)
  return pic
  
def quadruple_mirror(pic):
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, getWidth(pic) - (x + 1), y)
      setColor(pixel2, color)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      setColor(pixel2, color)
  return pic

def rotate_pic(picture):
  newpic = makeEmptyPicture(getHeight(picture), getWidth(picture))
  for y in range(0, getHeight(picture)):
    for x in range(0, getWidth(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(newpic, y, getWidth(picture) - (x + 1)), color)
  return newpic
    
def shrink(picture):
  newpic = makeEmptyPicture(getWidth(picture)/2 + 1, getHeight(picture)/2)
  for x in range(0, getWidth(picture), 2):
    for y in range(0, getHeight(picture), 2):
      setColor(getPixel(newpic, x/2, y/2), getColor(getPixel(picture, x, y)))
  return newpic

def doubleRed(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 2)
  return pic

  
"""This version you must define the x and y coordinates to copy each image to"""
def makeCollage():
  collage = makeEmptyPicture(2550, 3300)
  image1 = getPic()
  image2 = getPic()
  image3 = getPic()
  image4 = getPic()
  image5 = getPic()
  image6 = getPic()
  image7 = getPic()
  image8 = getPic()
  image9 = getPic()
  
  pyCopy(image1, collage, 50, 50)
  pyCopy(image2, collage, 850, 50)
  pyCopy(image3, collage, 1680, 50)
  pyCopy(image4, collage, 30, 700)
  pyCopy(image5, collage, 650, 750)
  pyCopy(image6, collage, 1500, 730)
  pyCopy(image7, collage, 50, 1500)
  pyCopy(image8, collage, 850, 1600)
  pyCopy(image9, collage, 1675, 1550)
 
  writePictureTo(collage, 'C:\\Users\\allie\\PythonCode\\images\\collage1.jpg')