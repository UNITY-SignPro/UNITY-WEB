import cv2
import csv
import time

STARTED_TIME = time.time()

data = list()
CSV_DF = {}
with open('./영상link합치기/human.csv', 'r', encoding='utf-8') as f:
    for word, link in list(csv.reader(f)):
        CSV_DF[word] = link

def video_output(words):
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (700, 466))
    for idx in range(len(words)) :
        cap = cv2.VideoCapture(CSV_DF[words[idx]])
        frame_pass = False if cap.get(cv2.CAP_PROP_FPS) < 30 else True; frame_cnt = 0
        while True:
            ret,frame = cap.read()
            frame_cnt += 1
            if not ret: break
            if frame_pass and frame_cnt % 2 == 1: continue
            out.write(frame)

video_output(['호박', '홍콩', '가마'])
ENDED_TIME = time.time()
print('Working Time: ', ENDED_TIME - STARTED_TIME)

