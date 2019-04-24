#lab 6 instructor solution
def BetterBnW():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  # first make picture black and white
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avgRGB = r*0.299 + g*0.587 + b*0.114
    avgColor = makeColor(avgRGB, avgRGB, avgRGB)
    setColor(p, avgColor)
    
  repaint(pic)
  #show
  #if in windows system , add r in front of the file path when writing to file
  writePictureTo(pic,'C:\\Users\\allie\\PythonCode\\images\\betterBnW.jpg')
    
#Write a program to make a picture Sephia toned
#first turn picture to black and white    
# then make picture fade/yellow
#current red value  multiplier for red   multiplier for blue 
#red < 63 1.1 0.9 
#62 < red < 192 1.15 0.85 
#red > 191 1.08* 0.93 
def SephiaToned():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  # first make picture black and white
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avgRGB = (r+g+b)/3
    if avgRGB < 63:
      r = avgRGB * 1.1
      b = avgRGB * 0.9
    elif avgRGB >191:
      r = avgRGB * 1.08
      b = avgRGB * 0.93  
    else :
      r = avgRGB * 1.15
      b = avgRGB * 0.85
    if r >255:
      r = 255  
    avgColor = makeColor(r, avgRGB, b)
    setColor(p, avgColor)
    
  repaint(pic)
  #show
  #if in windows system , add r in front of the file path when writing to file
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\SephiaToned.jpg')
  
#artify image
#Current color range   New value for color  
# color < 64 31 
#63 < color < 128 95 
#127 < color < 192 159 
#191 < color < 256 223 

def Artify():
  filename = pickAFile()
  print filename
  pic = makePicture(filename)
  pixels = getPixels(pic)
  # first make picture black and white
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    r = getArtifyValue(r)
    g = getArtifyValue(g)
    b = getArtifyValue(b)
    newColor = makeColor(r, g, b)  
    setColor(p, newColor)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\artified.jpg')

def getArtifyValue(val):
  if val <64:
    val = 31
  elif 63 < val and val < 128:
    val = 95
  elif 127 < val and val < 192:
    val = 159
  else:
    val = 223    
  return val  


def chromakey():
  filenameA = pickAFile()
  picA = makePicture(filenameA)
  pixelsA = getPixels(picA)
  filenameB = pickAFile()
  picB = makePicture(filenameB)
  pixelsB = getPixels(picB)    
  for pix in pixelsA:
    r = getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    if r < 70 and g > 120 and b < 80:
      xA = getX(pix)
      yA = getY(pix)
      pixB = getPixel(picB, xA, yA)
      rB = getRed(pixB)
      gB = getGreen(pixB)
      bB = getBlue(pixB)
      newColor = makeColor(rB, gB, bB) 
      setColor(pix, newColor)     
  repaint(picA)
  writePictureTo(picA, 'C:\\Users\\allie\\PythonCode\\images\\greenscreen_after.jpg')  