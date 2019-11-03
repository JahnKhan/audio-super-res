'''
This file is for runs tests.
'''

import sys, os
from subprocess import call
import shlex
import  _pickle as cPickle


sizes = ['8192']
models = ['audiounet']
rs =['4']
pool_size = '8'
pool_stride = '8'

for model in models:
    for size in sizes:
        for r in rs:
            stride = str(int(size)/2)
            #trainstr = '../piano/interp/piano-interp-train.' +r+'.16000.'+size+'.'+stride+'.0.1.h5'
            #valstr = '../piano/interp/piano-interp-val.' +r+'.16000.'+size+'.'+stride+'.0.1.h5'
            #trainstr = '../data/vctk/speaker1/vctk-speaker1-train.8.16000.-1.4096'
            #valstr = '../data/vctk/speaker1/vctk-speaker1-val.8.16000.-1.4096'
            trainstr = '../data/vctk/speaker1/vctk-speaker1-train.'+r+'.16000.' + size + '.' + stride + '.h5'
            valstr = '../data/vctk/speaker1/vctk-speaker1-val.'+r+'.16000.' + size + '.' + stride + '.h5'
            command = 'python run.py train --train ' + trainstr + ' --val ' + valstr + ' -e 50 --batch-size 8 --lr 3e-4 --layers 4 --epochs 1 --piano false  --logname full_end_normalized_parmas_ps'+pool_size+'.s'+pool_stride+'-'+model+'.lr0.00300.1.g4.b32.d'+size+'.r'+r+' --model ' + model + ' --r ' + r + ' --pool_size ' + pool_size + ' --strides ' + pool_stride 
            print(command)
            call(shlex.split(command))


            #ython run.py train --train ../data/vctk/speaker1/vctk-speaker1-train.8.16000.-1.4096
            #  --val ../data/vctk/speaker1/vctk-speaker1-val.8.16000.-1.4096
            #  -e 50 --batch-size 8 --lr 3e-4 
            #  --layers 4
            #  --piano false 
            #  --logname full_end_normalized_parmas_ps8.s8-audiounet.lr0.00300.1.g4.b32.d8192.r8
            #  --model audiounet --r 8 --pool_size 8 --strides 8



#  python run.py train --train ../data/vctk/speaker1/vctk-speaker1-train.4.16000.8192.4096.h5 
            #  --val ../data/vctk/speaker1/vctk-speaker1-val.4.16000.8192.4096.h5
            #   -e 120 --batch-size 64 --lr 3e-4 
            #  --logname singlespeaker           
