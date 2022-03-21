from django.conf import settings

def add_item(name, description):
  print('adding item', settings.BRING_API_ENDPOINT, flush=True)

