# True Blogs

True Blogs is a simple blog web application where users can create, edit, and manage blog posts.  
It allows users to share ideas, write articles, and read posts from other users in a clean and organized interface.

---

## Features

- User Registration and Login
- Create Blog Posts
- Edit Existing Posts
- Delete Blog Posts
- View Blogs Posted by Other Users
- Comment on Blog Posts
- Secure Authentication System

---

## Tech Stack

- **Backend:** Python  
- **Framework:** Flask  
- **Database:** MySQL  
- **Frontend:** HTML, CSS  
- **ORM:** SQLAlchemy

---

## Project Structure

```
TrueBlogs/
│
├── app.py
├── database.py
├── models.py
├── routes/
├── templates/
├── static/
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/priyanshu20051112/True-Blogs.git
cd TrueBlogs
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create environment variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

### 4. Run the application

```bash
python app.py
```

The application will run on:

```
http://localhost:5000
```

---

## Future Improvements

- Blog search functionality
- User profile pages
- Like and bookmark system
- Rich text editor for blogs
- Image uploads for blog posts

---

## Author

**Priyanshu Upadhyay**

---

## License

This project is for learning and educational purposes.
