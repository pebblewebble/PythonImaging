from PIL import Image, ImageEnhance, ImageDraw, ImageFilter
import numpy as np
import random
from IPython.display import display
from PIL import ImageSequence
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from transformers import pipeline
from moviepy.editor import ImageSequenceClip

# Load the image
img = Image.open("secondPicture.jpg").convert("RGBA")
protestors = Image.open("protestors.png")
newspapers = Image.open("newspaper.png")
pipe = pipeline(task="depth-estimation",
                model="depth-anything/Depth-Anything-V2-Base-hf")
                # perform depth estimation
depth = pipe(img)["depth"]

def overlay_transparent_layer(rgb_image, grayscale_image):
 
    # Create a white layer with the same size as the input images
    white_layer = Image.new('RGBA', rgb_image.size, (216,216,216,0))
 
    # Convert images to numpy arrays for easier manipulation
    rgb_array = np.array(rgb_image)
    grayscale_array = np.array(grayscale_image)
    white_array = np.array(white_layer)
 
    # Calculate alpha values (invert grayscale values)
    alpha = 255 - grayscale_array

    alpha = (alpha*0.9).astype(np.uint8)
 
    # Set the alpha channel of the white layer
    white_array[:, :, 3] = alpha
 
    # Convert back to PIL Image
    white_layer_transparent = Image.fromarray(white_array, 'RGBA')
 
    # Composite the images
    result = Image.alpha_composite(rgb_image.convert('RGBA'), white_layer_transparent)
 
    return result

def apply_random_yellow_sky(image, mask, white_threshold=240, num_yellow_pixels=500):
    # Convert image to RGBA if it isn't already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    # Convert to numpy arrays with correct orientation
    image_array = np.array(image)
    mask_array = np.array(mask)
    
    print("Image shape:", image_array.shape)
    print("Mask shape:", mask_array.shape)
    
    # Get coordinates where mask is above threshold
    white_coords = np.argwhere(mask_array > white_threshold)
    print(f"Found {len(white_coords)} coordinates above threshold {white_threshold}")
    
    if len(white_coords) == 0:
        return image
    
    # Make a copy of the image array
    modified_array = image_array.copy()
    
    # Select random coordinates
    num_pixels_to_change = min(num_yellow_pixels, len(white_coords))
    selected_indices = np.random.choice(len(white_coords), num_pixels_to_change, replace=False)
    selected_coords = white_coords[selected_indices]
    
    # Make yellow more visible and add some variation
    for y, x in selected_coords:
        # Add small random variations to make stars more visible
        brightness = np.random.randint(200, 256)
        # Larger size options: 3 to 6 pixels
        size = np.random.choice([15,20,25])  # Increased star sizes
        
        # Create a larger star pattern
        for dy in range(-size, size+1):
            for dx in range(-size, size+1):
                new_y, new_x = y + dy, x + dx
                if (0 <= new_y < image_array.shape[0] and 
                    0 <= new_x < image_array.shape[1]):
                    # Distance from center of star
                    dist = np.sqrt(dy**2 + dx**2)
                    if dist <= size:
                        # Smoother brightness falloff for larger stars
                        falloff = 2  # Adjust this to control how quickly brightness falls off
                        pixel_brightness = int(brightness * (1 - (dist/size)**falloff))
                        pixel_brightness = max(0, min(255, pixel_brightness))  # Ensure valid range
                        modified_array[new_y, new_x] = [
                            pixel_brightness,  # R
                            pixel_brightness,  # G
                            0,                # B
                            255              # A
                        ]
    
    return Image.fromarray(modified_array, 'RGBA')

def create_sky_mask(image, threshold=160, top_fraction=0.4, middle_fraction=0.2):
    """
    Creates a sky mask with specific region constraints.
    """
    # Convert to grayscale with more detail preservation
    grayscale = image.convert("L")
    
    # Enhance contrast slightly to better differentiate sky
    enhancer = ImageEnhance.Contrast(grayscale)
    enhanced = enhancer.enhance(1.2)  # Adjust this value to control contrast
    
    # Convert to numpy array to preserve full grayscale range
    mask_array = np.array(enhanced)
    
    # Create output mask array
    height, width = mask_array.shape
    refined_mask_array = np.zeros_like(mask_array)
    
    # Define region bounds
    top_cutoff = int(height * top_fraction)+500
    middle_start = int(width * (1 - middle_fraction) / 2) + 200
    middle_end = int(width * (1 + middle_fraction) / 2) + 250
    
    # Apply the grayscale values to the defined region
    refined_mask_array[:top_cutoff, middle_start:middle_end] = mask_array[:top_cutoff, middle_start:middle_end]
    
    refined_mask = Image.fromarray(refined_mask_array)
    refined_mask = refined_mask.filter(ImageFilter.GaussianBlur(radius=2))
    
    return refined_mask

# Create new mask with adjusted parameters
sky_mask = create_sky_mask(img)

image_array = np.array(protestors)
image_array[:, :, :3] = 0
protestors = Image.fromarray(image_array)
protestors = protestors.resize((1800,1200))

position = (700,1300)
img.paste(protestors, position, protestors)

newspaperPosition = (2100,2000)

img.paste(newspapers, newspaperPosition, newspapers)

newspaperPosition = (300,2000)
newspapers = newspapers.rotate(45, expand=True)
img.paste(newspapers, newspaperPosition, newspapers)

img = overlay_transparent_layer(img, depth)

def create_sun(size, radius, position=(0, 0)):
    sun_size = (size, size)
    sun_img = Image.new("RGBA", sun_size, (0, 0, 0, 0))
    sun_center = (sun_size[0] // 2, sun_size[1] // 2)
    sun_color = (255, 165, 0)

    draw = ImageDraw.Draw(sun_img)

    # Draw gradient circle
    for r in range(radius, 0, -1):
        color_factor = int(255 - (r / radius) * 50)
        color = (sun_color[0], sun_color[1], sun_color[2] - color_factor)
        draw.ellipse(
            [sun_center[0] - r, sun_center[1] - r, sun_center[0] + r, sun_center[1] + r],
            fill=color
        )

    # Apply glow effect
    glow_effect = sun_img.filter(ImageFilter.GaussianBlur(20))

    # Create aura
    aura_size = (size + 100, size + 100)
    aura_img = Image.new("RGBA", aura_size, (0, 0, 0, 0))
    aura_draw = ImageDraw.Draw(aura_img)
    aura_center = (aura_size[0] // 2, aura_size[1] // 2)
    aura_radius = radius + 100
    aura_color = (255, 140, 0, 100)

    for r in range(aura_radius, 0, -1):
        alpha = int(255 * (1 - r / aura_radius))
        aura_color_with_alpha = (aura_color[0], aura_color[1], aura_color[2], alpha)
        aura_draw.ellipse(
            [aura_center[0] - r, aura_center[1] - r, aura_center[0] + r, aura_center[1] + r],
            fill=aura_color_with_alpha
        )

    # Combine glow and aura
    glow_effect_resized = glow_effect.resize(aura_img.size, Image.Resampling.LANCZOS)
    return Image.alpha_composite(aura_img, glow_effect_resized)

def create_orange_gradient(size, intensity):
    """Create an orange gradient overlay with variable intensity"""
    gradient = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    
    # Create a gradient from top to bottom
    for y in range(size[1]):
        # Calculate alpha based on vertical position and overall intensity
        alpha = int(max(0, min(255, (1 - y/size[1]) * 120 * intensity)))
        color = (255, 165, 0, alpha)  # Orange with varying alpha
        draw.line([(0, y), (size[0], y)], fill=color)
    
    return gradient

def create_night_gradient(size, intensity):
    """Create a dark gradient overlay with variable intensity for a night effect"""
    gradient = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    
    # Create a gradient from top to bottom
    for y in range(size[1]):
        # Calculate alpha based on vertical position and overall intensity
        alpha = int(max(0, min(255, (1 - y/size[1]) * 255 * intensity)))  # More intense alpha
        # Dark blue or purple night color (RGB: (25, 25, 112) or a deep purple tone)
        color = (25, 25, 112, alpha)  # Dark blue with varying alpha for fading into night
        draw.line([(0, y), (size[0], y)], fill=color)
    
    return gradient

# Create animation frames
frames = []
num_frames = 50
num_frames_night = 50

# Initial values
initial_size = 500
initial_radius = 65
final_size = 100 
final_radius = 10  

for frame_num in range(num_frames):
    frame = img.copy()
    
    # Calculate current size and radius using linear interpolation
    current_size = int(initial_size - (initial_size - final_size) * (frame_num / num_frames))
    current_radius = int(initial_radius - (initial_radius - final_radius) * (frame_num / num_frames))
    
    # Create sun at current size
    sun = create_sun(current_size, current_radius)
    
    # Calculate position (moving down and slightly to the right)
    x_pos = 1400 + frame_num * 3   # Move slightly right
    y_pos = 50 + frame_num * 20   # Move down
    
    gradient_intensity = 1 - (frame_num/num_frames)*1.3
    img_size = img.size
    gradient = create_orange_gradient(img_size,gradient_intensity)
    frame = Image.alpha_composite(frame.convert('RGBA'),gradient)

    # Paste the sun onto the frame
    frame.paste(sun, (x_pos, y_pos), sun)
    frames.append(np.array(frame)) 

# Store the star pattern frame
star_frame = None

for frame_num in range(num_frames, num_frames + num_frames_night):
    frame = img.copy()
    
    # Generate new star pattern every 15 frames
    if (frame_num - num_frames) % 15 == 0:
        star_frame = apply_random_yellow_sky(
            frame,
            sky_mask,
            white_threshold=240,  
            num_yellow_pixels=10
        )
    
    # Use the current star pattern if it exists
    if star_frame is not None:
        frame = star_frame.copy()
    
    # Gradually darken the scene to simulate night
    darkening_factor = (frame_num - num_frames) / num_frames_night * 0.8
    night_gradient = create_night_gradient(img.size, intensity=darkening_factor)
    
    frame = Image.alpha_composite(frame.convert('RGBA'), night_gradient)
    frames.append(np.array(frame))

# Now save it as an MP4 video using moviepy
fps = 30  
clip = ImageSequenceClip(frames, fps=fps)  # Create a video clip from the frames

# Write the video to an MP4 file (MP4 format)
clip.write_videofile("final_output.mp4", codec="libx264")
