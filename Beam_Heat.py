import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def uniform_rectangular_array(M, N, dx, dy, wavelength):
    """
    Generate positions for a uniform rectangular array (URA)

    Parameters:
    -----------
    M : int
        Number of elements in x direction
    N : int
        Number of elements in y direction
    dx : float
        Element spacing in x direction (in wavelengths)
    dy : float
        Element spacing in y direction (in wavelengths)
    wavelength : float
        Signal wavelength

    Returns:
    --------
    positions : ndarray
        Array of element positions (x, y, z)
    """
    # Convert spacing from wavelengths to actual distance
    dx_actual = dx * wavelength
    dy_actual = dy * wavelength

    # Generate element positions
    x = np.arange(0, M) * dx_actual
    y = np.arange(0, N) * dy_actual

    # Center the array around the origin
    x = x - np.mean(x)
    y = y - np.mean(y)

    # Create a grid of positions
    xx, yy = np.meshgrid(x, y)

    # Create array of positions
    positions = np.zeros((M * N, 3))
    positions[:, 0] = xx.flatten()
    positions[:, 1] = yy.flatten()

    return positions


def steering_vector(positions, theta, phi, wavelength):
    """
    Calculate the steering vector for a given direction

    Parameters:
    -----------
    positions : ndarray
        Array of element positions (x, y, z)
    theta : float
        Elevation angle in radians (0 = horizon, pi/2 = zenith)
    phi : float
        Azimuth angle in radians (0 = x-axis, pi/2 = y-axis)
    wavelength : float
        Signal wavelength

    Returns:
    --------
    a : ndarray
        Steering vector
    """
    # Calculate wave vector
    k = 2 * np.pi / wavelength

    # Calculate wave vector components
    kx = k * np.cos(phi) * np.sin(theta)
    ky = k * np.sin(phi) * np.sin(theta)
    kz = k * np.cos(theta)

    # Calculate dot product between wave vector and positions
    k_vec = np.array([kx, ky, kz])
    phase = np.dot(positions, k_vec)

    # Calculate steering vector
    a = np.exp(1j * phase)

    return a


def array_factor(positions, weights, theta_range, phi_range, wavelength):
    """
    Calculate the array factor for a given set of weights

    Parameters:
    -----------
    positions : ndarray
        Array of element positions (x, y, z)
    weights : ndarray
        Array of complex weights
    theta_range : ndarray
        Range of elevation angles to calculate array factor for
    phi_range : ndarray
        Range of azimuth angles to calculate array factor for
    wavelength : float
        Signal wavelength

    Returns:
    --------
    AF : ndarray
        Array factor (complex)
    """
    # Initialize array factor
    AF = np.zeros((len(theta_range), len(phi_range)), dtype=complex)

    # Calculate array factor for each angle
    for i, theta in enumerate(theta_range):
        for j, phi in enumerate(phi_range):
            a = steering_vector(positions, theta, phi, wavelength)
            AF[i, j] = np.dot(weights, a)

    return AF


def beamforming_weights(positions, theta_desired, phi_desired, wavelength):
    """
    Calculate beamforming weights to steer in a desired direction

    Parameters:
    -----------
    positions : ndarray
        Array of element positions (x, y, z)
    theta_desired : float
        Desired elevation angle in radians
    phi_desired : float
        Desired azimuth angle in radians
    wavelength : float
        Signal wavelength

    Returns:
    --------
    weights : ndarray
        Array of complex weights
    """
    # Calculate steering vector for desired direction
    a = steering_vector(positions, theta_desired, phi_desired, wavelength)

    # Calculate weights (conjugate of steering vector)
    weights = np.conj(a)

    # Normalize weights
    weights = weights / np.sqrt(np.sum(np.abs(weights) ** 2))

    return weights


def plot_array_pattern_3d(AF, theta_range, phi_range):
    """
    Plot 3D array pattern

    Parameters:
    -----------
    AF : ndarray
        Array factor (complex)
    theta_range : ndarray
        Range of elevation angles
    phi_range : ndarray
        Range of azimuth angles
    """
    # Calculate array pattern (magnitude squared of array factor)
    pattern = np.abs(AF) ** 2

    # Convert to dB
    pattern_db = 10 * np.log10(pattern / np.max(pattern))

    # Create mesh grid for plotting
    theta_grid, phi_grid = np.meshgrid(theta_range, phi_range, indexing='ij')

    # Convert from spherical to Cartesian coordinates
    x = np.sin(theta_grid) * np.cos(phi_grid)
    y = np.sin(theta_grid) * np.sin(phi_grid)
    z = np.cos(theta_grid)

    # Create figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot surface
    norm_pattern = pattern_db.copy()
    norm_pattern[norm_pattern < -30] = -30  # Clip values below -30 dB
    surf = ax.plot_surface(x, y, z, facecolors=cm.jet((norm_pattern + 30) / 30),
                           alpha=0.8, linewidth=0, antialiased=True)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set title
    ax.set_title('3D Beam Pattern (dB)')

    # Add colorbar
    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(np.linspace(-30, 0, 100))
    plt.colorbar(m, label='Normalized Array Factor (dB)')

    # Equal aspect ratio
    ax.set_box_aspect([1, 1, 1])

    plt.tight_layout()

    return fig, ax


def plot_array_pattern_2d(AF, theta_range, phi_range):
    """
    Plot 2D array pattern

    Parameters:
    -----------
    AF : ndarray
        Array factor (complex)
    theta_range : ndarray
        Range of elevation angles
    phi_range : ndarray
        Range of azimuth angles
    """
    # Calculate array pattern (magnitude squared of array factor)
    pattern = np.abs(AF) ** 2

    # Convert to dB
    pattern_db = 10 * np.log10(pattern / np.max(pattern))

    # Create mesh grid for plotting
    theta_grid, phi_grid = np.meshgrid(theta_range, phi_range, indexing='ij')

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot contour
    contour = ax.contourf(np.degrees(phi_grid), np.degrees(theta_grid),
                          pattern_db, levels=np.linspace(-30, 0, 16),
                          cmap='jet', extend='min')

    # Set axis labels
    ax.set_xlabel('Azimuth Angle (degrees)')
    ax.set_ylabel('Elevation Angle (degrees)')

    # Set title
    ax.set_title('2D Beam Pattern (dB)')

    # Add colorbar
    plt.colorbar(contour, label='Normalized Array Factor (dB)')

    plt.tight_layout()

    return fig, ax


def plot_array_layout(positions):
    """
    Plot array layout

    Parameters:
    -----------
    positions : ndarray
        Array of element positions (x, y, z)
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot element positions
    ax.scatter(positions[:, 0], positions[:, 1], marker='o', color='b', s=100)

    # Set axis labels
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')

    # Set title
    ax.set_title('Array Layout')

    # Equal aspect ratio
    ax.set_aspect('equal')

    plt.grid(True)
    plt.tight_layout()

    return fig, ax


def main():
    # Set parameters
    M = 8  # Number of elements in x direction
    N = 8  # Number of elements in y direction
    dx = 0.5  # Element spacing in x direction (in wavelengths)
    dy = 0.5  # Element spacing in y direction (in wavelengths)
    frequency = 2.4e9  # Frequency (Hz)
    c = 3e8  # Speed of light (m/s)
    wavelength = c / frequency  # Wavelength (m)

    # Define desired beam direction
    theta_desired = np.radians(30)  # Elevation angle (radians)
    phi_desired = np.radians(45)  # Azimuth angle (radians)

    # Define angle ranges for pattern calculation
    theta_range = np.linspace(0, np.pi / 2, 91)  # Elevation: 0 to 90 degrees
    phi_range = np.linspace(0, 2 * np.pi, 181)  # Azimuth: 0 to 360 degrees

    # Generate uniform rectangular array
    positions = uniform_rectangular_array(M, N, dx, dy, wavelength)

    # Calculate beamforming weights
    weights = beamforming_weights(positions, theta_desired, phi_desired, wavelength)

    # Calculate array factor
    AF = array_factor(positions, weights, theta_range, phi_range, wavelength)

    # Plot array layout
    plot_array_layout(positions)

    # Plot 2D beam pattern
    plot_array_pattern_2d(AF, theta_range, phi_range)

    # Plot 3D beam pattern
    plot_array_pattern_3d(AF, theta_range, phi_range)

    plt.show()


if __name__ == "__main__":
    main()