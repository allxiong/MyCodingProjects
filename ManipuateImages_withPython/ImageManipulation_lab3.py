# make picture call
def set_Pic():
  return makePicture(pickAFile())

def halfRed():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 0.5)
  repaint(pic)
  
def newHalfRed():
  pic = set_Pic()
  #pixels = getPixels(pic)
  for x in range(0, getWidth(pic)/2):
    for y in range(getHeight(pic)/2, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      setRed(p, r * 0.5)
  repaint(pic)  
  writePictureTo(pic, 'D:\\MyDocuments\\ProfessionalDevelopment\\CollegeEducationCareer\\CSUMB\\CS205_Python_course_design\\images\\halfred_doggy.jpg')
  
def noBlue():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   setBlue(p, 0)
  repaint(pic)   
  
#Problem 1

def lessRed(pct):
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   r = getRed(p)
   if pct <= 100:
     setRed(p, r * pct / 100)
   else:  
     print "no change of red"
  repaint(pic)   
  
#Problem 2
def moreRed(pct):
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   r = getRed(p)
 if r * pct / 100 <= 255:
       setRed(p, r * pct / 100)
   else:  
     setRed(p, 255)
  repaint(pic)    
  
#Problem 3
#Hex Color and RGB Code for Rose pink, with Hex 
#Code #FF66CC and RGB code 255, 102, 204.   
def roseColoredGlasses():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   r = getRed(p)
   setRed(p, 255)
  repaint(pic)      
  
#Problem 4
def lightenUp():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
  repaint(pic)
  
#Problem 5
def makeNegative():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   r = getRed(p)
   r = 255 - r
   b = getBlue(p)
   b = 255 - b
   g = getGreen(p)
   g = 255 - g
   newColor = makeColor(r, g, b)
   setColor(p, newColor)
  repaint(pic)    
  
#Problem 6
def BnW():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   r = getRed(p)
   b = getBlue(p)
   g = getGreen(p)
   avg = (r + g + b)/3
   newColor = makeColor(avg, avg, avg)
   setColor(p, newColor)
  repaint(pic)      
  
def betterBnW():
  pic = set_Pic()
  pixels = getPixels(pic)
  for p in pixels:
   R = getRed(p)
   G = getBlue(p)
   B = getGreen(p)
   avg =  R*0.299 + G*0.587 + B*0.114
   newColor = makeColor(avg, avg, avg)
   setColor(p, newColor)
  repaint(pic)  

