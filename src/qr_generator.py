import qrcode
import pygame
import time

# Function to generate a QR code with timestamp data
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

# Main function
def main(fps=30):
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Generate QR code data with timestamp
        qr_data = f"Timestamp: {time.time()}"
        qr_image = generate_qr_code(qr_data)

        # Scale QR code to fit the screen
        qr_scaled = pygame.transform.scale(qr_image, screen.get_size())

        # Display QR code
        screen.blit(qr_scaled, (0, 0))
        pygame.display.flip()

        # Print QR data for reference (optional, for debugging)
        print(qr_data)

        # Control frame rate
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main(fps=30)  # Adjust FPS here (e.g., 30 FPS for your use case)
