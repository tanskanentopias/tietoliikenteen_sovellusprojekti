import numpy as np
import matplotlib.pyplot as plt
import math



'''def generate_data():
    data = np.zeros((60,3))
    for i in range (0,10):
        data[i,:] = np.array((1200,1500,1500))
    for i in range (10,20):
        data[i,:] = np.array((1800,1500,1500))   
    for i in range (20,30):
        data[i,:] = np.array((1500,1200,1500))     
    for i in range (30,40):
        data[i,:] = np.array((1500,1800,1500))         
    for i in range (40,50):
        data[i,:] = np.array((1500,1500,1200))      
    for i in range (50,60):
        data[i,:] = np.array((1500,1500,1800))
    noise = np.random.normal(0,10,data.shape)   
    data = data + noise
    return data    

data = generate_data()

def random_centroids():
    centroids = np.random.randint(1200,1800, size=(6,3))
    return centroids

centroids = random_centroids()

def euclidian_distance(point1, point2):
    for point in data:
        # Compute distances to all cluster centers
        distances = np.linalg.norm(centroids - point, axis=1)
    return distances

distances = euclidian_distance(data, centroids)

def calculate_closest_point():
    closest_point = np.argmin(distances)
    return closest_point

closest_point = calculate_closest_point()

centerPointCumulativeSum = np.zeros((6, 3))
#winning_points = np.zeros(len(centroids))

data #generate data

centroids # generate random centroids

max_iterations = 10
for iteration in range(max_iterations):
    centerPointCumulativeSum = np.zeros_like(centroids)  # Reset cumulative sums
    winning_points = np.zeros(len(centroids), dtype=int)  # Reset counts

    for point in data:
        # Compute distances to all cluster centers
        distances

        # Find the closest cluster center
        closest_point

        # Update the cumulative sum and count for the closest center
        centerPointCumulativeSum[closest_point] += point
        winning_points[closest_point] += 1

    # Update cluster centers, avoiding division by zero
    for i in range(len(centroids)):
        if winning_points[i] > 0:
            centroids[i] = centerPointCumulativeSum[i] / winning_points[i]





x = data[:,0]
y = data[:,1]
z = data[:,2]

print(f"data: {data}")
print(f"centroid: {centroids}")
print(f"distances: {distances}")
print(f"closest point: {closest_point}")
print(f"winning points: {winning_points}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='blue', marker='o', label='Data Points')

# Scatter plot for the centroids
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', s=200, marker='X', label='Centroids')

# Label axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the legend
ax.legend()

plt.show()'''


# Function to generate data points with noise
def generate_data():
    data = np.zeros((60, 3))
    for i in range(0, 10):
        data[i, :] = np.array((1200, 1500, 1500))
    for i in range(10, 20):
        data[i, :] = np.array((1800, 1500, 1500))
    for i in range(20, 30):
        data[i, :] = np.array((1500, 1200, 1500))
    for i in range(30, 40):
        data[i, :] = np.array((1500, 1800, 1500))
    for i in range(40, 50):
        data[i, :] = np.array((1500, 1500, 1200))
    for i in range(50, 60):
        data[i, :] = np.array((1500, 1500, 1800))
    noise = np.random.normal(0, 10, data.shape)
    return data + noise


# Generate random centroids
def random_centroids():
    return np.random.randint(1200, 1800, size=(6, 3))


# Compute distances between all data points and centroids
def compute_distances(data, centroids):
    return np.linalg.norm(data[:, np.newaxis, :] - centroids, axis=2)


# Main K-means clustering implementation
def k_means_clustering(data, initial_centroids, max_iterations=30):
    centroids = initial_centroids
    for iteration in range(max_iterations):
        distances = compute_distances(data, centroids)
        closest_centroids = np.argmin(distances, axis=1)
        for i in range(len(centroids)):
            points_in_cluster = data[closest_centroids == i]
            if len(points_in_cluster) > 0:
                centroids[i] = points_in_cluster.mean(axis=0)
    return centroids, closest_centroids


# Generate data and initial centroids
data = generate_data()
initial_centroids = random_centroids()

# Run K-means clustering
final_centroids, closest_centroids = k_means_clustering(data, initial_centroids)

print(f"datapoints: {data}")
print(f"centroids: {initial_centroids}")
print(f"closests centroids: {closest_centroids}")
print(f"final centroids: {final_centroids}")

# Plotting results
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Scatter plot for data points
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=closest_centroids, cmap="viridis", label="Data Points")

# Scatter plot for centroids
ax.scatter(final_centroids[:, 0], final_centroids[:, 1], final_centroids[:, 2],
           c="red", s=200, marker="X", label="Centroids")

# Label axes
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Show the legend
ax.legend()
plt.show()
