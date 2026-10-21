#!/usr/bin/env python3
"""
Solar System Simulation - Main Entry Point
School Project for Solar System Modeling
Adapted for Ursina Engine
"""

from ursina import *
from config.settings import PLANETS_DATA, SUN_SIZE, SUN_TEXTURE, SHOW_ORBITS, \
                           ORBIT_LINE_COLOR, ORBIT_LINE_ALPHA, ORBIT_LINE_WIDTH, ORBIT_LINE_SEGMENTS, \
                           ORBIT_SPEED_MULTIPLIER, SPIN_SPEED_MULTIPLIER, \
                           CAMERA_START_POSITION, CAMERA_START_ROTATION, \
                           BACKGROUND_COLOR_NEW
from systems.planet_orbit import update_planets, reset_all_orbits
from systems.orbits import create_orbit_rings, set_orbits_enabled


# Global variables for the simulation
sun = None
planet_entities = {}
orbit_entities = {}  # Dictionary for orbit rings


def create_solar_system():
    """Create and setup the solar system with Sun, orbit rings, and planets."""
    global sun, planet_entities, orbit_entities
    
    print("=== Solar System Simulation ===")
    print("Creating solar system...")
    
    # Create Sun
    sun = Entity(
        model='sphere', 
        scale=SUN_SIZE,
        texture=SUN_TEXTURE,
        position=(0, 0, 0)
    )
    
    # Add light to Sun
    PointLight(parent=sun, color=color.rgb(255, 242, 204), intensity=20)
    
    sun.name = "sun"
    print("✓ Sun created")
    
    # Create orbit rings first (behind planets visually)
    orbit_entities = create_orbit_rings(PLANETS_DATA)
    if SHOW_ORBITS:
        print(f"✓ Created {len(orbit_entities)} orbit rings")
    
    # Create planets
    planet_entities = {}
    print("Creating planets...")
    
    for planet_data in PLANETS_DATA:
        try:
            planet = Entity(
                model='sphere',
                scale=planet_data["size"],
                texture=planet_data["texture"]
            )
            planet.name = planet_data["name"]
            planet_entities[planet_data["name"]] = planet
            print(f"  ✓ Created {planet_data['name']}")
        except Exception as e:
            print(f"  ✗ Failed to create {planet_data['name']}: {e}")
    
    # Initialize orbits
    reset_all_orbits(planet_entities)
    print("Planets initialized with orbital positions")
    
    return sun, planet_entities, orbit_entities


def update():
    """Main update function called every frame."""
    global planet_entities
    
    if planet_entities:
        update_planets(planet_entities, time.dt)


def input(key):
    """Handle keyboard input."""
    global planet_entities, orbit_entities
    
    if key == 'escape':
        print("ESC pressed - exiting simulation")
        quit()
    
    # Reset orbits when R is pressed
    elif key == 'r':
        if planet_entities:
            reset_all_orbits(planet_entities)
            print("Planet orbits reset")
    
    # Toggle orbit visibility when O is pressed
    elif key == 'o':
        if orbit_entities:
            current_state = list(orbit_entities.values())[0].enabled
            set_orbits_enabled(orbit_entities, not current_state)
            state_text = "hidden" if current_state else "shown"
            print(f"Orbits {state_text}")
    
    # Reset camera position when C is pressed
    elif key == 'c':
        if hasattr(editor_camera, 'position'):
            editor_camera.position = CAMERA_START_POSITION
            editor_camera.rotation = CAMERA_START_ROTATION
            print("Camera reset to start position")
    
    # Print help when H is pressed
    elif key == 'h':
        print("\n=== Controls ===")
        print("ESC - Exit simulation")
        print("R - Reset planet orbits")
        print("O - Toggle orbit visibility")
        print("C - Reset camera position")
        print("H - Show this help")
        print("\n--- Camera Controls ---")
        print("Right Mouse + Mouse Move - Rotate camera")
        print("Mouse Wheel - Zoom in/out")
        print("Middle Mouse + Mouse Move - Pan camera")
        print("WASD/QE (with Right Mouse) - Fly around")


# Main execution
if __name__ == "__main__":
    print("Solar System Simulation - School Project")
    print("Running with Ursina Engine")
    print("Enhanced version with orbit rings and free camera control")
    
    try:
        # Create the app with clean interface
        app = Ursina(editor_ui_enabled=False, title='Solar System Simulation')
        
        # Set background color properly via window.color (not scene.background_color)
        # Ursina Color requires exactly 4 values (RGBA)
        window.color = Color(BACKGROUND_COLOR_NEW[0], BACKGROUND_COLOR_NEW[1], BACKGROUND_COLOR_NEW[2], BACKGROUND_COLOR_NEW[3])
        
        # Create solar system
        create_solar_system()
        
        # Create free camera (EditorCamera) instead of manual camera positioning
        editor_camera = EditorCamera(rotation_speed=120, move_speed=15)
        editor_camera.position = CAMERA_START_POSITION
        editor_camera.rotation = CAMERA_START_ROTATION
        
        print("\n=== Simulation Ready ===")
        print("Controls: ESC=Exit, R=Reset orbits, O=Toggle orbits, C=Reset camera, H=Help")
        print("Free camera: Right Mouse=Rotate, Wheel=Zoom, Middle Mouse=Pan, WASD/QE (with Right Mouse)=Fly")
        
        # Start the game loop
        app.run()
        
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("Simulation ended")