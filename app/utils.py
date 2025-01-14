import bleach
import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

def sanitize_input(user_input):
    """Sanitize user input to prevent XSS or HTML injection."""
    allowed_tags = []  # No HTML tags allowed
    return bleach.clean(user_input, tags=allowed_tags)


# Azure Cognitive Search credentials
search_service_endpoint = os.getenv("search_service_endpoint")
search_api_key = os.getenv("search_api_key")
index_name = os.getenv("index_name")

def get_text_embeddings(text):
    client = AzureOpenAI(api_key=os.getenv("openai_api_key"),
                         api_version=os.getenv("openai_api_version"),
                         azure_endpoint=os.getenv("openai_azure_endpoint"))

    response = client.embeddings.create(model = "text-embedding-ada-002", input = text).data[0].embedding
    print(response)
    return response

search_client = SearchClient(endpoint=search_service_endpoint, index_name=index_name, credential=AzureKeyCredential(search_api_key))


def search_service(query):
    query_embedding = get_text_embeddings(query)    
    vector_query = VectorizedQuery(vector=query_embedding, k_nearest_neighbors=1000, fields="embeddings")
    search_results = search_client.search(search_text=None, vector_queries=[vector_query], select=['id','supplierName','serviceName','serviceDescription',
                                                                                                   "serviceBenefits", "serviceFeatures", 'lotName',"standardsISOIEC27001", 
                                                                                                   "standardsISO28000", "standardsCSASTAR", "standardsPCI", 
                                                                                                   "standardsCyberEssentials", "standardsCyberEssentialsPlus", 
                                                                                                   "emailOrTicketingSupport", "phoneSupport", "webChatSupport", 
                                                                                                   "governmentSecurityClearances", "staffSecurityClearanceChecks", 
                                                                                                   "resellingType", "educationPricing", "freeVersionTrialOption"])
    print(search_results)
    results=[]
    for result in search_results:
        results.append({
            "id": result["id"], 
            "supplierName": result["supplierName"],  # Adjust based on your field names
            "serviceName": result["serviceName"],
            "serviceDescription": result["serviceDescription"],
            "serviceBenefits": result["serviceBenefits"],
            "serviceFeatures": result["serviceFeatures"],
            "lotName": result["lotName"],
            "standardsISOIEC27001": result["standardsISOIEC27001"],
            "standardsISO28000": result["standardsISO28000"],
            "standardsCSASTAR": result["standardsCSASTAR"],
            "standardsPCI": result["standardsPCI"],
            "standardsCyberEssentials": result["standardsCyberEssentials"],
            "standardsCyberEssentialsPlus": result["standardsCyberEssentialsPlus"],
            "standardsPCI": result["standardsPCI"],
            "standardsCyberEssentials": result["standardsCyberEssentials"],
            "standardsCyberEssentialsPlus": result["standardsCyberEssentialsPlus"],
            "emailOrTicketingSupport": result["emailOrTicketingSupport"],
            "phoneSupport": result["phoneSupport"],
            "webChatSupport": result["webChatSupport"],
            "governmentSecurityClearances": result["governmentSecurityClearances"],
            "staffSecurityClearanceChecks": result["staffSecurityClearanceChecks"],
            "resellingType": result["resellingType"],
            "educationPricing": result["educationPricing"],
            "freeVersionTrialOption": result["freeVersionTrialOption"],
            "score": result["@search.score"]  # Azure Search provides the score for each result
        })
    return results