#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-8-2'


def router_middleware(environ, start_response):
    """A simple router middleware."""
    host = environ['HTTP_HOST'].lower()
    path = environ['PATH_INFO'].lower()
    if host == 'sms.jayvic.sinaapp.com' and path == '/':
        from sms.sms_app import sms_app
        return sms_app(environ, start_response)
    if host == 'blog.jayvic.sinaapp.com':
        status = '301 Moved Permanently'
        response_headers = [('Location', 'http://GeekJayvic.sinaapp.com' + path)]
        start_response(status, response_headers)
        return []
    elif path == '/' or path == '/index.html':
        return static_app(environ, start_response, './index.html')
    else:
        # Forbid illegal request.
        return static_app(environ, start_response, './404.html')


def static_app(environ, start_response, path=None):
    """Function application to response static resources."""
    if path is None:
        path = '.' + environ['PATH_INFO']

    try:
        static_file = open(path, 'r')
        status = '200 OK'
    except IOError:
        static_file = []
        status = '404 Not Found'

    response_headers = [('Content-type', 'charset=utf-8')]
    start_response(status, response_headers)

    return static_file
