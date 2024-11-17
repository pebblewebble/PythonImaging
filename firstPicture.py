from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt


def create_green_gradient(size, intensity):
    """Create a green gradient overlay with variable intensity"""
    gradient = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    
    # Create a gradient from top to bottom
    for y in range(size[1]):
        # Calculate alpha based on vertical position and overall intensity
        alpha = int(max(0, min(255, (1 - y/size[1]) * 120 * intensity)))
        color = (0, 255, 0, alpha)  # Green with varying alpha
        draw.line([(0, y), (size[0], y)], fill=color)
    
    return gradient

def add_spherical_green_tint(image, intensity=0.5, center=None, radius=100):
    """
    Adds a spherical greenish tint to the image.
    
    Args:
    - image: The input image (PIL Image)
    - intensity: The maximum intensity of the green tint at the center of the sphere
    - center: The (x, y) position for the center of the sphere. If None, defaults to the center of the image.
    - radius: The radius of the spherical area where the green tint will be applied
    
    Returns:
    - Image with the spherical greenish tint applied
    """
    # Convert the PIL image to a numpy array
    image_np = np.array(image)

    # Ensure the image is in RGB format (drop alpha channel if present)
    if image_np.shape[2] == 4:
        image_np = image_np[:, :, :3]  # Keep only RGB channels
    
    # Get image dimensions
    height, width, _ = image_np.shape
    
    # Set the default center of the tint to the center of the image
    if center is None:
        center = (width // 2, height // 2)
    
    center_x, center_y = center
    
    # Create a mask for the spherical gradient
    Y, X = np.indices(image_np.shape[:2])
    
    # Calculate distance from the center point (in pixels)
    dist = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
    
    # Normalize the distance to a range of 0 to 1, using the radius to control the spread
    gradient = np.clip(1 - dist / radius, 0, 1)
    
    # Apply the green tint based on the spherical gradient
    tinted_image_np = image_np.copy()
    tinted_image_np[:, :, 1] = np.clip(tinted_image_np[:, :, 1] + intensity * 255 * gradient, 0, 255)
    
    # Convert the numpy array back to a PIL image
    tinted_image = Image.fromarray(tinted_image_np.astype(np.uint8))

    return tinted_image

image = Image.open("firstPicture.jpg")
deadfish = Image.open("deadfish.png")
center_position = (1400, 1450)  
center_position2 = (1200,1500)
center_position3 = (1600,1500)
center_position4= (2300,1500)
radius = 200
radius2 = 100
tinted_image = add_spherical_green_tint(image, intensity=0.5, center=center_position, radius=radius)
tinted_image = add_spherical_green_tint(tinted_image, intensity=0.5, center=center_position2, radius=radius2)
tinted_image = add_spherical_green_tint(tinted_image, intensity=0.8, center=center_position3, radius=radius)
tinted_image = add_spherical_green_tint(tinted_image, intensity=0.8, center=center_position4, radius=radius)
gradient=create_green_gradient(image.size,0.5)
tinted_image=Image.alpha_composite(tinted_image.convert('RGBA'),gradient)
tinted_image.show()
tinted_image.save("finalOutput.png")  
