import time
from testpage import OperationsHelper
import logging
import yaml
from testpage import get_post, get_my_post, create_post


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_get_post(login):
    logging.info('Test_get_post starting')
    output = get_post(login)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert testdata['id_test'] in res


def test_creation_post(login):
    logging.info('Test_creation_post starting')
    post_dict = dict()
    with open('./testdata.yaml', encoding='utf-8') as f:
        testdata = yaml.safe_load(f)
    for item in testdata['post_check'].keys():
        post_dict[item] = (testdata['post_check'], testdata['post_check'][item])
    new_post = create_post(login, post_dict)['description']
    assert new_post in [item['description'] for item in get_my_post(login)['data']]


def test_step_1(brows):
    logging.info('Test1 starting')
    test_page = OperationsHelper(brows)
    test_page.log_in(testdata['test_data'], testdata['test_data'])
    assert test_page.get_error_text() == '401', 'Test failed'


def test_step_2(brows):
    logging.info('Test2 starting')
    test_page = OperationsHelper(brows)
    test_page.log_in(testdata['login'], testdata['password'])
    assert test_page.get_success_text() == f"Hello, {testdata['login']}"


def test_step_3(brows):
    logging.info('Test3 starting')
    test_page = OperationsHelper(brows)
    test_page.click_contact_link()
    time.sleep(testdata['sleep_time_for_check'])
    assert test_page.get_go_to_contact_text() == 'Contact us!'


def test_step_4(brows):
    logging.info('Test4 starting')
    test_page = OperationsHelper(brows)
    test_page.enter_contact_name(testdata['test_data'])
    assert True


def test_step_5(brows):
    logging.info('Test5 starting')
    test_page = OperationsHelper(brows)
    test_page.enter_contact_email(testdata['test_email'])
    assert True


def test_step_6(brows):
    logging.info('Test6 starting')
    test_page = OperationsHelper(brows)
    test_page.enter_contact_content(testdata['test_data'])
    assert True


def test_step_7(brows):
    logging.info('Test7 starting')
    test_page = OperationsHelper(brows)
    test_page.click_contact_us_button()
    assert True


def test_step_8(brows):
    logging.info('Test8 starting')
    test_page = OperationsHelper(brows)
    time.sleep(testdata['sleep_time_for_check'])
    assert test_page.get_alert_text() == 'Form successfully submitted'