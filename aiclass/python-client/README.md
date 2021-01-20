# swagger-client
Speech Services API v2.0.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.microsoft.com/azure/cognitive-services/speech-service/support](https://docs.microsoft.com/azure/cognitive-services/speech-service/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))
test_definition = swagger_client.TestDefinition() # TestDefinition | The details of the new accuracy test.

try:
    # Creates a new accuracy test.
    api_instance.create_accuracy_test(test_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->create_accuracy_test: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://eastus.cris.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomSpeechAccuracyTestsApi* | [**create_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#create_accuracy_test) | **POST** /api/speechtotext/v2.0/accuracytests | Creates a new accuracy test.
*CustomSpeechAccuracyTestsApi* | [**delete_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#delete_accuracy_test) | **DELETE** /api/speechtotext/v2.0/accuracytests/{id} | Deletes the accuracy test identified by the given ID.
*CustomSpeechAccuracyTestsApi* | [**get_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#get_accuracy_test) | **GET** /api/speechtotext/v2.0/accuracytests/{id} | Gets the accuracy test identified by the given ID.
*CustomSpeechAccuracyTestsApi* | [**get_accuracy_tests**](docs/CustomSpeechAccuracyTestsApi.md#get_accuracy_tests) | **GET** /api/speechtotext/v2.0/accuracytests | Gets the list of accuracy tests for the authenticated subscription.
*CustomSpeechAccuracyTestsApi* | [**update_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#update_accuracy_test) | **PATCH** /api/speechtotext/v2.0/accuracytests/{id} | Updates the mutable details of the test identified by its id.
*CustomSpeechDatasetsForModelAdaptationApi* | [**delete_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#delete_dataset) | **DELETE** /api/speechtotext/v2.0/datasets/{id} | Deletes the specified dataset.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset) | **GET** /api/speechtotext/v2.0/datasets/{id} | Gets the dataset identified by the given ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_datasets) | **GET** /api/speechtotext/v2.0/datasets | Gets a list of datasets for the authenticated subscription.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_supported_locales_for_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_supported_locales_for_datasets) | **GET** /api/speechtotext/v2.0/datasets/locales | Gets a list of supported locales for data imports.
*CustomSpeechDatasetsForModelAdaptationApi* | [**update_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#update_dataset) | **PATCH** /api/speechtotext/v2.0/datasets/{id} | Updates the mutable details of the dataset identified by its ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**upload_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#upload_dataset) | **POST** /api/speechtotext/v2.0/datasets/upload | Uploads data and creates a new dataset.
*CustomSpeechEndpointsApi* | [**create_endpoint**](docs/CustomSpeechEndpointsApi.md#create_endpoint) | **POST** /api/speechtotext/v2.0/endpoints | Creates a new endpoint.
*CustomSpeechEndpointsApi* | [**create_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#create_endpoint_data_export) | **POST** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Create a new endpoint data export task.
*CustomSpeechEndpointsApi* | [**delete_endpoint**](docs/CustomSpeechEndpointsApi.md#delete_endpoint) | **DELETE** /api/speechtotext/v2.0/endpoints/{id} | Deletes the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**delete_endpoint_data**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_data) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Deletes the transcriptions and captured audio files associated with the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**delete_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_data_export) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Deletes the endpoint data export task identified by the given ID.
*CustomSpeechEndpointsApi* | [**get_endpoint**](docs/CustomSpeechEndpointsApi.md#get_endpoint) | **GET** /api/speechtotext/v2.0/endpoints/{id} | Gets the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**get_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#get_endpoint_data_export) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Gets the specified endpoint data export task for the authenticated user.
*CustomSpeechEndpointsApi* | [**get_endpoint_data_exports**](docs/CustomSpeechEndpointsApi.md#get_endpoint_data_exports) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Gets the list of endpoint data export tasks for the authenticated user.
*CustomSpeechEndpointsApi* | [**get_endpoints**](docs/CustomSpeechEndpointsApi.md#get_endpoints) | **GET** /api/speechtotext/v2.0/endpoints | Gets the list of endpoints for the authenticated subscription.
*CustomSpeechEndpointsApi* | [**get_supported_locales_for_endpoints**](docs/CustomSpeechEndpointsApi.md#get_supported_locales_for_endpoints) | **GET** /api/speechtotext/v2.0/endpoints/locales | Gets a list of supported locales for endpoint creations.
*CustomSpeechEndpointsApi* | [**update_endpoint**](docs/CustomSpeechEndpointsApi.md#update_endpoint) | **PATCH** /api/speechtotext/v2.0/endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.
*CustomSpeechModelsApi* | [**create_model**](docs/CustomSpeechModelsApi.md#create_model) | **POST** /api/speechtotext/v2.0/models | Creates a new model.
*CustomSpeechModelsApi* | [**delete_model**](docs/CustomSpeechModelsApi.md#delete_model) | **DELETE** /api/speechtotext/v2.0/models/{id} | Deletes the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_model**](docs/CustomSpeechModelsApi.md#get_model) | **GET** /api/speechtotext/v2.0/models/{id} | Gets the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_models**](docs/CustomSpeechModelsApi.md#get_models) | **GET** /api/speechtotext/v2.0/models | Gets the list of models for the authenticated subscription.
*CustomSpeechModelsApi* | [**get_supported_locales_for_models**](docs/CustomSpeechModelsApi.md#get_supported_locales_for_models) | **GET** /api/speechtotext/v2.0/models/locales | Gets a list of supported locales for model adaptation.
*CustomSpeechModelsApi* | [**update_model**](docs/CustomSpeechModelsApi.md#update_model) | **PATCH** /api/speechtotext/v2.0/models/{id} | Updates the metadata of the model identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**create_transcription**](docs/CustomSpeechTranscriptionsApi.md#create_transcription) | **POST** /api/speechtotext/v2.0/transcriptions | Creates a new transcription.
*CustomSpeechTranscriptionsApi* | [**delete_transcription**](docs/CustomSpeechTranscriptionsApi.md#delete_transcription) | **DELETE** /api/speechtotext/v2.0/transcriptions/{id} | Deletes the specified transcription task.
*CustomSpeechTranscriptionsApi* | [**get_supported_locales_for_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_supported_locales_for_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions/locales | Gets a list of supported locales for offline transcriptions.
*CustomSpeechTranscriptionsApi* | [**get_transcription**](docs/CustomSpeechTranscriptionsApi.md#get_transcription) | **GET** /api/speechtotext/v2.0/transcriptions/{id} | Gets the transcription identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**get_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions | Gets a list of transcriptions for the authenticated subscription.
*CustomSpeechTranscriptionsApi* | [**update_transcription**](docs/CustomSpeechTranscriptionsApi.md#update_transcription) | **PATCH** /api/speechtotext/v2.0/transcriptions/{id} | Updates the mutable details of the transcription identified by its ID.
*ServiceHealthApi* | [**get_health_status**](docs/ServiceHealthApi.md#get_health_status) | **GET** /api/common/v2.0/healthstatus | The action returns the health of the different components of the serivce.


## Documentation For Models

 - [Component](docs/Component.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetIdentity](docs/DatasetIdentity.md)
 - [DatasetUpdate](docs/DatasetUpdate.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointData](docs/EndpointData.md)
 - [EndpointDataDefinition](docs/EndpointDataDefinition.md)
 - [EndpointMetadataUpdate](docs/EndpointMetadataUpdate.md)
 - [ErrorContent](docs/ErrorContent.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [HealthStatusResponse](docs/HealthStatusResponse.md)
 - [IReadOnlyDictionary2](docs/IReadOnlyDictionary2.md)
 - [IReadOnlyDictionary21](docs/IReadOnlyDictionary21.md)
 - [InnerErrorV2](docs/InnerErrorV2.md)
 - [Model](docs/Model.md)
 - [ModelIdentity](docs/ModelIdentity.md)
 - [ModelUpdate](docs/ModelUpdate.md)
 - [SpeechEndpointDefinition](docs/SpeechEndpointDefinition.md)
 - [SpeechModelDefinition](docs/SpeechModelDefinition.md)
 - [Test](docs/Test.md)
 - [TestDefinition](docs/TestDefinition.md)
 - [TestUpdate](docs/TestUpdate.md)
 - [Transcription](docs/Transcription.md)
 - [TranscriptionDefinition](docs/TranscriptionDefinition.md)
 - [TranscriptionUpdate](docs/TranscriptionUpdate.md)
 - [WebHookConfiguration](docs/WebHookConfiguration.md)
 - [WebHookUpdateV21](docs/WebHookUpdateV21.md)


## Documentation For Authorization


## subscription_key

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

## token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


