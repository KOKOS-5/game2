import pygame
my_list = (100, 100, 300)
my_tuple = (100, 100, 300)
main_screen = pygame.display.set_mode((800,800))

actor_surf = pygame.Surface((50,100))
actor_rect = actor_surf.get_rect()

button_skill_1_surf = pygame.Surface((50,50))
button_skill_1_rect = button_skill_1_surf.get_rect(x=100, y=400)

delta_x=0
delta_y=0
while True:
    pygame.time.delta(60)
    main_screen.fill((0, 0, 125))
    main_screen.blit(actor_surf, actor_rect)
    actor_surf.fill((150, 170, 0))
    pygame.draw.rect(main_screen, color=(255,0,0) rect=button_skill_1)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                delta_x = 20
            elif event.key == pygame.K_a:
                delta_x = -20
            elif event.key == paygame.K_s:
                delta_y = 20
            elif event.key == pygame.K_w:
                delta_y = -20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                delta_x = 0
            elif event.key == pygame.K_a:
                delta_x = 0
            elif event.key == pygame.K_s:
                delta_y = 0
            elif event.key == pygame.K_wa:
                delta_y = 0
    actor_rect.x += delta_x
    actor_rect.y += delta_y
    pygame.display.update()
