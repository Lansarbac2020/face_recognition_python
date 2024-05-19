
# Real-Time Face Attendance System

## Overview
This project implements a real-time face attendance system integrated with a backend database. The system allows for the automatic recognition of students' faces during attendance sessions and updates the database in real-time with pertinent information such as ID number, student name, and last attendance time.

## Features
- Real-time face recognition for attendance tracking.
- Integration with a real-time database to store student information.
- Automatic updating of the database with attendance records.
- Easy-to-use interface for administrators to manage attendance data.

## Tools Used
- **OpenCV**: Utilized for real-time face detection and recognition.
- **dlib**: Used for its facial recognition capabilities.
- **face_recognition**: A high-level face recognition library built on top of dlib.
- **cmake**: A cross-platform tool for building, testing, and packaging software.
- **Firebase**: Integrated for real-time database functionality.
- **cvzone**: A computer vision library built on top of OpenCV for easy implementation of advanced vision tasks.

## Installation
 Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that your environment meets the hardware requirements for real-time face recognition (e.g., a webcam).
2. Run the main application:
   ```
   python main.py
   ```

## Configuration
- Modify the database connection settings in `main.py` and `env` file to match your environment.
- Adjust face recognition parameters in `config.py` for optimal performance.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.
7. lansarbacoro@gmail.com

