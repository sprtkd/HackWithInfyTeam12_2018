# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 09:01:43 2018

@author: supde
"""
import cv2
from pyzbar import pyzbar
import textwrap
import httpCall
import imutils
import time

class CameraObj:
    def __init__(self,source=0):
        load_image = cv2.imread('startup.png')
        load_image = imutils.resize(load_image, width=900)
        cv2.imshow("Welcome to Enrich", load_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.capObj = cv2.VideoCapture(source)
        self.currentData=None
        self.ProductDetails=None
         
    def __close(self):
        self.capObj.release()
        cv2.destroyAllWindows()
        
    def __returnVidFrame(self):
        ret, frame = self.capObj.read()
        frame = imutils.resize(frame, width=900)
        return frame
    
    def __QR_proc(self,frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            rectangleDim = barcode.rect
            barcodeData = barcode.data.decode("utf-8")
            frame = self.__drawARInfo(frame,barcodeData,rectangleDim)
            break
            
        cv2.imshow("Enrich App Client", frame)
        
        
    def __drawInfoOverlay(self,frame,rectangleDim):
        overlay = frame.copy()
        alpha = 0.75
        (x, y, w, h) = rectangleDim
        #draw a transparent white window
        Multiplier = 3
        NewWindowHt = h*Multiplier
        NewWindowWidth =  w*Multiplier
        CenterX = x+int(w/2)
        CenterY = y+int(h/2)
        
        x1 = CenterX - int(NewWindowWidth/2)
        y1 = CenterY - int(NewWindowHt/2)
        x4 = CenterX + int(NewWindowWidth/2)
        y4 = CenterY + int(NewWindowHt/2)
        
        cv2.rectangle(overlay, (x1, y1), (x4, y4), (240,240,240), -1)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha,	0, frame)
        
        borderOffset = 10
        
        cv2.rectangle(frame, (x1-borderOffset, y1-borderOffset), (x4+borderOffset, y4+borderOffset), (0,0,0), 1)
        newDim = (x1,y1,x4-x1,y4-y1)
        return frame,newDim
        
        
        
    def __drawInfoText(self,frame,rectangleDim, data):
        (x, y, w, h) = rectangleDim
        x=x+5
        wbase = 170
        lis=data.split("\n")
        
        display=""
        display+=textwrap.fill(lis[0], 30)+"\n"
        nLines=len(display.split("\n"))
        for i in range(1,len(lis)):
            display+=textwrap.fill(lis[i], 30)+"\n"
        
        #print(display)
        data = display.split('\n')
        
        y0=y + int(12*(w/wbase))
        dy = int(13*(w/wbase))
        i=0
        for line in data:
            line = line.title()
            y = y0 + i*dy
            if i<=nLines-2:
                cv2.putText(frame, line, (x, y ), cv2.FONT_HERSHEY_TRIPLEX, (w/wbase)*0.3, (0, 0, 0), 2)
            else:
                cv2.putText(frame, line, (x, y ), cv2.FONT_HERSHEY_DUPLEX, (w/wbase)*0.3, (0, 0, 0), 1)
            i=i+1
    
        return frame
        
    def __drawARInfo(self,frame,barcodeData,rectangleDim):
        frame,newDim = self.__drawInfoOverlay(frame,rectangleDim)
        if self.currentData==None or self.currentData!=barcodeData:
            self.currentData=barcodeData
            self.ProductDetails = httpCall.FormatBasicData(barcodeData)
            
        self.__drawInfoText(frame, newDim, self.ProductDetails)
        return frame
        
        
    def Mainloop(self):
        while True:
            self.__QR_proc(self.__returnVidFrame())
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        self.__close()

        


 
cb = CameraObj()
cb.Mainloop()

