from django.apps import AppConfig


class ExaminationConfig(AppConfig):
    name = 'examination'

    def ready(self):
        import examination.signals