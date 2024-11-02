import math

# Given coordinates
coordinates = [
    [497113.220, 5419946.461, 287.650],
    [497130.081, 5419948.322, 287.650],
    [497132.582, 5419926.619, 287.700],
    [497128.209, 5419926.155, 287.650],
    [497130.884, 5419901.053, 287.650],
    [497141.373, 5419902.170, 287.300],
    [497142.131, 5419895.066, 287.650],
    [497118.956, 5419892.610, 287.650],
    [497113.220, 5419946.461, 287.650]
]

# Convert gon to degrees
omega_g = 2.05968
phi_g = 0.67409
kappa_g = 199.23470

# Convert degrees to radians
omega_d = (omega_g / 400) * 360
phi_d = (phi_g / 400) * 360
kappa_d = (kappa_g / 400) * 360

omega_r = (math.pi / 180) * omega_d
phi_r = (math.pi / 180) * phi_d
kappa_r = (math.pi / 180) * kappa_d

# Convert pixel coordinates to list
pixel_coordinate = [[6912], [3840], [10000]]

# Exterior orientation matrix
exterior_orientation = [
    [1, 0, 0, -497049.238],
    [0, 1, 0, -5420301.525],
    [0, 0, 1, -1163.806],
    [0, 0, 0, 1]
]

# Interior orientation matrix
interior_orientation = [
    [-120/0.012, 0, 3840, 0],
    [0, 120/0.012, 6912, 0],
    [0, 0, 1, 0]
]

# Rotation matrix
R = [
    [math.cos(phi_r)*math.cos(kappa_r)+math.sin(phi_r)*math.sin(omega_r)*math.sin(kappa_r),
     math.cos(omega_r)*math.sin(kappa_r),
     -math.sin(phi_r)*math.cos(kappa_r)+math.cos(phi_r)*math.sin(omega_r)*math.sin(kappa_r), 0],
    [-math.cos(phi_r)*math.sin(kappa_r)+math.sin(phi_r)*math.sin(omega_r)*math.cos(kappa_r),
     math.cos(omega_r)*math.cos(kappa_r),
     math.sin(phi_r)*math.sin(kappa_r)+math.cos(phi_r)*math.sin(omega_r)*math.cos(kappa_r), 0],
    [math.sin(phi_r)*math.cos(omega_r), -math.sin(omega_r), math.cos(omega_r)*math.cos(phi_r), 0],
    [0, 0, 0, 1]
]

# Perspective projection matrix
perspective_projection = [
    [interior_orientation[0][0]*R[0][0] + interior_orientation[0][1]*R[1][0] + interior_orientation[0][2]*R[2][0],
     interior_orientation[0][0]*R[0][1] + interior_orientation[0][1]*R[1][1] + interior_orientation[0][2]*R[2][1],
     interior_orientation[0][0]*R[0][2] + interior_orientation[0][1]*R[1][2] + interior_orientation[0][2]*R[2][2],
     interior_orientation[0][0]*R[0][3] + interior_orientation[0][1]*R[1][3] + interior_orientation[0][2]*R[2][3]],
    [interior_orientation[1][0]*R[0][0] + interior_orientation[1][1]*R[1][0] + interior_orientation[1][2]*R[2][0],
     interior_orientation[1][0]*R[0][1] + interior_orientation[1][1]*R[1][1] + interior_orientation[1][2]*R[2][1],
     interior_orientation[1][0]*R[0][2] + interior_orientation[1][1]*R[1][2] + interior_orientation[1][2]*R[2][2],
     interior_orientation[1][0]*R[0][3] + interior_orientation[1][1]*R[1][3] + interior_orientation[1][2]*R[2][3]],
    [interior_orientation[2][0]*R[0][0] + interior_orientation[2][1]*R[1][0] + interior_orientation[2][2]*R[2][0],
     interior_orientation[2][0]*R[0][1] + interior_orientation[2][1]*R[1][1] + interior_orientation[2][2]*R[2][1],
     interior_orientation[2][0]*R[0][2] + interior_orientation[2][1]*R[1][2] + interior_orientation[2][2]*R[2][2],
     interior_orientation[2][0]*R[0][3] + interior_orientation[2][1]*R[1][3] + interior_orientation[2][2]*R[2][3]]
]

# Matrix multiplication for the full projection matrix
perspective_projection2 = [
    [perspective_projection[0][0]*exterior_orientation[0][0] + perspective_projection[0][1]*exterior_orientation[1][0] +
     perspective_projection[0][2]*exterior_orientation[2][0] + perspective_projection[0][3]*exterior_orientation[3][0],
     perspective_projection[0][0]*exterior_orientation[0][1] + perspective_projection[0][1]*exterior_orientation[1][1] +
     perspective_projection[0][2]*exterior_orientation[2][1] + perspective_projection[0][3]*exterior_orientation[3][1],
     perspective_projection[0][0]*exterior_orientation[0][2] + perspective_projection[0][1]*exterior_orientation[1][2] +
     perspective_projection[0][2]*exterior_orientation[2][2] + perspective_projection[0][3]*exterior_orientation[3][2],
     perspective_projection[0][0]*exterior_orientation[0][3] + perspective_projection[0][1]*exterior_orientation[1][3] +
     perspective_projection[0][2]*exterior_orientation[2][3] + perspective_projection[0][3]*exterior_orientation[3][3]],
    [perspective_projection[1][0]*exterior_orientation[0][0] + perspective_projection[1][1]*exterior_orientation[1][0] +
     perspective_projection[1][2]*exterior_orientation[2][0] + perspective_projection[1][3]*exterior_orientation[3][0],
     perspective_projection[1][0]*exterior_orientation[0][1] + perspective_projection[1][1]*exterior_orientation[1][1] +
     perspective_projection[1][2]*exterior_orientation[2][1] + perspective_projection[1][3]*exterior_orientation[3][1],
     perspective_projection[1][0]*exterior_orientation[0][2] + perspective_projection[1][1]*exterior_orientation[1][2] +
     perspective_projection[1][2]*exterior_orientation[2][2] + perspective_projection[1][3]*exterior_orientation[3][2],
     perspective_projection[1][0]*exterior_orientation[0][3] + perspective_projection[1][1]*exterior_orientation[1][3] +
     perspective_projection[1][2]*exterior_orientation[2][3] + perspective_projection[1][3]*exterior_orientation[3][3]],
    [perspective_projection[2][0]*exterior_orientation[0][0] + perspective_projection[2][1]*exterior_orientation[1][0] +
     perspective_projection[2][2]*exterior_orientation[2][0] + perspective_projection[2][3]*exterior_orientation[3][0],
     perspective_projection[2][0]*exterior_orientation[0][1] + perspective_projection[2][1]*exterior_orientation[1][1] +
     perspective_projection[2][2]*exterior_orientation[2][1] + perspective_projection[2][3]*exterior_orientation[3][1],
     perspective_projection[2][0]*exterior_orientation[0][2] + perspective_projection[2][1]*exterior_orientation[1][2] +
     perspective_projection[2][2]*exterior_orientation[2][2] + perspective_projection[2][3]*exterior_orientation[3][2],
     perspective_projection[2][0]*exterior_orientation[0][3] + perspective_projection[2][1]*exterior_orientation[1][3] +
     perspective_projection[2][2]*exterior_orientation[2][3] + perspective_projection[2][3]*exterior_orientation[3][3]]
]

# Initialize lists to store results
camera_coordinate_list = []
u_values = []
v_values = []

for i in range(len(coordinates)):
    # Append 1 to the world coordinates for matrix multiplication
    A = coordinates[i] + [1]
    
    # Perform matrix multiplication
    camera_coordinate = [
        A[0]*perspective_projection2[0][0] + A[1]*perspective_projection2[0][1] + A[2]*perspective_projection2[0][2] + A[3]*perspective_projection2[0][3],
        A[0]*perspective_projection2[1][0] + A[1]*perspective_projection2[1][1] + A[2]*perspective_projection2[1][2] + A[3]*perspective_projection2[1][3],
        A[0]*perspective_projection2[2][0] + A[1]*perspective_projection2[2][1] + A[2]*perspective_projection2[2][2] + A[3]*perspective_projection2[2][3]
    ]

    # Normalize by dividing by the last element
    camera_coordinate = [coord / camera_coordinate[-1] for coord in camera_coordinate]

# Print or use the results as needed
    camera_coordinate_list.append(camera_coordinate)
    u_values.append(camera_coordinate[0])
    v_values.append(camera_coordinate[1])

# Print or use the results as needed
print("perspective projection",perspective_projection2)
print("Pixel coordinates (u, v):")
for u, v in zip(u_values, v_values):
    print(f"({u}, {v})")
    
