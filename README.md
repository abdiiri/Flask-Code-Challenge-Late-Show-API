# Late Show API

A Flask REST API for managing a Late Night TV show system.

---

## 📦 Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Setup

- Ensure PostgreSQL is installed and running.
- Create the database:

```bash
sudo -u postgres createdb late_show_db
```

### 4. Configure Database URI

Edit `server/config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

Replace `<user>` and `<password>` with your PostgreSQL credentials.

### 5. Run Migrations and Seed Data

```bash
export FLASK_APP=server.app
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 6. Run the Server

```bash
flask run
```

---

## 🔐 Authentication Flow

- **Register:** `POST /register` with `username` and `password`.
- **Login:** `POST /login` with `username` and `password` to receive a JWT token.
- **Protected routes:** Send `Authorization: Bearer <token>` header.

---

## 🛣️ API Routes

| Route                  | Method | Auth Required | Description                       |
|------------------------|--------|---------------|-----------------------------------|
| /register              | POST   | ❌            | Register a user                   |
| /login                 | POST   | ❌            | Log in and get JWT token          |
| /episodes              | GET    | ❌            | List episodes                     |
| /episodes/<id>         | GET    | ❌            | Get episode + appearances         |
| /episodes/<id>         | DELETE | ✅            | Delete episode + appearances      |
| /guests                | GET    | ❌            | List guests                       |
| /appearances           | POST   | ✅            | Create appearance                 |

---

## 🧪 Postman Usage

1. Import `challenge-4-lateshow.postman_collection.json` into Postman.
2. Use the `/register` and `/login` endpoints to create a user and obtain a JWT token.
3. For protected routes, set the `Authorization` header to `Bearer <your_token>`.
4. Test all endpoints as described above.

---

## 📝 Sample Requests & Responses

### Register

**Request:**  
POST `/register`
```json
{
  "username": "testuser",
  "password": "testpass"
}
```
**Response:**  
```json
{
  "message": "User registered successfully"
}
```

### Login

**Request:**  
POST `/login`
```json
{
  "username": "testuser",
  "password": "testpass"
}
```
**Response:**  
```json
{
  "access_token": "<JWT_TOKEN>"
}
```

### Get Episodes

**Request:**  
GET `/episodes`

**Response:**  
```json
[
  {
    "id": 1,
    "date": "2024-06-22",
    "number": 1,
    "appearances": [...]
  }
]
```

---

## 🛠️ Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL

---

## 📚 Documentation

- All endpoints return JSON.
- Errors are returned as JSON with an `error` key.
- JWT token must be included in the `Authorization` header for protected routes.

---

## 🔗 GitHub Repository

[https://github.com/<your-username>/late-show-api-challenge](https://github.com/<your-username>/late-show-api-challenge)

---

## 💡 Notes

- Ensure PostgreSQL is running before running migrations or the server.
- All migrations and seeds must be run before using the API.
- For any issues, check the Flask server logs for error details.

---