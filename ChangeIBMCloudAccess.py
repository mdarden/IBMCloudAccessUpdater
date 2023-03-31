"""
This script updates access on IBM Cloud using the IAM API

IAM specifies the names of the environment variables used by the SDK.
Add these to your environment:
# export IAM_IDENTITY_URL=https://iam.cloud.ibm.com
# export IAM_IDENTITY_AUTHTYPE=iam
# export IAM_IDENTITY_APIKEY=<YOUR API KEY>
"""
import requests
# import json
import csv
# from ibm_platform_services import IamIdentityV1
import ibm_platform_services as ips

def main():
    # service_client = ips.IamIdentityV1.new_instance()

    # account_id = 'ebf33ad3ea2e538ed628a3697b5e1d30'
    # iam_id = 'IBMid-270007NXK2'
    # api_key_list = service_client.list_api_keys(account_id=account_id, iam_id=iam_id, include_history=True).get_result()
    # print(json.dumps(api_key_list, indent=2))

    iam_access_groups_service = ips.IamAccessGroupsV2.new_instance()
    test_group_id = 'AccessGroupId-0528089c-daed-480f-ab5a-07192140e22d'
    iam_id = 'IBMid-310002GB1S'
    response = iam_access_groups_service.remove_member_from_access_group(
        access_group_id=test_group_id,
        iam_id=iam_id
        )

    
if __name__ == "__main__":
    main()
