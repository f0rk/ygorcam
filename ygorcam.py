#!/usr/bin/env python

import tempfile
import subprocess

import web

urls = ("/camera", "Camera")
app = web.application(urls, globals())


class Camera(object):
    def GET(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tfp:
            process = subprocess.Popen(["raspistill", "-o", tfp.name])
            stdout, stderr = process.communicate()

            if process.returncode:
                raise Exception((process.returncode, stdout, stderr))

            web.header("Content-Type", "image/jpeg")
            return tfp.read()


if __name__ == "__main__":
    app.run()

