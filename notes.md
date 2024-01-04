1 Intro
2 Project Overview
3 Mac Python Installation
4 Mac VS Code install and setup
5 Windows Python Installation
6 Windows VS Code install and setup
7 Python virtual Env Basics
8 Virtual Env on windows
9 Virtual Env on Mac
10 Install dependencies w/ pip

```shell
pip install fastapi[all]
```

11 Starting FastAPI

```shell
uvicorn main:app

```

12 Path Operations
13 Intro toman
14 HTTP Requests
15 Schema Validation with Pydantic

### 16 CRUD Operations

always plural: /posts
put - all fields
patch - the fields need to update

```python
Create      POST        /posts      @app.post("posts")
Read        GET         /posts/:id  @app.get("/posts/{id}")
            GET         /posts      @app.get("/posts")
Update      PUT/PATCH   /posts/:id  @app.put("/posts/{id}")
Delete      DELETE      /posts/:id  @app.delete("/posts/{id}")
```

17 Storing in Array
18 Creating
19 Postman Collections & saving requests
20 Retrieve One
21 Path order Matters
22 Changing response Status Codes

```python
from fastapi import FastAPI, Response, status, HTTPException

# specify default status code for path operation
@app.post("/posts", status_code=status.HTTP_201_CREATED)


        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data": f"not found : id = {id}"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found : id = {id}"


```

23 Deleting
24 Updating
25 Automatic Documentation
26 Python packages
27 Database Intro
28 Postgres Windows Install
29 Postgres Mac Install
30 Database Schema & Tables
31 Managing Postgres with PgAdmin GUI
32 Your first SQL Query
33 Filter results with "where"
34 SQL Operators
35 IN
36 Pattern matching with LIKE
37 Ordering Results
38 LIMIT & OFFSET
39 Modifying Data
40 Setup App Database
41 Connecting to database w/ Python
42 Database CRUD
43 ORM intro
44 SQLALCHEMY setup
45 Adding CreatedAt Column
46 Get All
47 Create
48 Get by ID
49 Delete
50 Update
51 Pydantic vs ORM Models
52 Pydantic Models Deep Dive
53 Response Model
54 Creating Users Table
55 User Registration Path Operation
56 Hashing Passwords
57 Refractor Hashing Logic
58 Get User by ID
59 FastAPI Routers
60 Router Prefix
61 Router Tags
62 JWT Token Basics
63 Login Process  
64 Creating Token
65 OAuth2 PasswordRequestForm
66 Verify user is Logged In
67 Fixing Bugs
68 Protecting Routes
69 Test Expired Token
70 Fetching User in Protected Routes
71 Postman advanced Features
72 SQL Relationship Basics
73 Postgres Foreign Keys
74 SQLAlchemy Foreign Keys
75 Update Schema to include User
76 Assigning Owner id when creating new
77 Delete and Update only your own
78 Only Retrieving Logged in User's
79 Sqlalchemy Relationships
80 Query Parameters
81 Cleanup our main.py file
82 Env Variables
83 Vote/Like Theory
84 Votes Table
85 Votes Sqlalchemy
86 Votes Route
87 SQL Joins
88 Joins in SqlAlchemy
89 Get One with Joins
90 What is a database migration tool
91 Alembic Setup
92 Disable SqlAlchemy create Engine
93 What is CORS?
94 Git PreReqs
95 Git Install
96 Github
97 Heroku intro
98 Create Heroku App
99 Heroku procfile
100 Adding a Postgres database
101 Env Variables in Heroku
102 Alembic migrations on Heroku Postgres instance
103 Pushing changed to production
104 Create an Ubuntu VM
105 Update packages
106 Install Python
107 Install Postgres & setup password
108 Postgres Config
109 Create new user and setup python evironment
110 Env Variables
111 Alembic migrations on production database
112 Gunicorn
113 Creating a Systemd service
114 NGINX
115 Setting up Domain name
116 SSL/HTTPS
117 NGINX enable
118 Firewall
119 Pushing code changes to Production
120 Dockerfile
121 Docker Compose
122 Postgres Container
123 Bind Mounts
124 Dockerhub
125 Production vs Development
126 Testing Intro
127 Writing your first test
128 The -s & -v flags
129 Testing more functions
130 Parametrize
131 Testing Classes
132 Fixtures
133 Combining Fixtures + Parametrize
134 Testing Exceptions
135 FastAPI TestClient
136 Pytest flags
137 Test create user
138 Setup testing database
139 Create & destroy database after each test
140 More Fixtures to handle database interaction
141 Trailing slashes in path
142 Fixture scope
143 Test user fixture
144 Test/validate token
145 Conftest.py
146 Testing
147 CI/CD intro
148 Github Actions
149 Creating Jobs
150 setup python/dependencies/pytest
151 Env variables
152 Github Secrets
153 Testing database
154 Building Docker images
155 Deploy to heroku
156 Failing tests in pipeline
157 Deploy to Ubuntu
