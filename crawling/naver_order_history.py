import sys

from robobrowser import RoboBrowser
from key import NAVER_ID, NAVER_PW

browser = RoboBrowser(parser='html.parser', user_agent="Mozilla/5.0 (Macintosh; INtel Mac macOs 10.10; rv:45.0) Gecko/20100101 Firefox/45.0")

def main():
    print("Accessing to sign in page....", file=sys.stderr)

    browser.open("https://nid.naver.com/nidlogin.login")

    assert '네이버 : 로그인' in browser.parsed.title.string

    form = browser.get_form(attrs={'name': 'frmNIDLogin'})
    form['id'] = NAVER_ID
    form['pw'] = NAVER_PW

    print("Signing in ...", file=sys.stderr)

    browser.submit_form(form, headers={'Referer': browser.url, 'Accept-Language': 'ko,en-US;q=0.7;q=0.3'})

    browser.open("https://order.pay.naver.com/home?tabMenu=SHOPPING&frm=s_order")

    print(browser.parsed.prettify())

if __name__ == '__main__':
    main()

