# config/settings.py

# Sun parameters
SUN_SIZE = 2.0
SUN_TEXTURE = "assets/textures/sun.png"

# Planets parameters
# orbit_radius - distance from the Sun
# size - planet size  
# orbit_speed - orbital movement speed
# spin_speed - rotation speed around its own axis
PLANETS_DATA = [
    {"name": "mercury", "orbit_radius": 4.0,  "size": 0.2, "orbit_speed": 1.6, "spin_speed": 0.5, "texture": "assets/textures/mercury.png"},
    {"name": "venus",   "orbit_radius": 6.0,  "size": 0.3, "orbit_speed": 1.2, "spin_speed": 0.4, "texture": "assets/textures/venus.png"},
    {"name": "earth",   "orbit_radius": 8.0,  "size": 0.3, "orbit_speed": 1.0, "spin_speed": 0.4, "texture": "assets/textures/earth.png"},
    {"name": "mars",    "orbit_radius": 10.0, "size": 0.25, "orbit_speed": 0.8, "spin_speed": 0.3, "texture": "assets/textures/mars.png"},
    {"name": "jupiter", "orbit_radius": 15.0, "size": 0.8, "orbit_speed": 0.5, "spin_speed": 0.2, "texture": "assets/textures/jupiter.png"},
    {"name": "saturn",  "orbit_radius": 20.0, "size": 0.7, "orbit_speed": 0.4, "spin_speed": 0.2, "texture": "assets/textures/saturn.png"},
    {"name": "uranus",  "orbit_radius": 25.0, "size": 0.5, "orbit_speed": 0.3, "spin_speed": 0.2, "texture": "assets/textures/uranus.png"},
    {"name": "neptune", "orbit_radius": 30.0, "size": 0.5, "orbit_speed": 0.2, "spin_speed": 0.2, "texture": "assets/textures/neptune.png"},
]

# Additional settings
BACKGROUND_COLOR = (0.0, 0.0, 0.1)  # Dark blue background for space
LIGHT_INTENSITY = 1.5  # Sun light intensity

# --- Orbital Visualization ---
SHOW_ORBITS = True
ORBIT_LINE_COLOR = (1.0, 1.0, 1.0)   # White color for orbit rings
ORBIT_LINE_ALPHA = 0.35
ORBIT_LINE_WIDTH = 0.06              # Width in world units (~60 units in the system)
ORBIT_LINE_SEGMENTS = 128            # Circle smoothness

# --- Speed Multipliers (1.0 = current speed, 0.1 = 10x slower) ---
ORBIT_SPEED_MULTIPLIER = 0.1         # Slower orbital movement
SPIN_SPEED_MULTIPLIER = 0.1          # Slower rotation

# --- Camera ---
CAMERA_START_POSITION = (0, 35, -55) # EditorCamera start position
CAMERA_START_ROTATION = (25, 0, 0)   # EditorCamera start rotation

# --- Background (0..1, set via window.color) ---
BACKGROUND_COLOR_NEW = (0.02, 0.02, 0.06, 1.0)   # Must have 4 values (RGBA) for Ursina Color class