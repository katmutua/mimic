"""
Defines the GET api call to the otter api to allow mimic to return a
canned log response
"""

import json
from twisted.web.server import Request
from mimic.canned_responses.otter import get_static_history
from mimic.rest.mimicapp import MimicApp


Request.defaultContentType = 'application/json'


class OtterApi(object):

    """
    Mocked resources for the Otter API
    """
    app = MimicApp()

    @app.route('/v1.0/<string:tenant_id>/history', methods=['GET'])
    def get_static_history(self, request, tenant_id):
        """
        Return a canned history log
        """
        request.setResponseCode(208)
        events = get_static_history(tenant_id)
        return json.dumps(events)
