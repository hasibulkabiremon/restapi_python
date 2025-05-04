# Build REST API with Flask

## Description
This project is a Flask-based REST API for managing travel destinations. It provides endpoints to create, read, update, and delete destination records in a SQLite database.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```
3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv env
   ```
4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
5. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. **Database Setup**:
   - The application uses SQLite as the database. The database file `travel.db` will be created automatically when the application is run.

2. **Run the Development Server**:
   - Start the server to establish a connection:
     ```bash
     flask run
     ```
   - Access the application at `http://localhost:5000/` to verify a successful connection.

## API Endpoints
- **GET /destinations**: Retrieve a list of all destinations.
- **GET /destinations/<int:destination_id>**: Retrieve a specific destination by ID.
- **POST /destinations**: Add a new destination. Requires a JSON body with `destination`, `country`, and `rating`.
- **PUT /destinations/<int:destination_id>**: Update an existing destination by ID. Accepts partial updates.
- **DELETE /destinations/<int:destination_id>**: Delete a destination by ID.

## Successful Connection
- A successful connection is indicated by the ability to access the application in a web browser and interact with the API endpoints without errors.

## Contact Information
For questions or feedback, please contact [Your Name] at [Your Email].
