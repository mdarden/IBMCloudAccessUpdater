"""
This script updates access on IBM Cloud using the IAM API
See https://cloud.ibm.com/apidocs/iam-access-groups for usage details

IAM specifies the names of the environment variables used by the SDK.
Add these to your environment:
# export IAM_IDENTITY_URL=https://iam.cloud.ibm.com
# export IAM_IDENTITY_AUTHTYPE=iam
# export IAM_IDENTITY_APIKEY=<YOUR API KEY>
# export export IAM_ACCESS_GROUPS_APIKEY=<YOUR API_KEY>

Also set these env variables
ACCESS_GROUP_ID=<YOUR ACCESS GROUP ID>
TEST_USER_IAM_ID=<IAM ID OF YOUR TEST USER>

"""
# import requests
# import json
# import csv
# from ibm_platform_services import IamIdentityV1
import os
import ibm_platform_services as ips

def main():
    iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
    test_group_id = os.getenv('ACCESS_GROUP_ID')
    iam_id = os.getenv('TEST_USER_IAM_ID')
    response = iam_access_groups_service.remove_member_from_access_group(
        access_group_id=test_group_id,
        iam_id=iam_id
        )

    
if __name__ == "__main__":
    main()
