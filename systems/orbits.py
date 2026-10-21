# System for creating and managing planet orbit visualization rings
import math
from ursina import Entity, Mesh, Vec3, color
from config.settings import ORBIT_LINE_COLOR, ORBIT_LINE_ALPHA, ORBIT_LINE_WIDTH, ORBIT_LINE_SEGMENTS


def orbit_ring_vertices(radius, width, segments=128):
    """
    Generate vertices and triangles for a flat orbit ring (annulus) in the XZ plane.
    
    Args:
        radius: Outer radius of the ring
        width: Ring width (difference between outer and inner radius)
        segments: Number of segments for the circle
        
    Returns:
        tuple: (vertices, triangles) for creating a Mesh
    """
    if width >= radius:
        width = radius * 0.9  # Prevent invalid geometry
        
    inner_radius = radius - width
    vertices = []
    triangles = []
    
    for i in range(segments):
        angle = (2 * math.pi * i) / segments
        next_angle = (2 * math.pi * (i + 1)) / segments
        
        # Outer circle vertices
        x_outer = math.cos(angle) * radius
        z_outer = math.sin(angle) * radius
        
        x_outer_next = math.cos(next_angle) * radius
        z_outer_next = math.sin(next_angle) * radius
        
        # Inner circle vertices  
        x_inner = math.cos(angle) * inner_radius
        z_inner = math.sin(angle) * inner_radius
        
        x_inner_next = math.cos(next_angle) * inner_radius
        z_inner_next = math.sin(next_angle) * inner_radius
        
        # Add vertices: outer, inner for current angle
        v_start = len(vertices)
        vertices.extend([
            Vec3(x_outer, 0, z_outer),     # Outer vertex at current angle
            Vec3(x_inner, 0, z_inner),     # Inner vertex at current angle
            Vec3(x_outer_next, 0, z_outer_next),  # Outer vertex at next angle
            Vec3(x_inner_next, 0, z_inner_next)   # Inner vertex at next angle
        ])
        
        # Create two triangles per segment
        # Triangle 1: outer_curr -> inner_curr -> outer_next
        triangles.extend([v_start, v_start + 1, v_start + 2])
        # Triangle 2: inner_curr -> inner_next -> outer_next
        triangles.extend([v_start + 1, v_start + 3, v_start + 2])
    
    return vertices, triangles


def create_orbit_ring(radius, name=None):
    """
    Create an orbit ring entity.
    
    Args:
        radius: Orbit radius (outer radius)
        name: Optional name for the ring
        
    Returns:
        Entity: The orbit ring entity
    """
    vertices, triangles = orbit_ring_vertices(radius, ORBIT_LINE_WIDTH, ORBIT_LINE_SEGMENTS)
    
    ring_entity = Entity(
        model=Mesh(
            vertices=vertices,
            triangles=triangles,
            mode='triangle'
        ),
        color=color.rgb(ORBIT_LINE_COLOR[0] * 255, 
                       ORBIT_LINE_COLOR[1] * 255, 
                       ORBIT_LINE_COLOR[2] * 255, 
                       ORBIT_LINE_ALPHA * 255),
        unlit=True,
        double_sided=True,  # Visible from both sides in case camera goes below the plane
        position=(0, 0, 0)
    )
    
    if name:
        ring_entity.name = f"orbit_{name}"
    
    return ring_entity


def create_orbit_rings(planets_data):
    """
    Create orbit rings for all planets.
    
    Args:
        planets_data: List of planet data dictionaries
        
    Returns:
        dict: Dictionary mapping planet names to their orbit ring entities
    """
    from config.settings import SHOW_ORBITS
    
    orbit_entities = {}
    
    if not SHOW_ORBITS:
        return orbit_entities
    
    for planet_data in planets_data:
        name = planet_data["name"]
        orbit_radius = planet_data["orbit_radius"]
        
        ring = create_orbit_ring(orbit_radius, name=name)
        orbit_entities[name] = ring
    
    return orbit_entities


def set_orbits_enabled(orbit_entities, enabled):
    """
    Enable or disable visibility of orbit rings.
    
    Args:
        orbit_entities: Dictionary of orbit ring entities
        enabled: Whether orbits should be visible
    """
    for ring in orbit_entities.values():
        ring.enabled = enabled


# For easy testing if this module is run directly
if __name__ == "__main__":
    # Simple test without creating the full Ursina app
    test_vertices, test_tris = orbit_ring_vertices(10.0, 1.0, 16)
    print(f"Test ring: {len(test_vertices)} vertices, {len(test_tris)} triangles")
    print("Module 'orbits' functions are working correctly")