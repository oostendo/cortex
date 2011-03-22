import logging
import redis
import json
import freenect
import cv
import SimpleCV as scv
import numpy as np

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from cortex.lib.base import BaseController, render

log = logging.getLogger(__name__)
rd = redis.Redis(host='localhost', port=6379, db=0)

class FrameController(BaseController):

  def index(self):
    response.headers['Content-type'] = 'image/jpeg'
    response.headers['Cache-Control'] = 'max-age=14400'
    response.headers['Pragma'] = ''

    c = scv.Camera()
    img = c.getImage()

    h = img.histogram()
    rd.set("histogram", json.dumps(h))
    img.save("/dev/shm/img1.jpg") 
    image_file = open("/dev/shm/img1.jpg", 'r')
    return image_file.read()
    

  def kinect(self):
    response.headers['Content-type'] = 'image/jpeg'
    response.headers['Cache-Control'] = 'max-age=14400'
    response.headers['Pragma'] = ''

    img = scv.Image(self._get_video())
    depth = scv.Image(self._get_depth())
    h = img.histogram()
    rd.set("histogram", json.dumps(h))
    
    img.save("/dev/shm/img1.jpg") 
    image_file = open("/dev/shm/img1.jpg", 'r')

    return image_file.read()

  def _hist(self, i):
    (hist, bin_edges) = np.histogram(np.asarray(cv.GetMat(i)), bins=50)
    rd.set("histogram", json.dumps(hist.tolist()))

  def _get_depth(self):
    return self._pretty_depth_cv(freenect.sync_get_depth()[0])

  def _get_video(self):
    return self._video_cv(freenect.sync_get_video()[0])



  def _pretty_depth(self,depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        A numpy array that has been processed whos datatype is unspecified
    """
    np.clip(depth, 0, 2**10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth


  def _pretty_depth_cv(self,depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        An opencv image who's datatype is unspecified
    """
    import cv
    depth = self._pretty_depth(depth)
    image = cv.CreateImageHeader((depth.shape[1], depth.shape[0]),
                                 cv.IPL_DEPTH_8U,
                                 1)
    cv.SetData(image, depth.tostring(),
               depth.dtype.itemsize * depth.shape[1])
    return image


  def _video_cv(self,video):
    """Converts video into a BGR format for opencv

    This is abstracted out to allow for experimentation

    Args:
        video: A numpy array with 1 byte per pixel, 3 channels RGB

    Returns:
        An opencv image who's datatype is 1 byte, 3 channel BGR
    """
    import cv
    video = video[:, :, ::-1]  # RGB -> BGR
    image = cv.CreateImageHeader((video.shape[1], video.shape[0]),
                                 cv.IPL_DEPTH_8U,
                                 3)
    cv.SetData(image, video.tostring(),
               video.dtype.itemsize * 3 * video.shape[1])
    return image

