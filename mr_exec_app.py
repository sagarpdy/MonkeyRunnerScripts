reated on Mar 18, 2013

@author: aaa
'''
from com.android.monkeyrunner import MonkeyRunner as mr,MonkeyDevice as md
import os
import sys

cate_name=["全部","居家","配饰","鞋包","数码家电"]
cate_x=[80,160,240]
cate_y=[100,160,220,280]


def startApp(d):
    my_pack="com.test"
    my_act=".activities.SplashActivity"
    my_compon=my_pack+'/'+my_act
    d.startActivity(component=my_compon)
    mr.sleep(10)

def screenShot(d):
    result1=d.takeSnapshot()
    result1.writeToFile("zhe_image/st1.png","png")
    
def changeCategory(d):
    ''' Open category selection list '''
    #d.touch(160,50,md.DOWN_AND_UP)
    k=1
    rect=(80,30,150,30)
    mr.sleep(3)
    for i in xrange(3):
        for j in xrange(4):
            if i*j==6:
                print i,j
                break
            d.touch(160,50,md.DOWN_AND_UP)
            mr.sleep(2)
            d.touch(cate_x[i],cate_y[j],md.DOWN_AND_UP)
            mr.sleep(3)
            img=d.takeSnapshot().getSubImage(rect)
            img.writeToFile("zhe_image/shot%d.png"%k,"png")
            k+=1
            print "K is "+str(k)
           
                           
def execCommand(d): 
    print "Start execute command"
    command="python compare_image.py" 
    #command="ls -l"
    os.system(command) 
 
def main():
    device=mr.waitForConnection()
    if not device:
        print "Device is not found!"
        sys.exit()
    else:
        print "Device is connected!"
        
    startApp(device)
    screenShot(device)
    changeCategory(device)
    execCommand(device)
    

if __name__=="__main__":
    main()
