<div align="center">
<h1>SQLite User Management CLI</h1>
</div>

## 👩‍💻 Tech Stack
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff)](#)
[![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](#)
[![Pytest](https://img.shields.io/badge/Pytest-fff?style=for-the-badge&logo=pytest&logoColor=000)](#)

## 💡 Overview

This project is a command-line user management system built with Python and SQLite.  
It implements authentication, session management, and role-based access control through a secure CLI interface.

The application follows a layered architecture with controllers, services, repositories, and domain models, demonstrating backend best practices such as password hashing, input validation, and automated testing.

## ✨ Features
- User authentication system
- Role-based access control (admin / user)
- User management (CRUD)
- Secure password hashing with bcrypt
- Session lifecycle management
- Automatic admin seeding
- SQLite data persistence
- CLI interface with interactive menus
- Custom exception handling
- Automated tests with pytest

## 🏗️ Architecture

The project follows a layered architecture:

- **UI** – CLI interface
- **Controllers** – Application flow orchestration
- **Services** – Business logic
- **Repositories** – Data access layer
- **Domain** – Entities and enums

## 📂 Project Structure

```
sqlite-user-management-cli
├── app/
│   ├── controllers/
│   │   └── app_controller.py
│   ├── database/
│   │   ├── seeds/
│   │   │   └── admin_seed.py
│   │   ├── connection.py
│   │   └── migrations.py
│   ├── domain/
│   │   ├── session_active.py
│   │   ├── session.py
│   │   ├── user.py
│   │   └── user_role.py
│   ├── exceptions/
│   │   └── user_exceptions.py
│   ├── repositories/
│   │   ├── session_repository.py
│   │   └── user_repository.py
│   ├── services/
│   │   ├── password_service.py
│   │   ├── session_service.py
│   │   └── user_service.py
│   ├── ui/
│   │   ├── cli.py
│   │   ├── menus.py
│   │   └── prompts.py
│   └── utils/
│       └── terminal.py
├── tests/
│   ├── repositories/
│   │   ├── test_session_repository.py
│   │   └── test_user_repository.py
│   ├── services/
│   │   ├── test_session_service.py
│   │   └── test_user_service.py
│   └── conftest.py
├── main.py
└── pyproject.toml
```

## 🛠️ Installation

### 1. Clone the repository
```
git clone https://github.com/prodsimu/sqlite-user-management-cli.git
cd sqlite-user-management-cli
```

### 2. Install dependencies
```
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### 3. Run the application
```
python3 main.py
```
