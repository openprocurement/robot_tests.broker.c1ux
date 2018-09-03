# -*- coding: utf-8 -
from iso8601 import parse_date
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime, timedelta
from pytz import timezone
import os
import urllib
import pytz


def get_library():
    return BuiltIn().get_library_instance('Selenium2Library')

def convert_date_to_dash_format(date):
    return datetime.strptime(date,'%d.%m.%Y').strftime('%Y-%m-%d')

def contract_period(date):
    parseDateTime = parse_date(date)
    toFormat = parseDateTime.strftime("%d-%m-%Y")
    return toFormat

def get_webdriver_instance():
    return get_library()._current_browser()

def auction_period_to_broker_format(isodate):
    parseDateTime = parse_date(isodate)
    toFormat = parseDateTime.strftime("%d-%m-%Y %H:%M")
    return toFormat

def parse_iso(isoDate, toFormat):
    parseDateTime = parse_date(isoDate)
    return parseDateTime.strftime(toFormat)

def adapt_items_data(field_name, value):
    if field_name == 'quantity':
        value = float(value)
    elif field_name == "unit.code":
        value = view_to_cdb_fromat(value)
    elif field_name == "contractPeriod.startDate":
        value = toISO(value)
    elif field_name == "contractPeriod.endDate":
        value = toISO(value)
    return value

def toISO(v_date):
    time_zone = pytz.timezone('Europe/Kiev')
    d_date = datetime.strptime(v_date, '%d.%m.%Y')
    localized_date = time_zone.localize(d_date)
    return localized_date.isoformat()

def cdb_format_to_view_format(string):
    return {
        u"dgfFinancialAssets": u"Право вимоги",
        u"dgfOtherAssets": u"Майно банку",
        u"0": u"Невідомо",
        u"1": u'Вперше',
        u"2": u'Вдруге',
        u"3": u'Втретє',
        u"4": u'Вчетверте',
        u"CPV": u"ДК021",
        u"bidder1": u"Один",
        u"bidder2": u"Два",
        u"sub_False": u"Продажу",
        u"sub_True":  u"Оренди"
    }.get(string, string)

def getRegistrationDetailsStatus(string):
    return {
        u"unknown":     u'Дефолтне значення',
        u"registering": u'Об’єкт реєструється',
        u"complete":    u'Об’єкт зареєстровано',

    }.get(string, string)

def view_to_cdb_fromat(string):
    return {
            u"пар": u"PR" ,
            u"літр" : u"LTR",
            u"набір" : u"SET",
            u"пачка" : u"RM",
            u"упаковка" :u"PK",
            u"пачок" : u"NMP",
            u"метри" : u"MTR",
            u"ящик" : u"BX",
            u"метри кубічні" : u"MTQ",
            u"рейс" : u"E54",
            u"тони" : u"TNE",
            u"метри квадратні" : u"MTK",
            u"кілометри" : u"KMT",
            u"штуки" : u"H87",
            u"місяць" : u"MON",
            u"лот" : u"LO",
            u"блок" : u"D64",
            u"гектар" : u"HAR",
            u"кілограми" : u"KGM",
            u"кілограми": u"кілограм",
            u"кг.": u"кілограми",
            u"кг": u"кілограми",
            u"MTK":u"метри квадратні",
            u"Право вимоги": u"dgfFinancialAssets",
            u"Майно банку": u"dgfOtherAssets",
            u"Голландський аукціон": u"dgfInsider",
            u"грн.": u"UAH",
            u"грн": u"UAH",
            u" з ПДВ": True,
            u"послуга":"E48",
            u"Картонки": u"Картонні коробки",
            u"ПЕРІОД ПРОПОЗИЦІЙ": u"active.tendering",
            u"ПЕРІОД АУКЦІОНУ": u"active.auction",
            u"ПРОПОЗИЦІЇ РОЗГЛЯНУТО": u"active.awarded",
            u"ПЕРІОД КВАЛІФІКАЦІЇ": u"active.qualification",
            u"ЗАВЕРШЕНИЙ": u"complete",
            u"СКАСОВАНИЙ": u"cancelled",
            u"Аукціон скасовано" : u"active",
            u"НЕ ВІДБУВСЯ" : u"unsuccessful",
            u"Ліцензія" : u"financialLicense",
            u"Підписаний протокол" : u"auctionProtocol",
            u" - " : u"",
            u"Невідомо": u"",
            u'Вперше':1,
            u'Вдруге':2,
            u'Втретє':3,
            u'Вчетверте':4,
            u"Повідомлення про аукціон" : "notice",
            u"Документи аукціону" : u"biddingDocuments",
            u"Публічний паспорт активу" : u"technicalSpecifications",
            u"Критерії оцінки" : u"evaluationCriteria",
            u"Критерії прийнятності" : u"eligibilityCriteria",
            u"Публічний паспорт торгів" : u"virtualDataRoom",
            u"Ілюстрація" : u"illustration",
            u"Посилання на публічний паспорт активу" : u"x_dgfPublicAssetCertificate",
            u"Презентація" : u"x_presentation",
            u"Договір про нерозголошення(NDA)" : u"x_nda",
            u"Паспорт торгів" : u"tenderNotice",
            u"Юридична Інформація Майданчиків" : u"x_dgfPlatformLegalDetails",
            u'Порядку ознайомлення з активом у кімнаті даних' : u'x_dgfAssetFamiliarization',
            u"Порядку ознайомлення з майном" : u'x_dgfAssetFamiliarization',
            u"Очікується кінець кваліфікації" : u"pending.waiting",
            u"Очікується протокол" : u"pending.verification",
            u"ОЧІКУЄТЬСЯ ОПУБЛІКУВАННЯ ПРОТОКОЛУ" : u"active.qualification",
            u"Очікується оплата" : u"pending.payment",
            u"Кандидат забрав гарантійний внесок" : u"cancelled",
            u"Аукціон неуспішний" : u"unsuccessful",
            u"Оплачено, очікується підписання договору" : u"active",
            u"АУКЦІОН" : u"active.auction",
            u"АУКЦІОН НЕ ВІДБУВСЯ": u"unsuccessful",
            u"Аукціон відмінено": u'active',
            u"АУКЦІОН ВІДМІНЕНО" : u"cancelled",
            u"ПРИЙНЯТТЯ ЗАЯВ НА УЧАСТЬ":u"active.tendering"
    }.get(string, string)

def subtract_from_time(date_time, subtr_min, subtr_sec):
    sub = datetime.strptime(date_time, "%d.%m.%Y %H:%M")
    sub = (sub - timedelta(minutes=int(subtr_min),
                           seconds=int(subtr_sec)))
    return timezone('Europe/Kiev').localize(sub).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

def adapt_procuringEntity(auction_data):
    auction_data.data.procuringEntity['name'] = u"ПАТ \"Прайм Банк\""
    auction_data.data.procuringEntity['contactPoint']['telephone'] = u"0993698510"
    auction_data.data.procuringEntity['contactPoint']['faxNumber'] = u"0993698511"
    return auction_data

def before_create_auction(auction_data, role_name):
    if role_name != 'tender_owner':
        return auction_data
    if  auction_data.data.has_key('adapt_procuringEntity'):
            auction_data = adapt_procuringEntity(auction_data)
    if  auction_data.data.has_key('assetCustodian'):
        auction_data = adapt_assetCustodian(auction_data)
    return auction_data

def join(l, separator):
    return separator.join(l)

def adapt_assetCustodian(asset_data):
    asset_data.data.assetCustodian['name'] = u"ПАТ \"Прайм Банк\""
    asset_data.data.assetCustodian['identifier']['legalName'] = u"ПАТ \"Прайм Банк\""
    asset_data.data.assetCustodian['identifier']['id'] = u"11111111"
    asset_data.data.assetCustodian['contactPoint']['telephone'] = u"0993698510"
    asset_data.data.assetCustodian['contactPoint']['faxNumber'] = u"0993698511"
    return asset_data
