import os
import requests
import sys

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class LunaClient():
    def __init__(self):
        self.api_key= os.getenv("OPENROUTER_API_KEY")
        self.url= "https://openrouter.ai/api/v1/chat/completions"
        self.model = "nvidia/nemotron-3.5-lightning:free"
        
        if getattr(sys,"frozen",False):
            BASE_DIR = Path(sys.executable).parent
            RESOURCE_DIR = Path(sys._MEIPASS)
        else:
            BASE_DIR = Path(__file__).resolve().parent.parent
            RESOURCE_DIR = BASE_DIR
            
        load_dotenv(BASE_DIR/".env")
        
        personality_path = RESOURCE_DIR / "personality" / "luna.txt"
        
        with open(personality_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()
            
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]
            
    
    def send_message(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # Adiciona a mensagem do usuário ao histórico
        self.messages.append({
            "role": "user",
            "content": message
        })

        payload = {
            "model": self.model,
            "messages": self.messages
        }

        try:
            response = requests.post(
                self.url,
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()
            answer = data["choices"][0]["message"]["content"]

            # Salva a resposta da Luna no histórico
            self.messages.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except requests.exceptions.HTTPError as error:
            # Remove a mensagem que não conseguiu ser processada
            self.messages.pop()

            if response.status_code == 429:
                print("ERRO DETALHADO: ", response.text)
                print("RETRY AFTER: ", response.headers.get("Retry-After"))
                
                return "Calmaaa! Estou recebendo muitas requisições. Tente novamente daqui a pouquinho! 🥺"

            raise error
