# Doctor Appointment Multi-Agent System

## Overview

The **Doctor Appointment Multi-Agent System** is an intelligent, multi-agent framework designed to streamline the process of scheduling and managing doctor appointments. By leveraging advanced AI techniques, this system facilitates efficient interactions between patients, doctors, and administrators, ensuring a seamless experience for all users.

## Features

* **Multi-Agent Architecture**: Utilizes multiple agents to handle different roles and tasks within the system.
* **Streamlined Appointment Scheduling**: Simplifies the process of booking, viewing, and managing appointments.
* **Role-Based Access Control**: Differentiates functionalities and access levels for patients, doctors, and administrators.
* **User-Friendly Interface**: Provides an intuitive interface for all user roles to interact with the system effectively.

<img width="490" height="249" alt="WorkFlow" src="https://github.com/user-attachments/assets/66c1ef7c-1671-430f-80ab-fbbdb42a71bf" />


## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ganesh-xvi/Doctor-Appointment-Multi-Agent-System.git
   cd Doctor-Appointment-Multi-Agent-System
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   uvicorn main:app --reload --port 8003
   ```

   Alternatively, for the Streamlit interface:

   ```bash
   python -m streamlit run streamlit_ui.py
   ```

## Usage

Once the application is running, you can access the system through the provided interface. Depending on your role (patient, doctor, or administrator), you will have access to different functionalities, such as booking appointments, managing schedules, and viewing appointment histories.

## File Structure

* `main.py`: The main entry point for the application.
* `streamlit_ui.py`: The user interface built using Streamlit.
* `agent.py`: Contains the logic for the multi-agent system.
* `requirements.txt`: Lists the dependencies required for the project.
* `setup.py`: Contains setup configurations for the project.
* `data/`: Directory containing data files.
* `data_models/`: Directory for data models.
* `notebook/`: Jupyter notebooks for experimentation and analysis.
* `preprocess/`: Scripts for data preprocessing.
* `toolkit/`: Utility functions and classes.
* `utils/`: Additional helper functions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or have found a bug, please open an issue or submit a pull request. Ensure that your contributions align with the project's goals and follow the existing coding standards.
