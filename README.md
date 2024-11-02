# Object Space to Image Space Transformation

This project is a photogrammetry process that converts world coordinates (3D object space) into pixel coordinates (2D image space) using camera parameters and transformation matrices. The code performs calculations to simulate a camera's perspective projection, given specific interior, exterior, and rotation parameters.

## Project Structure

The project has the following structure:

Object-Space-to-Image-Space-Transformation/
├── transformation.py         # Main code for coordinate transformation
├── data/
│   └── parameters.json       # JSON file containing the camera parameters
└── README.md                 # Project description and instructions

- **transformation.py**: Contains the main logic for transforming world coordinates to image coordinates.
- **data/parameters.json**: Stores camera parameters (e.g., interior orientation, exterior orientation, rotation values).
- **README.md**: Documentation and instructions for using the project.

## Features

- **Coordinate Transformation**: Converts 3D world coordinates to 2D image coordinates using a perspective projection matrix.
- **Parameter Configuration**: Allows users to define camera parameters in a JSON file for easy modification.
- **Matrix Operations**: Utilizes mathematical operations to compute the required transformations, including orientation and rotation.

## Requirements

This project requires Python and the `math` library (included in Python by default). If additional libraries are added, you can install them with `pip`.

## Getting Started

### Clone the Repository

To get a copy of this project on your local machine, use the following command:

```bash
git clone https://github.com/aktercan/Object-Space-to-Image-Space-Transformation.git
cd Object-Space-to-Image-Space-Transformation

### Running the Code

1. Ensure you have all necessary files, especially `transformation.py` and `parameters.json` in the correct structure.
2. Open a terminal in the project directory.
3. Run the following command:

   ```bash
   python transformation.py

The code will output the pixel coordinates for each point defined in the `coordinates` list within `transformation.py`.

### How It Works

1. **Input Coordinates**: The 3D world coordinates for each point are listed in `coordinates` within `transformation.py`.
2. **Orientation Angles (Gon)**: Omega, Phi, and Kappa angles are given in gons and converted to radians for calculation.
3. **Transformation Matrices**: Using the orientation parameters, the code constructs the exterior orientation, interior orientation, and rotation matrices.
4. **Perspective Projection**: The transformation matrices are combined into a perspective projection matrix.
5. **Pixel Coordinates Calculation**: The 3D world coordinates are multiplied by the projection matrix to obtain 2D pixel coordinates, which are then normalized.

### Example Output

The output will display pixel coordinates (u, v) for each 3D world coordinate provided in the input. Here’s an example output:

perspective projection [[10039.313845252786, -244.36253641790051, 3728.0107922739617, -3669853349.3550463], [-50.47965979268584, -10217.632115389333, 6585.832503071403, 55400073181.98617], [0.010582841934294953, -0.03234773381099907, 0.9994206459613922, 168911.14564244283]]
Pixel coordinates (u, v):
(2938.3452497870217, 2484.7347824591498)
(2743.213186527079, 2508.085141001929)
(2710.216496287416, 2253.0345881900257)
(2760.9366348076373, 2247.452531144176)
(2725.3505760252447, 1952.197743758674)
(2604.165932604981, 1968.1017329853264)
(2593.5796075680564, 1882.5592302232726)
(2862.391769630859, 1851.7166617644239)
(2938.3452497870217, 2484.7347824591498)

### Customizing Parameters

You can modify the camera parameters in `data/parameters.json` to simulate different camera settings or orientations. Ensure that `transformation.py` reads these parameters correctly.

### Troubleshooting

- **Unexpected Output**: Verify the correctness of your input parameters (interior and exterior orientation values).
- **Matrix Dimension Errors**: Ensure matrices are defined with appropriate dimensions for multiplication.


