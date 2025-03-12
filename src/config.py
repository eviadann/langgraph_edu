# LANGSMITH_TRACING=True
# LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"
# LANGSMITH_API_KEY="LANGSMITH_API_KEY"
# LANGSMITH_PROJECT="pr-upbeat-barbecue-56"
# OPENAI_API_KEY="<your-openai-api-key>"

from langchain_gigachat.chat_models import GigaChat
import os


llm_gigachat = GigaChat(
    credentials=os.getenv("AUTHORIZATION_KEY_GIGACHAT_WORK"),
    verify_ssl_certs=False,
    scope='GIGACHAT_API_CORP',
    temperature=0,
    profanity_check = False,
    model="GigaChat-Max",        
    # auth_url="https://sm-auth-sd.prom-88-89-apps.ocp-geo.ocp.sigma.sbrf.ru/api/v2/oauth"
)