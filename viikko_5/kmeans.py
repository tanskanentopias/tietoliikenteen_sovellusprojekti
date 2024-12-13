import numpy as np
import matplotlib.pyplot as plt
import math

#generate data points with noise
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


#Generate random centroids
def random_centroids():
    return np.random.randint(1200, 1800, size=(6, 3))


#Compute distances between all data points and centroids
def compute_distances(data, centroids):
    return np.linalg.norm(data[:, np.newaxis, :] - centroids, axis=2)


#k-means operation
def k_means_clustering(data, initial_centroids, max_iterations=500):
    centroids = initial_centroids
    for iteration in range(max_iterations):
        distances = compute_distances(data, centroids)
        closest_centroids = np.argmin(distances, axis=1)
        for i in range(len(centroids)):
            points_in_cluster = data[closest_centroids == i]
            if len(points_in_cluster) > 0:
                centroids[i] = points_in_cluster.mean(axis=0)
    return centroids, closest_centroids


#Generate data and initial_centroids
data = generate_data()
initial_centroids = random_centroids()

#Run K-means clustering
final_centroids, closest_centroids = k_means_clustering(data, initial_centroids)

print(f"datapoints: {data}")
print(f"centroids: {initial_centroids}")
print(f"closests centroids: {closest_centroids}")
print(f"final centroids: \n {final_centroids}")

#Plotting 
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=closest_centroids, cmap="viridis", label="Data Points")


ax.scatter(final_centroids[:, 0], final_centroids[:, 1], final_centroids[:, 2], c="red", s=200, marker="X", label="Centroids")


ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")


ax.legend()
plt.show()

with open('python\Keskipisteet.h', mode='w') as file:
    file.write("int final_centroids[6][3];\n")
    for i in final_centroids:
        if (round(i[0], -2) == 1800):
            file.write(f"final_centroids[0] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[0], -2) == 1200):
            file.write(f"final_centroids[1] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[1], -2) == 1800):
            file.write(f"final_centroids[2] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[1], -2) == 1200):
            file.write(f"final_centroids[3] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[2], -2) == 1800):
            file.write(f"final_centroids[4] = {{{i[0]}, {i[1]}, {i[2]}}};\n")
        elif (round(i[2], -2) == 1200):
            file.write(f"final_centroids[5] = {{{i[0]}, {i[1]}, {i[2]}}};\n")