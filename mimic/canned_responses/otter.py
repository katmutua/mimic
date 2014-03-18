from datetime import datetime


fmt = '%Y-%m-%dT%H:%M:%S.%fZ'


def get_static_history(tenant_id):
    """
    Return a canned history response with the provided tenant_id
    """
    sample_log = {"events": [
        {
            "timestamp": datetime.utcnow().strftime(fmt),
            "_message": "Starting two new servers to satisfy desired capacity",
            "tenant_id": "{0}".format(tenant_id),
            "scaling_group_id": "10000000-0000-0000-0000-00000000001",
            "parent_id": "00000000-0000-0000-0000-00000000001",
            "transaction_id": "00000000-0000-0000-0000-00000000002",
            "as_user_id": "10000",
            "event_type": "convergence.scale_up",
            "is_error": False,
            "desired_capacity": 2,
            "pending_capacity": 2,
            "current_capacity": 0,
            "convergence_delta": 2
        },
        {
            "timestamp": "2013-01-01T00:05:01.000001Z",
            "_message": "Server is Active",
            "tenant_id": "{0}".format(tenant_id),
            "scaling_group_id": "10000000-0000-0000-0000-00000000001",
            "parent_id": "00000000-0000-0000-0000-00000000002",
            "transaction_id": "00000000-0000-0000-0000-00000000003",
            "server_id": "11111111-0000-0000-0000-00000000001",
            "event_type": "server.active",
            "is_error": False
        },
        {
            "timestamp": "2013-01-01T00:05:01.000001Z",
            "_message": "Server is Active",
            "tenant_id": "{0}".format(tenant_id),
            "scaling_group_id": "10000000-0000-0000-0000-00000000001",
            "parent_id": "00000000-0000-0000-0000-00000000002",
            "transaction_id": "00000000-0000-0000-0000-00000000004",
            "server_id": "11111111-0000-0000-0000-00000000002",
            "event_type": "server.active",
            "is_error": False
        }
    ],
        "event_links": []
    }
    return sample_log
