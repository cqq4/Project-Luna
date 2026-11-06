from PySide6.QtCore import QThread, Signal

class LunaWorker(QThread): #executa uma tarefa em outra thread
    response_received = Signal(str)
    error_occurred = Signal(str) #permite enviar o resultado para a interface
    
    def __init__(self, client, message):
        super().__init__()
        self.client = client
        self.message = message
        
    def run(self): #executado qnd iniciar o thread
        print("WORKER: inicio")
        try:
            print("WORKER: enviando mensagem...")
            response = self.client.send_message(self.message)  #chama a api
            print("WORKER: mensagem recebida...")
            self.response_received.emit(response)
            
        except Exception as error:
            print("WORKER: erro:", repr(error))
            self.error_occurred.emit(str(error))
            
        finally: 
            print("WORKER: finalizado")