# System for planet orbital movements around the Sun
import math


def update_planets(planet_entities, time_delta):
    """
    Update planet positions and rotations based on orbital mechanics.
    
    Args:
        planet_entities: Dictionary containing planet entities with their names as keys
        time_delta: Time elapsed since last update (in seconds)
    """
    from config.settings import PLANETS_DATA

    for planet_data in PLANETS_DATA:
        name = planet_data["name"]
        
        # Check if the planet exists in the scene
        if name not in planet_entities:
            continue
            
        entity = planet_entities[name]
        
        # Initialize angle and other orbital parameters if they don't exist
        if not hasattr(entity, '_orbital_angle'):
            # Give each planet a different starting angle for visual variety
            entity._orbital_angle = planet_data.get("initial_angle", 0.0)
            
        # Get orbital parameters
        from config.settings import ORBIT_SPEED_MULTIPLIER, SPIN_SPEED_MULTIPLIER
        orbit_speed = planet_data["orbit_speed"] * ORBIT_SPEED_MULTIPLIER
        orbit_radius = planet_data["orbit_radius"]
        spin_speed = planet_data["spin_speed"] * SPIN_SPEED_MULTIPLIER
        
        # 1. Orbital movement around the Sun (circular orbit)
        entity._orbital_angle += orbit_speed * time_delta
        
        # Keep the angle within 0-2π to avoid overflow
        entity._orbital_angle %= 2 * math.pi
        
        # Calculate new position using trigonometry (Ursina uses position instead of transform.position)
        x = math.cos(entity._orbital_angle) * orbit_radius
        z = math.sin(entity._orbital_angle) * orbit_radius
        entity.position = (x, 0, z)
        
        # 2. Rotation around own axis (for visual effect)
        entity.rotation_y += spin_speed * time_delta * 60  # Scale for smooth rotation
        
        # Optional: Keep rotation angle within reasonable bounds
        entity.rotation_y %= 360


def get_planet_orbit_info(entity):
    """
    Get current orbital information for a planet entity.
    
    Args:
        entity: Planet entity
        
    Returns:
        Dictionary with orbital information or None if not a valid planet
    """
    if not hasattr(entity, '_orbital_angle'):
        return None
        
    return {
        'orbital_angle': entity._orbital_angle,
        'orbital_angle_degrees': math.degrees(entity._orbital_angle),
        'position': entity.position
    }


def reset_all_orbits(planet_entities, initial_angles=None):
    """
    Reset all planets to their starting orbital positions.
    
    Args:
        planet_entities: Dictionary containing planet entities
        initial_angles: Optional dictionary mapping planet names to initial angles
    """
    from config.settings import PLANETS_DATA
    
    for planet_data in PLANETS_DATA:
        name = planet_data["name"]
        
        if name not in planet_entities:
            continue
            
        entity = planet_entities[name]
        
        # Set initial angle
        if initial_angles and name in initial_angles:
            entity._orbital_angle = initial_angles[name]
        else:
            # Default: evenly distribute planets around the Sun
            planet_index = next(i for i, p in enumerate(PLANETS_DATA) if p["name"] == name)
            entity._orbital_angle = (2 * math.pi / len(PLANETS_DATA)) * planet_index
        
        # Reset position based on new angle
        radius = planet_data["orbit_radius"]
        x = math.cos(entity._orbital_angle) * radius
        z = math.sin(entity._orbital_angle) * radius
        entity.position = (x, 0, z)
        
        # Reset rotation
        entity.rotation_y = 0.0