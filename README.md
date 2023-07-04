## GameManage
A prototype of a full-stack web application to collect your games in one place, search for new games, and connect with other gamers. 

Tech stack: Python, Flask, HTML, Bootstrap, GitLab, Heroku, Lucidchart, Figma  

You can read more about the project's requirements, design, plannning, implementation, testing, and review in the associated [wiki](https://github.com/nabilshadman/flask-gamemanage-app-prototype/wiki). The repository (and the wiki) has been migrated from GitLab to GitHub, and the current deployment uses Google Cloud Platform (GCP) instead of Heroku previously.

You can view the deployed app protoype [here](https://pacific-destiny-391109.ue.r.appspot.com/).  

If you want to clone the repository for further development of this application in your local machine, please refer to the instructions below.  


## Install Python 3.9  
We have used Python 3.9 for this project. Please ensure you have Python 3.9 or above installed in your system.  

See Python's [website](https://www.python.org/downloads/) for downloading the latest version for your system.  

Linux:  
You may follow this [page](https://docs.python-guide.org/starting/install3/linux/) for guidance on installing Python 3.9 on a Linux system.  

macOS:  
You may follow this [page](https://python.tutorials24x7.com/blog/how-to-install-python-3-9-on-mac) for guidance on installing Python 3.9 on a macOS system.  

Windows:  
You may follow this [page](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html) for guidance on installing Python 3.9 on a Windows system.  




## Clone Repository

(1) Clone with SSH:  
```git clone git@github.com:nabilshadman/flask-gamemanage-app-prototype.git```      

OR  

Clone with HTTPS:   
```git clone https://github.com/nabilshadman/flask-gamemanage-app-prototype.git```     

(2) Go to the project directory:  
```cd gamemanage-app-prototype```      




## Install Flask  
(1) Create environment  

Linux/macOS:  
```python3 -m venv venv```    

Windows:  
```py -3 -m venv venv```    

(2) Activate the environment  

Linux/macOS:  
```. venv/bin/activate```    

Windows:  
```venv\Scripts\activate```    

(3) Install Flask  

```pip install Flask```    

For more details, visit this [page](https://flask.palletsprojects.com/en/2.0.x/installation/).   

(4) Install other dependencies  

```pip install -r requirements.txt```    

If you are contributing to this project, please ensure to update the requirements.txt file for other developers or users with the following command:  

```pip freeze > requirements.txt```    




## Run Flask App  

Bash:  
```export FLASK_APP=app```    
```flask run```    

Powershell:  
```$env:FLASK_APP = "app"```    
```flask run```    

For more details on running Flask applications, visit this [page](https://flask.palletsprojects.com/en/2.0.x/quickstart/).    
