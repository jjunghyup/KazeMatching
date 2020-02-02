import cv2
from image_compare import find_almost_similar_image_locations


def showimage(img_path, result):
    src = cv2.imread(img_path, cv2.IMREAD_COLOR)

    dst = src.copy()
    y0 = int(result['rectangle'][0][0])
    y1 = int(result['rectangle'][2][0])
    x0 = int(result['rectangle'][0][1])
    x1 = int(result['rectangle'][2][1])
    roi = src[x0:x1, y0:y1]

    cv2.imshow("dst", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test1():
    result = find_almost_similar_image_locations('search1.jpg', 'source.jpg')
    showimage('source.jpg', result)


def test2():
    result = find_almost_similar_image_locations('search2.jpg', 'source.jpg')
    showimage('source.jpg', result)


def test3():
    result = find_almost_similar_image_locations('search2.jpg', 'source.jpg', 0.6)
    showimage('source.jpg', result)
