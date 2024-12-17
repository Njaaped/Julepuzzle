import matplotlib.pyplot as plt

def mark_differences(image_path):
    """
    Displays a single image (the 'right' image). The user can click on points
    where they see differences. After the user is done (by pressing the middle 
    mouse button), the selected coordinates will be printed to the CLI.
    
    Parameters:
    -----------
    image_path : str
        File path to the image where the user will identify differences.
    """
    
    # Load the image
    img = plt.imread(image_path)
    
    # Display the image
    fig, ax = plt.subplots(figsize=(10, 10), tight_layout=True)
    ax.imshow(img)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set(title="Click on the points that are wrong. Press middle mouse when done.")
    
    # Wait for user clicks until the user presses the middle mouse button
    clicks = plt.ginput(n=-1, timeout=-1, show_clicks=True)
    
    # Close the figure window
    plt.close(fig)
    
    # Print the collected coordinates to the CLI
    # The returned coordinates are in pixel units (image coordinates),
    # where (0,0) is the top-left corner.
    print("You clicked on the following points (x, y):")
    for point in clicks:
        print(point)
    
    return clicks


def normalize_points(points, image_path):
    """
    Normalizes the clicked points based on image dimensions.

    Parameters:
    - points: List of (x, y) coordinates.
    - image_path: Path to the image file to get dimensions.

    Returns:
    - List of normalized coordinates as (x_norm, y_norm).
    """
    img = plt.imread(image_path)
    image_height, image_width = img.shape[:2]  # Extract height and width
    
    normalized = [(x / image_width, y / image_height) for x, y in points]
    return normalized

if __name__ == "__main__":
    # Path to the image where differences will be marked
    image_right_path = "image_right.png"
    
    # Collect points where the user clicks
    clicks = mark_differences(image_right_path)
    
    # Normalize the clicked points
    norm = normalize_points(clicks, image_right_path)
    
    # Print normalized coordinates
    print("Normalized Coordinates:")
    for click in norm:
        print(click)