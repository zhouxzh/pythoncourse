import numpy as np
from scipy.io import wavfile

def fadeInOutMusic(srcMusicFile, dstMusicFile):
    # 读取WAV声音文件，返回采样频率与音乐数据
    # 二维数组musicData形状为(n,2)，每列表示一个声道
    sampleRate, musicData = wavfile.read(srcMusicFile)
    length = len(musicData)
    f = np.linspace(0, 1, length//10)
    # 系数，先越来越大，中间音量不变，最后再越来越小
    factors = np.concatenate((f, (1,)*(length-len(f)*2), f[::-1]))
    # 使用设置好的渐变系数调整音量大小
    musicData = np.int16(np.array(factors).reshape(-1,1) * musicData)
    # 写入结果文件
    wavfile.write(dstMusicFile, sampleRate, musicData)

fadeInOutMusic('北国之春.wav', 'result.wav')
