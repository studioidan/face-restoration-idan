from inference_codeformer import start
import cv2
import time


# img = cv2.imread('tests/t2.png', cv2.IMREAD_COLOR)
start_time = time.time()
img = start('t1.png')
cv2.imwrite('restored.png', img)
print(f'job done {int(time.time() - start_time)} secs')

