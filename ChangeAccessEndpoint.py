'''
This set of endpoints adds and removes a user from a user group.
See https://cloud.ibm.com/apidocs/iam-access-groups for usage detail.
'''
from flask import Flask, request, jsonify
import ibm_platform_services as ips

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Flask"

@app.route('/remove', methods=["POST"])
def remove_access():
    iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
    test_group_id = 'AccessGroupId-0528089c-daed-480f-ab5a-07192140e22d'
    test_iam_id = 'IBMid-310002GB1S'
    remove_response = iam_access_groups_service.remove_member_from_access_group(
        access_group_id=test_group_id,
        iam_id=test_iam_id
        )
    return("removed")

# @app.route('/add', methods=["POST"])
# def add_access():
#     iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
#     test_group_id = 'AccessGroupId-0528089c-daed-480f-ab5a-07192140e22d'
#     test_iam_id = 'IBMid-310002GB1S'
#     members = [(test_iam_id, 'user')]

#     add_response = iam_access_groups_service.add_members_to_access_group(
#     access_group_id=test_group_id,
#     members=members
#     ).get_result()
#     return("added")

if __name__ == '__main__':
    app.run(debug=True)
