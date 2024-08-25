# canvas_editor/views.py

from django.shortcuts import render
import google.generativeai as genai  # Import the Google Gemini SDK

# Securely store and configure your Google API key
GOOGLE_API_KEY = 'AIzaSyDtiq-CBPFG500PMG_UJtO08wf4EQnz9H4'
genai.configure(api_key=GOOGLE_API_KEY)

global x,y
x = ''
y = []

def canvas_editor_view(request):
    global x,y
    print(x)
    generated_code = ''
    if request.method == 'POST':
        command = request.POST.get('command')
        y.append(command)

        model = genai.GenerativeModel('gemini-pro')  # Specify the correct model for Gemini
        instructions = f'''
                        - Your task is to generate fabric.js code according to the prompt, previous prompts and from your previous response.
                        - According to your previous response you should adjust the code or append more components into the canvas.
                        - You will be provided with a code for reference, the user prompt and the previous code given by you.
                        - The code you are providing should be of the following form.
                        - Use fromUrl syntax in fabric.js to insert image from external url.
                        ---        var canvas = new fabric.Canvas('designCanvas');
                                    canvas.add(new fabric.Circle( {{ radius: 30, fill: '#f55', top: 100, left: 100 }}));
                                    canvas.item(0).hasControls = false;
                                    canvas.setActiveObject(canvas.item(0));
                                    this.__canvases.push(canvas);
                        - The code should always in the above form.
                        - You should always update the code and give full code right from the initialization. This is very Important.
                        - Never start and end the code with ```Javascript stuff.. it is not at all needed. 
                        - prompt = {command}
                        - previous code = {x}
                        - previous prompts = {y}
                        - Provide only the code not anything else or explanation.
                        - Dont need any language name to be embedded with the code. just give me the code and it is enough.
                        '''
        response = model.generate_content(f"Generate Fabric.js code for the following command: {instructions}")

        generated_code = response.text.strip()  # Adjust the extraction of content based on API response
        x = generated_code

    return render(request, 'canvas_editor.html', {'generated_code': generated_code})
