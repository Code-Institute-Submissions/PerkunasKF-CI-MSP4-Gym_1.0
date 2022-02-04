from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(sefl, request):
        self.request = request

    
    def handle_event(self, event):
        """ Handle a genric/unknown/unexpected webhook evebt """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status = 200
        )