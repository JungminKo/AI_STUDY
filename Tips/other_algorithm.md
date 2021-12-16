## salt and pepper noise
```Python
def salt_pepper_noise(image, prob):
    '''
    Add salt and pepper noise to image
    image: Input image
    prob: Probability of the noise
    '''
    src = image.copy().astype('uint8')
    thres = 1-prob
    
    mask = np.random.rand(*img.shape[:2])
    src[mask<prob]=0
    src[mask>thres]=255
    
    return src
```
