```Python
pip install Pillow
from PIL import Image
```
- `Image.open("Image.jpg")`


- Convert pillow Image to numpy array  or numpy array to pillow Image
  - `np.array(img)` # pillow Image to numpy array
  - `Image.fromarray(img_array)` # numpy array to pillow Image



- Add Text on Image 
  ```Python
  font = "./fonts/FreeMono.ttf" # font location
  draw = ImageDraw.Draw(img) # img must be `Pillow Image`
  text = 'ADD TEXT'
  draw.text(position, text, color, font, align ="left") # position : xy coordinate tuple
  ```
