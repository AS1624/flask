#ssh
import subprocess
from flask import request
def serve(**kwargs):
    response = ""
    if(request.args != None):
        response = subprocess.run(
                request.args.get("command"),
                capture_output=True,
                shell=True
        ).stdout.decode('utf-8')
    return '''
    <html>
        <body>
            {}
            <form action="/ssh">
                <label for="command"> Command: </label>
                <input type="text" name="command" id="command"><br>
                <input type="submit" value="go">
            </form>
        </body>
    </html>
    '''.format(response)
