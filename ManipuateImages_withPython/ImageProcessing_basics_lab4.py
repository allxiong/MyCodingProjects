#Multimedia programming with Python lab 4 
#warmup
def half_better():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)):
    for y in range(getHeight(pic)/2, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      setRed(p, r*0.5)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\half_better.jpg')     

#problem 1    
def lr_mirror():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)):
      p =getPixel(pic, x, y)
      c = getColor(p)
      p1 = getPixel(pic, getWidth(pic)-x-1, y)
      setColor(p1,c)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\lr_mirror.jpg') 
      
def updown_mirror():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      p =getPixel(pic, x, y)
      c = getColor(p)
      p1 = getPixel(pic, x, getHeight(pic)-1-y)
      setColor(p1,c)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\updown_mirror.jpg')  
  
def downup_mirror():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)):
    for y in range(getHeight(pic)/2, getHeight(pic)):
      p =getPixel(pic, x, y)
      c = getColor(p)
      p1 = getPixel(pic, x, getHeight(pic)-1-y)
      setColor(p1,c)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\downup_mirror.jpg')           
  
def quadruple():
  pic = makePicture(pickAFile())
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)/2):
      p = getPixel(pic, x, y)
      c = getColor(p)
      p1 = getPixel(pic, x, getHeight(pic)-1-y)
      p2 = getPixel(pic, getWidth(pic)-1-x, y)
      p3 = getPixel(pic, getWidth(pic)-1-x, getHeight(pic)-1-y)
      setColor(p1,c)
      setColor(p2,c)
      setColor(p3,c)
  repaint(pic)
  writePictureTo(pic, 'C:\\Users\\allie\\PythonCode\\images\\downup_mirror.jpg')                 