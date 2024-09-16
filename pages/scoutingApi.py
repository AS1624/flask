#api/scouting, post
from flask import request

def serve(**kwargs):
    match = int(request.form.get("match"))
    robot = int(request.form.get("robot"))
    samples = int(request.form.get("samples"))
    specimens = int(request.form.get("specimens"))


    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv='refresh' content='0; URL=/scoutPortal'>
            </head>
        </html>
        '''

