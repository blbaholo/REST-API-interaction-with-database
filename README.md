## **PROJECT DESCRIPTION**

This Flask app consists of a database that stores all computers owned by Umuzi. The contents of the database are accessed using CRUD operations, list all computers, add a computer, update a computer and delete a computer, which are exposed at REST api endpoints.

## **RUNNING THE APPLICATION**:

1. Create a virtual environment and activate.

    *Windows (cmd)*
    ```shell
    python -m venv rest-api
    ```

    ```shell
    rest-api\Scripts\activate
    ```

    *Linux/MacOS*

    ```shell
    python3 -m venv rest-api
    ```

    ```shell
    source rest-api/bin/activate
    ```

2. Install dependencies in requirements file.

    ```shell
    pip install -r requirements.txt
    ```

3. Install project

    *Windows (cmd)*
    ```shell
    python setup.py develop
    ```

    *Linus/MacOS*
    ```shell
    python3 setup.py develop
    ```

4. Start up docker container

    *Windows (cmd)*
    ```shell
    docker-compose up
    ```

    *Linux/MacOS*
    ```shell
    docker compose up
    ```

5. Run the application

    ```shell
    flask --app src run
    ```

    This will run the flask app on the default app 5000. To make use of a different port use the following command. Making the necessary adjustments to the port number.

    ```shell
    flask --app src run -port [port]
    ```


**NOTE**: You aren't expected to set any environmental variables. These have already been set within a .env file. Default values have been created in the event of an error occuring in retreiving the environmental variables.

## **CONSUMING API**:

### **This can be done using curl on the terminal or using postman.** 

### List all computers:


**POSTMAN**

Method: GET  
API endpoint: http://127.0.0.1:5000/computers

**CURL**

*Windows/Linux/MacOS*
```shell
curl http://127.0.0.1:5000/computers
```
Returns: list of computers

### Add a computer:


**POSTMAN**

Method: POST  
API endpoint: http://127.0.0.1:5000/computers/
URL_body_parameter: (Type=JSON, accepts data in {key: value} format)

e.g. 

{"hard_drive_type": "HDD",
"processor": "Intel Core i3-10110U",
"ram_amount": 2,
"maximum_ram": 4,
"hard_drive_space": 256,  
"form_factor": "E-ATX"}

**CURL**

*Windows (cmd)* 
```shell
curl -H "Content-Type: application/json" -d "{\"hard_drive_type\":\"HDD\",\"processor\":\"Intel Core i3-10110U\",\"ram_amount\":2,\"maximum_ram\":4,\"hard_drive_space\":256,\"form_factor\":\"E-ATX\"}" -X POST http://127.0.0.1:5000/computers/
```

*Windows (Powershell)*
```shell
Invoke-WebRequest -ContentType "application/json" -Method 'Post' -Body '{"hard_drive_type": "HDD","processor": "Intel Core i3-10110U","ram_amount": 2, "maximum_ram": 4,"hard_drive_space": 256,  "form_factor": "E-ATX"}' -Uri http://127.0.0.1:5000/computers/
```

*Linux/MacOS*
```shell
curl -H "Content-Type: application/json" -d '{"hard_drive_type":"HDD","processor":"Intel Core i3-10110U","ram_amount":2,"maximum_ram":4,"hard_drive_space":256,"form_factor":"E-ATX"}' -X POST http://127.0.0.1:5000/computers/
```
Returns: "MESSAGE: Computer details successfully added"  

### Update a computer:


**POSTMAN**

Method: PATCH  
Basic API endpoint: http://127.0.0.1:5000/computers/{id}  
URL_body_parameter (Type=JSON, accepts data in {key: value} format):

e.g.

{"ram_amount": "3"}

**CURL**

*Windows (cmd)*
```shell
curl -X PATCH http://127.0.0.1:5000/computers/1 -H "Content-Type: application/json" -d "{\"ram_amount\":3}"
```

*Windows (Powershell)*
```shell
Invoke-WebRequest -ContentType "application/json" -Method 'Patch' -Body '{"ram_amount": "3"}' -Uri http://127.0.0.1:5000/computers/1
```

*Linux/MacOS*
```shell
curl -X PATCH http://127.0.0.1:5000/computers/1 -H "Content-Type: application/json" -d '{"ram_amount":3}'
```
Returns: Details of the computer with updated column/s  

### Delete a computer:


**POSTMAN**

Method: DELETE  
Basic API endpoint: http://127.0.0.1:5000/computers/{id}  

**CURL**

*Windows (Powershell)*
```shell
Invoke-WebRequest -Method 'Delete' -Uri http://127.0.0.1:5000/computers/1
```

*Windows(cmd)/Linux/MacOS*
```shell
curl -X DELETE http://127.0.0.1:5000/computers/{id}
```
Returns: "MESSAGE: Computer details successfully deleted"
