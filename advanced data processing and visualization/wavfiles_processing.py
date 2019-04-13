# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:32:31 2018

@author: bxu601
"""

import scipy.io.wavfile
import wave
import matplotlib.pyplot
import matplotlib.pylab
import urllib.request
import numpy

response = urllib.request.urlopen('http://www.nch.com.au/acm/11k16bitpcm.wav')
WAV_FILE = 'english.wav'
file = open(WAV_FILE, 'wb+')
file.write(response.read())
file.close()
wavefile = wave.open(WAV_FILE,'r')
params = wavefile.getparams()
nchannels, sample_width, framerate, numframes = params[:4]
sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
matplotlib.pyplot.subplot(2,1,1)
matplotlib.pyplot.title('Original')
matplotlib.pyplot.plot(data)
newdata = data * 0.2
newdata = newdata.astype(numpy.int16)
scipy.io.wavfile.write('silent.wav', sample_rate, newdata)
matplotlib.pyplot.subplot(2,1,2)
matplotlib.pyplot.title('Quiet')
matplotlib.pyplot.plot(newdata)
matplotlib.pyplot.show()
result = matplotlib.pylab.specgram(newdata, NFFT=1024, Fs = sample_rate, noverlap=900)
#y:音频信号
#NFFT：每个进行快速傅里叶变换的数据块大小，一般取2的幂次
#Fs:采样率
#noverlap：数据块之间重叠数据点的个数

matplotlib.pylab.show()


'''

#注：Python的wave模块也可以实现相应的wav文件读取，示例代码如下：

wavefile = wave.open(WAV_FILE,'r')
params = wavefile.getparams()
nchannels, sample_width, framerate, numframes = params[:4]
#nchannels:声道数
#sample_width:采样宽度,每个采样的字节数
#framerate:采样率
#numframes:总采样数

y_data = wavefile.readframes(numframes)
y = numpy.fromstring(y_data, dtype=numpy.int16)
result = matplotlib.pylab.specgram(y, NFFT=1024, Fs = framerate, noverlap=900)
'''