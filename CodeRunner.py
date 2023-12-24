from model.face_detect_rectangle import detect_face
from model.face_mosaic import face_mosaic
from model.gray_scale import gray_scale
from model.outline_extraction import outline_extract
from model.yolo import modelpicture

def img_code_run(filename):

    filename = 'human.jpg'

    detect_face(filename)
    face_mosaic(filename)
    gray_scale(filename)
    outline_extract(filename)
    modelpicture(filename)

if __name__ == "__main__":
    img_code_run('human.jpg')