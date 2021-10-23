BOT_NAME = 'olx_scraper'
PROXY_MAX_TRY = 70
PROXY_ENABLED = False
EXTRA_STATUS_LIST = []
# HTTPERROR_ALLOWED_CODES = [403, 400]

ROBOTSTXT_OBEY = False
CLOSESPIDER_ITEMCOUNT = 0
CONCURRENT_REQUESTS = 250
CONCURRENT_ITEMS = 250

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'modules.rotate_useragent.RotateUserAgentMiddleware': 400,
    # 'modules.proxy.proxy_retry_middleware.ProxyRetryMiddleware': 400,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://localhost:8050/'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

AUTOTHROTTLE_ENABLED = True
RETRY_ENABLED = False
# RETRY_TIMES = 0
# RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403]
DOWNLOAD_TIMEOUT = 20

DNSCACHE_ENABLED = False

try:
    from local_settings import *
except ImportError as e:
    pass

PROXY6_API_KEY = 'e7d36d71c0-0b7f449a0c-430e027e40'
