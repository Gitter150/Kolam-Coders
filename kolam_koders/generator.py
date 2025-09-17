import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np
import random

class KolamGenerator:
    """
    A class to programmatically generate Kolam designs using a symmetry engine.
    """
    def __init__(self, width, height):
        if width % 2 == 0 or height % 2 == 0:
            raise ValueError("Grid dimensions must be odd for a clear center point.")
        self.width = width
        self.height = height
        self.center_x = (width - 1) / 2
        self.center_y = (height - 1) / 2

        # --- Setup the plot ---
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.invert_yaxis()

        # --- Data Storage ---
        self.dots = [[(x, y) for x in range(width)] for y in range(height)]
        self.instructions = []

    def _rotate_point(self, point):
        """Rotates a single point 90 degrees clockwise around the grid center."""
        px, py = point
        # Translate point to origin
        translated_x = px - self.center_x
        translated_y = py - self.center_y
        # Rotate
        rotated_x = translated_y
        rotated_y = -translated_x
        # Translate back
        new_x = rotated_x + self.center_x
        new_y = rotated_y + self.center_y
        return (new_x, new_y)

    def add_curve(self, dot1, dot2, control_point):
        """Adds a 'curve' instruction to the list."""
        self.instructions.append(('curve', dot1, dot2, control_point))

    def add_line(self, dot1, dot2):
        """Adds a 'line' instruction to the list."""
        self.instructions.append(('line', dot1, dot2))

    def draw_clover_loop(self, top_left_dot_coords):
        """Adds instructions for a four-sided loop around a 2x2 group of dots."""
        x, y = top_left_dot_coords
        p1 = self.dots[y][x]
        p2 = self.dots[y][x+1]
        p3 = self.dots[y+1][x+1]
        p4 = self.dots[y+1][x]
        # Define control points that bulge outwards
        c1 = ((p1[0] + p2[0]) / 2, y - 0.5)
        c2 = (x + 1.5, (p2[1] + p3[1]) / 2)
        c3 = ((p4[0] + p3[0]) / 2, y + 1.5)
        c4 = (x - 0.5, (p1[1] + p4[1]) / 2)
        self.add_curve(p1, p2, c1)
        self.add_curve(p2, p3, c2)
        self.add_curve(p3, p4, c3)
        self.add_curve(p4, p1, c4)

    def draw_diamond(self, center_dot_coords, radius=1):
        """Adds instructions to draw a diamond centered at a specific dot."""
        cx, cy = center_dot_coords

        # Calculate the four corner points of the diamond
        top    = self.dots[cy - radius][cx]
        right  = self.dots[cy][cx + radius]
        bottom = self.dots[cy + radius][cx]
        left   = self.dots[cy][cx - radius]

        # Add the four line instructions
        self.add_line(top, right)
        self.add_line(right, bottom)
        self.add_line(bottom, left)
        self.add_line(left, top)

    def draw_curved_diamond(self, center_dot_coords, radius=1):
        """Adds instructions for a diamond with inward-curving edges."""
        cx, cy = center_dot_coords

        # The center dot will act as the control point for all curves
        control_point = self.dots[cy][cx]

        # Calculate the four corner points of the diamond
        top    = self.dots[cy - radius][cx]
        right  = self.dots[cy][cx + radius]
        bottom = self.dots[cy + radius][cx]
        left   = self.dots[cy][cx - radius]

        # Add the four curve instructions, all pulled toward the center
        self.add_curve(top, right, control_point)
        self.add_curve(right, bottom, control_point)
        self.add_curve(bottom, left, control_point)
        self.add_curve(left, top, control_point)
    
    def draw_weaving_loop(self, top_left_dot_coords):
        """Adds instructions for two 'S' curves that weave around a 2x2 dot group."""
        x, y = top_left_dot_coords
        p_tl = self.dots[y][x]      # Top-left
        p_tr = self.dots[y][x+1]    # Top-right
        p_br = self.dots[y+1][x+1]  # Bottom-right
        p_bl = self.dots[y+1][x]    # Bottom-left

        # First S-curve from top-left to bottom-right
        control1 = (p_tl[0], p_tl[1] + 0.5)
        self.add_curve(p_tl, p_bl, control1)
        control2 = (p_br[0], p_br[1] - 0.5)
        self.add_curve(p_tr, p_br, control2)

        # Second S-curve from top-right to bottom-left
        control3 = (p_tr[0] - 0.5, p_tr[1])
        self.add_curve(p_tr, p_tl, control3)
        control4 = (p_bl[0] + 0.5, p_bl[1])
        self.add_curve(p_bl, p_br, control4)

    def draw_lotus_petal(self, base_dot_coords, tip_dot_coords, width=0.5):
        """
        Adds instructions for a pointed petal shape.
        'width' controls how wide the petal is.
        """
        # Vector from base to tip to determine orientation
        vx = tip_dot_coords[0] - base_dot_coords[0]
        vy = tip_dot_coords[1] - base_dot_coords[1]

        # Control points are placed perpendicular to the base-tip vector
        c1 = (base_dot_coords[0] - vy * width, base_dot_coords[1] + vx * width)
        c2 = (base_dot_coords[0] + vy * width, base_dot_coords[1] - vx * width)

        # Two curves sharing a tip to create the point
        self.add_curve(base_dot_coords, tip_dot_coords, c1)
        self.add_curve(base_dot_coords, tip_dot_coords, c2)


    def generate_from_seed(self, seed, num_motifs=5):
        """
        Generates a dense, symmetric kolam with varied motif sizes.
        Motifs closer to the center are drawn with a larger radius.
        """
        random.seed(seed)

        motif_library = [
            self.draw_clover_loop, self.draw_weaving_loop,
            self.draw_curved_diamond, self.draw_lotus_petal, self.draw_diamond
        ]

        # Use a single, large safe zone for initial anchor points
        if self.width < 9 or self.height < 9:
            print("Warning: Grid is small. For best results, use a grid of at least 11x11.")

        safe_margin = 1 # We can use a smaller margin now
        safe_x_range = range(safe_margin, int(self.center_x) + 1)
        safe_y_range = range(safe_margin, int(self.center_y) + 1)
        
        safe_anchor_points = [self.dots[y][x] for y in safe_y_range for x in safe_x_range]

        if not safe_anchor_points:
            print("Error: Grid too small for the safe margin.")
            self.apply_4_fold_symmetry_and_render(output_path=f"data/output/kolam_seed_{seed}_empty.png")
            return

        # --- Randomly place motifs with dynamic radius ---
        for _ in range(num_motifs):
            if not safe_anchor_points:
                break

            anchor_point = random.choice(safe_anchor_points)
            safe_anchor_points.remove(anchor_point)
            
            chosen_motif_func = random.choice(motif_library)

            # --- DYNAMIC RADIUS LOGIC ---
            if chosen_motif_func in [self.draw_diamond, self.draw_curved_diamond]:
                # Calculate the maximum possible radius from this anchor point
                max_safe_radius = min(anchor_point[0], anchor_point[1])
                
                # Choose a random radius between 1 and the max safe radius
                # This makes motifs near the center potentially much larger
                if max_safe_radius > 1:
                    chosen_radius = random.randint(1, max_safe_radius)
                    chosen_motif_func(anchor_point, radius=chosen_radius)
                else: # If max radius is only 1, just draw with that
                    chosen_motif_func(anchor_point, radius=1)

            elif chosen_motif_func == self.draw_lotus_petal:
                if safe_anchor_points:
                    tip_point = random.choice(safe_anchor_points)
                    chosen_motif_func(anchor_point, tip_point, width=random.uniform(0.3, 0.6))
            
            else: # Clover and Weaving loops are a fixed 2x2 size
                # Check if it fits before drawing
                if anchor_point[0] < self.width - 1 and anchor_point[1] < self.height - 1:
                    chosen_motif_func(anchor_point)

        # --- Apply symmetry and render ---
        output_filename = f"data/output/kolam_seed_{seed}.png"
        self.apply_4_fold_symmetry_and_render(output_path=output_filename)

    def apply_4_fold_symmetry_and_render(self, output_path="data/output/symmetric_kolam.png"):
        """Renders the final kolam by applying 4-fold rotational symmetry."""
        # Draw the background dots first
        for row in self.dots:
            for x, y in row:
                self.ax.plot(x, y, 'wo', markersize=5)

        all_instructions = []
        
        # Process original instructions and their three rotations
        for rotation in range(4):
            for instruction in self.instructions:
                cmd_type, p1, p2 = instruction[0], instruction[1], instruction[2]
                
                # Apply rotation to each point
                current_p1 = p1
                current_p2 = p2
                for _ in range(rotation):
                    current_p1 = self._rotate_point(current_p1)
                    current_p2 = self._rotate_point(current_p2)

                if cmd_type == 'curve':
                    control = instruction[3]
                    current_control = control
                    for _ in range(rotation):
                        current_control = self._rotate_point(current_control)
                    all_instructions.append(('curve', current_p1, current_p2, current_control))
                elif cmd_type == 'line':
                    all_instructions.append(('line', current_p1, current_p2))

        # --- Execute all drawing commands ---
        for instruction in all_instructions:
            cmd_type, p1, p2 = instruction[0], instruction[1], instruction[2]
            if cmd_type == 'curve':
                control = instruction[3]
                vertices = [p1, control, p2]
                codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
                path = Path(vertices, codes)
                patch = PathPatch(path, facecolor='none', edgecolor='white', lw=1.5)
                self.ax.add_patch(patch)
            elif cmd_type == 'line':
                self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='white', lw=1.5)
        
        # --- Save and close ---
        self.ax.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1, facecolor='black')
        plt.close(self.fig)
        print(f"Symmetric kolam saved to {output_path}")


if __name__ == '__main__':
    generator = KolamGenerator(9, 9) # Use a larger grid

    seed = "presentation is the only thing left"
    generator.generate_from_seed(seed=seed, num_motifs=5)

    # 2. Design a dense pattern in the top-left quadrant by layering motifs

    # --- Layer 1: A central weaving loop ---
    # Place a weaving loop near the center of the quadrant

    """ generator.draw_weaving_loop(generator.dots[1][1]) """

    # --- Layer 2: Add corner petals ---
    # Add lotus petals pointing outwards from the corners of the weaving loop
    # Petal pointing top-left

    """ generator.draw_lotus_petal(generator.dots[1][1], generator.dots[0][0], width=0.4) """

    # Petal pointing top-right

    """ generator.draw_lotus_petal(generator.dots[1][2], generator.dots[0][3], width=0.4)

    generator.draw_lotus_petal(generator.dots[2][1], generator.dots[3][0], width=0.4) """

    # --- Layer 3: Connect with a larger diamond ---
    # Enclose the existing motifs with a larger diamond to frame them.
    # The center of this diamond is the center of the 2x2 weaving loop grid.

    """ diamond_center_dot = generator.dots[4][4]
    generator.draw_curved_diamond(diamond_center_dot, radius=4) """


    # 3. Apply symmetry and render the complete image
    """ generator.apply_4_fold_symmetry_and_render() """