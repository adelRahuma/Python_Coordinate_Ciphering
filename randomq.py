import shapefile
import random
import csv
sf = shapefile.Reader("LBY_adm0.shp")
# num_polygons = len(sf.shapes())
# print(num_polygons)
# random_numbers = [random.randint(0, num_polygons - 1) for _ in range(num_polygons)] # generate 10 random numbers
# sorted_numbers = sorted(random_numbers) # sort the random numbers
# with open('sorted_numbers.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Sorted Numbers'])
#     for num in sorted_numbers:
#         writer.writerow([num])



num_polygons = len(sf.shapes())

# Generate a list of unique random numbers based on the number of polygons
#random_numbers = random.sample(range(1, num_polygons + 1), num_polygons)
num_rand_nums = 60000  # or however many random numbers you want to generate
random_numbers = random.sample(range(1, num_polygons + 1), min(num_rand_nums, num_polygons))

# Sort the random numbers
sorted_numbers = sorted(random_numbers)

# Write the sorted numbers to a CSV file
with open("sorted_numbers.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sorted Numbers"])
    for num in sorted_numbers:
        writer.writerow([num])