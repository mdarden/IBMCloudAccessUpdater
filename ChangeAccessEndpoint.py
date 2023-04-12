'''
This set of endpoints adds and removes a user from a user group.

This script updates access on IBM Cloud using the IAM API
See https://cloud.ibm.com/apidocs/iam-access-groups for usage detail.

IAM specifies the names of the environment variables used by the SDK.
Add these to your environment:
# export IAM_IDENTITY_URL=https://iam.cloud.ibm.com
# export IAM_IDENTITY_AUTHTYPE=iam
# export IAM_IDENTITY_APIKEY=<YOUR API KEY>
# export export IAM_ACCESS_GROUPS_APIKEY=<YOUR API_KEY>

Also set these env variables
ACCESS_GROUP_ID=<YOUR ACCESS GROUP ID>
TEST_USER_IAM_ID=<IAM ID OF YOUR TEST USER>
'''
import os
from flask import Flask, request, jsonify
import ibm_platform_services as ips

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Flask"

@app.route('/remove', methods=["POST"])
def remove_access():
    iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
    test_group_id = os.getenv('ACCESS_GROUP_ID')
    test_iam_id = os.getenv('TEST_USER_IAM_ID')
    remove_response = iam_access_groups_service.remove_member_from_access_group(
        access_group_id=test_group_id,
        iam_id=test_iam_id
        )
    return("removed")

# @app.route('/add', methods=["POST"])
# def add_access():
#     iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
#     test_group_id = os.getenv('ACCESS_GROUP_ID')
#     test_iam_id = os.getenv('TEST_USER_IAM_ID')
#     members = [(test_iam_id, 'user')]

#     add_response = iam_access_groups_service.add_members_to_access_group(
#     access_group_id=test_group_id,
#     members=members
#     ).get_result()
#     return("added")

if __name__ == '__main__':
    app.run(debug=True)
