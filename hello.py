def application(env,start_response):
    status = '200 OK'
    headers=[('Content-Type', 'text/plain')]
    start_response(status,headers)
    resp = env['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
    return resp
