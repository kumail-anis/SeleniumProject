
# Selenium Project

## Task

Write a test automation script that goes to the website (http://the-internet.herokuapp.com/) and completes the following actions. Ensure that industry best practices are maintained.

- Click on the “Javascript Alerts” link and once that page has loaded; 
        
- Click on the “Click on JS Confirm” button and hit the Confirm button once the prompt has loaded. 
        
- Once this is done validate that the Result “You clicked: Ok” is shown. 


## Project

Built with python, this project consists of the file main.py that runs the selenium project that runs the website the-internet.herokuapp. The main.py file runs through a docker container as an additional challenge for this task. In order to run the program, a user must have docker installed in their local system. Below is the following steps to run this project as a docker container using terminal:

```bash
 sudo docker build Main -t pythondriver:3.8
```

then run the built container:

```bash
 sudo docker run -t pythondriver:3.8
```

Otherwise, in order to run the program locally run the following terminal line once cloned the repository, run the following command on terminal and run the localmain.py by the following command

```bash
python3 localmain.py
```
or run the project in your favorable Python IDE. 




## TODO TASKS!
This project is incomplete as the following tasks must be achieved in order for suitable delivery:

1- use of proper stoppers instead of implicitly_wait


## Contributing

The following websites have helped with understanding Selenium:

https://stackoverflow.com/questions/40299451/error-while-installing-selenium-in-pip3
https://www.npmjs.com/package/selenium-standalone
https://stackoverflow.com/questions/38589434/selenium-find-button-element#38590490
https://www.techbeamers.com/locate-elements-selenium-python/
https://pythonspot.com/selenium-click-button/
https://www.youtube.com/watch?v=mQ7-mPJYJ5A&t=739s&ab_channel=SeleniumMaster

## Author

Created by Syed Kumail Anis



