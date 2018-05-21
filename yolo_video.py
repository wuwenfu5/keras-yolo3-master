from yolo import YOLO
from yolo import detect_video

if __name__ == '__main__':
    # video_path = '/media/wuwenfu5/Win_Ubuntu_Swap/Python_/Material/MyMOT/shitang7.AVI'
    video_path = 0
    detect_video(YOLO(), video_path)
