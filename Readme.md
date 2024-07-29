# Daily Expenses Sharing Application

## Objective
Design and implement a backend for a daily-expenses sharing application. This application will allow users to add expenses and split them based on three different methods: exact amounts, percentages, and equal splits. The application should manage user details, validate inputs, and generate downloadable balance sheets.

## Requirements
Python
MySQL
FastAPI

### User Management
- Each user should have an email, name, and mobile number.

### Expense Management
- Users can add expenses.
- Expenses can be split using three methods:
  1. Equal: Split equally among all participants.
  2. Exact: Specify the exact amount each participant owes.
  3. Percentage: Specify the percentage each participant owes. (Ensure percentages add up to 100%).

### Expense Calculation Examples
1. **Equal**:
    - Scenario: You go out with 3 friends. The total bill is 3000. Each friend owes 1000.
2. **Exact**:
    - Scenario: You go shopping with 2 friends and pay 4299. Friend 1 owes 799, Friend 2 owes 2000, and you owe 1500.
3. **Percentage**:
    - Scenario: You go to a party with 2 friends and one of your cousins. You owe 50%, Friend 1 owes 25%, and Friend 2 owes 25%.

### API Endpoints

#### User Endpoints
- Create user.
- Retrieve user details.

#### Expense Endpoints
- Add expense.
- Retrieve individual user expenses.
- Retrieve overall expenses.
- Download balance sheet.

### Data Validation
- Validate user inputs.
- Ensure percentages in the percentage split method add up to 100%.

## Project Structure
```
expense-sharing-app/ 
├── app/ 
│ ├── init.py 
│ ├── main.py 
│ ├── models.py 
│ ├── schemas.py 
│ ├── database.py
│ ├── crud.py │ 
├── utils.py 
│ ├── routers/ 
│ │ ├── init.py 
│ │ ├── users.py 
│ │ └── expenses.py 
│ └── tests/ 
│ ├── init.py 
│ ├── test_users.py 
│ └── test_expenses.py 
├── alembic 
├── .env 
├── Readme.md 
├── alembic.ini 
├── requirements.txt 
├── README.md 
└── setup.sql
```

## Setup and Installation Instructions

### Prerequisites
- Python 3.8+
- MySQL
- FastAPI
- SQLAlchemy
- Alembic

### Setting Up the Database
1. Install MySQL: Ensure MySQL is installed and running on your machine.
2. Create Database: Execute the following commands in your MySQL shell to create the database:

```
CREATE DATABASE expense_sharing;
USE expense_sharing;
```

Run the setup.sql script provided
```
SOURCE setup.sql;
```
## Create a Database and User
Open the MySQL command line client and log in as the root user:
```
mysql -u root -p
```
Create a new database for your application:
```
CREATE DATABASE expense_sharing;
```
Create a new user and grant them privileges on the new database. Replace your_username and your_password with your desired username and password:

```
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON expense_sharing.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;
```
Construct the DATABASE_URL
The DATABASE_URL is a connection string that specifies how to connect to your database. For MySQL, the format is:
```
DATABASE_URL=mysql+pymysql://<username>:<password>@<host>/<database_name>
```
Given the username, password, and database name from the previous steps, the DATABASE_URL might look like this:
```
DATABASE_URL=mysql+pymsql://your_username:your_password@localhost/expense_sharing
```
**Installing Dependencies**:
Create a virtual environment and install the dependencies:
```
python -m venv venv
venv/Scripts/activate
```
```
pip install -r requirements.txt
```
## requirements.txt
```
Python
MySQL
fastapi
uvicorn
sqlalchemy
alembic
pydantic
mysqlclient
python-dotenv
```

## Running the Application

Database Migrations

Use Alembic for database migrations.
```
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
 ```
## Start the FastAPI Server
 ```
uvicorn app.main:app --reload
 ```

**Access the Application**
- Once the server is running, you can access your FastAPI application by navigating to http://127.0.0.1:8000 in your web browser.

You can also explore the interactive API documentation generated by FastAPI at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Stop the Server
To stop the server, press Ctrl+C in the terminal where the server is running.

## Unit Tests

1. **Navigate to the root directory**:
   ```
   cd testsfolderpath
   ```

2. **Run the tests**:
   ```
   pytest
   ```
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License

This project is Open Source and can be updated in the future. 

## Contact

For any questions or support, don't hesitate to contact [your email](Ilamugil.balasubramaniam1@gmail.com).
