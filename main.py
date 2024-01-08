from inference_codeformer import start
import cv2

# img = cv2.imread('tests/t2.png', cv2.IMREAD_COLOR)
img = start('tests/t1.png')
cv2.imwrite('restored.png', img)
