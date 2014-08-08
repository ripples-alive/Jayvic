#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-8-8'

import ConfigParser
import json

from url_decode import url_decode
from message_factory import MessageFactory


def sms_app(environ, start_response):
    """Function application to response to sending sms request."""
    # Get the parameters with GET method.
    url_para = url_decode(environ['QUERY_STRING'])
    try:
        # Get the parameters with POST method.
        content_length = int(environ['CONTENT_LENGTH'])
        content = environ['wsgi.input'].read(content_length)
        url_para.update(url_decode(content))
    except Exception, error:
        print(error)

    # Check whether the parameters are legal.
    if 'from' not in url_para or 'pswd' not in url_para or 'msg' not in url_para:
        status = '200 OK'
        response_headers = [('Content-type', 'application/json;charset=utf-8')]
        start_response(status, response_headers)
        return ['{"sendCode":"-1","info":"参数错误！"}']
    # If receiver's mobile phone number is not set, send to the sender as default.
    if 'to' not in url_para:
        url_para['to'] = url_para['from']

    config = ConfigParser.ConfigParser()
    try:
        config.read('./sms/config.ini')
        msg_cls_type = config.get('Message', 'class type')
    except Exception, error:
        print(error)
        print('Use short fetion message as default message sender class.')
        msg_cls_type = 'Short Fetion'

    sms_sender = MessageFactory.create_message(msg_cls_type, url_para['from'], url_para['pswd'])

    status = '200 OK'
    response_headers = [('Content-type', 'application/json;charset=utf-8')]
    start_response(status, response_headers)

    return [json.dumps(sms_sender.send(url_para['msg'], url_para['to']))]
