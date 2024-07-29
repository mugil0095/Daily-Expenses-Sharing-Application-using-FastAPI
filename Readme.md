# Daily Expenses Sharing Application

## Objective
Design and implement a backend for a daily-expenses sharing application. This application will allow users to add expenses and split them based on three different methods: exact amounts, percentages, and equal splits. The application should manage user details, validate inputs, and generate downloadable balance sheets.

## Requirements

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

```sql
CREATE DATABASE expense_sharing;
USE expense_sharing;
```
-- Run the setup.sql script provided
SOURCE setup.sql;
```
setup.sql Content;


Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL
);

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payer_id INT NOT NULL,
    FOREIGN KEY (payer_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE expense_splits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_id INT NOT NULL,
    user_id INT NOT NULL,
    amount DECIMAL(10, 2),
    percentage DECIMAL(5, 2),
    split_type ENUM('equal', 'exact', 'percentage') NOT NULL,
    FOREIGN KEY (expense_id) REFERENCES expenses(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
Installing Dependencies
Create a virtual environment and install the dependencies:

bash
Always show details

Copy code
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
requirements.txt Content
Always show details

Copy code
fastapi
uvicorn
sqlalchemy
alembic
pydantic
mysqlclient
python-dotenv
Running the Application
Database Migrations
Use Alembic for database migrations.

bash
Always show details

Copy code
alembic init alembic
# Configure alembic.ini and env.py to connect to your MySQL database
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
Start the FastAPI Server:
bash
Always show details

Copy code
uvicorn app.main:app --reload
Create a Database and User
Open the MySQL command line client and log in as the root user:

bash
Always show details

Copy code
mysql -u root -p
Create a new database for your application:

sql
Always show details

Copy code
CREATE DATABASE expense_sharing;
Create a new user and grant them privileges on the new database. Replace your_username and your_password with your desired username and password:

sql
Always show details

Copy code
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON expense_sharing.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;
Construct the DATABASE_URL
The DATABASE_URL is a connection string that specifies how to connect to your database. For MySQL, the format is:

php
Always show details

Copy code
mysql://<username>:<password>@<host>/<database_name>
Given the username, password, and database name from the previous steps, the DATABASE_URL might look like this:

bash
Always show details

Copy code
mysql://your_username:your_password@localhost/expense_sharing
Access the Application
Once the server is running, you can access your FastAPI application by navigating to http://127.0.0.1:8000 in your web browser.

You can also explore the interactive API documentation generated by FastAPI at:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Stop the Server
To stop the server, press Ctrl+C in the terminal where the server is running.
