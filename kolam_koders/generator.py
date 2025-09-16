import matplotlib.pyplot as plt

def create_and_save_grid_inverted(width, height, output_path="data/output/grid.png"):
    """
    Generates a visual grid of white dots on a black background.
    """
    # Create a new plot
    fig, ax = plt.subplots(figsize=(5, 5))

    # --- NEW: Set background color to black ---
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Scatter plot for the dots
    for y in range(height):
        for x in range(width):
            # --- MODIFIED: 'wo' means white circle ---
            ax.plot(x, y, 'wo', markersize=5)

    # --- Set up the appearance ---
    ax.set_aspect('equal', adjustable='box')
    ax.invert_yaxis()
    ax.axis('off')

    # Save the figure, ensuring the background is black
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1, facecolor='black')
    plt.close(fig)
    print(f"Inverted grid image saved to {output_path}")

# --- Example of how to run it ---
if __name__ == '__main__':
    create_and_save_grid_inverted(7, 7)