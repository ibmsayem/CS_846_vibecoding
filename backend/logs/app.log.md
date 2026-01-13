**2026-01-13T13:52:11.365622-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T13:52:11.366376-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T13:52:11.366457-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T13:53:30.727778-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T13:53:30.728641-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T13:53:30.728734-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T13:54:12.784244-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T13:54:12.787812-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T13:54:12.787895-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T13:54:34.299545-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T13:54:34.300248-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T13:54:34.300324-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T13:55:04.468889-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T13:55:04.483516-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.015s
**2026-01-13T13:55:19.413899-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"nam","email":"nam@gmail.com","password":"pass1234"}
**2026-01-13T13:55:19.424430-0500** | **INFO** | Registration request received for username: nam, email: nam@gmail.com
**2026-01-13T13:55:19.429619-0500** | **INFO** | Hashing password for nam
**2026-01-13T13:55:19.440069-0500** | **ERROR** | Unexpected error during registration for nam: ValueError: password cannot be longer than 72 bytes, truncate manually if necessary (e.g. my_password[:72])
**2026-01-13T13:55:19.441030-0500** | **INFO** | Response: POST /api/users/register | Status: 500 | Time: 0.027s
**2026-01-13T13:55:50.907360-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T13:55:50.908998-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T13:55:50.909236-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T13:56:42.133638-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username": "alice", "email": "alice@example.com", "password": "password123"}
**2026-01-13T13:56:42.141305-0500** | **INFO** | Registration request received for username: alice, email: alice@example.com
**2026-01-13T13:56:42.146847-0500** | **INFO** | Hashing password for alice
**2026-01-13T13:56:42.355664-0500** | **INFO** | Creating new user: alice
**2026-01-13T13:56:42.356045-0500** | **INFO** | Saving user to database: alice
**2026-01-13T13:56:42.359475-0500** | **INFO** | User registered successfully: alice (ID: 1)
**2026-01-13T13:56:42.364519-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.231s
**2026-01-13T13:56:51.888617-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username": "alice", "password": "password123"}
**2026-01-13T13:56:52.065861-0500** | **INFO** | User logged in: alice
**2026-01-13T13:56:52.066180-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.178s
**2026-01-13T13:56:59.489410-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username": "alice", "password": "password123"}
**2026-01-13T13:56:59.658434-0500** | **INFO** | User logged in: alice
**2026-01-13T13:56:59.658778-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.169s
**2026-01-13T13:56:59.660560-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content": "Hello world! This is my first post!"}
**2026-01-13T13:56:59.663456-0500** | **INFO** | Response: POST /api/posts/ | Status: 422 | Time: 0.003s
**2026-01-13T13:57:19.507224-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username": "alice", "password": "password123"}
**2026-01-13T13:57:19.676522-0500** | **INFO** | User logged in: alice
**2026-01-13T13:57:19.676843-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.170s
**2026-01-13T13:57:19.678604-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content": "Hello world! This is my first post!"}
**2026-01-13T13:57:19.679258-0500** | **INFO** | Response: POST /api/posts/ | Status: 422 | Time: 0.001s
**2026-01-13T13:59:44.363906-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T13:59:44.365488-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:00:04.417304-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username": "bob", "email": "bob@example.com", "password": "secret456"}
**2026-01-13T14:00:04.417982-0500** | **INFO** | Registration request received for username: bob, email: bob@example.com
**2026-01-13T14:00:04.418419-0500** | **INFO** | Hashing password for bob
**2026-01-13T14:00:04.586069-0500** | **INFO** | Creating new user: bob
**2026-01-13T14:00:04.586271-0500** | **INFO** | Saving user to database: bob
**2026-01-13T14:00:04.587553-0500** | **INFO** | User registered successfully: bob (ID: 2)
**2026-01-13T14:00:04.587989-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.171s
**2026-01-13T14:00:04.589743-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username": "bob", "password": "secret456"}
**2026-01-13T14:00:04.757688-0500** | **INFO** | User logged in: bob
**2026-01-13T14:00:04.757989-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.168s
**2026-01-13T14:00:55.744531-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:00:55.745268-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:00:55.745338-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:01:15.025021-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:01:15.031596-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.007s
**2026-01-13T14:01:28.258051-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibmsayem","email":"abc@gmail.com","password":"pass1234"}
**2026-01-13T14:01:28.261599-0500** | **INFO** | Registration request received for username: ibmsayem, email: abc@gmail.com
**2026-01-13T14:01:28.262778-0500** | **INFO** | Hashing password for ibmsayem
**2026-01-13T14:01:28.432860-0500** | **INFO** | Creating new user: ibmsayem
**2026-01-13T14:01:28.433013-0500** | **INFO** | Saving user to database: ibmsayem
**2026-01-13T14:01:28.435667-0500** | **INFO** | User registered successfully: ibmsayem (ID: 1)
**2026-01-13T14:01:28.436107-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.178s
**2026-01-13T14:01:36.746186-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username":"ibmsayem","password":"pass1234"}
**2026-01-13T14:01:36.915759-0500** | **INFO** | User logged in: ibmsayem
**2026-01-13T14:01:36.916016-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.170s
**2026-01-13T14:01:36.937264-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:01:36.938804-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:01:43.197211-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"hello everyone"}
**2026-01-13T14:01:43.200561-0500** | **INFO** | Response: POST /api/posts/ | Status: 422 | Time: 0.003s
**2026-01-13T14:02:15.167924-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:02:15.168617-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:02:15.168693-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:02:16.648759-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:02:16.649495-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:02:16.649563-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:02:21.171580-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:02:21.172282-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:02:21.172353-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:02:40.223568-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:02:40.224298-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:02:40.224365-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:03:20.433955-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"user1","email":"user1@gmail.com","password":"pass1234"}
**2026-01-13T14:03:20.440265-0500** | **INFO** | Registration request received for username: user1, email: user1@gmail.com
**2026-01-13T14:03:20.446311-0500** | **INFO** | Hashing password for user1
**2026-01-13T14:03:20.621154-0500** | **INFO** | Creating new user: user1
**2026-01-13T14:03:20.621244-0500** | **INFO** | Saving user to database: user1
**2026-01-13T14:03:20.623037-0500** | **INFO** | User registered successfully: user1 (ID: 2)
**2026-01-13T14:03:20.623521-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.190s
**2026-01-13T14:03:28.345377-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username":"user1","password":"pass1234"}
**2026-01-13T14:03:28.529512-0500** | **INFO** | User logged in: user1
**2026-01-13T14:03:28.529770-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.184s
**2026-01-13T14:03:28.545544-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:03:28.547124-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:03:34.962509-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"hello everyone!"}
**2026-01-13T14:03:34.975014-0500** | **INFO** | Post created by user1: 1
**2026-01-13T14:03:34.976434-0500** | **INFO** | Response: POST /api/posts/ | Status: 200 | Time: 0.014s
**2026-01-13T14:03:34.987859-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:03:34.990076-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:03:39.538435-0500** | **INFO** | Incoming request: POST /api/posts/1/like | Body: {}
**2026-01-13T14:03:39.541984-0500** | **INFO** | User user1 liked post 1
**2026-01-13T14:03:39.542209-0500** | **INFO** | Response: POST /api/posts/1/like | Status: 200 | Time: 0.004s
**2026-01-13T14:03:39.548618-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:03:39.549373-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:03:47.595195-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"hi"}
**2026-01-13T14:03:47.600224-0500** | **INFO** | Post created by user1: 2
**2026-01-13T14:03:47.600782-0500** | **INFO** | Response: POST /api/posts/ | Status: 200 | Time: 0.006s
**2026-01-13T14:03:47.605649-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:03:47.606880-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:04:25.513108-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:25.513787-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:25.513858-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:29.228204-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:29.228942-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:29.229011-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:30.001410-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:30.002129-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:30.002209-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:33.424019-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:33.424808-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:33.424880-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:35.336260-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:35.337056-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:35.337157-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:37.270257-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:37.271117-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:37.271297-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:39.172031-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:39.172763-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:39.172831-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:40.674371-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:40.675086-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:40.675157-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:42.799204-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:04:42.809653-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.010s
**2026-01-13T14:04:44.296199-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:04:44.298408-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:04:44.785900-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:44.786716-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:44.786811-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:04:49.954700-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:04:49.955425-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:04:49.955571-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:05:18.798352-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:05:18.799073-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:05:18.799150-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:05:30.112010-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:05:30.120218-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.008s
**2026-01-13T14:05:36.631908-0500** | **INFO** | Incoming request: GET /api/users/user1 | Body: empty
**2026-01-13T14:05:36.632851-0500** | **INFO** | Incoming request: GET /api/posts/user/user1 | Body: empty
**2026-01-13T14:05:36.637030-0500** | **INFO** | Response: GET /api/posts/user/user1 | Status: 200 | Time: 0.004s
**2026-01-13T14:05:36.639843-0500** | **INFO** | Response: GET /api/users/user1 | Status: 200 | Time: 0.008s
**2026-01-13T14:05:40.718981-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:05:40.720996-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:05:45.851587-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:05:45.853326-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:05:46.873729-0500** | **INFO** | Incoming request: GET /api/users/user1 | Body: empty
**2026-01-13T14:05:46.874418-0500** | **INFO** | Incoming request: GET /api/posts/user/user1 | Body: empty
**2026-01-13T14:05:46.876374-0500** | **INFO** | Response: GET /api/users/user1 | Status: 200 | Time: 0.003s
**2026-01-13T14:05:46.877043-0500** | **INFO** | Response: GET /api/posts/user/user1 | Status: 200 | Time: 0.003s
**2026-01-13T14:07:57.456833-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:07:57.458154-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:07:57.459831-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:07:57.460937-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:08:50.051103-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:08:50.052601-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:09:10.536507-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:09:10.538943-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:13:54.582280-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:13:54.582978-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:13:54.583047-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:14:04.577079-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:14:04.584559-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.007s
**2026-01-13T14:14:04.587163-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:14:04.588240-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:14:10.381753-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:14:10.385133-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:14:12.246027-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:14:12.247495-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:14:56.231704-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibmsayem","email":"ibm@gmail.com","password":"pass1234","bio":"I am generated by Github copilot"}
**2026-01-13T14:14:56.241428-0500** | **INFO** | Registration request received for username: ibmsayem, email: ibm@gmail.com
**2026-01-13T14:14:56.244672-0500** | **WARNING** | Registration failed: ibmsayem already exists.
**2026-01-13T14:14:56.245694-0500** | **INFO** | Response: POST /api/users/register | Status: 400 | Time: 0.014s
**2026-01-13T14:15:03.997129-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibmsayem","email":"ibm1@gmail.com","password":"pass1234","bio":"I am generated by Github copilot"}
**2026-01-13T14:15:04.001472-0500** | **INFO** | Registration request received for username: ibmsayem, email: ibm1@gmail.com
**2026-01-13T14:15:04.003756-0500** | **WARNING** | Registration failed: ibmsayem already exists.
**2026-01-13T14:15:04.004975-0500** | **INFO** | Response: POST /api/users/register | Status: 400 | Time: 0.008s
**2026-01-13T14:15:07.294458-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibmsayem1","email":"ibm1@gmail.com","password":"pass1234","bio":"I am generated by Github copilot"}
**2026-01-13T14:15:07.295797-0500** | **INFO** | Registration request received for username: ibmsayem1, email: ibm1@gmail.com
**2026-01-13T14:15:07.296815-0500** | **INFO** | Hashing password for ibmsayem1
**2026-01-13T14:15:07.476596-0500** | **INFO** | Creating new user: ibmsayem1
**2026-01-13T14:15:07.476761-0500** | **INFO** | Saving user to database: ibmsayem1
**2026-01-13T14:15:07.479087-0500** | **INFO** | User registered successfully: ibmsayem1 (ID: 3)
**2026-01-13T14:15:07.479588-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.185s
**2026-01-13T14:15:16.994131-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username":"ibmsayem1","password":"pass1234"}
**2026-01-13T14:15:17.179086-0500** | **INFO** | User logged in: ibmsayem1
**2026-01-13T14:15:17.179370-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.185s
**2026-01-13T14:15:17.202310-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:15:17.205142-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:15:17.243890-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:15:17.245265-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:15:21.659005-0500** | **INFO** | Incoming request: POST /api/posts/2/like | Body: {}
**2026-01-13T14:15:21.672045-0500** | **INFO** | User ibmsayem1 liked post 2
**2026-01-13T14:15:21.672872-0500** | **INFO** | Response: POST /api/posts/2/like | Status: 200 | Time: 0.014s
**2026-01-13T14:15:21.682760-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:15:21.685745-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:15:36.972891-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"hello vibe coder!!!"}
**2026-01-13T14:15:36.976114-0500** | **INFO** | Post created by ibmsayem1: 3
**2026-01-13T14:15:36.976422-0500** | **INFO** | Response: POST /api/posts/ | Status: 200 | Time: 0.004s
**2026-01-13T14:15:36.981124-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:15:36.982243-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:15:39.598692-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T14:15:39.599840-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T14:15:39.603488-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.005s
**2026-01-13T14:15:39.605304-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.005s
**2026-01-13T14:16:56.684207-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:16:56.686079-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:21:54.995210-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:21:54.996750-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:21:54.996824-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:22:11.899462-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:22:11.900123-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:22:11.900190-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:24:08.055133-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:24:08.055859-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:24:08.055932-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:24:20.747791-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:20.754541-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.007s
**2026-01-13T14:24:20.757241-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:20.758408-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:24:23.530976-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:23.532841-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:24:26.640933-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T14:24:26.643724-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T14:24:26.653724-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.010s
**2026-01-13T14:24:26.654493-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.014s
**2026-01-13T14:24:35.015073-0500** | **INFO** | Incoming request: PUT /api/users/ibmsayem1 | Body: {"bio":"I am generated by Github copilot"}
**2026-01-13T14:24:35.019392-0500** | **WARNING** | Unauthorized profile update attempt by <app.models.user.User object at 0x107853460> for ibmsayem1
**2026-01-13T14:24:35.019899-0500** | **INFO** | Response: PUT /api/users/ibmsayem1 | Status: 403 | Time: 0.005s
**2026-01-13T14:24:41.680033-0500** | **INFO** | Incoming request: PUT /api/users/ibmsayem1 | Body: {"bio":"I am generated by Github copilot."}
**2026-01-13T14:24:41.681790-0500** | **WARNING** | Unauthorized profile update attempt by <app.models.user.User object at 0x107850520> for ibmsayem1
**2026-01-13T14:24:41.682322-0500** | **INFO** | Response: PUT /api/users/ibmsayem1 | Status: 403 | Time: 0.002s
**2026-01-13T14:24:42.446470-0500** | **INFO** | Incoming request: PUT /api/users/ibmsayem1 | Body: {"bio":"I am generated by Github copilot."}
**2026-01-13T14:24:42.448392-0500** | **WARNING** | Unauthorized profile update attempt by <app.models.user.User object at 0x107ad8c10> for ibmsayem1
**2026-01-13T14:24:42.448987-0500** | **INFO** | Response: PUT /api/users/ibmsayem1 | Status: 403 | Time: 0.003s
**2026-01-13T14:24:44.746515-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:44.750496-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.004s
**2026-01-13T14:24:48.884163-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"hello"}
**2026-01-13T14:24:48.892800-0500** | **INFO** | Post created by ibmsayem1: 4
**2026-01-13T14:24:48.893449-0500** | **INFO** | Response: POST /api/posts/ | Status: 200 | Time: 0.009s
**2026-01-13T14:24:48.898577-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:48.900447-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:24:55.083235-0500** | **INFO** | Incoming request: POST /api/posts/4/like | Body: {}
**2026-01-13T14:24:55.094321-0500** | **INFO** | User ibmsayem1 liked post 4
**2026-01-13T14:24:55.095156-0500** | **INFO** | Response: POST /api/posts/4/like | Status: 200 | Time: 0.012s
**2026-01-13T14:24:55.104151-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:55.107032-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:24:56.326055-0500** | **INFO** | Incoming request: POST /api/posts/3/like | Body: {}
**2026-01-13T14:24:56.328519-0500** | **INFO** | User ibmsayem1 liked post 3
**2026-01-13T14:24:56.328737-0500** | **INFO** | Response: POST /api/posts/3/like | Status: 200 | Time: 0.003s
**2026-01-13T14:24:56.332715-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:56.333807-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:24:58.363930-0500** | **INFO** | Incoming request: POST /api/posts/2/like | Body: {}
**2026-01-13T14:24:58.367497-0500** | **WARNING** | User ibmsayem1 already liked post 2
**2026-01-13T14:24:58.368312-0500** | **INFO** | Response: POST /api/posts/2/like | Status: 400 | Time: 0.004s
**2026-01-13T14:24:59.582258-0500** | **INFO** | Incoming request: POST /api/posts/1/like | Body: {}
**2026-01-13T14:24:59.591242-0500** | **INFO** | User ibmsayem1 liked post 1
**2026-01-13T14:24:59.592242-0500** | **INFO** | Response: POST /api/posts/1/like | Status: 200 | Time: 0.010s
**2026-01-13T14:24:59.601484-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:24:59.604530-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:25:03.866459-0500** | **INFO** | Incoming request: POST /api/posts/1/reply | Body: {"content":"hi"}
**2026-01-13T14:25:03.870317-0500** | **INFO** | User ibmsayem1 replied to post 1
**2026-01-13T14:25:03.870741-0500** | **INFO** | Response: POST /api/posts/1/reply | Status: 200 | Time: 0.004s
**2026-01-13T14:25:03.877695-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:25:03.879092-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:25:15.916545-0500** | **INFO** | Incoming request: POST /api/posts/2/reply | Body: {"content":"hello"}
**2026-01-13T14:25:15.919714-0500** | **INFO** | User ibmsayem1 replied to post 2
**2026-01-13T14:25:15.920035-0500** | **INFO** | Response: POST /api/posts/2/reply | Status: 200 | Time: 0.004s
**2026-01-13T14:25:15.926795-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:25:15.928049-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:26:18.362750-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:26:18.363478-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:26:18.363554-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:26:20.561677-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:26:20.562381-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:26:20.562448-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:26:22.002070-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:22.010207-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.008s
**2026-01-13T14:26:22.012125-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:22.013500-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:26:22.106115-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:22.107513-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:26:23.403414-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:23.405167-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:26:23.406792-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:23.408406-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:26:47.336466-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T14:26:47.337888-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T14:26:47.346143-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.008s
**2026-01-13T14:26:47.346525-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.010s
**2026-01-13T14:26:53.950356-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:53.952341-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:26:59.457194-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:59.458605-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:26:59.562469-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:26:59.564171-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:01.175098-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:01.176673-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:01.353120-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:01.355291-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:03.389928-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:03.391546-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:03.548530-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:03.550811-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:04.914802-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:04.916156-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.001s
**2026-01-13T14:27:05.020063-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:27:05.021745-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:27:48.775742-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:48.776556-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:48.776627-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:50.989486-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:50.990171-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:50.990248-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:51.780093-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:51.780866-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:51.780936-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:54.098893-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:54.099570-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:54.099637-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:55.608765-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:55.609448-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:55.609519-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:56.797769-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:56.798431-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:56.798499-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:27:58.707491-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:27:58.708190-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:27:58.708258-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:28:00.901114-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:28:00.901815-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:28:00.901885-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:28:02.799006-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:28:02.799662-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:28:02.799734-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:28:04.038403-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:28:04.039122-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:28:04.039188-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:28:06.712197-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:06.721163-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.009s
**2026-01-13T14:28:06.813368-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:06.816261-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:28:08.829442-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:08.831812-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:28:08.926876-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:08.927236-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:08.930387-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.004s
**2026-01-13T14:28:08.930992-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.004s
**2026-01-13T14:28:09.041030-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:09.044152-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:28:09.941052-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:09.943330-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:28:10.044804-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:28:10.047069-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:28:25.032625-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T14:28:25.033214-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T14:28:25.041741-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.009s
**2026-01-13T14:28:25.042146-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.010s
**2026-01-13T14:28:29.233650-0500** | **INFO** | Incoming request: PUT /api/users/ibmsayem1 | Body: {"bio":"I am generated by Github copilot"}
**2026-01-13T14:28:29.247946-0500** | **WARNING** | Unauthorized profile update attempt by <app.models.user.User object at 0x10c2f9900> for ibmsayem1
**2026-01-13T14:28:29.249222-0500** | **INFO** | Response: PUT /api/users/ibmsayem1 | Status: 403 | Time: 0.016s
**2026-01-13T14:29:00.123356-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:29:00.124087-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:29:00.124156-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:29:01.936491-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:29:01.937247-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:29:01.937315-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:29:28.327391-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T14:29:28.328247-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T14:29:28.328318-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T14:29:42.010456-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:29:42.019584-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.009s
**2026-01-13T14:29:42.022122-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:29:42.023959-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:29:44.479065-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T14:29:44.479326-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T14:29:44.496044-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.017s
**2026-01-13T14:29:44.499200-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.020s
**2026-01-13T14:29:49.915294-0500** | **INFO** | Incoming request: PUT /api/users/ibmsayem1 | Body: {"bio":"I am generated by Github copilot."}
**2026-01-13T14:29:49.924224-0500** | **INFO** | Profile bio updated for ibmsayem1
**2026-01-13T14:29:49.928359-0500** | **INFO** | Response: PUT /api/users/ibmsayem1 | Status: 200 | Time: 0.013s
**2026-01-13T14:29:51.880244-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:29:51.882879-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:29:54.281027-0500** | **INFO** | Incoming request: GET /api/posts/4/replies | Body: empty
**2026-01-13T14:29:54.283393-0500** | **INFO** | Response: GET /api/posts/4/replies | Status: 200 | Time: 0.002s
**2026-01-13T14:29:58.834113-0500** | **INFO** | Incoming request: POST /api/posts/4/reply | Body: {"content":"hi"}
**2026-01-13T14:29:58.842758-0500** | **INFO** | User ibmsayem1 replied to post 4
**2026-01-13T14:29:58.843280-0500** | **INFO** | Response: POST /api/posts/4/reply | Status: 200 | Time: 0.009s
**2026-01-13T14:29:58.849236-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:29:58.850047-0500** | **INFO** | Incoming request: GET /api/posts/4/replies | Body: empty
**2026-01-13T14:29:58.854256-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.005s
**2026-01-13T14:29:58.855029-0500** | **INFO** | Response: GET /api/posts/4/replies | Status: 200 | Time: 0.005s
**2026-01-13T14:30:03.193143-0500** | **INFO** | Incoming request: POST /api/posts/7/like | Body: {}
**2026-01-13T14:30:03.195953-0500** | **INFO** | User ibmsayem1 liked post 7
**2026-01-13T14:30:03.196164-0500** | **INFO** | Response: POST /api/posts/7/like | Status: 200 | Time: 0.003s
**2026-01-13T14:30:03.201153-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:30:03.204318-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T14:30:04.946255-0500** | **INFO** | Incoming request: POST /api/posts/4/like | Body: {}
**2026-01-13T14:30:04.948913-0500** | **WARNING** | User ibmsayem1 already liked post 4
**2026-01-13T14:30:04.949618-0500** | **INFO** | Response: POST /api/posts/4/like | Status: 400 | Time: 0.003s
**2026-01-13T14:30:59.522581-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:30:59.524518-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:30:59.625491-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:30:59.627581-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:31:02.039430-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:31:02.041566-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T14:31:02.145396-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T14:31:02.147870-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T16:05:50.593080-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T16:05:50.596807-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T16:05:50.596894-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T16:06:06.185514-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:06.200016-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.015s
**2026-01-13T16:06:06.202579-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:06.204354-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T16:06:07.994655-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:07.997272-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T16:06:10.388242-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:10.391260-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T16:06:16.383223-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T16:06:16.385509-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T16:06:16.399154-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.016s
**2026-01-13T16:06:16.401035-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.016s
**2026-01-13T16:06:22.057823-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:22.060133-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T16:06:25.058037-0500** | **INFO** | Incoming request: GET /api/users/user1 | Body: empty
**2026-01-13T16:06:25.059519-0500** | **INFO** | Incoming request: GET /api/posts/user/user1 | Body: empty
**2026-01-13T16:06:25.061504-0500** | **INFO** | Response: GET /api/users/user1 | Status: 200 | Time: 0.003s
**2026-01-13T16:06:25.062028-0500** | **INFO** | Response: GET /api/posts/user/user1 | Status: 200 | Time: 0.003s
**2026-01-13T16:06:48.269954-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:06:48.272064-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T16:09:43.910619-0500** | **INFO** | Incoming request: GET /api/users/user1 | Body: empty
**2026-01-13T16:09:43.911981-0500** | **INFO** | Incoming request: GET /api/posts/user/user1 | Body: empty
**2026-01-13T16:09:43.914806-0500** | **INFO** | Response: GET /api/users/user1 | Status: 200 | Time: 0.004s
**2026-01-13T16:09:43.916130-0500** | **INFO** | Response: GET /api/posts/user/user1 | Status: 200 | Time: 0.004s
**2026-01-13T16:09:50.173604-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:09:50.175732-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T16:16:49.218844-0500** | **INFO** | Incoming request: GET /api/users/ibmsayem1 | Body: empty
**2026-01-13T16:16:49.219840-0500** | **INFO** | Incoming request: GET /api/posts/user/ibmsayem1 | Body: empty
**2026-01-13T16:16:49.224814-0500** | **INFO** | Response: GET /api/users/ibmsayem1 | Status: 200 | Time: 0.006s
**2026-01-13T16:16:49.228591-0500** | **INFO** | Response: GET /api/posts/user/ibmsayem1 | Status: 200 | Time: 0.009s
**2026-01-13T16:16:53.014052-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:16:53.016938-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T16:27:04.341837-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:27:04.346273-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.004s
**2026-01-13T16:27:04.355867-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T16:27:04.358933-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T17:07:07.744023-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T17:07:07.744701-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T17:07:07.744768-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T17:07:12.478733-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T17:07:12.479406-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T17:07:12.479470-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T17:15:15.762729-0500** | **INFO** | Backend startup: Creating database tables...
**2026-01-13T17:15:15.763511-0500** | **INFO** | Database tables created/verified successfully.
**2026-01-13T17:15:15.763619-0500** | **INFO** | Backend server started and ready to accept requests.
**2026-01-13T17:15:31.668093-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:15:31.678598-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.011s
**2026-01-13T17:15:31.682112-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:15:31.684652-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T17:15:36.358511-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:15:36.361087-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T17:16:17.695429-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibrahim sayem","email":"abc@gmail.com","password":"password1234","bio":"Computer Science PhD student."}
**2026-01-13T17:16:17.707452-0500** | **INFO** | Registration request received for username: ibrahim sayem, email: abc@gmail.com
**2026-01-13T17:16:17.710820-0500** | **WARNING** | Registration failed: ibrahim sayem already exists.
**2026-01-13T17:16:17.711924-0500** | **INFO** | Response: POST /api/users/register | Status: 400 | Time: 0.017s
**2026-01-13T17:16:28.007430-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibm sayem","email":"abc@gmail.com","password":"password1234","bio":"Computer Science PhD student."}
**2026-01-13T17:16:28.008405-0500** | **INFO** | Registration request received for username: ibm sayem, email: abc@gmail.com
**2026-01-13T17:16:28.008952-0500** | **WARNING** | Registration failed: ibm sayem already exists.
**2026-01-13T17:16:28.009293-0500** | **INFO** | Response: POST /api/users/register | Status: 400 | Time: 0.002s
**2026-01-13T17:16:29.639952-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibm sayem","email":"abc@gmail.com","password":"password1234","bio":"Computer Science PhD student."}
**2026-01-13T17:16:29.642362-0500** | **INFO** | Registration request received for username: ibm sayem, email: abc@gmail.com
**2026-01-13T17:16:29.644606-0500** | **WARNING** | Registration failed: ibm sayem already exists.
**2026-01-13T17:16:29.645641-0500** | **INFO** | Response: POST /api/users/register | Status: 400 | Time: 0.006s
**2026-01-13T17:16:55.574760-0500** | **INFO** | Incoming request: POST /api/users/register | Body: {"username":"ibm sayem","email":"ibmsayem@waterloo.com","password":"password1234","bio":"Computer Science PhD student."}
**2026-01-13T17:16:55.576229-0500** | **INFO** | Registration request received for username: ibm sayem, email: ibmsayem@waterloo.com
**2026-01-13T17:16:55.577123-0500** | **INFO** | Hashing password for ibm sayem
**2026-01-13T17:16:55.762918-0500** | **INFO** | Creating new user: ibm sayem
**2026-01-13T17:16:55.763109-0500** | **INFO** | Saving user to database: ibm sayem
**2026-01-13T17:16:55.766188-0500** | **INFO** | User registered successfully: ibm sayem (ID: 4)
**2026-01-13T17:16:55.766650-0500** | **INFO** | Response: POST /api/users/register | Status: 200 | Time: 0.192s
**2026-01-13T17:17:08.907085-0500** | **INFO** | Incoming request: POST /api/users/login | Body: {"username":"ibm sayem","password":"password1234"}
**2026-01-13T17:17:09.111317-0500** | **INFO** | User logged in: ibm sayem
**2026-01-13T17:17:09.111618-0500** | **INFO** | Response: POST /api/users/login | Status: 200 | Time: 0.205s
**2026-01-13T17:17:09.126471-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:17:09.128449-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T17:17:09.193463-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:17:09.195636-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T17:17:12.699157-0500** | **INFO** | Incoming request: GET /api/users/ibm sayem | Body: empty
**2026-01-13T17:17:12.700185-0500** | **INFO** | Incoming request: GET /api/posts/user/ibm sayem | Body: empty
**2026-01-13T17:17:12.707826-0500** | **INFO** | Response: GET /api/users/ibm sayem | Status: 200 | Time: 0.009s
**2026-01-13T17:17:12.710178-0500** | **INFO** | Response: GET /api/posts/user/ibm sayem | Status: 200 | Time: 0.010s
**2026-01-13T17:17:20.853408-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:17:20.859351-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.006s
**2026-01-13T17:17:28.937931-0500** | **INFO** | Incoming request: POST /api/posts/ | Body: {"content":"Hello CS846"}
**2026-01-13T17:17:28.942389-0500** | **INFO** | Post created by ibm sayem: 8
**2026-01-13T17:17:28.942725-0500** | **INFO** | Response: POST /api/posts/ | Status: 200 | Time: 0.005s
**2026-01-13T17:17:28.948863-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:17:28.951075-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.002s
**2026-01-13T17:17:33.869354-0500** | **INFO** | Incoming request: POST /api/posts/8/like | Body: {}
**2026-01-13T17:17:33.875603-0500** | **INFO** | User ibm sayem liked post 8
**2026-01-13T17:17:33.876014-0500** | **INFO** | Response: POST /api/posts/8/like | Status: 200 | Time: 0.007s
**2026-01-13T17:17:33.881479-0500** | **INFO** | Incoming request: GET /api/posts/feed | Body: empty
**2026-01-13T17:17:33.884621-0500** | **INFO** | Response: GET /api/posts/feed | Status: 200 | Time: 0.003s
**2026-01-13T17:17:34.765355-0500** | **INFO** | Incoming request: POST /api/posts/8/like | Body: {}
**2026-01-13T17:17:34.767180-0500** | **WARNING** | User ibm sayem already liked post 8
**2026-01-13T17:17:34.767687-0500** | **INFO** | Response: POST /api/posts/8/like | Status: 400 | Time: 0.002s
