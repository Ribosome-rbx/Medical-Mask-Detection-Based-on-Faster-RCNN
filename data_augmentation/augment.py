import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import cv2
from pascal_voc_writer import Writer
import xml.etree.ElementTree as ET
import glob
from util import sequence
from util import annotation as an
import shutil
import sys

INPUT_DIR = '../data_augmentation/input'
OUTPUT_DIR = '../data_augmentation/output'
AUGMENT_SIZE = 4
num = 0

def main():
  filelist = glob.glob('%s/annotations/*.xml' % INPUT_DIR)
  _num = 0
  for file in filelist:
    _num += 1
    f_name = file.split('%s/annotations/' % INPUT_DIR)[-1].split('.')[0]
    print('Augmenting {}/{} Name: {}'.format(_num, len(filelist), f_name))
    annotation = an.parse_xml(file)
    augment(annotation)

  for file in glob.glob('%s/*.xml' % OUTPUT_DIR):
    an.inspect(file)


def augment(annotation):
  seq = sequence.get()

  for i in range(AUGMENT_SIZE):
    filename = annotation['filename']
    sp = filename.split('.')
    global num
    outfile_img = '%s/images/%s%d.%s' % (OUTPUT_DIR, 'maksssksksss', num, sp[-1])
    outfile_ann = '%s/annotations/%s%d.xml' % (OUTPUT_DIR, 'maksssksksss', num)
    num += 1

    seq_det = seq.to_deterministic()

    image = cv2.imread('%s/images/%s' % (INPUT_DIR, annotation['filename']))
    _bbs = []
    for obj in annotation['objects']:
      x1=int(obj['xmin'])
      y1=int(obj['ymin'])
      x2=int(obj['xmax'])
      y2=int(obj['ymax'])
      bb = ia.BoundingBox(x1,y1,x2,y2,label=obj['name'])
      if int((x2-x1)*(y2-y1)) > 0:
        _bbs.append(bb)

    bbs = ia.BoundingBoxesOnImage(_bbs, shape=image.shape)

    image_aug = seq_det.augment_images([image])[0]
    bbs_aug = seq_det.augment_bounding_boxes(
        [bbs])[0].remove_out_of_image().cut_out_of_image()

    writer = Writer(outfile_ann,
                    annotation['size']['width'],
                    annotation['size']['height'])
    count = len(bbs_aug.bounding_boxes)
    for bb in bbs_aug.bounding_boxes:
      bb.x1 = int(bb.x1)+1 if int(bb.x1) < 1 else int(bb.x1)
      bb.y1 = int(bb.y1)+1 if int(bb.y1) < 1 else int(bb.y1)
      bb.x2 = int(bb.x2)+1 if int(bb.x2) < 1 else int(bb.x2)
      bb.y2 = int(bb.y2)+1 if int(bb.y2) < 1 else int(bb.y2)
      if (bb.x2-bb.x1)*(bb.y2-bb.y1) > 0:
        writer.addObject(bb.label, bb.x1, bb.y1, bb.x2, bb.y2)
      else:
        print("augmentet boundingbox has non existing area. Skipping")
        count = count -1
        continue
      
    if count > 0:
      cv2.imwrite(outfile_img, image_aug)
      writer.save(outfile_ann)



if __name__ == '__main__':
    main()
