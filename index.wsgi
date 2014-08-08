#!/usr/bin/env python
# encoding:utf-8

import sae

from router import router_middleware


application = sae.create_wsgi_app(router_middleware)
