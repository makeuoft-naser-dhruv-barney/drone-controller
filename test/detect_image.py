import http.client, urllib.request, urllib.parse, urllib.error, base64


def get_byte_array(img_path):
    with open(img_path, "rb") as imageFile:
        f = imageFile.read()
        return bytearray(f)

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cc0261b3b4534ecabca75b855c0b0516',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('canadacentral.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v2.0/detect?%s" % params,
                 "{'url':'https://upload.wikimedia.org/wikipedia/en/e/e8/Samfacejr.jpg'}", headers)
    # conn.request("POST", "/vision/v2.0/detect?%s" % params, [get_byte_array("C:/person.jpg")],headers)
    # conn.request("POST", "/vision/v2.0/detect?%s" % params, "{'url':'C:\person.jpg'}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except IOError as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
