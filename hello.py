def application(env,start_response):
    status = '200 OK'
    headers=[('Content-Type', 'text/plain')]
    start_response(status,headers)
    out = env['QUERY_STRING'].split("&")
    out =[item+'\r\n' for item in out]
    return out
