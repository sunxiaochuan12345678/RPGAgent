# llm_config.py
DEEPSEEK_API_KEY = "Your API"

LLM_CONFIG = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": OPENAI_API_KEY,
            "base_url": "https://api.openai.com/v1"  
        }
    ],
    "temperature": 0.7,  
    "seed": None,  
} 
