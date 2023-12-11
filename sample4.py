import os
from flask import Flask, request

app = Flask(_name_)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file.
    '''
    filename = request.form.get('filename')
    # Add validation for the filename as needed
    if filename:
        filepath = os.path.join('path/to/image/directory', filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return f"File {filename} deleted successfully", 200
        else:
            return f"File {filename} not found", 404
    else:
        return "Filename not provided in request", 400

if _name_ == '_main_':
    app.run(debug=True)