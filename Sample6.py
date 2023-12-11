from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader

app = Flask(_name_)

@app.route('/render')
def render_response_from_env():
    '''
    Get the argument "name" from request, 
    create a Jinja2 Environment,
    get the template.html from the environment, and render it.
    '''
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided

    # Create a Jinja2 Environment
    env = Environment(loader=FileSystemLoader('path/to/template/directory'))
    
    # Get the template
    template = env.get_template('template.html')
    
    # Render the template with the provided name
    rendered_template = template.render(name=name)
    
    return rendered_template

if _name_ == '_main_':
    app.run(debug=True)