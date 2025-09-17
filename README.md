# Kolam Koders

An exploration into the mathematical DNA of traditional Kolam art, developed for the Smart India Hackathon 2025.  
This project aims to analyze the design principles of Kolams and procedurally generate new, authentic designs.

- **Event:** Smart India Hackathon 2025  
- **Problem Statement ID:** SIH12507  
- **Theme:** Heritage and Culture  

## Core Features

Our solution is divided into two main components:

1.  **Analysis Engine**: Upload an image of a Kolam, and the program will extract its fundamental design principles, such as:
    * Grid structure and dot matrix  
    * Symmetry type (rotational, reflectional)  
    * Stroke and path patterns  
2.  **Generation Engine**: Specify a set of mathematical rules (e.g., "7x7 grid, 4-fold rotational symmetry, single stroke"), and the program will generate a valid, high-resolution Kolam that adheres to them.

## Tech Stack

-   **Backend**: Python  
-   **Frontend**: HTML5 Canvas  
-   **Key Python Libraries**:  
    -   OpenCV (Image Processing)  
    -   NumPy (Computation)  
    -   Matplotlib/PIL (Image Generation)  
    -   SciPy (Geometric Algorithms)  
    -   NetworkX (Graph-based Path Analysis)  

## Getting Started

### Prerequisites

-   Python 3.8+  
-   `pip` and `venv`  

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Gitter150/Kolam-Coders
    cd Kolam-Coders
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
