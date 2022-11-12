import cv2
import sys
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
        if word == x :
            new_list.append(y)

link('ㄱ')
link('가다')
link('가마')

def video_output() :
    for i in range(len(new_list)) :
        cap = cv2.VideoCapture(new_list[i])

        if not cap.isOpened() :
            sys.exit
    
        frame_cnt = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        effect_frames = int(fps)

        delay = int(1000/fps)

        w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'DIVX')    
        out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

        while True :
            ret,frame = cap.read()

            if not ret :
                break
    
            cv2.imshow('frame',frame)
            cv2.waitKey(delay)
            out.write(frame)

video_output()

