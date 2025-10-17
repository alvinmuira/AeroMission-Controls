# 🚀 AeroMissions Controls CLI

**AeroMissions Controls** is a **Command-Line Interface (CLI)** application designed to manage **Missions**, **Engineers**, and **Equipment** data efficiently.  
It provides a structured way to create, update, assign, and view mission-related records ; ideal for aerospace or technical project management systems.

---

## ⚙️ Overview

The system is built with **Python**, using **SQLite** as the database and an **Object-Relational Mapping (ORM)** structure to simplify data interactions.  
Each entity (Mission, Engineer, Equipment) is represented as a Python class with validation, relationships, and ORM methods such as `create()`, `delete()`, `get_all()`, and `find_by_id()`.

---

## ✨ Features

The program offers several core features for managing mission data:

1. **Create**
   - Allows the user to input new records for Missions, Engineers, or Equipment.
   - Validates inputs to ensure data accuracy.

2. **Delete**
   - Enables the removal of any record and its related data (such as mission equipment or engineer assignments).

3. **Update**
   - Modify existing records directly from the CLI.

4. **View Table Data**
   - Displays all saved records from any selected table.

5. **Search**
   - Find specific entries by name, ID, or related field.

6. **Mission Resources**
   - View all relevant data linked to a mission, including assigned engineers and associated equipment.

7. **Assign**
   - Assign engineers or equipment to missions easily, maintaining proper database relationships.

---

## 🧩 Relationships

- **One-to-Many:**  
  - A single **Mission** can have multiple **Equipment** items.  

- **Many-to-Many:**  
  - **Engineers** can be assigned to multiple **Missions**, and each **Mission** can have multiple **Engineers** — managed via an `engineer_mission` join table.

---

## 🧠 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python |
| **Database** | SQLite |
| **ORM** | Custom ORM classes (no external libraries) |
| **CLI Framework** | Click |
| **Environment** | Pipenv virtual environment |

---

## 📁 Project Structure

``` bash
AeroMission-Controls/
├── lib/
| |
│ ├── init.py
│ ├── cli
| | ├── init.py
| | ├── cli.py
| | ├── cli_helpers
| | | ├── init.py
| | | ├── create_helper.py
| | | ├── delete_helper.py
| | | ├── update_helper.py
| | | ├── view_helper.py
| | | ├── search_helper.py
| | | ├── view_mission_resources_helper.py
| | | ├── assign_helper.py
| | ├── models
| | | ├── init.py
| | | ├── mission.py
| | | ├── engineer.py
| | | ├── equipment.py
| | | ├── engineer_mission.py
├── db_setup.py
├── database.db
└── README.md
├── main.py
├── .gitignore
├── requirements.txt
```

## 🧰 Setup & Usage

### 1. Clone the Repository
```bash
git clone <your_repo_url>
cd AeroMission-Controls
```
### 2. Navigate and activate Virtual Enviroment
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependancies
```bash
pip install -r requirements.txt
```
### 4. Activate the CLI
```bash
python main.py
```
## 🧾 License
This project was developed as part of the Phase 3 Project to demonstrate ORM integration, data relationships, and Python CLI design.

## Author
**Alvin Muira**
