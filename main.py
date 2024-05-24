import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages

# Function to generate ellipsoid data
def generate_ellipsoid(a, b, c, num_points=100):
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, np.pi, num_points)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = c * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# Ellipsoid parameters (semi-axes lengths)
width = 14  # Total width in cm
height = 8  # Total height in cm
depth = 6  # Depth in cm for better visualization (adjust as needed)

a = width / 2  # Semi-major axis along x-axis
b = depth / 2  # Semi-major axis along y-axis
c = height / 2  # Semi-major axis along z-axis

# Generate ellipsoid data
x, y, z = generate_ellipsoid(a, b, c)

# Plot the ellipsoid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the wireframe without grid and without filling color
ax.plot_wireframe(x, y, z, color='k', linewidth=0.5)

# Remove grid
ax.grid(False)

# Set labels and title
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Z (cm)')
ax.set_title('Ellipsoid')

# Adjust the aspect ratio
ax.set_box_aspect([a, b, c])

# Save the plot as a PDF
with PdfPages('ellipsoid.pdf') as pdf:
    pdf.savefig(fig)

# Show the plot (optional)
plt.show()
