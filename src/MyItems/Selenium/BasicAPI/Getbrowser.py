import os
from selenium import webdriver
import time
import string
import shutil
import zipfile

from selenium.webdriver.chrome.options import Options

proxy_http = "http://47.94.158.171:8118"
proxy_socks5 = "socks5://209.151.135.126:11747"

def create_proxyauth_extension(proxy_host, proxy_port,
                               proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    if plugin_path is None:
        plugin_path = '/Users/winfred_sui/PycharmProjects/MyPython/vimm_chrome_proxyauth_plugin.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template(
        """
        var config = {
                mode: "fixed_servers",
                rules: {
                  singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                  },
                  bypassList: ["foobar.com"]
                }
              };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path

proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host="216.144.230.99",
    proxy_port=21127,
    proxy_username="",
    proxy_password="qwe092266"
)

def IE():
    if os.name == 'nt':
        IEDriverFile =  os.path.join(os.path.abspath('..'),'Drivers','IEDriverServer.exe')
        os.environ['webdriver.ie.driver'] = IEDriverFile
        driver = webdriver.Ie(IEDriverFile)
        driver.maximize_window()
    else:
        print("IE Browser cannot be ran on non-Windows os.")
    return driver


def Chrome():
    # =============== chrome UI ====================================
    # options = Options()
    # options.add_argument("user-data-dir=/Users/winfred_sui/Library/Application Support/Google/Chrome");
    # # option.add_argument('--headless')
    # # option.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    if os.name == 'nt':
        ChromeDrvier = os.path.join(os.path.abspath('..'),'Drivers','chromedriver.exe')
    elif os.name == 'posix':
        ChromeDrvier = os.path.join(os.path.abspath('..'),'Drivers','chromedriver')
    os.environ['webdriver.chrome.driver'] = ChromeDrvier
    # driver = webdriver.Chrome(executable_path=ChromeDrvier, chrome_options=options)
    chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('window-size=1920x3000')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--hide-scrollbars')
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_extension(proxyauth_plugin_path)

    # proxy_socks_argument = '--proxy-server=socks5://{ip}:{port}'.format(ip='188.166.83.20', port=1080)
    # chrome_options.add_argument(proxy_socks_argument)
    # chrome_options.add_argument('--proxy-server=socks5://114.55.63.81:1080')

    chrome_options.binary_location = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    driver = webdriver.Chrome(executable_path=ChromeDrvier, chrome_options=chrome_options)

    # # =============== phantomjs ====================================
    # proxy_type = proxy_socks5.split("://")[0]
    # proxy_ip = proxy_socks5.split("://")[1].split(":")[0]
    # proxy_port = int(proxy_socks5.split("://")[1].split(":")[1])
    # service_args = [
    #     "--proxy-type=%(http)s" % {"http": proxy_type},
    #     "--proxy=%(host)s:%(port)s" % {
    #         "host": proxy_ip,
    #         "port": proxy_port,
    #     },
    #     #         "--proxy-auth=%(user)s:%(pass)s" % {
    #     #             "user" : 'mimvp-user',
    #     #             "pass" : 'mimvp-pass',
    #     #         },
    # ]
    # phantomjs_path = r"/Users/winfred_sui/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs"
    # driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_args=service_args)



    driver.maximize_window()
    return driver


def FireFox():
    if 'nt' in os.name:
        FFDriver = os.path.join(os.path.abspath('..'),'Drivers','geckodriver.exe')
        FFBrowser = 'C:\Program Files\Mozilla Firefox'
        if not os.path.exists(os.path.join(FFBrowser,'geckodriver.exe')):
            shutil.copy(FFDriver,os.path.join(FFBrowser,'geckodriver.exe'))
        os.environ['PATH'] = FFBrowser
    elif 'posix' in os.name:
        FFDriver = os.path.join(os.path.abspath('..'),'Drivers','geckodriver')
        if not os.path.exists(os.path.join(FFBrowser,'geckodriver')):
            shutil.copy(FFDriver,os.path.join(FFBrowser,'geckodriver'))
        FFBrowser = 'Mac OS path of Firefox'
    driver = webdriver.Firefox(FFBrowser)
    driver.maximize_window()
    return driver

