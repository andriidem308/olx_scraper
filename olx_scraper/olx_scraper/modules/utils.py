def get_page(url: str, symbol='=', count=1) -> str:
    numb = url.rindex(symbol)
    part = url[numb:]
    if (url[-1] == symbol) and (symbol == '/'):
        end = url.rindex('/')
        start = url[:end].rindex('/')
        part = url[start + 1:end]
        page = str(int(part) + count)
        result_url = f'{url[:start]}/{page}/'
    elif '&' in part:
        start = numb
        end = numb + part.index('&')
        part = url[start:end]
        core_part = part.rindex(symbol[-1]) + 1
        page = part[:core_part] + str(int(part[core_part:]) + count)
        result_url = f'{url[:start]}{page}{url[end:]}'
    else:
        # if symbol is end
        result_url = f'{url[:numb + 1]}{str(int(url[numb + 1:]) + count)}'
    return result_url
