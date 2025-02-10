import pygame
import serial

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arduino Nano Serial Input")

# Set up the serial connection
ser = serial.Serial('/dev/ttyACM0', 115200)  # Replace 'COM3' with the appropriate port and baud rate

# Set up the pixel position
pixel_x = screen_width // 2
pixel_y = screen_height // 2



# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read serial input
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        try:
            sensor_x = float(data[data.index("X:") + 2:data.index(" Y:")])
            sensor_y = float(data[data.index("Y:") + 2:])
            print(sensor_x, sensor_y)
            # Update pixel position based on sensor values
            pixel_x += int(sensor_x)
            pixel_y += int(sensor_y)

            # Prevent pixel from going out of screen bounds
            pixel_x = max(0, min(pixel_x, screen_width))
            pixel_y = max(0, min(pixel_y, screen_height))
        except ValueError:
            pass

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the pixel
    pygame.draw.rect(screen, (255, 255, 255), (pixel_x, pixel_y, 10, 10))

    # Update the screen
    pygame.display.flip()

# Clean up
ser.close()
pygame.quit()
