import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sqrt

def draw_game(image_left_path, image_right_path, differences):
    """
    Draws two images side by side. The left image is the original.
    The right image includes a few small 'differences' highlighted by circles.
    The player can click on the differences in the right image.
    
    Parameters:
    -----------
    image_left_path : str
        File path to the left/original image.
    image_right_path : str
        File path to the right image (with differences).
    differences : list of tuples (x, y, r)
        Hardcoded coordinates and radius of differences in normalized image coordinates.
        Example: differences = [(0.3, 0.4, 0.03), (0.6, 0.7, 0.03), ...]
    """

    # Load the two images
    left_img = plt.imread(image_left_path)
    right_img = plt.imread(image_right_path)

    # Set up figure and axes
    fig, axes = plt.subplots(1, 2, figsize=(10, 10), tight_layout=True)
    axes[0].imshow(left_img)
    axes[1].imshow(right_img)
    for ax in axes:
        ax.set(xticks=[], yticks=[])

    axes[0].set(title="Original Image")
    axes[1].set(title="Find the Differences")

    # Draw circles (differences) on the right image
    # These are visible hints. If you want them hidden initially, you could skip
    # drawing them first and only highlight them after the user is done.
    # For now, let's just draw them to show where differences are.
    for (dx, dy, dr) in differences:
        # Note: Coordinates (dx, dy) should correspond to normalized coordinates
        # relative to the image displayed. If images are displayed in their full
        # extent, (0,0) is top-left and (1,1) is bottom-right when imshow uses
        # aspect='equal' and no extent is specified. 
        # The circle radius 'dr' should be a recognizable size.
        circle = Circle(
        (dx * right_img.shape[1], dy * right_img.shape[0]),
        radius=dr * min(right_img.shape[0], right_img.shape[1]),
        fill=False,
        edgecolor='red',
        linewidth=2,
        alpha=0  # Initially invisible
    )
        # We add the circle as an annotation. Transforms by default map data coords.
        # We need to make sure the coordinates align with image pixels:
        axes[1].add_artist(circle)

    # Wait for user clicks on the figure
    # The user can click until they press middle mouse button.
    clicks = plt.ginput(n=-1, timeout=-1, show_clicks=True)

    # Check how many differences were found
    found = 0
    for i, diff in enumerate(differences):
        dx, dy, dr = diff
        diff_found = False
        for click in clicks:
            cx, cy = click
            # Convert click coordinates (in pixels) to image-normalized coordinates
            # cx, cy are in figure coordinates. We need to map them back to image coordinates.
            # Since we called imshow without extent, image is displayed with:
            # x from 0 to width-1, y from 0 to height-1 in pixel coordinates of the Axes.
            # The 'click' returned by ginput is in data coordinates matching the axes.
            # So (cx, cy) should directly correspond to pixel positions in the displayed image.
            
            # Distance between click and diff center in pixels
            d = sqrt((cx - dx*right_img.shape[1])**2 + (cy - dy*right_img.shape[0])**2)
            if d <= dr * min(right_img.shape[0], right_img.shape[1]):
                diff_found = True
                found += 1
                break

        # Color code found/not found differences
        color = 'green' if diff_found else None
        if color != None:
            axes[1].scatter(dx * right_img.shape[1], dy * right_img.shape[0], 
                            marker='o', s=100, c=color, edgecolor='k')

    axes[0].set(title="Game Finished!")
    axes[1].set(title=f"You found {found}/{len(differences)} differences.")
    plt.show()


if __name__ == "__main__":

    # Example usage:
    # Assume we have two identical images "image_left.png" and "image_right.png"
    # The right one visually has 5 small differences you decided to highlight with circles.
    # differences = [(x1, y1, r1), (x2, y2, r2), ...] in normalized coords.
    # Here we choose some arbitrary points. Adjust these to actual difference locations:

    # (np.float64(0.6859205571283585), np.float64(0.9677048524706718))
    # (np.float64(0.1307659179531008), np.float64(0.9725075542125843))
    # (np.float64(0.5709721035201112), np.float64(0.3906945431923212))
    # (np.float64(0.34210612413866787), np.float64(0.42431345538570914))
    # (np.float64(0.05138447465413173), np.float64(0.05793592250266607))



    differences = [
        (0.6859, 0.9677, 0.04),
        (0.1307, 0.972, 0.04),
        (0.5709, 0.3906, 0.04),
        (0.3421, 0.4243, 0.04),
        (0.0513, 0.05793, 0.04)
    ]

    # (np.float64(0.8780360151773882), np.float64(0.09728063547113121))
    # (np.float64(0.14341992547101168), np.float64(0.8056432496664934))
    # (np.float64(0.04960531661240515), np.float64(0.3929587802357132))
    # (np.float64(0.8674354944024044), np.float64(0.34815906133198865))
    # (np.float64(0.6458846102052432), np.float64(0.41456805641280386))

    differences2 = [
        (0.8780, 0.0972, 0.04),
        (0.1434, 0.8056, 0.04),
        (0.0496, 0.3929, 0.04),
        (0.8674, 0.3481, 0.04),
        (0.6458, 0.4145, 0.04)
    ]

    # (np.float64(0.8683947839324824), np.float64(0.7705744885422786))
    # (np.float64(0.5518999385716575), np.float64(0.5162789558962305))
    # (np.float64(0.8730339591902143), np.float64(0.09909682531203806))
    # (np.float64(0.7183947839324824), np.float64(0.07091813115396242))
    # (np.float64(0.8323123097056783), np.float64(0.9781346259993234))

    differences3 = [
        (0.8683, 0.7705, 0.04),
        (0.55189, 0.5162, 0.04),
        (0.8730, 0.09909, 0.04),
        (0.71839, 0.070918, 0.04),
        (0.8323, 0.9781, 0.04)
    ]

    # Provide your actual image paths:
    image_left_path = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/image_left.png"
    image_right_path = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/image_right.png"

    image_left_path2 = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/right_image2.png"
    image_right_path2 = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/left_image2.png"

    image_left_path3 = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/left_image3.png"
    image_right_path3 = "/Users/njalpedersen/Documents/Dokumenter – njåls MacBook Pro/5. semester/jul/Julepuzzle/right_image3.png"

    draw_game(image_left_path, image_right_path, differences)
    draw_game(image_left_path2, image_right_path2, differences2)
    draw_game(image_left_path3, image_right_path3, differences3)
