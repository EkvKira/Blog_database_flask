# Flask

**Installing PIP**
To check if you have PIP, enter in the console:
```
pip --version
python3 -m pip --version
```
For installation:
```
python -m ensurepip --default-pip
```

**Installing Flask**
The Flask download process will begin, after which it will be ready to use.
```
pip install Flask
```
To check if Flask is running, enter the following command:
```
pip show flask
```

Run the file using the command in the console/terminal:
```
python app.py
```

**Page Home**

![Page Home](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Home.jpg)

**Add new post**

![Page Add new post](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Page_add_new_post.jpg)
![Add new post](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Add_new_post.jpg)
![Success Add new post](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Success_add_post.jpg)


**Work with the database**
We used the SQLite database because it takes up very little space and is easy to learn. It does not need to be downloaded separately, because it is immediately available in Python.

Import SQLite3 module:
```
import sqlite3
```
![Page for verify the database](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Page_check_db.jpg)
![Check the database](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/Check_DB.jpg)
![Work in DBeaver](https://github.com/EkvKira/Blog_database_flask/blob/main/img_for_README/DBeaver_bd.jpg)