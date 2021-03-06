import argparse
from PIL import ImageOps
from PIL import Image
import os
import sys

def get_width_height(img):
    return img.size

def fillcrop(image, width = None, height = None):
    return ImageOps.fit(image, (width, height),
                        method = Image.ANTIALIAS, centering = (0.5, 0.5))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("imagepath", nargs = 1,
        help = "Path to image file")
    parser.add_argument('dim', nargs = 1,
        help = "[width]x[height]. Either is optional, e.g. [width]x or x[height]"
    )
    parser.add_argument('--output', '-o',
        help ='Path to output file, default is: input.crop.jpg' )


    # set up args
    args = parser.parse_args()
    imgpath = os.path.expanduser(args.imagepath[0])
    # open image
    img = Image.open(imgpath)
    # set up variables for the biggest crop
    cw, _o, ch = args.dim[0].partition('x')
    crop_width = int(cw) if cw else None
    crop_height = int(ch) if ch else None
    new_img = fillcrop(img, crop_width, crop_height)
    # save the file
    if not args.output:
       fn, ext = os.path.splitext(imgpath)
       nw, nh = get_width_height(new_img)
       outpath = '%s.crop.%sx%s%s' % (fn, nw, nh, ext)
    else:
        outpath = os.path.expanduser(args.output)
    ## TODO: Pillow save
    new_img.save(outpath)




