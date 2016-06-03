'''
Method to resize an image

To load an image:
  from scipy import misc
  arr = misc.imread('lena.png')
'''
from scipy import misc
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image
import time
from munkres import Munkres, print_matrix

PATCH_SIZE = 5
RESIZE_WIDTH = 20
RESIZE_HEIGHT = 20

def patchDistance(file1, file2):
  img1 = Image.open(file1)
  img2 = Image.open(file2)
  img1 = img1.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)
  img2 = img2.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)

  def distance(i1, j1, i2, j2):
    '''
    Compute the Euclidean distance of img1[i1:i1 + PATCH_SIZE, j1:j1 + PATCH_SIZE] and img2[i2:i2 + PATCH_SIZE, j2:j2 + PATCH_SIZE]
    '''
    rtn = 0.0
    for i in range(PATCH_SIZE):
      for j in range(PATCH_SIZE):
        for channel in range(3):
          rtn += (img1.getpixel((j1 + j, i1 + i))[channel] - img2.getpixel((j2 + j, i2 + i))[channel]) ** 2
    return np.sqrt(rtn)

  # Flatten the patches into an array
  # Coding:
  # (i, j) -> i * (n - PATCH_SIZE + 1) + j
  # Use a matrix of size (m - PATCH_SIZE + 1)(n - PATCH_SIZE + 1) x (m...)(n...) to store the pairwise distance of all patches
  rowSize = RESIZE_HEIGHT - PATCH_SIZE + 1
  colSize = RESIZE_WIDTH - PATCH_SIZE + 1
  flatSize = rowSize * colSize
  distanceMatrix = np.zeros((flatSize, flatSize))
  for idx1 in range(flatSize):
    i1, j1 = idx1 // colSize, idx1 % colSize
    sys.stdout.write('%s/%s\r' % (idx1, flatSize))
    for idx2 in range(flatSize):
      i2, j2 = idx2 // colSize, idx2 % colSize
      distanceMatrix[idx1, idx2] = distance(i1, j1, i2, j2)

  # Get the cost of minimum cost perfect matching
  matrix = distanceMatrix.tolist()
  m = Munkres()
  indexes = m.compute(matrix)
  total = sum([matrix[row][column] for row, column in indexes])
  print('Total cost: %d' % (total, ))
  return total
