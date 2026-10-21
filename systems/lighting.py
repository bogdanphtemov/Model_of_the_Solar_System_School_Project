# Lighting system with Sun as main light source
from ursina import *
from config.settings import SUN_SIZE, SUN_TEXTURE, LIGHT_INTENSITY, BACKGROUND_COLOR


def create_sun():
    """
    Create the Sun entity with appropriate lighting and visual properties.
    
    Args:
        scene: The scene to add the Sun to
        
    Returns:
        Entity: The created Sun entity
    """
    # 1. Create the Sun entity
    sun = Entity(
        model='sphere',
        scale=SUN_SIZE,
        texture=SUN_TEXTURE,
        position=(0, 0, 0)
    )
    sun.name = "sun"
    
    # 2. Add point light source (Ursina uses PointLight directly on Entity)
    sun_light = PointLight(
        color=color.rgb(255, 242, 204),  # Warm white with yellow tint (RGB: 255, 242, 204)
        intensity=LIGHT_INTENSITY * 15,   # Adjusted for Ursina's scaling
        range=100.0
    )
    sun_light.parent = sun
    
        # Add the Sun to the scene automatically (Ursina adds entities to scene by default)
    
    return sun


def setup_scene_lighting():
    """
    Set up complete lighting system for the solar system scene.
    
    Returns:
        Sun entity and associated light
    """
    # Set window background color properly (scene.background_color doesn't work in Ursina 8.3.0)
    from ursina.window import instance as window
    from config.settings import BACKGROUND_COLOR_NEW
    # Ursina Color requires exactly 4 values (RGBA)
    window.color = Color(BACKGROUND_COLOR_NEW[0], BACKGROUND_COLOR_NEW[1], BACKGROUND_COLOR_NEW[2], BACKGROUND_COLOR_NEW[3])
    
    # Create and return the Sun as the main light source
    sun = create_sun()
    
    return {"sun": sun}


def adjust_sun_intensity(sun_entity, new_intensity):
    """
    Adjust the intensity of the Sun's light.
    
    Args:
        sun_entity: The Sun entity
        new_intensity: New light intensity value
    """
    # Find the point light that's a child of the sun
    for child in sun_entity.children:
        if isinstance(child, PointLight):
            child.intensity = new_intensity
            break


def toggle_sun_shadows(sun_entity, enabled=True):
    """
    Toggle shadow casting for the Sun.
    
    Args:
        sun_entity: The Sun entity
        enabled: Whether shadows should be enabled
    """
    print("Shadow toggling not implemented in this Ursina version")


def get_lighting_info():
    """
    Get information about the current lighting setup.
    
    Returns:
        Dictionary with lighting information
    """
    return {
        "sun_exists": True,
        "lighting_system": "Ursina PointLight",
        "message": "Lighting info available when entities are created"
    }