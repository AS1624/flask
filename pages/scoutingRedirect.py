#scoutingRedirect, post

from flask import request, make_response
import json
def serve(**kwargs):
    with open("/home/Avery/Documents/flask/scouts.json", "r") as file:
        data = json.loads(file.read())

    scout = request.form.get("scout")
    match = request.form.get("match")
    matchRobots = data.get("matches")[int(match) - 1]
    robot = 0
    for i, robotData in enumerate(matchRobots):
        if robotData.get("scout") is scout:
            robot = i

    if robot == 0:
        response = make_response('''
        <!DOCTYPE html>
        <html>
            <body>
                wrong match or name, you do not scout this match. <a href='/scoutPortal'>back</a>
        </html>
        ''')
        response.set_cookie("name", scout)
    else:
        response = make_response('''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta http-equiv='refresh' content='0; URL=/{}'>
                </head>
            </html>
        '''.format(f"scouting?match={match}&robot={robot}")
        )
        response.set_cookie("name", "")

    return response
