from nose.tools import assert_greater, eq_, ok_

from scrapezillow.scraper import scrape_url

zpid_1_expected = {
    'city': u'Oakland',
    'bathrooms': u'1',
    'sqft': u'545',
    'bedrooms': u'1',
    'zipcode': u'94610',
    'state': u'CA',
}


def test_scrape_url():
    zpid = "24743857"
    response = scrape_url(None, zpid, 5)
    for k, v in zpid_1_expected.items():
        eq_(response[k], v)
    ok_(response['sales_info'])
    if not response['sales_info']['price']:
        eq_(response['sales_info']['status'], 'Off Market')
    else:
        assert_greater(int(response['sales_info']['price'].replace(',', '')), 0)
    ok_(response['description'])
    ok_(response['price_history'])
