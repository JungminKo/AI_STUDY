### Crop images
- crop images given 4 points of image (lefttop, righttop, rightbottom, leftbottom)

```Python
def crop_img(img, polygon):
    minX, minY = polygon.min(axis=0)
    maxX, maxY = polygon.max(axis=0)

    width = int(max (np.linalg.norm(polygon[0]-polygon[1]), 
                   np.linalg.norm(polygon[2]-polygon[3])))

    height = int(max (np.linalg.norm(polygon[1]-polygon[2]), 
                   np.linalg.norm(polygon[0]-polygon[3])))

    polygonStrecth = np.float32([[0,0],[width,0],
                                 [width,height], [0,height]])

    polygonForTransform = polygon - np.array((minX, minY))

    finalImage = img[minY:maxY,minX:maxX]


    # affine transform
    M = cv2.getPerspectiveTransform(np.asarray(polygonForTransform).astype(np.float32), 
                                    np.asarray(polygonStrecth).astype(np.float32))

    # Warp one image to the other
    warpedImage = cv2.warpPerspective(img, M, (finalImage.shape[1], finalImage.shape[0]))

    return warpedImage
```
