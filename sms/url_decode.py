#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Jayvic'
__date__ = '14-8-8'


def url_decode(query_string):
    """Parse the url get and post data."""
    if query_string.strip() == '':
        return {}

    from urllib import unquote
    query_string = unquote(query_string.replace('+', ' '))

    query_dict = {}
    query_list = query_string.split('&')
    for one in query_list:
        param = one.split('=')
        try:
            query_dict[param[0]] = param[1]
        except IndexError:
            raise UrlDecodeError('Can\'t decode "%s"' % one)
    return query_dict


class UrlDecodeError(Exception):
    """Exception class for error while decoding."""
    def __init__(self, describe):
        super(UrlDecodeError, self).__init__(describe)
