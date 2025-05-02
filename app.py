from flask import Flask, render_template, request
import feedparser
import os

app = Flask(__name__)

def get_rss(seccio, diari, mode='local'):
    if mode == 'local':
        xml_path = os.path.join('rss', diari, f'{seccio}.xml')
        if not os.path.exists(xml_path):
            return None
        return feedparser.parse(xml_path)
    else:
        if diari == 'lavanguardia':
            url = f'https://www.lavanguardia.com/rss/{seccio}.xml'
        elif diari == 'puntavui':
                url = f'https://www.elpuntavui.cat/{seccio}.feed?type=rss'
        else:
            return None
        return feedparser.parse(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    mode = request.args.get('mode', 'local')
    rss = get_rss(seccio, 'lavanguardia', mode)
    if not rss:
        return "No s'ha pogut carregar l'RSS", 404
    return render_template('lavanguardia.html', rss=rss)

@app.route('/puntavui/<seccio>')
def puntavui(seccio):
    mode = request.args.get('mode', 'local')
    rss = get_rss(seccio, 'puntavui', mode)
    if not rss:
        return "No s'ha pogut carregar l'RSS", 404
    return render_template('puntavui.html', rss=rss)

if __name__ == '__main__':
    app.run(debug=True)
