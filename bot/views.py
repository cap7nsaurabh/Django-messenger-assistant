

from django.http import HttpResponse
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

VERIFY_TOKEN = "generate yours ..you can keep as simple as you want but keep it secret" 
from bot.utils import *

# """
# FB_ENDPOINT & PAGE_ACCESS_TOKEN
# Come from the next step.
# """
FB_ENDPOINT = 'https://graph.facebook.com/v3.3/'
PAGE_ACCESS_TOKEN = "get your at  developer.facebook.com"


def parse_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    message=""
    print(recevied_message)
    matches={}
    command=recevied_message.split(' ',1)
    if command[0]=='!help':
        message=get_help()
        send_message(fbid,message)
    if command[0]=='!movie_rating':
        try:
            msg=command[1]
            print(msg)
            message=getmovies(msg)
        except:
            message="input error try again"
        send_message(fbid,message)
    if command[0]=='!matches':
        li=get_cricket_matches()
        matches=li
        message=extract_message(matches)
        send_message(fbid,message)
    if re.match(r"GM[0-9]+$", command[0]):
        try:
            dat=matches[command[0]]
            message=getm(dat)
        except:
            message="no match associated with this code! try !matches command again"
def send_message(fbid,msg):
    if msg is not None:
        endpoint = f"{FB_ENDPOINT}/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": msg}})
        status = requests.post(
            endpoint,
            headers={"Content-Type": "application/json"},
            data=response_msg)
        print(status.json())
        return status.json()
    return None


class FacebookWebhookView(View):
    @method_decorator(csrf_exempt)  # required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  # python3.6+ syntax

    #    '''
    #    hub.mode
    #    hub.verify_token
    #    hub.challenge
    #    Are all from facebook. We'll discuss soon.
    #    '''

    def get(self, request, *args, **kwargs):
        hub_mode = request.GET.get('hub.mode')
        hub_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')
        if hub_token != VERIFY_TOKEN:
            return HttpResponse('Error, invalid token', status_code=403)
        print("verification succesful")
        return HttpResponse(hub_challenge)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))
        print(incoming_message)
        mes=""
        sender=""
        try:
            for it in incoming_message['entry'][0]['messaging'][0].items():
                if 'message' in it:
                    print(it[1]['text'])
                    mes = it[1]['text']
                if 'sender' in it:
                    print(it[1]['id'])
                    sender = it[1]['id']
        except:
            print("no message found")

        #            fb_user_id = message['sender']['id']  # sweet!
        #            fb_user_txt = message['message'].get('text')
        try:
            if mes:
                parse_message(sender, mes)
                print("success")
        except:
            print("could not send message")
        return HttpResponse("Success", status=200)
    # bot.utils.get_news(country)
    # bot.utils.getmovies(msg)#msg in form id,name,type,year
