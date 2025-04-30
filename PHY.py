import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 8                      # Number of antenna elements
d = 0.5                    # Distance between elements (in wavelengths)
theta = np.linspace(-90, 90, 1000)  # Angles to evaluate
theta_rad = np.radians(theta)      # Convert to radians
wavelength = 1             # Assume wavelength = 1 unit

# Steering angle (main beam direction)
theta_0 = 30               # degrees
theta_0_rad = np.radians(theta_0)

# Compute the array factor
k = 2 * np.pi / wavelength
beta = k * d * np.sin(theta_rad)
beta_0 = k * d * np.sin(theta_0_rad)

# Array factor for uniform weights (no tapering)
AF = np.abs(np.sum(np.exp(1j * (np.arange(N)[:, np.newaxis] * (beta - beta_0))), axis=0))

# Normalize and convert to dB
AF_dB = 20 * np.log10(AF / np.max(AF))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(theta, AF_dB)
plt.title(f'Beam Pattern of {N}-Element ULA (Steered to {theta_0}°)')
plt.xlabel('Angle (degrees)')
plt.ylabel('Array Factor (dB)')
plt.grid(True)
plt.ylim(-40, 0)
plt.show()