from app.services.image_generator import generate_image
from app.schemas import Panel

p = Panel(
    panel_number=1,
    title='Test',
    scene_description='A hero looks at a mountain',
    image_prompt='A comic panel of a hero looking at a mountain, detailed illustration',
)

result = generate_image(p)
print(result)
import os
print(os.path.exists('static/panels/panel_1.png'))
