# Background Remover Project


This project provides a real-time background removal tool for a webcam feed using Python, OpenCV, and the CVzone library. It replaces your background with a custom image of your choice, allows you to capture snapshots, and logs the captured images.

## Features

-   **Real-time Background Removal**: Utilizes the `SelfiSegmentationModule` from CVzone to remove the background from a live webcam feed.
-   **Custom Backgrounds**: Choose any image from the `Backgrounds` folder to serve as your virtual background.
-   **Add New Backgrounds**: Interactively add new background images to the `Backgrounds` folder directly from the command line when starting the application.
-   **Image Capture**: Save the current frame with the virtual background as a JPG image.
-   **Capture Logging**: Automatically logs details of every captured image, including a timestamp, filename, and the background used, in a CSV file.

## Getting Started

### Prerequisites

-   Python 3.11.9
-   A webcam connected to your computer.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/pavi040315/background-remover-project.git
    cd background-remover-project
    ```

2.  **Install the required Python libraries:**
    ```sh
    pip install opencv-python cvzone numpy
    ```

## Usage

1.  **Add Background Images**: Place your desired background images (e.g., `.jpg`, `.png`) into the `Backgrounds` directory. The script will automatically create this folder on first run if it doesn't exist.

2.  **Run the script:**
    ```sh
    python program.py
    ```

3.  **Follow the on-screen prompts:**
    -   The script will first ask if you want to add a new background image from a specific file path. You can add as many as you like.
    -   Next, it will list all available backgrounds in the `Backgrounds` folder and prompt you to select one by entering its full filename (e.g., `beach.jpg`).

4.  **Interact with the application window:**
    -   A window will open, displaying your original webcam feed side-by-side with the feed featuring the replaced background.
    -   Press `s` to save a snapshot of the current view with the replaced background. The image will be saved in the `Captured_Images` folder.
    -   Press `q` to quit the application.

## Directory Structure

-   `program.py`: The main Python script that runs the application.
-   `Backgrounds/`: This directory stores the image files used for virtual backgrounds.
-   `Captured_Images/`: All captured snapshots are saved in this directory with a timestamp in the filename.
-   `CSV Files/`:
    -   `capture_log.csv`: A log file that records the timestamp, file path, and background used for each captured image.
