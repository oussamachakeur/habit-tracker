import requests
from datetime import datetime 

today = datetime.now()


endpoint='https://pixe.la/v1/users'
graph_endpoint= "https://pixe.la/v1/users/aubameyang/graphs"
pixel_endpoint= "https://pixe.la/v1/users/aubameyang/graphs/oussama5699"
update_endpoint=f"https://pixe.la/v1/users/aubameyang/graphs/oussama5699/{today.strftime('%Y%m%d')}"
delete_endpoint=f"https://pixe.la/v1/users/aubameyang/graphs/oussama5699/{today.strftime('%Y%m%d')}"

user_param={
    "token":"oussamaalgeria", 
    "username":"aubameyang",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

graph_param={
    "id": "oussama5699",
    "name":"Habit Tracker",
    "unit": "commit",
    "type":'int',
    "color":"sora"

}

headers={
    "X-USER-TOKEN": "oussamaalgeria",

}

pixel_param={
    "date": today.strftime("%Y%m%d"),
    "quantity":"1",
}


update_param={
    "quantity":"23"
}



respons1=requests.post(url=endpoint , json=user_param)
respons2=requests.post(url=graph_endpoint , json= graph_param , headers=headers)
respons3=requests.post(url=pixel_endpoint, json=pixel_param , headers=headers)
update= requests.put(url=update_endpoint , json=update_param ,headers=headers )
delete = requests.delete(url=delete_endpoint ,headers=headers)

print(update.text)


