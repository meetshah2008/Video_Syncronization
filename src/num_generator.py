import pygame
import cv2
import numpy as np
import time

# Main function
def main(fps=30, output_file="number_sequence.mp4"):
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
    pygame.font.init()
    clock = pygame.time.Clock()
    running = True

    # Set up font for displaying numbers
    font_size = screen.get_height() // 2  # Large font size for clear visibility
    font = pygame.font.Font(None, font_size)
    unique_number = 0  # Start with an initial unique number

    # Set up video writer
    frame_width, frame_height = screen.get_size()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Generate a new unique number for each frame
        unique_number += 1

        # Render the number
        number_surface = font.render(str(unique_number), True, (255, 255, 255))
        number_rect = number_surface.get_rect(center=screen.get_rect().center)

        # Clear screen and display number
        screen.fill((0, 0, 0))  # Black background
        screen.blit(number_surface, number_rect)
        pygame.display.flip()

        # Convert the pygame surface to a numpy array for OpenCV
        frame = pygame.surfarray.array3d(screen)
        frame = np.transpose(frame, (1, 0, 2))  # Convert to (height, width, channels)
        out.write(frame)

        # Print the number for debugging/reference (optional)
        print(f"Frame number: {unique_number}")

        # Control frame rate (30 FPS)
        clock.tick(fps)

    # Release resources
    out.release()
    pygame.quit()

if __name__ == "__main__":
    main(fps=30, output_file="number_sequence.mp4")  # Adjust FPS and output file name
