# Project Tracker CLI

A command-line project management tool for team developers to manage users, projects, and tasks.

## Features

- **User Management**: Create and list users with email validation
- **Project Management**: Create projects with due dates and assign to users
- **Task Management**: Add tasks to projects, assign to users, mark as complete
- **Data Persistence**: Automatic saving/loading using JSON files
- **Beautiful CLI Output**: Rich formatting with colors and tables
- **Relationship Management**: One-to-many (User->Projects) and many-to-many (Projects->Tasks)

## Installation

### Prerequisites
- Python 3.8 or higher
- pipenv (recommended) or pip

### Setup with pipenv (Recommended)

```bash
# Install pipenv if not already installed
pip install pipenv

# Clone or create project directory
cd project_tracker

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell
