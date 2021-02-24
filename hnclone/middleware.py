import json
import sys
from urllib.parse import unquote
import uuid

import django
from django.conf import settings

from mixpanel import Mixpanel


def mixpanel_middleware(get_response):

    mp = Mixpanel(settings.MIXPANEL_PROJECT_TOKEN)

    def _get_client_ip(request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        elif 'HTTP_X_REAL_IP' in request.META:
            ip = request.META['HTTP_X_REAL_IP']
        elif 'REMOTE_ADDR' in request.META:
            ip = request.META['REMOTE_ADDR']
        return ip

    def middleware(request):
        # get session id, create one if not exists
        session_id = request.COOKIES.setdefault('sess', str(uuid.uuid4()))

        # check if user is authenticated so we can check after processing thhe r
        request_started_authenticated = request.user.is_authenticated

        response = get_response(request)

        tracking_props = {
            "host": request.get_host(),
            "ip": _get_client_ip(request),
            "method": request.method,
            "path": request.path,
            "django_version": django.get_version(),
            "python_version": "{}.{}".format(sys.version_info.major, sys.version_info.minor),
            "status_code": response.status_code,
            "user_agent": request.META.get("HTTP_USER_AGENT"),
            "referrer": request.META.get("HTTP_REFERER"),
        }

        ignore_paths = ['/proxy/', 'lib.js', 'lib.min.js']

        if not any([substr in request.path for substr in ignore_paths]):
            mp.track(session_id, "Django request", tracking_props)

        if request_started_authenticated and not request.user.is_authenticated:
            # user logged out
            mp.track(session_id, "Logged out")

            # create a new session id
            response.set_cookie('sess', str(uuid.uuid4()))

        return response

    return middleware
