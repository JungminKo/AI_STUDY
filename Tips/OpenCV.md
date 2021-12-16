
- Perspective Transformation

```Python
pts1 # 4 points topLeft, bottomRight, topRight, bottomLeft
pts2 # 4 points topLeft, bottomRight, topRight, bottomLeft

matrix = cv2.getPerspectiveTransform(pts1, pts2)

# transform image
src = cv2.warpPerspective(img, matrix, (width, height))
      # default : black background
      # add parameter `borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)` to fill white in background 
      
# transform points
# points_array : shape : (n, 2) # x_point, y_point
transform_points = np.matmul(mtrx[:3, :2], point_array.T) + mtrx[:, 2][:,np.newaxis]
dst_points = np.array([transform_points[0]/transform_points[2], transform_points[1]/transform_points[2]]).T
```
