from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as genai

GOOGLE_API_KEY = ''
genai.configure(api_key=GOOGLE_API_KEY)

global x, y
x = ''
y = []

def canvas_editor_view(request):
    global x, y
    generated_code = ''

    if request.method == 'POST':
        command = request.POST.get('command')
        y.append(command)
        images = {
            'cat' : 'https://w7.pngwing.com/pngs/174/600/png-transparent-cat-animal-lovely-cat.png',
            'car' : 'https://png.pngtree.com/png-clipart/20220625/ourmid/pngtree-car-sports-car-transportation-png-image_5320963.png',
            'truck' : 'https://w7.pngwing.com/pngs/229/783/png-transparent-yellow-dump-truck-art-transportation-pickup-truck-dump-truck-truck-freight-transport-truck-mode-of-transport-thumbnail.png'
        }

        model = genai.GenerativeModel('gemini-pro')
        instructions = f'''
                        - Your task is to generate fabric.js code according to the prompt, previous prompts and from your previous response.
                        - According to your previous response you should adjust the code or append more components into the canvas.
                        - You will be provided with a code for reference, the user prompt and the previous code given by you.
                        - Dont start your result capsulated with ```javascript. It is important.
                        - The code you are providing should update the below canvas.
                        
                        ---        var canvas = new fabric.Canvas('designCanvas');
                                    canvas.add(new fabric.Circle( {{ radius: 30, fill: '#f55', top: 100, left: 100 }}));
                                    canvas.item(0).hasControls = false;
                                    canvas.setActiveObject(canvas.item(0));
                                    this.__canvases.push(canvas);
                        - Only provide the adding code not the full code.
                        - Never start and end the code with unnecessary text.
                        - you can use only these images---> images = {images}.
                        - give the image url explicitly and do not give images['cat'] etc..give the complete url value.
                        - Use fromUrl syntax in fabric.js to insert image from external url.
                        - prompt = {command}
                        - previous code = {x}
                        - previous prompts = {y}
                        - Provide only the code, nothing else.
                        '''
        response = model.generate_content(f"Generate Fabric.js code for the following command: {instructions}")

        generated_code = response.text.strip()
        x = generated_code
        print(x)

        return JsonResponse({'generated_code': generated_code})

    return render(request, 'canvas_editor.html', {'generated_code': generated_code})
