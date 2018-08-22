import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999
s = socket.socket()

s.setsockopt( socket.SOL_SOCKET ,socket.SO_REUSEADDR , 0)
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=s
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
from sklearn import svm
from sklearn.model_selection import train_test_split

#Setting working directory
#os.chdir('C:/Users/admin/Desktop/')

#Reading the Analytical dataset
MasterAD= pd.read_excel('245_1.xlsx', sheet_name = 'Sheet1')
MasterAD = MasterAD.loc[:,['reviews_text','review_class']]

#Splitting Dataset in Train and Test 75:25
train, test = train_test_split(MasterAD, test_size=0.25, random_state = 21)

# Cleaning of text
def clean_text(text):
    text = re.sub(r"what's","what is ",text)
    text = re.sub(r"\'s"," ",text)
    text = re.sub(r"\'ve"," have ",text)
    text = re.sub(r"can't","cannot ",text)
    text = re.sub(r"n't"," not ",text)
    text = re.sub(r"i'm","i am ",text)
    text = re.sub(r"\'re"," are ",text)
    text = re.sub(r"\'d"," would ", text)
    text = re.sub(r"\'ll", " will ",text)
    text = re.sub(r"\ 'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

#Apply the above function to both train and  test dataset 
cleaned_train_comment = []
TrainDataKeys = list(train['reviews_text'].keys())
for i in TrainDataKeys:
    cleaned_comment = clean_text(str(train['reviews_text'][i]))
    cleaned_train_comment.append(cleaned_comment)
train['reviews_text'] = pd.Series(cleaned_train_comment).astype(str)

cleaned_test_comment = []
TestDataKeys = list(test['reviews_text'].keys())
for i in TestDataKeys :
    cleaned_comment = clean_text(str(test['reviews_text'][i]))
    cleaned_test_comment.append(cleaned_comment)
test['reviews_text'] = pd.Series(cleaned_test_comment).astype(str)

#Dependent variables of train and test datset
X=train.reviews_text
test_X=test.reviews_text

# Instantiate TfidfVectorizer
vect = TfidfVectorizer(max_features=20000,stop_words='english')
# learn the vocabulary in the train and test data, then use it to create a document-term matrix
X_dtm = vect.fit_transform(X.values.astype(str))
test_X_dtm = vect.transform(test_X.values.astype(str))

#SUPPORT VECTOR MACHINE (LINEAR KERNEL)

#model = LogisticRegression(C=4.0)
#model = LinearSVC(random_state=0)
model = svm.SVC(kernel='linear',probability = True)
y = train['review_class']
y_test = test['review_class']
# train the model using X_dtm & y
model.fit(X_dtm, y)

'''
# compute the training accuracy
y_pred_X_train = model.predict(X_dtm)
print('Training accuracy is {}'.format(accuracy_score(y,y_pred_X_train)))

#compute test accuracy
y_pred_X_test = model.predict(test_X_dtm)
print('Testing accuracy is {}'.format(accuracy_score(y_test,y_pred_X_test)))
'''

print( 'Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    request=request.decode()
    test_comment=vect.transform([request])
    comment_polarity = model.predict_proba(test_comment).tolist()
    review_rating = (comment_polarity[0][1])*10

    print( 'Received {}'.format(request))
    sendtext=str(review_rating).encode()
    client_socket.send(sendtext)
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print( 'Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()
