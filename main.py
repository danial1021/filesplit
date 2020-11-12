import math

def splitFile(fileData):
  n = math.ceil(len(fileData)/4)
  return [fileData[i:i+n] for i in range(0, len(fileData), n)]