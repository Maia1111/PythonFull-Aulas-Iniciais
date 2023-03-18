# Protocolo SGI
def application(amb, start_response):
    with open('index.html', 'rb') as arq:
        body = arq.read()
    status = "200 ok"
    headers = [("Content-Type", "text/html")]
    start_response(status, headers)
    return [body]

