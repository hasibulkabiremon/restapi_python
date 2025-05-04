# Learning Django REST Framework

## Description
This project is a learning exercise to explore and understand the Django REST Framework. It includes basic setup and examples to demonstrate the core features of the framework.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the development server:
   ```bash
   python manage.py runserver
   ```
2. Access the API endpoints at `http://localhost:8000/`.

## Contributing
This project is primarily for personal learning. However, if you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact Information
For questions or feedback, please contact [Your Name] at [Your Email].

## Project Structure

### `drf` Directory
The `drf` directory contains the core configuration files for the Django project. It includes:

- `asgi.py`: The ASGI configuration for the project, which allows for asynchronous communication.
- `settings.py`: The main settings file for the Django project, containing configurations like installed apps, middleware, and database settings.
- `urls.py`: The URL configuration file, which routes URLs to the appropriate views.
- `views.py`: Contains view functions that handle requests and return responses.
- `wsgi.py`: The WSGI configuration for the project, used for deploying the application.
- `__init__.py`: An empty file that indicates the directory is a Python package.

### `drfapp` Directory
The `drfapp` directory is a Django app within the project. It includes:

- `admin.py`: Configuration for the Django admin interface.
- `apps.py`: Configuration for the app itself.
- `migrations/`: A directory containing database migration files.
- `models.py`: Defines the data models for the app.
- `serializers.py`: Contains serializers for converting complex data types to native Python data types.
- `tests.py`: Contains test cases for the app.
- `views.py`: Contains view functions specific to this app.
- `__init__.py`: An empty file that indicates the directory is a Python package.
