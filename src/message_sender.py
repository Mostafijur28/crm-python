class MessageSender:
    def __init__(self, logger):
        self.logger = logger

    def send_message(self, lead, persona, output_channel):
        if output_channel == 'Whatsapp':
            self.send_whatsapp_message(lead, persona)
        elif output_channel == 'iMessage':
            self.send_imessage(lead, persona)
        else:
            self.logger.log(f"Unsupported output channel: {output_channel}")

    def send_whatsapp_message(self, lead, persona):
        message = f"{persona} is contacting you via Whatsapp about your interest."
        self.logger.log(f"Sending Whatsapp message to lead: {lead['lead_data']} - Message: {message}")

    def send_imessage(self, lead, persona):
        message = f"{persona} is contacting you via iMessage about your interest."
        self.logger.log(f"Sending iMessage to lead: {lead['lead_data']} - Message: {message}")
