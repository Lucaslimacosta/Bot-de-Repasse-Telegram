from telethon import TelegramClient, events
from senhas import api_hash, api_id
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sessao = 'Repassar_Mensagem'

def main():
    logger.info('Monitoramento iniciado ...')
    client = TelegramClient(sessao, api_id, api_hash)
    
    @client.on(events.NewMessage(chats=[]))  # ID do chat de origem
    async def enviar_mensagem(event):
        try:
            logger.info('Mensagem recebida: %s', event.message.text)
            await event.forward_to()  # ID do chat de destino
            logger.info('Mensagem encaminhada com sucesso.')
        except Exception as e:
            logger.error('Erro ao encaminhar a mensagem: %s', e)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
