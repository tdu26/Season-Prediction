
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 17:40:32 2016

@author: Yijin
"""
import json
from datetime import date
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('ascii')
#r=open('yelp_academic_dataset_review.json')
#t=open('reviewsample.txt', 'w')
#r=open('yelp_academic_dataset_business.json')
#t=open('businessample.txt', 'w')
#r=open('yelp_academic_dataset_checkin.json')
#t=open('checkinsample.txt', 'w')
#r=open('yelp_academic_dataset_tip.json')
#t=open('tipsample.txt', 'w')
#r=open('yelp_academic_dataset_user.json')
#t=open('usersample.txt', 'w')
#strs = ""
#k = 0
#for i in r:
#    k = k + 1
#    strs = strs + str(i) + '\n'
#    if k >= 11:
#        break;
#t.write(strs[0:-1])
#r.close()
#t.close()
#reference from stack overflow : http://stackoverflow.com/questions/16139306/determine-season-given-timestamp-in-python-using-datetime/24582617#24582617

Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]


def get_season(time):
    y,m,d = time.split('-')
    y = int(y)
    m = int(m)
    d = int(d)
    time = date(y,m,d)
    time = time.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= time <= end)

def read_bussiness(line):
    j = json.loads(line)
    business_id = j["business_id"]
    categories = j["categories"]
    return business_id, categories
    
def createResturantBusiness():
    r=open('yelp_academic_dataset_business.json')
    t=open('resturantBusiness.json', 'w')
    for i in r:
        business_id, categories = read_bussiness(i)
        strs = ""
        flag = False
        for item in categories:
            if item == "Restaurants":
                flag = True
            else:
                strs = strs + item + "#$#"
        strs = strs[0:-3]
        if flag and len(strs) > 1:
            t.write(str(business_id) + "\t" + strs + "\n")
    r.close()
    t.close()
    print "done"

def buildBussinessMap():
    r=open('resturantBusiness.json')
    m = {}    
    for i in r:
        ID, categories = i.split('\t')
        m[ID] = categories.strip()
    r.close()
    return m

def readResturantReview(m):
    r=open('reviewsample.txt')
    t=open('reviewsampleresturantparsed.txt', 'w')
    #r=open('yelp_academic_dataset_review.json')
    #t=open('resturant_and_season_clearndata.txt', 'w')
    for i in r:
        j = json.loads(i)
        business_id = j["business_id"]
        #text = j["text"]
        text = i.split(", \"text\": \"")[1].split("\", \"type\"")[0]
        time = j["date"]
        if business_id in m:
            season = get_season(time)
            strs = season+ '\t\t' + m[business_id] + '\t\t' + text + "\n"
            try:
                t.write(strs)
            except:
                print "ignore"
    r.close()
    t.close()
    print "done"

def createSample():
    r=open('resturant_and_season_clearndata.txt')
    t=open('datasample.txt', 'w')
    strs = ""
    k = 0
    for i in r:
        k = k + 1
        strs = strs + str(i)
        if k >= 101:
            break;
    t.write(strs[0:-1])
    r.close()
    t.close()

if __name__=="__main__":
    #createResturantBusiness()
    #m = buildBussinessMap()
    #readResturantReview(m)
    createSample()
    print "completed"
