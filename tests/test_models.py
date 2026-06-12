from app.models import User, Project, Task


def test_user_to_dict():
    user = User(1, "Roy", "RoyG@example.com")

    assert user.to_dict() == {
        "user_id": 1,
        "name": "Roy",
        "email": "RoyG@example.com"
    }


def test_project_to_dict():
    project = Project(1, "CLI Tracker", "Manage projects", 1)

    assert project.to_dict() == {
        "project_id": 1,
        "title": "CLI Tracker",
        "description": "Manage projects",
        "user_id": 1
    }


def test_task_to_dict():
    task = Task(1, "Create models", 1, ["Roy"], False)

    assert task.to_dict() == {
        "task_id": 1,
        "title": "Create models",
        "project_id": 1,
        "contributors": ["Roy"],
        "completed": False
    }


def test_mark_task_complete():
    task = Task(1, "Create models", 1)

    task.mark_complete()

    assert task.completed is True