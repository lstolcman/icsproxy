from flask import Flask, send_file, request
from requests import get
import re
import os
import tempfile

ics = os.environ['ICS_URL']

app = Flask(__name__)

from flask import Response
@app.route('/')
def ajax_ddl():
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        with open(tmp.name, 'wb') as f:
            c = get(ics).content
            f.write(c)
            f.flush()

        cu = None
        with open(tmp.name, 'r', encoding='utf-8') as f:
            cu = f.readlines()
        with open(tmp.name, 'w', encoding='utf-8') as f:
            f.flush()
            for i, l in enumerate(cu):
                if l.startswith('ORGANIZER'):
                    cu[i]=re.sub('"', '\\"', l)

            f.writelines(cu)
            f.flush()

        response = Response(cu, mimetype='text/calendar')
        response.headers['Content-Disposition'] = 'attachment; filename=calendar.ics'
        return response
    finally:
        os.remove(tmp.name)


