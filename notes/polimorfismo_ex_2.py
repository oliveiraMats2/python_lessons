from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self): ...


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('E-mail: enviando - ', self.mensagem)


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando - ', self.mensagem)


notificacao_email = NotificacaoEmail('testando e-mail')
notificacao_email.enviar()

notificacao_sms = NotificacaoSMS('testando SMS')
notificacao_sms.enviar()
