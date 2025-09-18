import os
from flask import Flask, render_template, request, jsonify
from kolam_koders.generator import KolamGenerator
import time

# Initialize the Flask app
app = Flask(__name__)

# Ensure the output directory exists
os.makedirs("static/kolams", exist_ok=True)

@app.route('/')
def index():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handles the Kolam generation request."""
    data = request.get_json()
    seed = data.get('seed', 'default_seed')
    grid_size = int(data.get('grid_size', 13))
    num_motifs = int(data.get('num_motifs', 7))

    # --- Create a unique filename ---
    timestamp = int(time.time())
    output_filename = f"kolam_seed_{seed}_{timestamp}.png"
    output_path_for_generator = f"static/kolams/{output_filename}"

    # --- Call the generator with the correct output path ---
    generator = KolamGenerator(grid_size, grid_size)
    generator.generate_from_seed(
        seed=seed,
        num_motifs=num_motifs,
        output_path=output_path_for_generator
    )

    # --- Return the path to the frontend ---
    return jsonify({'image_url': output_path_for_generator})

if __name__ == '__main__':
    app.run(debug=True)