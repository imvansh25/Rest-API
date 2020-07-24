import pyrebase
config = {
	"apiKey": "AIzaSyCp3jtcln4foYgcd-vR0zgXRIDFKrMz2UY",
    "authDomain": "picameme-3c3a9.firebaseapp.com",
    "databaseURL": "https://picameme-3c3a9.firebaseio.com",
    "projectId": "picameme-3c3a9",
    "storageBucket": "picameme-3c3a9.appspot.com",
    "messagingSenderId": "727804947779",
    "appId": "1:727804947779:web:7caa6214c0f4ecfdbcd3f6",
    "measurementId": "G-HYHTPVCW43"
    }

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def upload(path_on_cloud,path_local):
	storage.child(path_on_cloud).put(path_local)

def download(path_on_cloud,path_local):
	storage.child(path_on_cloud).download(path_local)

def get_url(path_on_cloud):
	return storage.child(path_on_cloud).get_url(None)