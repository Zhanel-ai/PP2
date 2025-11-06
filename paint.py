import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing Tools: Brush (1), Rect (2), Circle (3), Eraser (4)")
    clock = pygame.time.Clock()

    radius = 10
    mode = 'blue'        
    tool = 'brush'        
    drawing = False       
    start_pos = None      
    points = []          

    # drawings permanently
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

            # controlling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_c:
                    # Clear the screen
                    canvas.fill((0, 0, 0))

            #
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                start_pos = event.pos
                if tool == 'brush':
                    points.append(event.pos)

            
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
                end_pos = event.pos

                # Drawing shape
                if tool == 'rect':
                    rect = rect_from_points(start_pos, end_pos)
                    pygame.draw.rect(canvas, getColor(mode), rect, radius // 2)
                elif tool == 'circle':
                    cx, cy = start_pos
                    ex, ey = end_pos
                    rad = int(((cx - ex)**2 + (cy - ey)**2)**0.5)
                    pygame.draw.circle(canvas, getColor(mode), start_pos, rad, radius // 2)

                start_pos = None
                points.clear()

            # movement
            elif event.type == pygame.MOUSEMOTION and drawing:
                pos = event.pos
                if tool == 'brush':
                    # smooth line
                    points.append(pos)
                    if len(points) > 1:
                        drawLineBetween(canvas, len(points), points[-2], points[-1], radius, mode)
                    #points = points[-256:]  
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (0, 0, 0), pos, radius)

        # display
        screen.blit(canvas, (0, 0))

        
        if drawing and start_pos and tool in ('rect', 'circle'):
            mouse_pos = pygame.mouse.get_pos()
            if tool == 'rect':
                rect = rect_from_points(start_pos, mouse_pos)
                pygame.draw.rect(screen, getColor(mode), rect, radius // 2)
            elif tool == 'circle':
                cx, cy = start_pos
                ex, ey = mouse_pos
                rad = int(((cx - ex)**2 + (cy - ey)**2)**0.5)
                pygame.draw.circle(screen, getColor(mode), start_pos, rad, radius // 2)

        pygame.display.flip()
        clock.tick(60)

# color
def getColor(mode):
    
    if mode == 'blue': return (0, 0, 255)
    elif mode == 'red': return (255, 0, 0)
    elif mode == 'green': return (0, 255, 0)
    return (255, 255, 255)

# rect
def rect_from_points(a, b):
   
    x1, y1 = a
    x2, y2 = b
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

# gradient
def drawLineBetween(surface, index, start, end, width, color_mode):
   
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue': color = (c1, c1, c2)
    elif color_mode == 'red': color = (c2, c1, c1)
    elif color_mode == 'green': color = (c1, c2, c1)
    else: color = (255, 255, 255)

    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy), 1)
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(surface, color, (x, y), width)


main()
