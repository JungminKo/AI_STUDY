1. draw contours satisfying condition that the size of rotated rectangle containing contour is greater than given size
2. find the largest contour and transform raw image into contour image 

```Python
image = cv2.imread(image_path)
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## Filter can be added here
## laplacian = cv2.Laplacian(imgray, cv2.CV_8U, ksize=5)

_, thr = cv2.threshold(imgray,100,255,cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# 1. draw contours
lbd = imgray.size//2
iou = []
for contour in contours:
    center, size, angle = cv2.minAreaRect(contour)
    if size[0]*size[1] > lbd:
        iou.append((center, size, angle))

for rect in iou:
    box = cv2.boxPoints(rect)
    box = box.astype('int')
    image = cv2.drawContours(image, [box], -1, (255, 0, 0), 5) 
    
# 2. perspective transformation
max_size = 0
rect = None
for contour in contours:
    center, size, angle = cv2.minAreaRect(contour)
    if size[0]*size[1] > max_size:
        max_size = size[0]*size[1]
        rect = (center, size, angle)
       
box = cv2.boxPoints(rect)
if rect[2]>0 and rect[2]<45:
    box = np.roll(box,-2)

width = int(np.linalg.norm(box[0] - box[1])) # image.shape[1]
height = int(np.linalg.norm(box[1]- box[2])) # image.shape[0]

pts1 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(box, pts1)

src = cv2.warpPerspective(image, matrix, (width, height))
plt.figure(figsize=(18,8))
plt.imshow(src)

```
