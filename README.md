#  Project Tracker CLI

A comprehensive command-line project management tool for development teams to efficiently manage users, projects, and tasks with persistent data storage.


### Core Functionality
- **User Management**: Create, list, and manage system users with email validation
- ** Project Management**: Create projects with descriptions, due dates, and ownership
- ** Task Management**: Add tasks to projects, assign to users, track completion status
- ** Data Persistence**: Automatic save/load using JSON files for all data
- ** Search & Filter**: View projects by user, tasks by project
- ** Progress Tracking**: Automatic completion percentage calculation for projects

### Technical Features
- **Object-Oriented Design**: Clean class hierarchy with inheritance and encapsulation
- **Relationship Management**: One-to-many (User→Projects) and many-to-many (Projects→Tasks)
- **Data Validation**: Email format validation, date validation, required field checks
- **Error Handling**: Comprehensive try-catch blocks for file operations
- **Beautiful CLI Output**: Rich formatting with colors, tables, and panels
- **Backup System**: One-command backup of all data files
- **Unit Testing**: Complete test suite for all models

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- pipenv (recommended) or pip

### Installation

#### Option 1: Using pipenv (Recommended)

```bash
# Clone or download the project
git clone <your-repo-url>
cd project_tracker

# Install pipenv if not already installed
pip install pipenv

# Install dependencies and create virtual environment
pipenv install

# Activate virtual environment
pipenv shell
