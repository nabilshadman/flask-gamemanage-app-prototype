## GameManage
A prototype of a full-stack web application to collect your games in one place, search for new games, and connect with other gamers.  

Deployed prototype version used in usability testing: https://gamemanage-flask-app.herokuapp.com/  
Deployed final version of protoype: https://gamemanage-prototype-app.herokuapp.com/  

If you want to clone the repository for further development of this application in your local machine, please refer to the instructions below.  


## Install Python 3.9  
We have used Python 3.9 for this project. Please ensure you have Python 3.9 or above installed in your system.  

Refer to https://www.python.org/downloads/ for downloading the latest version for your system.  

Linux:  
You may follow this page https://docs.python-guide.org/starting/install3/linux/ for guidance on installing Python 3.9 in a Linux system.  

macOS:  
You may follow this page https://python.tutorials24x7.com/blog/how-to-install-python-3-9-on-mac for guidance on installing Python 3.9 in a macOS system.  

Windows:  
You may follow this page https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html for guidance on installing Python 3.9 in a Windows system.  




## Clone Repository

Clone with SSH:  
```git clone git@github.com:nabilshadman/gamemanage-app-prototype.git```      

Clone with HTTPS:   
```git clone https://github.com/nabilshadman/gamemanage-app-prototype.git```     

Go to the project directory:  
```cd gamemanage-app-prototype```      




## Install Flask  
1. Create environment  

Linux/macOS:  
```python3 -m venv venv```    

Windows:  
```py -3 -m venv venv```    

2. Activate the environment  

Linux/macOS:  
```. venv/bin/activate```    

Windows:  
```venv\Scripts\activate```    

3. Install Flask  

```pip install Flask```    

For more details, visit this [link](https://flask.palletsprojects.com/en/2.0.x/installation/).   

4. Install other dependencies  

```pip install -r requirements.txt```    

If you are contributing to this project, please ensure to update the requirements.txt file for other developers or users using the following command:  

```pip freeze > requirements.txt```    




## Run Flask App  

Bash:  
```export FLASK_APP=app```    
```flask run```    

Powershell:  
```$env:FLASK_APP = "app"```    
```flask run```    

For more details on running Flask applications, visit this [link](https://flask.palletsprojects.com/en/2.0.x/quickstart/).    
