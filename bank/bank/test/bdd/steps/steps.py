from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp

from bank_app import app

@step(u'When I enter the account number "([^"]*)"')
def when_i_enter_the_account_number_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:500/')
    assert_equal(world.response.status_code, 200)
    assert_equal(world.response.text, u'Hello World!')
    
@step(u'I enter the account number " ([^"]*)"')
def when_i_enter_the_account_number_group1(step, account_number):
    form = world.responseforms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.statu_code, 200)
