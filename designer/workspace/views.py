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
        y=[]
        images = {
            'cat' : 'https://static.vecteezy.com/system/resources/thumbnails/027/192/627/small/a-white-cat-with-big-eyes-on-a-transparent-background-ai-generated-png.png',
            'car' : 'https://static.vecteezy.com/system/resources/previews/024/543/581/non_2x/car-transparent-background-free-png.png',
            'truck' : 'https://w7.pngwing.com/pngs/229/783/png-transparent-yellow-dump-truck-art-transportation-pickup-truck-dump-truck-truck-freight-transport-truck-mode-of-transport-thumbnail.png',
            'ufo' : 'https://static.vecteezy.com/system/resources/previews/011/731/539/non_2x/hand-drawn-ufo-illustration-png.png',
            'sound' : 'https://static.vecteezy.com/system/resources/previews/039/349/642/non_2x/starburst-bomb-blast-big-explosion-abstract-comic-book-explosion-flash-flash-beam-explosion-flash-glow-anime-illustration-on-transparent-background-vector.jpg',
            'blast' : 'https://static.vecteezy.com/system/resources/previews/041/933/691/non_2x/ai-generated-nuclear-bomb-explosion-isolated-on-transparent-background-free-png.png',
            'phone_icon' : 'https://static.vecteezy.com/system/resources/previews/010/829/986/large_2x/phone-icon-in-trendy-flat-style-free-png.png',
            'insta_icon' : 'https://static.vecteezy.com/system/resources/previews/018/930/692/original/instagram-logo-instagram-icon-transparent-free-png.png',
            'leetcode_icon' : 'https://cdn.iconscout.com/icon/free/png-512/leetcode-3521542-2944960.png',
            'coding': 'https://vectorified.com/images/code-icon-5.png',
            'ai_image' : 'https://cdn0.iconfinder.com/data/icons/robotics-4/48/5-Artificial_intelligence-1024.png',
            'school' : 'https://static.vecteezy.com/system/resources/previews/000/396/264/original/kids-learning-and-playing-illustration-vector.jpg',
            'google logo' : 'https://static.vecteezy.com/system/resources/thumbnails/022/484/503/small_2x/google-lens-icon-logo-symbol-free-png.png',
        }

        model = genai.GenerativeModel('gemini-pro')
        instructions = f'''

                        - Your task is to act ans a fabric.js developer generate fabric.js code according to the prompt, previous prompts and from your previous response.
                        - According to your previous response you should adjust the code or append more components into the canvas.
                        - You will be provided with a code for reference, the user prompt and the previous code given by you.
                        - Dont start your result capsulated with ```javascript. It is important.
                        - You should be able to draw lines, curves also...
                        - The code you are providing should update the below canvas.
                        - If the user asked for any text box, always give an editable textbox.
                        - Text box code format : 

                                canvas.add(new fabric.Textbox('Enter text here', {{
                                top: 100,
                                left: 100,
                                width: 200,
                                fontSize: 16
                                }}));

                            canvas.setActiveObject(canvas.item(1));
                            canvas.item(1).hasControls = true;
                        - always use fontFamily: 'cursive' in textboxes.
                        - See all i have is a 300x300 canvas and i want the content only inside it.
                        - create the component and always add it to the canvas using canvas.add() use the below format for adding shapes.
                                
                                    canvas.add(new fabric.Circle( {{ radius: 30, fill: '#f55', top: 100, left: 100 }}));
                                    canvas.item(0).hasControls = true;
                                    canvas.setActiveObject(canvas.item(0));
                                    this.__canvases.push(canvas);
                        - Please dont forget to use the above command for adding shapes. if the user asks for shapes, you have to use the above format only...
                        
                        - Never start and end the code with unnecessary text.
                        - you can use only these images---> images = {images}.
                        - format for image insertion is as follows : 

                        ---fabric.Image.fromURL('https://w7.pngwing.com/pngs/229/783/png-transparent-yellow-dump-truck-art-transportation-pickup-truck-dump-truck-truck-freight-transport-truck-mode-of-transport-thumbnail.png', function(img) {{
                                    img.set({{
                                        left: 120,
                                        top: 200,
                                        angle: 0,
                                        scaleX: 0.3,
                                        scaleY: 0.3,
                                        crossOrigin: 'anonymous'
                                    }});
                                    
                                    // Add the image to the canvas
                                    canvas.add(img);
                                    
                                    // Disable controls for this specific image
                                    img.hasControls = true;

                                    // Set the newly added image as the active object
                                    canvas.setActiveObject(img);

                                    // Render the canvas again to reflect changes
                                    canvas.renderAll();
                                }});
                        - give the image url explicitly and do not give images['cat'] etc..give the complete url value.
                        - Use fromUrl syntax in fabric.js to insert image from external url.
                        - prompt = {command}
                        - previous code = {x}
                        - previous prompts = {y}
                        - Provide only the code, nothing else.
                        - Againt never start the code with the ```javascript. it will ruin the process.
                        '''
        response = model.generate_content(instructions)

        generated_code = response.text.strip()
        x = ''
        print(generated_code)

        return JsonResponse({'generated_code': generated_code})

    return render(request, 'canvas_editor.html', {'generated_code': generated_code})
