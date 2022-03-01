# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Inder, Tanjodh
# Date: Dec,7,2020
# Description: Image processing and manipulating


import cmpt120imageProj
import numpy


# a function that inverts an image
def invert(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: inverts the pixels (colors)
  """

  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y] 
      pixel[0] = 255 - (pixel[0])
      pixel[1] = 255 - (pixel[1])
      pixel[2] = 255 - (pixel[2])
      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]
    
  return(pixels)  


#a function that flips an image horizontally
def flipHorizontal(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Flips the image along a vertical axis in the middle
  """
  
  pixel = cmpt120imageProj.createBlackImage(len(pixels),(len(pixels[0])))
  
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel[x][y] = pixels[x][y]
      pixel[x][y] = pixels[-x-1][y] 
   
  return(pixel)


#a function that flips an image vertically
def flipVertical(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Flips the image along a horizontal axis in the middle.
  """
  
  pixel = cmpt120imageProj.createBlackImage(len(pixels),(len(pixels[0])))
  
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel[x][y] = pixels[x][y]
      pixel[x][y] = pixels[x][-y-1] 
      
     
  return(pixel)


# a function that removes all the red pixels in an image
def red(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Takes out red channel, sets r value pixels to 0
  """ 
  
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      
      pixel[0] = 0
      pixel[1] = pixel[1]
      pixel[2] = pixel[2]

      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]
  
  return(pixels)  


#a function that removes all the green pixels in an image
def green(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Takes out green channel, sets g value pixels to 0
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      pixel[0] = pixel[0]
      pixel[1] =  0
      pixel[2] = pixel[2]
      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)  


# a function that removes all the blue pixels in an image
def blue(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Takes out blue channel, sets b value pixels to 0
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      pixel[0] = pixel[0]
      pixel[1] = pixel[1]
      pixel[2] = 0
      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)  


# a function that tints an image grey
def greyscale(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: turns pixels grey ( greyscales the image)
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      red = pixel[0] 
      green = pixel[1] 
      blue = pixel[2] 
      average = (red+blue+green)/3
      pixel[0] = int(average)
      
      pixel[1] = int(average)
      pixel[2] = int(average)
      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)  


#a function that tints an image brownish
def sepia(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Brown tints the pixels (image)
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      red = pixel[0] 
      green = pixel[1] 
      blue = pixel[2] 
      # Gets the sepia color of each rgb value
      SepiaRed = (red * .393) + (green *.769) + (blue * .189)
      if SepiaRed > 255:
        SepiaRed = 255
      
      
      SepiaGreen = (red * .349) + (green *.686) + (blue * .168)
      if SepiaGreen > 255:
        SepiaGreen = 255
      
      SepiaBlue = (red * .272) + (green *.534) + (blue * .131)
      if SepiaBlue > 255:
        SepiaBlue = 255
      # makes the pixels the sepia versions
      pixel[0] = SepiaRed
      pixel[1] = SepiaGreen 
      pixel[2] = SepiaBlue
      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)  


#a function that decreases the brightness of an image
def decrease_brightness(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Decreases brightness of image
  
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      # Decreases each pixel rgb value by 10 unitl 255 reached, once reached it stays the same
      pixel[0] = (pixel[0]) - 10
      if pixel[0] < 0:
        pixel[0] = 0
       
      pixel[1] = (pixel[1]) - 10
      if pixel[1] < 0:
        pixel[1] = 0

      pixel[2] = (pixel[2]) - 10
      if pixel[2] < 0:
        pixel[2] = 0

      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)  


#a function that increases the brightness of an image
def increase_brightness(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Increases brightness of image
  """
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      pixel = pixels[x][y]
      # Increases each pixel rgb value by 10 unitl 255 reached, once reached it stays the same
      pixel[0] = (pixel[0]) + 10
      if pixel[0] > 255:
        pixel[0] = 255
       
      pixel[1] = (pixel[1]) + 10
      if pixel[1] > 255:
        pixel[1] = 255

      pixel[2] = (pixel[2]) + 10
      if pixel[2] > 255:
        pixel[2] = 255

      pixels[x][y] = [pixel[0],pixel[1],pixel[2]]

  return(pixels)


# a function that rotates an image to the left
def RotateLeft(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Rotated pixels (image)
  """
  pixel = cmpt120imageProj.createBlackImage(len(pixels[0]),(len(pixels)))
  # makes a copy and then goes thorugh pixels flipping the copy and returning copy as orignal
  for x in range(len(pixel)):
    for y in range(len(pixel[0])):

      pixel[x][y] = pixels[y][x]
      pixel[x][y] = pixels[-y-1][x]

  return pixel
  return pixels 


# a function that rotates an image to the right
def RotateRight(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Rotated pixels (image)
  """
  pixel = cmpt120imageProj.createBlackImage(len(pixels[0]),(len(pixels)))
  # makes a copy and then goes thorugh pixels flipping the copy and returning copy as orignal
  for x in range(len(pixel)):
    for y in range(len(pixel[0])):

      pixel[x][y] = pixels[y][x]
      pixel[x][y] = pixels[y][-x-1]

  return pixel
  return pixels
  

#a function that pixelates an image
def pixelate(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: Replaces pixels with average of surrounding pixels
  """
  for x in range(0,(len(pixels)),4):
    for y in range(0,(len(pixels[0])),4):
      # Splits pixels into groups of 4x4
      red_av = 0
      green_av = 0
      blue_av = 0

      for w in range(4):
        for h in range(4):
          # goes through pixels individually adds the blurred verison
          red_av += pixels[x+w][y+h][0]
          green_av += pixels[x+w][y+h][1]
          blue_av += pixels[x+w][y+h][2]
        
      red_av = int(red_av/16)
      green_av = int(green_av/16)
      blue_av = int(blue_av/16)
      all_avg = [red_av, green_av, blue_av]

      for r in range(4):
        for t in range(4):
          # goes through and puts them all into an average
          pixels[x+r][y+t] = all_avg
  
  return pixels


# a function that turns an image black and white depending on its grey scale
def binarize(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: sets pixel to black or white depending on grey scale
  """
  
  threshold = 0
  total_pixel = 0

  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      # Greyscales the pixels
      pixel = pixels[x][y]
      red = pixel[0] 
      green = pixel[1] 
      blue = pixel[2] 
      average = (red+blue+green)/3
      
      pixels[x][y] = average
      # increases threshold of pixels by average of orignal pixels
      threshold += pixels[x][y]
      
      total_pixel += 1
  print(threshold)
  # get average threshold and goes through the height and width of the pixels
  # changes pixels of rgb values to either black or white depending on average thresh
  avg_threshold = (threshold/total_pixel)/2
  print(avg_threshold)
  for x in range(len(pixels)):
    for y in range(len(pixels[0])):
      if pixels[x][y] > avg_threshold:
        pixels[x][y] = [255,255,255]

      elif pixels[x][y] < avg_threshold:
        pixels[x][y] = [0,0,0]
  
  return pixels
