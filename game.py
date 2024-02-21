import pygame
import sys
import random
import os

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game 2D đơn giản')

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Hình chữ nhật
rect_width = 100
rect_height = 5
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect_speed = 20

# Hình chữ nhật quà
gift_image = pygame.image.load('C:/Users/ADMIN/Desktop/pygame/gift11.png')  # Đường dẫn của hình ảnh quà
gift_image = pygame.transform.scale(gift_image, (50, 50))  # Thay đổi kích thước hình ảnh
gift_rect = gift_image.get_rect()
gift_speed = 2

class Gift:
    def __init__(self):
        self.x = random.randint(0, screen_width - gift_rect.width)
        self.y = -gift_rect.height  # Thay đổi vị trí y ban đầu
        self.hung = False  # Biến để kiểm tra xem hộp quà đã được hứng hay chưa
        self.active = True  # Biến để kiểm tra xem hộp quà có còn hoạt động hay không

    def move(self):
        self.y += gift_speed
        if self.y > screen_height:
            self.y = -gift_rect.height  # Thiết lập lại vị trí y nếu quà rơi hết màn hình
            self.hung = False  # Reset biến hứng quà
            self.x = random.randint(0, screen_width - gift_rect.width)  # Chọn một vị trí x ngẫu nhiên

    def check_collision(self, rect_x, rect_y, rect_width, rect_height):
        if self.x < rect_x + rect_width and self.x + gift_rect.width > rect_x and self.y < rect_y + rect_height and self.y + gift_rect.height > rect_y and not self.hung:
            self.hung = True
            self.active = False  # Đặt hộp quà này là không hoạt động


    def draw(self):
     if self.active:
        screen.blit(gift_image, (self.x, self.y))


# Tạo một danh sách chứa tất cả các hộp quà
gifts = []

# Tạo một hộp quà mới và thêm vào danh sách
gift = Gift()
gifts.append(gift)

# Vòng lặp chính
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển và vẽ hộp quà
    for gift in gifts:
        gift.move()

        # Kiểm tra va chạm giữa hộp quà và hình chữ nhật
        gift.check_collision(rect_x, rect_y, rect_width, rect_height)

        # Xử lý phím di chuyển
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_x -= rect_speed
        if keys[pygame.K_RIGHT]:
            rect_x += rect_speed
        if keys[pygame.K_UP]:
            rect_y -= rect_speed
        if keys[pygame.K_DOWN]:
            rect_y += rect_speed

        # Giới hạn di chuyển của hình chữ nhật
        if rect_x < 0:
            rect_x = 0
        elif rect_x > screen_width - rect_width:
            rect_x = screen_width - rect_width
        if rect_y < 0:
            rect_y = 0
        elif rect_y > screen_height - rect_height:
            rect_y = screen_height - rect_height

        # Di chuyển và vẽ hình chữ nhật
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

        # Vẽ hình ảnh quà
        if gift.hung and not gift.active:
            gifts.remove(gift)  # Xóa hộp quà trước đó
            gift = Gift()  # Tạo một hộp quà mới
            gifts.append(gift)  # Thêm hộp quà mới vào danh sách
            gift.active = True  # Đặt hộp quà mới là hoạt động

        if gift.active:
            gift.draw()

        pygame.display.flip()

        # Điều chỉnh tốc độ vòng lặp
        clock.tick(60)

# Kết thúc Pygame
pygame.quit()
sys.exit()
