import falcon, json, requests
from falcon_cors import CORS
from DB import Record

cors    = CORS(allow_all_origins=True,
               allow_all_methods=True,
               allow_all_headers=True,
               allow_credentials_all_origins=True,)
api     = application = falcon.API(middleware=[cors.middleware])
# https://newsapi.org/docs/get-started
URL     = "https://newsapi.org/v2/top-headlines"
COUNTRY = "tr"
APIKEY  = "124ed9f55e614537a0788773e0ff9196"
QUERY   = ('{}?country={}&apiKey={}'.format(URL, COUNTRY, APIKEY))


class FetchTopNews(object):
    def on_get(self, req, resp):
        result = requests.get(QUERY).text
        resp.body = result

class SaveSingle(object):
    def on_post(self, req, resp):
        data        = json.loads(req.stream.read().decode("utf-8"))
        title       = data['title']
        description = data['description']
        url         = data['url']
        imageURL    = data['urlToImage']

        news        = Record(title=title, description=description, url=url, imageURL=imageURL)
        news.save()

        resp.body = "OK"

class FetchSaved(object):
    def on_get(self, req, resp):
        result = Record.objects().to_json(indent=2)
        resp.body = result



api.add_route('/', FetchTopNews())
api.add_route('/save', SaveSingle())
api.add_route('/mylist', FetchSaved())


"""
{'articles': [
  {'author': None,
   'description': 'İçişleri Bakanlığından, son bir haftada düzenlenen iç güvenlik  operasyonlarında 36 teröristin etkisiz hale getirildiği bildirildi.',
   'publishedAt': '2018-07-30T07:00:51Z',
   'source': {'id': None, 'name': 'Milliyet.com.tr'},
   'title': 'İçişleri Bakanlığı: 36 terörist etkisiz hale getirildi',
   'url': 'http://www.milliyet.com.tr/icisleri-bakanligi-36-terorist-gundem-2715540/',
   'urlToImage': 'http://i.milliyet.com.tr/YeniAnaResim/2018/07/30/fft99_mf12027133.Jpeg'},],
 'status': 'ok',
 'totalResults': 20}
"""
