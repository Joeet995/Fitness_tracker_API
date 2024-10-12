#Fitness Tracker API#

This is a Fitness Tracker API built using Django and Django Rest Framework (DRF). It allows users to track fitness activities, manage user accounts, and view activity summaries with filtering and pagination options. The backend is deployed using AWS Lambda with Zappa, and the database is hosted on AWS RDS MySQL.

#Features:
    - User registration, authentication, and management.
    - CRUD operations for fitness activities (e.g., running, cycling, weightlifting).
    - Filtering and pagination on activities list.
    - Activity summaries (total duration, calories burned, etc.) with optional date filtering.
    - Deployed as a serverless application using AWS Lambda and Zappa.
    - Integrated with a MySQL database hosted on AWS RDS.

#Technologies Used:
    - Backend Framework: Django, Django Rest Framework
    - Database: MySQL on AWS RDS
    - Deployment: AWS Lambda, Zappa
    - Python Version: 3.x
    - Other Libraries: mysqlclient for MySQL

#Prerequisites:
    all found in requirments.txt

#Project Setup:
    1. Clone the repository
    2. Create a Virtual Environment
    3. Install Dependencies
    4. Database Configuration
    5. Apply Database Migrations
    6. Create a Superuser
    7. Run the Development Server

#AWS Lambda Deployment:
    1. Install Zappa
    2. Configure Zappa
    3. Update Zappa Settings (For MySQL and VPC)
    4. Deploy to AWS Lambda
    5. Update After Changes
    6. Database Migrations in Production

#API Endpoints:

User Management:
    - POST users/api-register/: Register a new user
    - GET users/api-users/: List all users
    - GET, PUT, DELETE users/api-user/{id}/: Retrieve, update, delete a user
    - POST users/token/: Authenticate user ( Logging in)

Activity Management:
    - GET, POST activity/api-activities/: List or create activities
    - GET, PUT, DELETE activity/api-activities/{id}/: Retrieve, update, or delete an activity
    - GET activity/api-activity-summary/: View a summary of user activities






