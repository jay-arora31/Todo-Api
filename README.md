# Todo-Api

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jay-arora31/Todo-Api.git
$ cd Todo-Api
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ virtualenv -p python venv
$ venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
 Then run makemigrations and migrate the app
 ```sh
 python manage.py makemigrations
 
 python manage.py migrate
 
 ````
 
 
Task Model
```sh

class Task(models.Model):
    task_title=models.CharField(max_length=200,blank=True,null=True)
    task_status=models.BooleanField(default=False, blank=True,null=True)
    def __str__(self):
        return self.task_title
```


api access points
 ```sh

 navigate to : http://127.0.0.1:8000/
 
 api_urls = {
        'Todo List' :'/todo-list/',
        'Todo Task Detail' :'/task-detail/<int:pk>/',
        'Todo Task Create' :'/task-create/',
        'Todo Task Update' :'/task-update/<int:pk>/',
        'Todo Task Status Update' :'/task-status-update/<int:pk>/',
        'Todo Task Delete' :'/task-delete/<int:pk>/',
       
    }
  
 ````
 
 
 
 Todo task create
 
  ```sh
 navigate to : http://127.0.0.1:8000/task-create/
 
  {
  "task_title":"task 6"
  }
  
 ````
 
 
 Todo Task Status Update
 
   ```sh
 navigate to : http://127.0.0.1:8000/task-status-update/2/
 
  {
  "task_status": false
  }
  
 ````
