# import numpy as np
# import random   

# # Define the distance matrix (distances between cities)

# # Replace this with your distance matrix or generate one based on
# # your problem

# # Example distance matrix (replace this with your actual data)
# distance_matrix = np.array([
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ])

# # Parameters for Ant Colony Optimization
# num_ants = 10
# num_iterations = 50

# evaporation_rate = 0.5
# pheromone_constant = 1.0
# heuristic_constant = 1.0

# # Initialize pheromone matrix and visibility matrix
# num_cities = len(distance_matrix)
# pheromone = np.ones((num_cities, num_cities))  # Pheromone matrix
# visibility = 1 / distance_matrix  # Visibility matrix (inverse of distance)

# # ACO algorithm
# for iteration in range(num_iterations):
#     for ant in range(num_ants):
#         # Initialize ant's route and visited cities
#         ant_routes = []
#         current_city = random.randint(0, num_cities - 1)
#         visited_cities = [current_city]
#         route = [current_city]

#         while len(visited_cities) < num_cities:
#             # Calculate probabilities for each unvisited city
#             probabilities = []
#             for city in range(num_cities):
#                 if city not in visited_cities:
#                     pheromone_value = pheromone[current_city][city]
#                     visibility_value = visibility[current_city][city]
#                     probability = (pheromone_value**pheromone_constant) * (visibility_value**heuristic_constant)
#                     probabilities.append((city, probability))

#             # Select the next city based on probability
#             probabilities = sorted(probabilities, key=lambda x: x[1], reverse=True)
#             selected_city = probabilities[0][0]
#             route.append(selected_city)
#             visited_cities.append(selected_city)
#             current_city = selected_city

#         # Update pheromone levels based on ant's route
#         delta_pheromone = np.zeros((num_cities, num_cities))
#         for i in range(len(route) - 1):
#             city_a = route[i]
#             city_b = route[i + 1]
#             delta_pheromone[city_a][city_b] += 1 / distance_matrix[city_a][city_b]
#             delta_pheromone[city_b][city_a] += 1 / distance_matrix[city_a][city_b]

#         pheromone = (1 - evaporation_rate) * pheromone + delta_pheromone

# # Find the best route
# total_distances = [sum(distance_matrix[cities[i]][cities[(i + 1) % num_cities]] for i in range(num_cities)) for cities in ant_routes]

# # Get the index of the route with the maximum total distance
# best_route_index = np.argmax(total_distances)
# # best_route_index = np.argmax(sum(distance_matrix[cities(i)][cities[(i + 1) % num_cities]]) for i in range(num_cities)) for cities in ant_routes
# best_route = ant_routes[best_route_index]
# shortest_distance = sum(distance_matrix[best_route[i]][best_route[(i + 1) % num_cities]] for i in range(num_cities))

# print("Best route:", best_route)
# print("Shortest distance:", shortest_distance)

import numpy as np
import random

# Define the distance matrix (distances between cities)

# Replace this with your distance matrix or generate one based on
# your problem

# Example distance matrix (replace this with your actual data)
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

# Parameters for Ant Colony Optimization
num_ants = 10
num_iterations = 50

evaporation_rate = 0.5
pheromone_constant = 1.0
heuristic_constant = 1.0

# Initialize pheromone matrix and visibility matrix
num_cities = len(distance_matrix)
pheromone = np.ones((num_cities, num_cities))  # Pheromone matrix
visibility = 1 / distance_matrix  # Visibility matrix (inverse of distance)

# ACO algorithm
ant_routes = []  # Store routes of all ants
for iteration in range(num_iterations):
    for ant in range(num_ants):
        # Initialize ant's route and visited cities
        current_city = random.randint(0, num_cities - 1)
        visited_cities = [current_city]
        route = [current_city]

        while len(visited_cities) < num_cities:
            # Calculate probabilities for each unvisited city
            probabilities = []
            for city in range(num_cities):
                if city not in visited_cities:
                    pheromone_value = pheromone[current_city][city]
                    visibility_value = visibility[current_city][city]
                    probability = (pheromone_value**pheromone_constant) * (visibility_value**heuristic_constant)
                    probabilities.append((city, probability))

            # Select the next city based on probability
            probabilities = sorted(probabilities, key=lambda x: x[1], reverse=True)
            selected_city = probabilities[0][0]
            route.append(selected_city)
            visited_cities.append(selected_city)
            current_city = selected_city

        ant_routes.append(route)  # Store the route of the current ant

        # Update pheromone levels based on ant's route
        delta_pheromone = np.zeros((num_cities, num_cities))
        for i in range(len(route) - 1):
            city_a = route[i]
            city_b = route[i + 1]
            delta_pheromone[city_a][city_b] += 1 / distance_matrix[city_a][city_b]
            delta_pheromone[city_b][city_a] += 1 / distance_matrix[city_a][city_b]

        pheromone = (1 - evaporation_rate) * pheromone + delta_pheromone

# Find the best route
total_distances = [sum(distance_matrix[cities[i]][cities[(i + 1) % num_cities]] for i in range(num_cities)) for cities in ant_routes]

# Get the index of the route with the maximum total distance
best_route_index = np.argmin(total_distances)
best_route = ant_routes[best_route_index]
shortest_distance = sum(distance_matrix[best_route[i]][best_route[(i + 1) % num_cities]] for i in range(num_cities))

print("Best route:", best_route)
print("Shortest distance:", shortest_distance)
