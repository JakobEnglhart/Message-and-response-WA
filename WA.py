import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


endpoint = 'https://api.eu-de.assistant.watson.cloud.ibm.com/instances/afebd8e7-8c22-42fd-98b3-a2b4b88288c7'
assistant_id = '3e8794a4-372e-4ce2-8393-18245cf23358'
api_key = 'M_8oCl9lYcTRIqRMykKwQjcqxCFygkVex3X2m4ydpZmA'

authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url(endpoint)

response = assistant.message(
    assistant_id='3e8794a4-372e-4ce2-8393-18245cf23358',
    session_id='3e8794a4-372e-4ce2-8393-18245cf23358',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))