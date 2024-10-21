from PIL import Image, ImageDraw
import math


# Parameters
width = 200  # Width of the flag
height = 200  # Height of the flag
num_frames = 30  # Number of frames for animation
flag_color = (255, 180, 25)  # Red flag color

# Create a blank image for the flag
flag = Image.new('RGB', (width, height), color=(255, 255, 255))

# Create a sequence of frames for animation
frames = []

for i in range(num_frames):
    # Create a new frame with a waving effect
    frame = flag.copy()
    draw = ImageDraw.Draw(frame)

    # Calculate waving effect (sinusoidal movement)
    wave_amplitude = 10  # Amplitude of the wave
    phase_shift = (math.pi * 2) * (i / num_frames)  # Phase shift for animation

    # Draw the flag with a wave effect
    for x in range(width):
        y_offset = math.sin((x / width) * (math.pi * 2) + phase_shift) * wave_amplitude
        draw.line([(x, 0), (x, height)], fill=flag_color, width=2)
        draw.line([(x, 0), (x, y_offset)], fill=(255, 255, 255))  # Add a white area above the wave

    frames.append(frame)

# Save the frames as an animated GIF
frames[0].save('flag_animation.gif', save_all=True, append_images=frames[1:], optimize=False, duration=50, loop=0)

#part2

# Parameters
width = 200  # Width of the flag
height = 200  # Height of the flag
num_frames = 30  # Number of frames for animation
flag_color = (255, 180, 25)  # Red flag color

# Create a blank image for the flag
flag = Image.new('RGB', (width, height), color=(255, 255, 255))

# Create a sequence of frames for animation
frames = []

for i in range(num_frames):
    # Create a new frame with a waving effect
    frame = flag.copy()
    draw = ImageDraw.Draw(frame)

    # Calculate waving effect (sinusoidal movement)
    wave_amplitude = 10  # Amplitude of the wave
    phase_shift = (math.pi * 2) * (i / num_frames)  # Phase shift for animation

    # Draw the flag with a wave effect
    for x in range(width):
        y_offset = math.sin((x / width) * (math.pi * 2) + phase_shift) * wave_amplitude

        # Add a gradient effect based on the y_offset
        gradient_color = (255, int(255 - abs(y_offset) * 10), 25)  # Adjust the gradient color

        # Draw lines with gradient color
        draw.line([(x, 0), (x, height)], fill=gradient_color, width=2)
        draw.line([(x, 0), (x, y_offset)], fill=(255, 255, 255))  # Add a white area above the wave

    frames.append(frame)

# Save the frames as an animated GIF
frames[0].save('flag_animation_unique.gif', save_all=True, append_images=frames[1:], optimize=False, duration=50,
               loop=0)


#part 3
from PIL import Image, ImageDraw
import math

# Parameters
width = 200  # Width of the flag
height = 200  # Height of the flag
num_frames = 30  # Number of frames for animation
flag_color = (255, 180, 25)  # Red flag color

# Create a blank image for the flag
flag = Image.new('RGB', (width, height), color=(255, 255, 255))

# Create a sequence of frames for animation
frames = []

for i in range(num_frames):
    # Create a new frame with a waving effect
    frame = flag.copy()
    draw = ImageDraw.Draw(frame)

    # Calculate waving effect (custom irregular wave)
    wave_amplitude = 15  # Amplitude of the wave
    wave_period = width / 4  # Period of the wave
    phase_shift = (math.pi * 2) * (i / num_frames)  # Phase shift for animation

    # Draw the flag with a wave effect
    for x in range(width):
        # Calculate y_offset using a combination of sine and cosine functions
        y_offset = math.sin((x / wave_period) * (math.pi * 2) + phase_shift) * wave_amplitude * math.cos(
            (x / wave_period) * (math.pi * 2) + phase_shift)

        # Add a gradient effect based on the y_offset
        gradient_color = (255, int(255 - abs(y_offset) * 10), 25)  # Adjust the gradient color

        # Draw lines with gradient color
        draw.line([(x, 0), (x, height)], fill=gradient_color, width=2)
        draw.line([(x, 0), (x, y_offset)], fill=(255, 255, 255))  # Add a white area above the wave

    frames.append(frame)

# Save the frames as an animated GIF with a custom name
frames[0].save('unique_flag_animation2.gif', save_all=True, append_images=frames[1:], optimize=False, duration=50,
               loop=0)
