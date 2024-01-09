from inference_codeformer import start
import cv2
import time



start_time = time.time()
img = start('t1.png')
cv2.imwrite('restored.png', img)
print(f'job done {int(time.time() - start_time)} secs')


start_time = time.time()
img = cv2.imread('tests/t2.png', cv2.IMREAD_COLOR)
img2 = start('t1.png')
cv2.imwrite('restored2.png', img2)
print(f'job done {int(time.time() - start_time)} secs')


