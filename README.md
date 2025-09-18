# Kolam Koders

An exploration into the mathematical DNA of traditional Kolam art, developed for the Smart India Hackathon 2025. This project uses a modular system of motifs and a symmetry engine to procedurally generate new, authentic, and complex Kolam designs from a simple seed value.

- **Event:** Smart India Hackathon 2025
- **Problem Statement ID:** SIH12507
- **Theme:** Heritage and Culture



## Core Features

- **Procedural Generation Engine**: Specify a seed value (any text or number) to generate a unique, intricate, and aesthetically pleasing Kolam. The engine combines a library of artistic motifs with a 4-fold symmetry system to create dense and beautiful patterns.
- **Web Interface**: A clean, simple web UI built with Flask to interact with the generator. Enter a seed, generate a Kolam in real-time, and download the high-resolution result.
- **Analysis Engine (MVP)**: A proof-of-concept analyzer that can determine the grid size and primary symmetries of a clean, digital Kolam image.

## Tech Stack

-   **Backend**: Python, Flask
-   **Core Python Libraries**:
    -   Matplotlib
    -   NumPy
    -   OpenCV

## Getting Started

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/Kolam.git
    cd Kolam
    ```

2.  **Create and activate a virtual environment:**
    -   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   On Windows:
        ```sh
        py -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

---

### Running the Application

1.  **Start the Flask web server:**
    ```sh
    python app.py
    ```

2.  **Open your web browser:**
    Navigate to the local address provided in the terminal, which will be:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

3.  **Generate a Kolam:**
    Enter any text or number into the seed input box and click the "Generate Kolam" button. The generated image will appear below, with an option to download it.