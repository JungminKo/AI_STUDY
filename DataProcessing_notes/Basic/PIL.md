```Python
pip install Pillow
from PIL import Image
```
- `Image.open("Image.jpg")`
- `Image.new("L", (width, height))` # RGB : color, L : grayscale
- `img.size` # (600, 400)
- `img.save('./output.png', 'png')`

- Convert pillow Image to numpy array  or numpy array to pillow Image
  - `np.array(img)` # pillow Image to numpy array
  - `Image.fromarray(img_array)` # numpy array to pillow Image

- change color channels
  ```Python
    # split pillow Image to 3 channels 
    r, g, b = img.split()
    
    # increase reds
    r = r.point(lambda i: i*1.2)
    
    # decrease greens
    g = g.point(lambda i: i*0.9)
    
    # recombine back to RGB image
    new_img = Image.merge('RGB', (r, g, b))
  ```
- set unifrom transparency : `img.putalpha(128)` 
   - _caution_ : it overwrites the original image / change type of the image to RGBA


- rotate : `img.rotate(angle, resample=2, expand=True, fillcolor=(255,255,255))`



- Add Text on Image ; [Official Link](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html)
  ```Python
  font = "./fonts/FreeMono.ttf" # font location
  draw = ImageDraw.Draw(img) # img must be `Pillow Image`
  text = 'ADD TEXT'
  draw.text(position, text, fill=None, font, align ="left") # position : xy coordinate tuple # fill: color
  ```
