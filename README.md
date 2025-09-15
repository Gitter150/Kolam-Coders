# Kolam Koders

[cite_start]An exploration into the mathematical DNA of traditional Kolam art, developed for the Smart India Hackathon 2025[cite: 1, 12]. [cite_start]This project aims to analyze the design principles of Kolams and procedurally generate new, authentic designs[cite: 4].

- [cite_start]**Event:** Smart India Hackathon 2025 [cite: 1, 12]
- [cite_start]**Problem Statement ID:** SIH12507 [cite: 2]
- [cite_start]**Theme:** Heritage and Culture [cite: 5]

## Core Features

Our solution is divided into two main components:

1.  **Analysis Engine**: Upload an image of a Kolam, and the program will extract its fundamental design principles, such as:
    * [cite_start]Grid structure and dot matrix [cite: 23, 28]
    * [cite_start]Symmetry type (rotational, reflectional) [cite: 25, 28]
    * [cite_start]Stroke and path patterns [cite: 28, 51]
2.  [cite_start]**Generation Engine**: Specify a set of mathematical rules (e.g., "7x7 grid, 4-fold rotational symmetry, single stroke"), and the program will generate a valid, high-resolution Kolam that adheres to them[cite: 26, 29].

## Tech Stack

-   **Backend**: Python
-   [cite_start]**Frontend**: HTML5 Canvas [cite: 42]
-   **Key Python Libraries**:
    -   [cite_start]OpenCV (Image Processing) [cite: 43]
    -   [cite_start]NumPy (Computation) [cite: 43]
    -   [cite_start]Matplotlib/PIL (Image Generation) [cite: 43]
    -   [cite_start]SciPy (Geometric Algorithms) [cite: 43]
    -   [cite_start]NetworkX (Graph-based Path Analysis) [cite: 43]

## Getting Started

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/Kolam.git](https://github.com/your-username/Kolam.git)
    cd Kolam
    ```

2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```sh
        py -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

*(Instructions on how to run your Flask server will go here once it's built)*