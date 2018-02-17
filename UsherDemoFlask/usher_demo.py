from flask import Flask,render_template,request
import requests
import json
import random
import base64
from tracking.Tracker import *

import TCPServer

app = Flask(__name__)



#domain = "env-66916.customer.cloud.microstrategy.com:2443"
domain = "env-72355.customer.cloud.microstrategy.com:2443"
clientId = "13"
orgId = "Paul"
session = requests.session()

mesh_server = TCPServer.TCPServer('localhost', 8000)


@app.route('/updateMesh')
def updateMesh():
    # status = STATUSES[random.randint(0,2)]

    resp = {
        'sector': mesh_server.tracker.sector,
        'status': STATUSES[mesh_server.tracker.status]
    }#, 'rssis': rssis}
    return json.dumps(resp)

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')

@app.route('/')
def welcome():
    return 'Welcome to Usher!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/qr')
def display_qr():
    return render_template('qr.html')


# API to shutdown the server
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# Generate QR code
@app.route('/genQRcode', methods=['POST'])
def genQRcode():
    ssoCreateAPI = "https://" + domain + "/sso/create_registration_session"
    payload = {'client_id': clientId,
               'return_image': 'true',
               'session_data': '{"descirption":"RESTSample"}'
    }
    response = session.post(ssoCreateAPI, payload)
    # print response.content
    return json.dumps(response.json())


# Check if QR code has been scanned
# Return token if successfully scan the QR code
@app.route('/ssowait')
def ssoWait():
    ssoWaitAPI = "https://" + domain + "/sso/wait" + "?session_type=nonblock" + "&client_id=" + clientId
    response = session.get(ssoWaitAPI)
    respDict = response.json()
    if 'access_token' in respDict:
        accessToken = respDict['access_token']
        session.cookies.set("token", accessToken)
        return getBadgeInfo()
    else:
        return json.dumps(respDict)


# Get info of the badge that scans the QR code
def getBadgeInfo():
    accessToken = session.cookies.get("token")
    badgeOrgUrl = "https://" + domain + "/badge/org/" + orgId + "?uid_only=false&access_token=" + accessToken
    badgeRes = session.get(badgeOrgUrl)
    session.cookies.set("token", accessToken)
    badgeId = badgeRes.json()[0]['id']
    session.cookies.set("badgeId", str(badgeId))
    return json.dumps(badgeRes.json()[0])


# Retrieve badge image
@app.route('/badgeImage')
def getBadgeImage():
    accessToken = session.cookies.get("token")
    badgeId = session.cookies.get("badgeId")
    badgeImageUrl = "https://" + domain + "/user/get_public_image/badge/" + badgeId + "?access_token=" + accessToken
    badgeImageResponse = session.get(badgeImageUrl)
    session.cookies.clear()
    return base64.encodestring(badgeImageResponse.content)




