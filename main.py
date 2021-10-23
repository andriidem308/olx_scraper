categories = {
    'Дитячий світ': 'detskiy-mir',
    'Нерухомість': 'nedvizhimost',
    'Авто': 'transport',
    'Запчастини для транспорту': 'zapchasti-dlya-transporta',
    'Робота': 'rabota',
    'Тварини': 'zhivotnye',
    'Дім і сад': 'dom-i-sad',
    'Електроніка': 'elektronika',
    'Бізнес та послуги': 'uslugi',
    'Мода і стиль': 'moda-i-stil',
    'Хобі, відпочинок і спорт': 'hobbi-otdyh-i-sport',
}

subcategories = {
    'Дитячий світ': {
        '':''
    },
    'Нерухомість': {
        '':''
    },
    'Авто': {
        '':''
    },
    'Запчастини для транспорту': {
        '':''
    },
    'Робота': {
        '':''
    },
    'Тварини': {
        '':''
    },
    'Дім і сад': {
        '':''
    },
    'Електроніка': {
        'Комп\'ютери та комплектуючі': 'kompyutery-i-komplektuyuschie',
        'Телефони та аксесуари': 'telefony-i-aksesuary',
        'Фото / відео': 'foto-video',
        'Тв / відеотехніка': 'tv-videotehnika',
        'Аудіотехніка': 'audiotehnika',
        'Ігрові приставки': 'igry-i-igrovye-pristavki',
        'Планшети / ел. книги': 'planshety-el-knigi-i-aksessuary',
        'Ноутбуки та аксесуари': 'noutbuki-i-aksesuary',
        'Побутова техніка для кухні': 'tehnika-dlya-kuhni',
        'Техніка для дому': 'tehnika-dlya-doma',
        'Аксесуари та комплектуючі': 'aksessuary-i-komplektuyuschie',
        'Інша електроніка': 'prochaja-electronika',
    },
    'Бізнес та послуги': {
        '': ''
    },
    'Мода і стиль': {
        '': ''
    },
    'Хобі, відпочинок і спорт': {
        '': ''
    }
}


def build_url(query='',
              phone=False, brand=None,
              category=None, subcategory=None,
              price_from=None, price_to=None,
              state=None):

    base_url = 'https://www.olx.ua/uk/'

    if phone:
        base_url = f'{base_url}elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/'
    else:
        if category:
            base_url = f'{base_url}{categories[category]}/'
            if subcategory:
                base_url = f'{base_url}{subcategories[category][subcategory]}/'

    if brand:
        base_url = f'{base_url}{brand.lower()}/'

    if query:
        base_url = f'{base_url}q-{query.replace(" ", "-")}/'

    if any([price_from, price_to]):
        filters = []

        if price_from:
            filters.append(f'search[filter_float_price%3Afrom]={price_from}')
        if price_to:
            filters.append(f'search[filter_float_price%3Ato]={price_to}')
        if state:
            filters.append(f'search[filter_enum_state][0]={state}')

        base_url += '?' + '&'.join(filters)

    return base_url


print(build_url('iphone 8', phone=True, price_from=10000, price_to=15000, state='new'))
