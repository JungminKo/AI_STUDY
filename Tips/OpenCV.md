
- Perspective Transformation

```Python
pts1 # 4 points
pts2 # 4 points

matrix = cv2.getPerspectiveTransform(pts1, pts2)
src = cv2.warpPerspective(img, matrix, (width, height))
      # default : black background
      # add parameter `borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)` to fill white in background 
```
