# Model of the Solar System - School Project

Interactive 3D model of the Solar System with orbit visualization and free camera control.

## Features

- **Complete Solar System**: Sun and all 8 planets with realistic textures
- **Orbit Rings**: Visual representation of planetary orbits as thin white rings
- **Free Camera**: Intuitive EditorCamera controls (rotate, zoom, pan with mouse)
- **Realistic Speeds**: Slower, more realistic orbital and rotational speeds
- **Dark Space Background**: Eliminates gray grid for authentic cosmic view
- **Interactive Controls**: Toggle orbits, reset camera, reset positions

## Installation

1. Install Ursina Engine:
```bash
pip install ursina
```

2. Run the program:
```bash
python main.py
```

## Controls

### Keyboard
- **ESC** - Exit simulation
- **R** - Reset planet orbits to starting positions
- **O** - Toggle orbit visibility on/off
- **C** - Reset camera to starting position
- **H** - Show help information

### Mouse (Free Camera)
- **Right Mouse + Move** - Rotate camera around the scene
- **Mouse Wheel** - Zoom in/out
- **Middle Mouse + Move** - Pan camera
- **WASD/QE** - Fly around (must hold Right Mouse to move)

## Project Structure

- `main.py` - main program with enhanced controls and visualization
- `config/settings.py` - all configuration parameters (orbits, speeds, camera, colors)
- `systems/` - game logic modules:
  - `planet_orbit.py` - planetary movement and rotation
  - `orbits.py` - **NEW**: creates visual orbit rings
  - `lighting.py` - Sun lighting (currently not used in main program)
- `assets/textures/` - planet and Sun textures (missing Venus texture)
- `scenes/` - configuration files for scene setup