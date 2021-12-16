
- Perspective Transformation

```Python
pts1 # 4 points topLeft, bottomRight, topRight, bottomLeft
pts2 # 4 points topLeft, bottomRight, topRight, bottomLeft

matrix = cv2.getPerspectiveTransform(pts1, pts2)
src = cv2.warpPerspective(img, matrix, (width, height))
      # default : black background
      # add parameter `borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)` to fill white in background 
```
