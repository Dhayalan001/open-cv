import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\HP\AppData\Local\Temp\tmp8ix9x61m.PNG')
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')
plt.axis('off')
plt.show()
