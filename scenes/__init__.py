# Scene management for the Solar System simulation
import json
import os
from pathlib import Path
from ursina.color import Color  # Import Color class for background color


def load_scene_config(scene_name="solar_system"):
    """
    Load configuration from a scene JSON file.
    
    Args:
        scene_name: Name of the scene file (without .json extension)
        
    Returns:
        Dictionary with scene configuration
    """
    json_path = Path(__file__).parent / f"{scene_name}.json"
    
    if not json_path.exists():
        print(f"Warning: Scene file {json_path} not found, using defaults")
        return get_default_scene_config()
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"Loaded scene configuration from {json_path}")
            return config
    except Exception as e:
        print(f"Error loading scene config: {e}")
        return get_default_scene_config()


def get_default_scene_config():
    """
    Get default scene configuration.
    
    Returns:
        Dictionary with default scene settings
    """
    return {
        "name": "Solar System Scene",
        "description": "Default scene with Sun and planets",
        "version": "1.0",
        "camera": {
            "position": [0, 40, -50],
            "look_at": [0, 0, 0],
            "fov": 60,
            "near_plane": 0.1,
            "far_plane": 200.0
        },
        "scene_settings": {
            "background_color": [0.0, 0.0, 0.1],
            "exposure": 1.0
        },
        "created_by": "Solar System School Project"
    }


def apply_camera_settings(camera, camera_settings):
    """
    Apply camera settings from scene configuration.
    
    Args:
        camera: The camera object to configure
        camera_settings: Dictionary with camera settings
    """
    if not camera_settings:
        return
    
    # Apply position if available
    if "position" in camera_settings:
        pos = camera_settings["position"]
        if hasattr(camera, 'transform') and hasattr(camera.transform, 'position'):
            camera.transform.position.set(pos[0], pos[1], pos[2])
    
    # Apply look-at target if available
    if "look_at" in camera_settings:
        target = camera_settings["look_at"]
        # Implementation depends on your engine's camera API
        # camera.look_at(target[0], target[1], target[2])
        pass
    
    # Apply FOV if available
    if "fov" in camera_settings:
        if hasattr(camera, 'fov'):
            camera.fov = camera_settings["fov"]
    
    # Apply near/far planes if available
    if "near_plane" in camera_settings:
        if hasattr(camera, 'near_plane'):
            camera.near_plane = camera_settings["near_plane"]
    if "far_plane" in camera_settings:
        if hasattr(camera, 'far_plane'):
            camera.far_plane = camera_settings["far_plane"]


def apply_scene_settings(scene, scene_settings):
    """
    Apply scene-wide settings from configuration.
    
    Args:
        scene: The scene object to configure
        scene_settings: Dictionary with scene settings
    """
    if not scene_settings:
        return
    
    # Apply background color
    if "background_color" in scene_settings:
        bg_color = scene_settings["background_color"]
        # Set window background color instead of scene.background_color (which doesn't work)
        from ursina.window import instance as window
        # Handle both RGB (3 values) and RGBA (4 values) color formats
        # Ursina Color requires exactly 4 values, so convert RGB to RGBA if needed
        if len(bg_color) == 3:
            window.color = Color(bg_color[0], bg_color[1], bg_color[2], 1.0)  # RGB + alpha=1.0
        else:
            window.color = Color(bg_color[0], bg_color[1], bg_color[2], bg_color[3])  # RGBA
    
    # Apply exposure
    if "exposure" in scene_settings:
        if hasattr(scene, 'exposure'):
            scene.exposure = scene_settings["exposure"]


def get_scene_info(scene_config):
    """
    Get formatted information about the scene.
    
    Args:
        scene_config: Scene configuration dictionary
        
    Returns:
        String with scene information
    """
    return f"""
Scene: {scene_config.get('name', 'Unknown')}
Description: {scene_config.get('description', 'No description')}
Version: {scene_config.get('version', 'Unknown')}
Created by: {scene_config.get('created_by', 'Unknown')}
Camera Position: {scene_config.get('camera', {}).get('position', 'Default')}
""".strip()


# Export functions
__all__ = [
    'load_scene_config',
    'get_default_scene_config', 
    'apply_camera_settings',
    'apply_scene_settings',
    'get_scene_info'
]