from moviepy.editor import *

def enhance_brightness(image):
    # image是一个三维数组
    # 红绿蓝分量都调整为1.3倍
    image_new = image*1.3
    # 把每个分量值都限制在255之内
    image_new[image_new>255] = 255
    return image_new

mp4_file = r'测试视频.mp4'
video = VideoFileClip(mp4_file)
(video.fl_image(enhance_brightness)
 .write_videofile(mp4_file[:-4]+'_new.mp4'))
