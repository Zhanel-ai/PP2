import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Brush(1), Rect(2), Circle(3), Square(4), Right Triangle(5), Equilateral(6), Rhombus(7), Eraser(0)")
    clock = pygame.time.Clock()

    radius = 10                      # Brush and outline thickness
    mode = 'blue'                   # Color mode
    tool = 'brush'                  # Selected tool (brush/rect/circle/etc.)
    drawing = False                # Whether mouse is pressed (drawing in progress)
    start_pos = None               # Starting position for shape drawing
    points = []                    # Points for smooth brush strokes

    # Surface where drawings are saved permanently
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))         # Fill canvas with black

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

            # -------------------- KEYBOARD SHORTCUTS --------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                elif event.key == pygame.K_r:
                    mode = 'red'    # Set color red
                elif event.key == pygame.K_g:
                    mode = 'green'  # Set color green
                elif event.key == pygame.K_b:
                    mode = 'blue'   # Set color blue
                elif event.key == pygame.K_c:
                    canvas.fill((0, 0, 0))   # Clear canvas (black background)

                # Tool selection shortcuts
                elif event.key == pygame.K_0:
                    tool = 'eraser'           # Eraser tool
                elif event.key == pygame.K_1:
                    tool = 'brush'            # Brush tool
                elif event.key == pygame.K_2:
                    tool = 'rect'             # Rectangle
                elif event.key == pygame.K_3:
                    tool = 'circle'           # Circle
                elif event.key == pygame.K_4:
                    tool = 'square'           # Square
                elif event.key == pygame.K_5:
                    tool = 'right_triangle'   # Right triangle
                elif event.key == pygame.K_6:
                    tool = 'equilateral'      # Equilateral triangle
                elif event.key == pygame.K_7:
                    tool = 'rhombus'          # Rhombus

            # -------------------- MOUSE PRESSED --------------------
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True                 # Start drawing
                start_pos = event.pos          # Store starting position
                if tool == 'brush':
                    points.append(event.pos)   # Add first point for brush

            # -------------------- MOUSE RELEASED --------------------
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
                end_pos = event.pos

                x1, y1 = start_pos
                x2, y2 = end_pos

                # Draw selected shapes permanently on canvas
                if tool == 'rect':
                    rect = rect_from_points(start_pos, end_pos)
                    pygame.draw.rect(canvas, getColor(mode), rect, radius // 2)

                elif tool == 'circle':
                    cx, cy = start_pos
                    rad = int(math.hypot(x2 - cx, y2 - cy))   # Distance = radius
                    pygame.draw.circle(canvas, getColor(mode), start_pos, rad, radius // 2)

                elif tool == 'square':
                    side = max(abs(x2 - x1), abs(y2 - y1))     # Square side = max dimension
                    rect = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(canvas, getColor(mode), rect, radius // 2)

                elif tool == 'right_triangle':
                    pts = [(x1, y1), (x1, y2), (x2, y2)]       # Right triangle points
                    pygame.draw.polygon(canvas, getColor(mode), pts, radius // 2)

                elif tool == 'equilateral':
                    side = abs(x2 - x1)
                    h = (3**0.5 / 2) * side                    # Height of equilateral triangle
                    pts = [(x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - h)]
                    pygame.draw.polygon(canvas, getColor(mode), pts, radius // 2)

                elif tool == 'rhombus':
                    cx = (x1 + x2) / 2
                    cy = (y1 + y2) / 2                         # Center point
                    pts = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                    pygame.draw.polygon(canvas, getColor(mode), pts, radius // 2)

                start_pos = None          # Reset start
                points.clear()            # Clear brush points

            # -------------------- MOUSE DRAGGING --------------------
            elif event.type == pygame.MOUSEMOTION and drawing:
                pos = event.pos

                # Smooth brush drawing
                if tool == 'brush':
                    points.append(pos)
                    if len(points) > 1:
                        drawLineBetween(canvas, len(points), points[-2], points[-1], radius, mode)

                # Eraser drawing
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (0, 0, 0), pos, radius)  # Draw black circle as eraser

        # -------------------- DRAW CANVAS --------------------
        screen.blit(canvas, (0, 0))

        # ---------------- PREVIEW SHAPES (NOT FINAL) ----------------
        if drawing and start_pos and tool in ('rect', 'circle', 'square', 'right_triangle', 'equilateral', 'rhombus'):
            mouse_pos = pygame.mouse.get_pos()
            x1, y1 = start_pos
            x2, y2 = mouse_pos

            # Temporary preview shapes drawn on screen
            if tool == 'rect':
                rect = rect_from_points(start_pos, mouse_pos)
                pygame.draw.rect(screen, getColor(mode), rect, radius // 2)

            elif tool == 'circle':
                cx, cy = start_pos
                rad = int(math.hypot(x2 - cx, y2 - cy))
                pygame.draw.circle(screen, getColor(mode), start_pos, rad, radius // 2)

            elif tool == 'square':
                side = max(abs(x2 - x1), abs(y2 - y1))
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, getColor(mode), rect, radius // 2)

            elif tool == 'right_triangle':
                pts = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, getColor(mode), pts, radius // 2)

            elif tool == 'equilateral':
                side = abs(x2 - x1)
                h = (3**0.5 / 2) * side
                pts = [(x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - h)]
                pygame.draw.polygon(screen, getColor(mode), pts, radius // 2)

            elif tool == 'rhombus':
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                pts = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                pygame.draw.polygon(screen, getColor(mode), pts, radius // 2)

        pygame.display.flip()
        clock.tick(60)


# -------------------- COLOR SELECTION --------------------
def getColor(mode):
    if mode == 'blue': return (0, 0, 255)
    elif mode == 'red': return (255, 0, 0)
    elif mode == 'green': return (0, 255, 0)
    return (255, 255, 255)


# -------------------- RECTANGLE FROM 2 POINTS --------------------
def rect_from_points(a, b):
    x1, y1 = a
    x2, y2 = b
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))


# -------------------- SMOOTH BRUSH GRADIENT LINE --------------------
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