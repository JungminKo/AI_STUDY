

## BasicIoU
## Not Consider the angle of rectangles
def basic_iou(rect1, rect2) : 
    '''
    Input : rect1 -> tuple (center_x, center_y, width, height)
            rect2 -> tuple (center_x, center_y, width, height)

    Output : iou
    '''
    rect1_center_x, rect1_center_y, rect1_width, rect1_height = rect1
    rect2_center_x, rect2_center_y, rect2_width, rect2_height = rect2

    rect1_x1 = rect1_center_x - rect1_width//2
    rect1_y1 = rect1_center_y - rect1_height//2 
    rect1_x2 = rect1_x1 + rect1_width
    rect1_y2 = rect1_y1 + rect1_height

    rect2_x1 = rect2_center_x - rect2_width//2
    rect2_y1 = rect2_center_y - rect2_height//2 
    rect2_x2 = rect2_x1 + rect2_width
    rect2_y2 = rect2_y1 + rect2_height

    inter_x1 = max(rect1_x1, rect2_x1)
    inter_y1 = max(rect1_y1, rect2_y1)
    inter_x2 = min(rect1_x2, rect2_x2)
    inter_y2 = max(rect1_y2, rect2_y2)

    inter_width = max(inter_x2 - inter_x1, 0)
    inter_height= max(inter_y2 - inter_y1, 0)

    inter_area = inter_width * inter_height

    rect1_area = rect1_width * rect1_height
    rect2_area = rect2_width * rect2_height
    union_area = rect1_area + rect2_area - inter_area

    iou = inter_area/union_area

    return iou


## Non maximum Suppression
# tf.image.non_max_suppression() https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression
# torchvision.ops.batched_nms() https://pytorch.org/vision/stable/ops.html