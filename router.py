#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-8-2'


def router_middleware(environ, start_response):
    path = environ['PATH_INFO']
    if path == '/SMS':
        from sms.sms_app import sms_app
        return sms_app(environ, start_response)
    elif path == '/':
        return static_app(environ, start_response, './index.html')
    else:
        return static_app(environ, start_response)


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
