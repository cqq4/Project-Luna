from api.client import LunaClient

luna = LunaClient()

response = luna.send_message("Oi, Luna! Quem e voce?")

print(response)