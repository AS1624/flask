#scoutPortal

import json
from flask import request
def serve(**kwargs):
    nameTemplate = '<label><input type="radio" name="scout" value="{}" required> {}</label>'
    matchTemplate = '<label><input type="radio" name="match" value="{}"> {}</label>'

    if "name" in request.cookies:
        name = request.cookies.get("name")

else:
    name = ""
    request.get()

    with open("scouts.json", "r") as file:
        data = json.loads(file.read())
        scoutNames = data.get("scouts")
        scouts = ""
        for name in scoutNames:
            scouts += nameTemplate.format(name, name) + "\n"

        matchNames = range(1, 1 + len(data.get("matches")))
        matches = ""
        for name in matchNames:
            matches += matchTemplate.format(name, name) + "\n"
        print(scouts)

    return '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scouting Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            form {
                max-width: 400px;
                margin: 0 auto;
            }
            label {
                font-weight: bold;
                margin-top: 10px;
                display: block;
            }
            .radio-group {
                margin-bottom: 20px;
            }
            input[type="radio"] {
                margin-right: 10px;
            }
            textarea {
                display: block;
                width: 100%;
                margin-bottom: 10px;
                padding: 8px;
                font-size: 16px;
            }
            button {
                padding: 10px 15px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>

        <h2>Scout Portal</h2>

        <form action="/scoutingRedirect" method="post">

            <label>Select Your Name:</label>
            <div class="radio-group">
            ''' + scouts + '''
            </div>

            <label>Select Match Number:</label>
            <div class="radio-group">
            ''' + matches + '''
            </div>

            <button type="submit">Go!</button>
        </form>

    </body>
</html>
'''
