from flask import Flask
import os

# Create a Flask instance
app = Flask(__name__)

def compileText(file: str):
    global_vars = {}
    def fun(**kwargs):
        with open("/home/Avery/Documents/flask/pages/" + file, "r") as openFile:
            text = openFile.read().split("\n")[1:]

        if file.endswith("py"):    
            exec("\n".join(text), global_vars)
            return global_vars['serve'](**kwargs)

        elif file.endswith("html"):
            return "\n".join(text)
        
        else:
            return "unsupported filetype: {file.split('.')[-1]}\n this is a server error, nothing you do will fix it."
    return fun



for page in os.listdir("/home/Avery/Documents/flask/pages"):
    with open("/home/Avery/Documents/flask/pages/" + page, "r") as file:
        text = file.read()
        headers = (
                text
                .replace("#", "")
                .split('\n')[0]
                .split(", ")
        )

        path = "/" + headers[0]
        print(path)

        methods = ["GET"]
        if len(headers) > 1:
            methods = headers[1:]
        
        app.add_url_rule(
            path,
            page,
            view_func=compileText(page),
            methods=methods
        )

# Run the app when the script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

