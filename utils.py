import logging

# Set up logging configuration
logging.basicConfig(filename='trade_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_action(action_type, token, success):
    message = f"{action_type} {token['name']} - {'Success' if success else 'Failure'}"
    print(message)
    logging.info(message)
