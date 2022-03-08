### image read / write 
```Python
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR) # cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED (alpha channel 까지 읽음)
cv2.imwrite('lena.jpg', img)
```
- convert color
```Python
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2RGB
```

- resize 
```Python
# 이미지를 확대할 때는 cv2.INTER_CUBIC, cv2.INTER_AREA
# 이미지를 축소할 때는 cv2.INTER_AREA
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA) 
```
- thresholding
```Python
# Simple thresholding 
ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# adaptive thresholding
## two filter options : mean / gaussian
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,15,2)
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,15,2)

# Otsu's thresholding
## using in bimodal image
### biomodal image : 픽셀에 대한 히스토그램 그리면 2개의 peak가 있는 이미지
ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


```
### Transformation

- Perspective Transformation

```Python
pts1 # 4 points array(dtype:float32) topLeft, bottomRight, topRight, bottomLeft, 
pts2 # 4 points array(dtype:float32) topLeft, bottomRight, topRight, bottomLeft

matrix = cv2.getPerspectiveTransform(pts1, pts2)

# transform image
src = cv2.warpPerspective(img, matrix, (width, height))
      # default : black background
      # add parameter `borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)` to fill white in background 
      
# transform points
# points_array : shape : (n, 2) # x_point, y_point
# https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87 : warpPerspective()
transform_points = np.matmul(mtrx[:3, :2], point_array.T) + mtrx[:, 2][:,np.newaxis]
dst_points = np.array([transform_points[0]/transform_points[2], transform_points[1]/transform_points[2]]).T
```

### FindContours

- `cv2.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)` : find_contour [pactice](https://github.com/JungminKo/AI_STUDY/blob/main/Others_notes/FindRect_Practice.md)
  - return : image, contours, hierarchy     
- `cv2.boundingRect(contour)` : Calculates the **up-right bounding rectangle** of a point set  _# angle is not considered_
  - return : min_x, min_y, w, h     
- `cv2.minAreaRect(contour)` : Finds a **rotated rectangle of the minimum** area enclosing the input 2D point set 
  - return : center, size, angle 
- `cv2.contourArea(contour)` : find size 

- `cv2.boxPoints(rect)` : Finds the four vertices of a rotated rect 


### Corner Detection
- Harris Corner Detection
```Python
corner = cv.cornerHarris(gray,2,3,0.04)
coord = np.where(corner > 0.5* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
```

### Extra
- `cv2.Laplacian(image, cv2.CV_64F).var()` : blur detection
