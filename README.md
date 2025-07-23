# RESTful_API

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/48c49c05bffe42738acd5a6e2f50a2dd)](https://app.codacy.com/manual/alex.sulea/RESTful_API?utm_source=github.com&utm_medium=referral&utm_content=Alexandru-S/RESTful_API&utm_campaign=Badge_Grade_Dashboard)

A simple web app using the Amazon RDS Oracle database to serve information using a RESTfull API with basic authentication.

<pre><font color="#3465A4"><b>.RESTful_API</b></font>
├── config.py
├── main.py
├── README.md
├── requirements.txt
└── <font color="#3465A4"><b>web_app</b></font>
    ├── <font color="#3465A4"><b>badge</b></font>
    │   ├── __init__.py
    │   ├── models.py
    ├── crud.py
    ├── db_creds.py <font color="#f44336"><b>File to be added by user, contains the db credentials, instructions below</b></font>
    ├── <font color="#3465A4"><b>department</b></font>
    │   ├── __init__.py
    │   ├── models.py
    ├── <font color="#3465A4"><b>employee</b></font>
    │   ├── __init__.py
    │   ├── models.py
    ├── __init__.py
    ├── <font color="#3465A4"><b>job_title</b></font>
    │   ├── __init__.py
    │   ├── models.py
    └── <font color="#3465A4"><b>tests</b></font>
        ├── db_creds.py <font color="#f44336"><b>File to be added by user, contains the db credentials, instructions below</b></font>
        ├── __init__.py
        ├── new_tests.py
        └── test.py
</pre>
## Technologies
### Languages
Python 3.8.2
### Frameworks
Flask 1.1.2
### Databases
Oracle AWS RDS Standard Edition 2 Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

## Instructions on Running the Code

I have developed and run the code on Ubuntu 20.04.1 LTS. Should you wish to run the code on a different OS please take care to make sure that the packages in use are supported on the different systems.

The first step is to copy the code to a local directory to be run, this can be achieved by running the following git command:

```bash
git clone https://github.com/Alexandru-S/RESTful_API.git
```

Once the code is cloned to your directory a virtual environment will need to be created to store the python packages we are using.  
This can be achieved by running the following commands in the command line:  
> if virtualenv is not present in the system already

```bash
pip install virtualenv
```  

> create a python3 virtual environment

```bash
virtualenv --python python3 env3
```  

> activate the environment

```bash
source env3/bin/activate
```  

> install all the required packages

```bash
cd RESTful_API
```
  
```bash
pip install -r requirements.txt
```  

After all the packages have been successfully installed in the system we can go ahead and run the application.

## Running the application in Localhost (**IMPORTANT**)
You will need to create a file with the name **db_creds.py** with the following format inside of it  
```
HOSTNAME = 'developmentb.xxxxxYOUR_DB_ID_HERExxxxxx.eu-west-1.rds.amazonaws.com'
USERNAME = 'your_username for the database'
PASSWORD = 'your_password for the database'
SID = 'your sid'
PORT = '1521'
```
Once the file is created place one copy of it in the web_app directory and another copy in the tests directory.  
Why 2? For some reason I was not able to access it from inside the tests directory so added a copy in the tests directory as well.  

Once this is all filled and set up, run the following commands to launch the web app.
> run the application

```bash
python main.py
```  

You should see something like this in your command line  

```
* Debug mode: on  
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
* Restarting with stat  
* Debugger is active!  
* Debugger PIN: 101-649-027
```

Click on the <http://127.0.0.1:5000/> link and then choose to add one of the 4 endpoint options at the end of the URL.  
A webpage should begin to load and ask for username and password.  
The user credentials are the same as the ones provided in the db_creds.py



> stop the application  
You need to click on the command line that is running the web app and click `CTRL + C `  

> exit the virtual environment

```bash
deactivate
```

If you wish to run the application you will need to cd into the tests directory and run the following commands  
> cd into tests
  
```bash
cd tests
```  

> Run the small testing script

```bash
python test.py
```  

> Run the tests

```bash
python new_tests.py -v
```  

## Feature Explanations

###Departments

#### GET /department
Going to the /department endpoint will returns back all the department table rows in JSON format.
No more features were asked to be added for this endpoint so none more were added, although there is a possibility for expansion.

### Badges

#### GET /badges/active
This endpoint will retrieve back all (**BADGE_STATUS** == active) **AND** (**BADGE_EXPIRY_DATE** > datetime.date.today())
As per the instruction provided.  
Should no badges be active a **404 error** message will be returned.  

#### GET /badges?badge_number=badge_number
Only the badge number that matches the query parameter will be returned, if it exists.  
If it doesn't exist a 404 error will be returned.  
If the format is malformed or not matching specifications a **422 error** will be returned by the reqparse add_argument() function.

As the above example, no more options were added due to none more being asked at this endpoint but there is room for expansion.

### Job Titles

#### GET /job_titles
Returns all job titles as per requirements.

#### GET /job_titles/:department_name
Returns all job titles with the given department name.
I was not able to escape the colon (:) in reqparse and the online documentation is deprecated and misleading if one should even use colons.  
The restcountries.eu uses the semi-colon (;) to split between different variables passed and may recommended to use semi-colons.   
However given the lack of documentation I instead treated it as another argument without having special characters in front of it.

### Employees

#### GET /employees
Returns all the rows in table **EMPLOYEE** with the **COUNTRY_CODE** key value pair replaced by the **COUNTRY** key which retrieves back the country name using the <https://restcountries.eu/rest/v2/alpha?codes={code1};{code1};{code1}> API endpoint from <https://restcountries.eu>.  
This function is present in all queries that involve retrieving back **EMPLOYEE** information.

#### GET /employees/active
The document specified "Return all employees who DO NOT have a leave_date set or have a leave_date set in the
**past**".  
Returns all rows where the (**LEAVE_DATE** == **None**) **OR** (**LEAVE_DATE** < datetime.date.today())  
There is *one small issue with the logic*.  
If leave date is set as before the current date of today that would mean that the employee has already left the company.
This query will thus retrieve all current employees and all employees who have already left the company, leaving absent the employees that are yet to leave the company.  
The logic to return only the current employees would be (**LEAVE_DATE** == **None**) **OR** (**LEAVE_DATE** > datetime.date.today()) thus only employees still in the company will be retrieved. 
Should no employees be current a **404 error** message will be returned.  

#### GET /employees?department_name=department_name
Returns all employees given the department name.
This requires a left join between the **EMPLOYEE**, **JOB_TITLE** and **DEPARTMENT** tables.

## Observations
### restcountries.eu
During development, while attempting to call the **restcountries** recommended API endpoint for country names I noticed that while it being given **irl** it would not return Ireland. This was due to the **COUNTRY_CODE** value being correct for alpha encoding but not being the official supported country prefix which is ie. Thus I was forced to get creative and instead query by alpha encodings which were able to cover all edge cases.  

Thus the endpoint <https://restcountries.eu/rest/v2/name/irl?fullText=true> will not return the name Ireland but if using the alternative endpoint <https://restcountries.eu/rest/v2/alpha?codes=irl;irl;irl> the name of the country can be extracted from the returned json.  

While this method does work, it is not the most optimal solution.  
Everytime the **employees** endpoint is called, it has to make a call to the **restcountries** API. Thus the time delay is significantly increased and should the number of rows increase into the thousands it will adversely effect this endpoint.  

A better solution would be to perhaps have a table which can have the **COUNTRY_NAMES** as a variable. Therefore to get country names we would only have to do a basic join rather than query another API.

### reqparse
I chose to use the reqparse library in combination with the flask_restful.  
Although reqparse is deprecated, it is still stable and working, the decision to use it was made due to the marshmallow library not being thoroughly enough documented for my needs.
The link to the reqparse announcement here <https://flask-restful.readthedocs.io/en/latest/reqparse.html>

### Basic Authentication
The HTTPBasicAuth package is used for generating a login popup asking for username and password.  
The username and password will then be compared to the stored information.  
Due to not having a USER table with login information, the password and username are fetched from the ones given in the db_cred.py file.

### CRUD
crud.py designated for Create.Read.Update.Delete although due to the requirements of the project only being about reading and listing the only query is that for reading.  

