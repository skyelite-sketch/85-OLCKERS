import ezdxf

def create_floor_plan():
    # Create a new DXF document
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Define dimensions
    wall_thickness = 0.1  # thickness of the walls
    room_dimensions = {"room1": (5, 4), "room2": (3, 3), "hallway": (4, 1)}

    # Draw walls
    for room, (width, height) in room_dimensions.items():
        # Example of drawing a rectangle for a room (walls)
        msp.add_lwpolyline(points=[(0, 0), (width, 0), (width, height), (0, height)], close=True, width=wall_thickness)

        # Add labels
        msp.add_text(room, insert=(width/2, height/2), height=0.2)

    # Draw doors and windows (placeholders)
    msp.add_line(start=(2.5, 0), end=(2.5, 0.1))  # door example
    msp.add_line(start=(1, 2), end=(1.1, 2))      # window example

    # Save the DXF document
    doc.saveas("85-OLCKERS_floor_plan.dxf")

if __name__ == '__main__':
    create_floor_plan()