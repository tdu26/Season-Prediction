# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:49:50 2016

@author: Yijin
"""
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
#from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
#from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV
#import sys

def create_training_and_testing():
    r = open('dataToDo.txt')
    count = 0
    for i in r:
        count += 1
    num_train = int(0.7 * count) 
    #num_test = count - num_train
    r.close()
    r = open('dataToDo.txt')
    train = open('train.txt', 'w')
    test = open('test.txt', 'w')
    count = 0
    for i in r:
        if count <= num_train:
            train.write(i)
            count+=1
        else:
            test.write(i)

number_of_line = 30000
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    count=0
    for line in f:
        if count > number_of_line:
            break
        season, resturant_type, review =line.strip().split('\t\t')
        resturant_type = re.sub(' ','_',resturant_type)
        resturant_type = resturant_type.split('#$#')
        resturant_type = ' '.join(resturant_type)
        #the review contains resturants' types
        review = resturant_type + ' ' + review
        reviews.append(review.lower())    
        labels.append(season)
        count+=1
    f.close()
    #print(count)
    return reviews,labels 

if __name__ == "__main__":
    #create_training_and_testing()
    #the review contains resturants' types
    train_reviews, train_labels = loadData('train.txt')
    test_reviews, test_labels = loadData('test.txt')
    #sys.exit()
    print('dataload completed')
    counter = CountVectorizer()
    counter.fit(train_reviews)
    #count the number of times each term appears in a document and transform each doc into a count vector
    counts_train = counter.transform(train_reviews)#transform the training data
    counts_test = counter.transform(test_reviews)#transform the testing data
    #print(counts_train)
    # You can find more in gridSearch.py in Canvas week10 
    # Code for reference(Auto tuning), KNN:
    # Change the code here begin:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    param_grid = [
    {'n_neighbors': [13],'weights':['uniform','distance']}
    ]
    #build a grid search to find the best parameters
    #http://scikit-learn.org/stable/modules/grid_search.html
    #http://scikit-learn.org/stable/supervised_learning.html
    clf = GridSearchCV(KNeighborsClassifier(), param_grid, cv=2)
    # Change the code  end:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    
    #run the grid search
    print('predication start')
    clf.fit(counts_train, train_labels)  
    
    #get the best parameters 
    best_paras = clf.best_params_
    print("\nBest parameters",clf.best_params_)

    #change the code here end
    clf.fit(counts_train, train_labels)
    print('predict line')
    pred=clf.predict(counts_test)

    #KNN=KNeighborsClassifier(n_neighbors=clf.best_params_['n_neighbors'],weights=clf.best_params_['weights'])
    #KNN.fit(counts_train,train_labels)
    #use the classifier to predict
    #pred=KNN.predict(counts_test)  
    
    #get the best prediction results:
    print('getting score')
    pred_results = accuracy_score(pred,test_labels)
    learnname = 'KNN'    #Change the name Here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    pred_and_paras = open('result/'+learnname + 'pred_and_paras.txt', 'w')
    strs = 'learner: ' +  learnname + ' accuracy is ' + str(pred_results) + '\n' + 'The paras are ' + str(best_paras) + '\n'
    pred_and_paras.write(strs)
    pred_and_paras.close()
        
    prediction = open('result/'+learnname + 'prediction.txt', 'w')
    pred = '\n'.join(pred)
    prediction.write(pred)
    prediction.close()
    
    actual = open('result/'+'actual.txt', 'w')
    test_labels = '\n'.join(test_labels)
    actual.write(test_labels)
    actual.close()
    print('done')
