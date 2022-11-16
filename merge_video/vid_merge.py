import cv2
import numpy as np
import sys
from link_merge import link
import csv

data = list()
f=open('human.csv','r')
rea=csv.reader(f)
for row in rea:
    data.append(row)
f.close

new_list =[]

def link(word) :
    for x,y in data :
        if word in x :
            new_list.append(y)


link('ㄱ')
link('가나')


cap1 = cv2.VideoCapture(new_list[0])
cap2 = cv2.VideoCapture(new_list[1])

if not cap1.isOpened() or not cap2.isOpened():
	sys.exit()
    
    
#각 영상 프레임 수
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps*2)

delay = int(1000/fps)

#영상 가로 세로 설정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

#비디오 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

#1번 영상 열기
for i in range(frame_cnt1 -effect_frames) :
    ret1,frame1 = cap1.read()

    if not ret1 :
        break
    
    out.write(frame1)
    cv2.imshow('frame',frame1)
    cv2.waitKey(delay)
    
#합성하기
for i in range(effect_frames) :
    ret1,frame1 = cap1.read()
    ret2,frame2=cap2.read()

    alpha = 1.0 - i /effect_frames
    frame = cv2.addWeighted(frame1,alpha,frame2,1-alpha,0)
    out.write(frame)

for i in range(effect_frames,frame_cnt2) :
    ret2,frame2=cap2.read()

    if not ret2 :
        break

    out.write(frame2)
    cv2.imshow('frame',frame2)
    cv2.waitKey(delay)