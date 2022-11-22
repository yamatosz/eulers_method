import wolframalpha
from credenciais import secrets

def euler(fxy: str, a, b, h, y0):
    m = (b-a)/h
    xlist = xlist_create(a, h, m)
    ylist = ylist_create(fxy=fxy, y0=y0, m=m, h=h,xlist=xlist)
    

    return xlist, ylist

def wolf(fxy: str, a, b, h, y0):
    m = (b-a)/h
    xlist = xlist_create(a,h,m)
    ylist = ylist_wolf(fxy, m, xlist, y0)
    return xlist, ylist

def get_wolf(fxy, x):
    fxy = fxy[7:]
    res = client.query(f'{fxy}, x=={x}')
    return next(res.results).text

def ylist_wolf(fxy, m, xlist, y0):
    ylist = []
    res = client.query(f'dy/dx={fxy};y(0)={y0}')
    fxy = next(res.results).text
    for j in range(int(m)+1):
        x = xlist[j]
        y = get_wolf(fxy=fxy, x=x)
        ylist.append(float(y))
    return ylist

def floatc(num):
    return float(f'{num:.2f}')


def ylist_create(fxy, y0, m, h, xlist, lista= []):
    lista = [y0]
    for j in range(int(m)):
        y = lista[j]
        x = xlist[j]
        yi = y + h*eval(fxy)
        lista.append(yi)
    return lista

def xlist_create(a , h, m, lista = []):
    lista = [a]
    for j in range(int(m)):
        lista[j] = floatc(lista[j])
        lista.append(h+lista[j])

    return lista

def teste():
    return app_id

app_id = secrets.get('API_KEY')
client = wolframalpha.Client(app_id=app_id)