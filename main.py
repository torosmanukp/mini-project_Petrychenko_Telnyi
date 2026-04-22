import matplotlib.pyplot as plt
from matplotlib import colormaps
import numpy as np
from scipy import ndimage

def natural_terrain_exp(x, y, num_hills=30, amplitude=1):
    Z = np.zeros_like(x)
    for _ in range(num_hills):
        x0 = np.random.uniform(x.min(), x.max())
        y0 = np.random.uniform(y.min(), y.max())
        h = np.random.uniform(0.8, 6) * amplitude
        sigma = np.random.uniform(3.0, 6.0)
        d = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
        Z += h * np.exp(-d ** 2 / (2 * sigma ** 2))
    Z = ndimage.gaussian_filter(Z, sigma=1.0)
    return Z

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100    )
X, Y = np.meshgrid(x, y)
Z = natural_terrain_exp(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='terrain', alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Випадкова 3D‑поверхня з амплітудою")
plt.show()

N = 20
idx_x = np.random.randint(0, X.shape[0], N)
idx_y = np.random.randint(0, X.shape[1], N)

x_rand = X[idx_x, idx_y]
y_rand = Y[idx_x, idx_y]
z_rand = Z[idx_x, idx_y]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='terrain', alpha=0.8)
ax.scatter(x_rand, y_rand, z_rand, c='red', s=30, label='клієнти', marker="*")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Випадкова 3D‑поверхня з амплітудою")
plt.legend()
plt.show()