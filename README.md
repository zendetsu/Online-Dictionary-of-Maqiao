# Online-Dictionary-of-Maqiao
Columbia University - China in the Modern World (jp4371)

# Online Dictionary of Maqiao

Welcome to the **Online Dictionary of Maqiao Dictionary** – an online dictionary application inspired by the vocabulary and cultural richness of Maqiao, based on the book by Han Shaogong. This web app allows users to browse, search for, and explore words, definitions, examples, and related terms.

---

## 🚀 Features

- Search for specific words and view related details.
- Display definitions, examples, and page numbers for clarity.
- Responsive and clean UI for ease of use.

---

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3
- **Hosting**: Local Development / Ready for Deployment

---

## ⚙️ Installation and Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd maqiao_project
```

### 2. Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On MacOS/Linux
env\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note**: Generate `requirements.txt` if missing:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Configure the Database
- Make sure **PostgreSQL** is installed and running.
- Create a database:
   ```sql
   CREATE DATABASE maqiao_db;
   ```
- Update the database URI in `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost/maqiao_db'
   ```

### 5. Initialize and Migrate Database
```bash
flask db init
flask db migrate -m "Initial migration - create dictionary_entry table"
flask db upgrade
```

### 6. Add Initial Entries
Run the script to populate the database:
```bash
python add_entries.py
```

### 7. Start the Application
```bash
python app.py
```

Visit the app in your browser at: **`http://127.0.0.1:5000`**

---

## 📁 Project Structure

```
maqiao_project/
│
├── app.py               # Flask application
├── add_entries.py       # Script to add initial dictionary entries
├── requirements.txt     # Project dependencies
├── migrations/          # Database migration files
├── templates/           # HTML templates
│   ├── home.html
│   ├── search.html
│
├── static/              # Static assets
│   ├── styles.css       # CSS file for styling
│   ├── images/          # Image assets
│
└── README.md            # Project documentation
```

---

## 🎨 Aesthetic Notes
- The app features **Courier New** for buttons and **Arial** for body text.
- Color palette inspired by **#8B0000 (Dark Red)** for a traditional and clean look.
- Images are appropriately scaled and centered.

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.
=======

>>>>>>> 5ebf183 (Initial commit - Maqiao Dictionary Project)
