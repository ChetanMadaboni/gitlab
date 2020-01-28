from firebase import firebase

firebase=firebase.FirebaseApplication("https://jaltrack.firebaseio.com/",None)
data={
    'Name':'M.chetan',
    'Email':'cetanmadabony19@gmail.com',
    'Phone':'200'
   }
result=firebase.post('/jaltrack/pythonS',data)
print(result)
