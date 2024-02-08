# A Django Project

This is a personal Django project built to learn Django

![Wakatime badge(Time tracker)](https://wakatime.com/badge/user/a834cc3a-cc0a-4aa3-83a4-a825e4e9c3bf/project/018bf9fa-01fa-443d-b4c4-11947b759d23.svg)

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Emaryllis/A-Django-Project.git
    cd A-Django-Project-master
    ```

2. **Create a Virtual Environment:**
    ```bash
    py -m venv venv
    ```

3. **Activate the Virtual Environment:**
    - On Unix/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
      or
      ```bash
       ./activate
      ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations & Run the Development Server:**
    ```bash
    py manage.py migrate
    py manage.py runserver
    ```
   or
   ```bash
   ./start-server
   ```

6. **Access the Application:**
   Open your web browser and go to [http://localhost:8000/](http://localhost:8000/)
