# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import silver.models.documents.base
import silver.models.documents.pdf
import django_fsm
from decimal import Decimal
import silver.utils.models
import django.utils.timezone
import livefield.fields
import django.core.validators
import annoying.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDocumentBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=8, verbose_name=silver.models.documents.base.get_billing_documents_kinds, db_index=True)),
                ('series', models.CharField(db_index=True, max_length=20, null=True, blank=True)),
                ('number', models.IntegerField(db_index=True, null=True, blank=True)),
                ('archived_customer', annoying.fields.JSONField(default=dict, null=True, blank=True)),
                ('archived_provider', annoying.fields.JSONField(default=dict, null=True, blank=True)),
                ('due_date', models.DateField(null=True, blank=True)),
                ('issue_date', models.DateField(db_index=True, null=True, blank=True)),
                ('paid_date', models.DateField(null=True, blank=True)),
                ('cancel_date', models.DateField(null=True, blank=True)),
                ('sales_tax_percent', models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('sales_tax_name', models.CharField(max_length=64, null=True, blank=True)),
                ('currency', models.CharField(default=b'USD', help_text=b'The currency used for billing.', max_length=4, choices=[('AED', 'AED (UAE Dirham)'), ('AFN', 'AFN (Afghani)'), ('ALL', 'ALL (Lek)'), ('AMD', 'AMD (Armenian Dram)'), ('ANG', 'ANG (Netherlands Antillean Guilder)'), ('AOA', 'AOA (Kwanza)'), ('ARS', 'ARS (Argentine Peso)'), ('AUD', 'AUD (Australian Dollar)'), ('AWG', 'AWG (Aruban Florin)'), ('AZN', 'AZN (Azerbaijanian Manat)'), ('BAM', 'BAM (Convertible Mark)'), ('BBD', 'BBD (Barbados Dollar)'), ('BDT', 'BDT (Taka)'), ('BGN', 'BGN (Bulgarian Lev)'), ('BHD', 'BHD (Bahraini Dinar)'), ('BIF', 'BIF (Burundi Franc)'), ('BMD', 'BMD (Bermudian Dollar)'), ('BND', 'BND (Brunei Dollar)'), ('BOB', 'BOB (Boliviano)'), ('BRL', 'BRL (Brazilian Real)'), ('BSD', 'BSD (Bahamian Dollar)'), ('BTN', 'BTN (Ngultrum)'), ('BWP', 'BWP (Pula)'), ('BYR', 'BYR (Belarusian Ruble)'), ('BZD', 'BZD (Belize Dollar)'), ('CAD', 'CAD (Canadian Dollar)'), ('CDF', 'CDF (Congolese Franc)'), ('CHF', 'CHF (Swiss Franc)'), ('CLP', 'CLP (Chilean Peso)'), ('CNY', 'CNY (Yuan Renminbi)'), ('COP', 'COP (Colombian Peso)'), ('CRC', 'CRC (Costa Rican Colon)'), ('CUC', 'CUC (Peso Convertible)'), ('CUP', 'CUP (Cuban Peso)'), ('CVE', 'CVE (Cabo Verde Escudo)'), ('CZK', 'CZK (Czech Koruna)'), ('DJF', 'DJF (Djibouti Franc)'), ('DKK', 'DKK (Danish Krone)'), ('DOP', 'DOP (Dominican Peso)'), ('DZD', 'DZD (Algerian Dinar)'), ('EGP', 'EGP (Egyptian Pound)'), ('ERN', 'ERN (Nakfa)'), ('ETB', 'ETB (Ethiopian Birr)'), ('EUR', 'EUR (Euro)'), ('FJD', 'FJD (Fiji Dollar)'), ('FKP', 'FKP (Falkland Islands Pound)'), ('GBP', 'GBP (Pound Sterling)'), ('GEL', 'GEL (Lari)'), ('GHS', 'GHS (Ghana Cedi)'), ('GIP', 'GIP (Gibraltar Pound)'), ('GMD', 'GMD (Dalasi)'), ('GNF', 'GNF (Guinea Franc)'), ('GTQ', 'GTQ (Quetzal)'), ('GYD', 'GYD (Guyana Dollar)'), ('HKD', 'HKD (Hong Kong Dollar)'), ('HNL', 'HNL (Lempira)'), ('HRK', 'HRK (Kuna)'), ('HTG', 'HTG (Gourde)'), ('HUF', 'HUF (Forint)'), ('IDR', 'IDR (Rupiah)'), ('ILS', 'ILS (New Israeli Sheqel)'), ('INR', 'INR (Indian Rupee)'), ('IQD', 'IQD (Iraqi Dinar)'), ('IRR', 'IRR (Iranian Rial)'), ('ISK', 'ISK (Iceland Krona)'), ('JMD', 'JMD (Jamaican Dollar)'), ('JOD', 'JOD (Jordanian Dinar)'), ('JPY', 'JPY (Yen)'), ('KES', 'KES (Kenyan Shilling)'), ('KGS', 'KGS (Som)'), ('KHR', 'KHR (Riel)'), ('KMF', 'KMF (Comoro Franc)'), ('KPW', 'KPW (North Korean Won)'), ('KRW', 'KRW (Won)'), ('KWD', 'KWD (Kuwaiti Dinar)'), ('KYD', 'KYD (Cayman Islands Dollar)'), ('KZT', 'KZT (Tenge)'), ('LAK', 'LAK (Kip)'), ('LBP', 'LBP (Lebanese Pound)'), ('LKR', 'LKR (Sri Lanka Rupee)'), ('LRD', 'LRD (Liberian Dollar)'), ('LSL', 'LSL (Loti)'), ('LYD', 'LYD (Libyan Dinar)'), ('MAD', 'MAD (Moroccan Dirham)'), ('MDL', 'MDL (Moldovan Leu)'), ('MGA', 'MGA (Malagasy Ariary)'), ('MKD', 'MKD (Denar)'), ('MMK', 'MMK (Kyat)'), ('MNT', 'MNT (Tugrik)'), ('MOP', 'MOP (Pataca)'), ('MRO', 'MRO (Ouguiya)'), ('MUR', 'MUR (Mauritius Rupee)'), ('MVR', 'MVR (Rufiyaa)'), ('MWK', 'MWK (Malawi Kwacha)'), ('MXN', 'MXN (Mexican Peso)'), ('MYR', 'MYR (Malaysian Ringgit)'), ('MZN', 'MZN (Mozambique Metical)'), ('NAD', 'NAD (Namibia Dollar)'), ('NGN', 'NGN (Naira)'), ('NIO', 'NIO (Cordoba Oro)'), ('NOK', 'NOK (Norwegian Krone)'), ('NPR', 'NPR (Nepalese Rupee)'), ('NZD', 'NZD (New Zealand Dollar)'), ('OMR', 'OMR (Rial Omani)'), ('PAB', 'PAB (Balboa)'), ('PEN', 'PEN (Sol)'), ('PGK', 'PGK (Kina)'), ('PHP', 'PHP (Philippine Peso)'), ('PKR', 'PKR (Pakistan Rupee)'), ('PLN', 'PLN (Zloty)'), ('PYG', 'PYG (Guarani)'), ('QAR', 'QAR (Qatari Rial)'), ('RON', 'RON (Romanian Leu)'), ('RSD', 'RSD (Serbian Dinar)'), ('RUB', 'RUB (Russian Ruble)'), ('RWF', 'RWF (Rwanda Franc)'), ('SAR', 'SAR (Saudi Riyal)'), ('SBD', 'SBD (Solomon Islands Dollar)'), ('SCR', 'SCR (Seychelles Rupee)'), ('SDG', 'SDG (Sudanese Pound)'), ('SEK', 'SEK (Swedish Krona)'), ('SGD', 'SGD (Singapore Dollar)'), ('SHP', 'SHP (Saint Helena Pound)'), ('SLL', 'SLL (Leone)'), ('SOS', 'SOS (Somali Shilling)'), ('SRD', 'SRD (Surinam Dollar)'), ('SSP', 'SSP (South Sudanese Pound)'), ('STD', 'STD (Dobra)'), ('SVC', 'SVC (El Salvador Colon)'), ('SYP', 'SYP (Syrian Pound)'), ('SZL', 'SZL (Lilangeni)'), ('THB', 'THB (Baht)'), ('TJS', 'TJS (Somoni)'), ('TMT', 'TMT (Turkmenistan New Manat)'), ('TND', 'TND (Tunisian Dinar)'), ('TOP', 'TOP (Pa\u2019anga)'), ('TRY', 'TRY (Turkish Lira)'), ('TTD', 'TTD (Trinidad and Tobago Dollar)'), ('TWD', 'TWD (New Taiwan Dollar)'), ('TZS', 'TZS (Tanzanian Shilling)'), ('UAH', 'UAH (Hryvnia)'), ('UGX', 'UGX (Uganda Shilling)'), ('USD', 'USD (US Dollar)'), ('UYU', 'UYU (Peso Uruguayo)'), ('UZS', 'UZS (Uzbekistan Sum)'), ('VEF', 'VEF (Bol\xedvar)'), ('VND', 'VND (Dong)'), ('VUV', 'VUV (Vatu)'), ('WST', 'WST (Tala)'), ('XAF', 'XAF (CFA Franc BEAC)'), ('XAG', 'XAG (Silver)'), ('XAU', 'XAU (Gold)'), ('XBA', 'XBA (Bond Markets Unit European Composite Unit (EURCO))'), ('XBB', 'XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))'), ('XBC', 'XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))'), ('XBD', 'XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))'), ('XCD', 'XCD (East Caribbean Dollar)'), ('XDR', 'XDR (SDR (Special Drawing Right))'), ('XOF', 'XOF (CFA Franc BCEAO)'), ('XPD', 'XPD (Palladium)'), ('XPF', 'XPF (CFP Franc)'), ('XPT', 'XPT (Platinum)'), ('XSU', 'XSU (Sucre)'), ('XTS', 'XTS (Codes specifically reserved for testing purposes)'), ('XUA', 'XUA (ADB Unit of Account)'), ('XXX', 'XXX (The codes assigned for transactions where no currency is involved)'), ('YER', 'YER (Yemeni Rial)'), ('ZAR', 'ZAR (Rand)'), ('ZMW', 'ZMW (Zambian Kwacha)'), ('ZWL', 'ZWL (Zimbabwe Dollar)')])),
                ('transaction_currency', models.CharField(help_text=b'The currency used when making a transaction.', max_length=4, choices=[('AED', 'AED (UAE Dirham)'), ('AFN', 'AFN (Afghani)'), ('ALL', 'ALL (Lek)'), ('AMD', 'AMD (Armenian Dram)'), ('ANG', 'ANG (Netherlands Antillean Guilder)'), ('AOA', 'AOA (Kwanza)'), ('ARS', 'ARS (Argentine Peso)'), ('AUD', 'AUD (Australian Dollar)'), ('AWG', 'AWG (Aruban Florin)'), ('AZN', 'AZN (Azerbaijanian Manat)'), ('BAM', 'BAM (Convertible Mark)'), ('BBD', 'BBD (Barbados Dollar)'), ('BDT', 'BDT (Taka)'), ('BGN', 'BGN (Bulgarian Lev)'), ('BHD', 'BHD (Bahraini Dinar)'), ('BIF', 'BIF (Burundi Franc)'), ('BMD', 'BMD (Bermudian Dollar)'), ('BND', 'BND (Brunei Dollar)'), ('BOB', 'BOB (Boliviano)'), ('BRL', 'BRL (Brazilian Real)'), ('BSD', 'BSD (Bahamian Dollar)'), ('BTN', 'BTN (Ngultrum)'), ('BWP', 'BWP (Pula)'), ('BYR', 'BYR (Belarusian Ruble)'), ('BZD', 'BZD (Belize Dollar)'), ('CAD', 'CAD (Canadian Dollar)'), ('CDF', 'CDF (Congolese Franc)'), ('CHF', 'CHF (Swiss Franc)'), ('CLP', 'CLP (Chilean Peso)'), ('CNY', 'CNY (Yuan Renminbi)'), ('COP', 'COP (Colombian Peso)'), ('CRC', 'CRC (Costa Rican Colon)'), ('CUC', 'CUC (Peso Convertible)'), ('CUP', 'CUP (Cuban Peso)'), ('CVE', 'CVE (Cabo Verde Escudo)'), ('CZK', 'CZK (Czech Koruna)'), ('DJF', 'DJF (Djibouti Franc)'), ('DKK', 'DKK (Danish Krone)'), ('DOP', 'DOP (Dominican Peso)'), ('DZD', 'DZD (Algerian Dinar)'), ('EGP', 'EGP (Egyptian Pound)'), ('ERN', 'ERN (Nakfa)'), ('ETB', 'ETB (Ethiopian Birr)'), ('EUR', 'EUR (Euro)'), ('FJD', 'FJD (Fiji Dollar)'), ('FKP', 'FKP (Falkland Islands Pound)'), ('GBP', 'GBP (Pound Sterling)'), ('GEL', 'GEL (Lari)'), ('GHS', 'GHS (Ghana Cedi)'), ('GIP', 'GIP (Gibraltar Pound)'), ('GMD', 'GMD (Dalasi)'), ('GNF', 'GNF (Guinea Franc)'), ('GTQ', 'GTQ (Quetzal)'), ('GYD', 'GYD (Guyana Dollar)'), ('HKD', 'HKD (Hong Kong Dollar)'), ('HNL', 'HNL (Lempira)'), ('HRK', 'HRK (Kuna)'), ('HTG', 'HTG (Gourde)'), ('HUF', 'HUF (Forint)'), ('IDR', 'IDR (Rupiah)'), ('ILS', 'ILS (New Israeli Sheqel)'), ('INR', 'INR (Indian Rupee)'), ('IQD', 'IQD (Iraqi Dinar)'), ('IRR', 'IRR (Iranian Rial)'), ('ISK', 'ISK (Iceland Krona)'), ('JMD', 'JMD (Jamaican Dollar)'), ('JOD', 'JOD (Jordanian Dinar)'), ('JPY', 'JPY (Yen)'), ('KES', 'KES (Kenyan Shilling)'), ('KGS', 'KGS (Som)'), ('KHR', 'KHR (Riel)'), ('KMF', 'KMF (Comoro Franc)'), ('KPW', 'KPW (North Korean Won)'), ('KRW', 'KRW (Won)'), ('KWD', 'KWD (Kuwaiti Dinar)'), ('KYD', 'KYD (Cayman Islands Dollar)'), ('KZT', 'KZT (Tenge)'), ('LAK', 'LAK (Kip)'), ('LBP', 'LBP (Lebanese Pound)'), ('LKR', 'LKR (Sri Lanka Rupee)'), ('LRD', 'LRD (Liberian Dollar)'), ('LSL', 'LSL (Loti)'), ('LYD', 'LYD (Libyan Dinar)'), ('MAD', 'MAD (Moroccan Dirham)'), ('MDL', 'MDL (Moldovan Leu)'), ('MGA', 'MGA (Malagasy Ariary)'), ('MKD', 'MKD (Denar)'), ('MMK', 'MMK (Kyat)'), ('MNT', 'MNT (Tugrik)'), ('MOP', 'MOP (Pataca)'), ('MRO', 'MRO (Ouguiya)'), ('MUR', 'MUR (Mauritius Rupee)'), ('MVR', 'MVR (Rufiyaa)'), ('MWK', 'MWK (Malawi Kwacha)'), ('MXN', 'MXN (Mexican Peso)'), ('MYR', 'MYR (Malaysian Ringgit)'), ('MZN', 'MZN (Mozambique Metical)'), ('NAD', 'NAD (Namibia Dollar)'), ('NGN', 'NGN (Naira)'), ('NIO', 'NIO (Cordoba Oro)'), ('NOK', 'NOK (Norwegian Krone)'), ('NPR', 'NPR (Nepalese Rupee)'), ('NZD', 'NZD (New Zealand Dollar)'), ('OMR', 'OMR (Rial Omani)'), ('PAB', 'PAB (Balboa)'), ('PEN', 'PEN (Sol)'), ('PGK', 'PGK (Kina)'), ('PHP', 'PHP (Philippine Peso)'), ('PKR', 'PKR (Pakistan Rupee)'), ('PLN', 'PLN (Zloty)'), ('PYG', 'PYG (Guarani)'), ('QAR', 'QAR (Qatari Rial)'), ('RON', 'RON (Romanian Leu)'), ('RSD', 'RSD (Serbian Dinar)'), ('RUB', 'RUB (Russian Ruble)'), ('RWF', 'RWF (Rwanda Franc)'), ('SAR', 'SAR (Saudi Riyal)'), ('SBD', 'SBD (Solomon Islands Dollar)'), ('SCR', 'SCR (Seychelles Rupee)'), ('SDG', 'SDG (Sudanese Pound)'), ('SEK', 'SEK (Swedish Krona)'), ('SGD', 'SGD (Singapore Dollar)'), ('SHP', 'SHP (Saint Helena Pound)'), ('SLL', 'SLL (Leone)'), ('SOS', 'SOS (Somali Shilling)'), ('SRD', 'SRD (Surinam Dollar)'), ('SSP', 'SSP (South Sudanese Pound)'), ('STD', 'STD (Dobra)'), ('SVC', 'SVC (El Salvador Colon)'), ('SYP', 'SYP (Syrian Pound)'), ('SZL', 'SZL (Lilangeni)'), ('THB', 'THB (Baht)'), ('TJS', 'TJS (Somoni)'), ('TMT', 'TMT (Turkmenistan New Manat)'), ('TND', 'TND (Tunisian Dinar)'), ('TOP', 'TOP (Pa\u2019anga)'), ('TRY', 'TRY (Turkish Lira)'), ('TTD', 'TTD (Trinidad and Tobago Dollar)'), ('TWD', 'TWD (New Taiwan Dollar)'), ('TZS', 'TZS (Tanzanian Shilling)'), ('UAH', 'UAH (Hryvnia)'), ('UGX', 'UGX (Uganda Shilling)'), ('USD', 'USD (US Dollar)'), ('UYU', 'UYU (Peso Uruguayo)'), ('UZS', 'UZS (Uzbekistan Sum)'), ('VEF', 'VEF (Bol\xedvar)'), ('VND', 'VND (Dong)'), ('VUV', 'VUV (Vatu)'), ('WST', 'WST (Tala)'), ('XAF', 'XAF (CFA Franc BEAC)'), ('XAG', 'XAG (Silver)'), ('XAU', 'XAU (Gold)'), ('XBA', 'XBA (Bond Markets Unit European Composite Unit (EURCO))'), ('XBB', 'XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))'), ('XBC', 'XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))'), ('XBD', 'XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))'), ('XCD', 'XCD (East Caribbean Dollar)'), ('XDR', 'XDR (SDR (Special Drawing Right))'), ('XOF', 'XOF (CFA Franc BCEAO)'), ('XPD', 'XPD (Palladium)'), ('XPF', 'XPF (CFP Franc)'), ('XPT', 'XPT (Platinum)'), ('XSU', 'XSU (Sucre)'), ('XTS', 'XTS (Codes specifically reserved for testing purposes)'), ('XUA', 'XUA (ADB Unit of Account)'), ('XXX', 'XXX (The codes assigned for transactions where no currency is involved)'), ('YER', 'YER (Yemeni Rial)'), ('ZAR', 'ZAR (Rand)'), ('ZMW', 'ZMW (Zambian Kwacha)'), ('ZWL', 'ZWL (Zimbabwe Dollar)')])),
                ('transaction_xe_rate', models.DecimalField(help_text=b'Currency exchange rate from document currency to transaction_currency.', null=True, max_digits=16, decimal_places=4, blank=True)),
                ('transaction_xe_date', models.DateField(help_text=b'Date of the transaction exchange rate.', null=True, blank=True)),
                ('state', django_fsm.FSMField(default=b'draft', help_text=b'The state the invoice is in.', max_length=10, verbose_name=b'State', choices=[(b'draft', 'Draft'), (b'issued', 'Issued'), (b'paid', 'Paid'), (b'canceled', 'Canceled')])),
                ('_total', models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True)),
                ('_total_in_transaction_currency', models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True)),
            ],
            options={
                'ordering': ('-issue_date', 'series', '-number'),
            },
        ),
        migrations.CreateModel(
            name='BillingLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billing_date', models.DateField(help_text=b'The date when the invoice/proforma was issued.')),
                ('plan_billed_up_to', models.DateField(help_text=b'The date up to which the plan base amount has been billed.')),
                ('metered_features_billed_up_to', models.DateField(help_text=b'The date up to which the metered features have been billed.')),
                ('total', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(related_name='invoice_billing_logs', blank=True, to='silver.BillingDocumentBase', null=True)),
                ('proforma', models.ForeignKey(related_name='proforma_billing_logs', blank=True, to='silver.BillingDocumentBase', null=True)),
            ],
            options={
                'ordering': ['-billing_date'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('company', models.CharField(max_length=128, null=True, blank=True)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, null=True, blank=True)),
                ('country', models.CharField(max_length=3, choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua and Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AX', '\xc5land Islands'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BL', 'Saint Barth\xe9lemy'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia, Plurinational State of'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CD', 'Congo, The Democratic Republic of the'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', "C\xf4te d'Ivoire"), ('CK', 'Cook Islands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cabo Verde'), ('CW', 'Cura\xe7ao'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia, Federated States of'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GA', 'Gabon'), ('GB', 'United Kingdom'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran, Islamic Republic of'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'Saint Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('ME', 'Montenegro'), ('MF', 'Saint Martin (French part)'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia, Republic of'), ('ML', 'Mali'), ('MM', 'Myanmar'), ('MN', 'Mongolia'), ('MO', 'Macao'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'Saint Pierre and Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PS', 'Palestine, State of'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'R\xe9union'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SI', 'Slovenia'), ('SJ', 'Svalbard and Jan Mayen'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SV', 'El Salvador'), ('SX', 'Sint Maarten (Dutch part)'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TR', 'Turkey'), ('TT', 'Trinidad and Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')])),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.CharField(max_length=254, null=True, blank=True)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=32, null=True, blank=True)),
                ('extra', models.TextField(help_text=b'Extra information to display on the invoice (markdown formatted).', null=True, blank=True)),
                ('meta', annoying.fields.JSONField(default={}, null=True, blank=True)),
                ('first_name', models.CharField(help_text=b"The customer's first name.", max_length=128)),
                ('last_name', models.CharField(help_text=b"The customer's last name.", max_length=128)),
                ('payment_due_days', models.PositiveIntegerField(default=5, help_text=b'Due days for generated proforma/invoice.')),
                ('consolidated_billing', models.BooleanField(default=False, help_text=b'A flag indicating consolidated billing.')),
                ('customer_reference', models.CharField(blank=True, max_length=256, null=True, help_text=b"It's a reference to be passed between silver and clients. It usually points to an account ID.", validators=[django.core.validators.RegexValidator(regex=b'^[^,]*$', message='Reference must not contain commas.')])),
                ('sales_tax_number', models.CharField(max_length=64, null=True, blank=True)),
                ('sales_tax_percent', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)], max_digits=4, blank=True, help_text=b"Whenever to add sales tax. If null, it won't show up on the invoice.", null=True)),
                ('sales_tax_name', models.CharField(help_text=b"Sales tax name (eg. 'sales tax' or 'VAT').", max_length=64, null=True, blank=True)),
                ('currency', models.CharField(blank=True, max_length=4, null=True, help_text=b'Used to enforce a certain currency when making transactionsfor the customer.', choices=[('AED', 'AED (UAE Dirham)'), ('AFN', 'AFN (Afghani)'), ('ALL', 'ALL (Lek)'), ('AMD', 'AMD (Armenian Dram)'), ('ANG', 'ANG (Netherlands Antillean Guilder)'), ('AOA', 'AOA (Kwanza)'), ('ARS', 'ARS (Argentine Peso)'), ('AUD', 'AUD (Australian Dollar)'), ('AWG', 'AWG (Aruban Florin)'), ('AZN', 'AZN (Azerbaijanian Manat)'), ('BAM', 'BAM (Convertible Mark)'), ('BBD', 'BBD (Barbados Dollar)'), ('BDT', 'BDT (Taka)'), ('BGN', 'BGN (Bulgarian Lev)'), ('BHD', 'BHD (Bahraini Dinar)'), ('BIF', 'BIF (Burundi Franc)'), ('BMD', 'BMD (Bermudian Dollar)'), ('BND', 'BND (Brunei Dollar)'), ('BOB', 'BOB (Boliviano)'), ('BRL', 'BRL (Brazilian Real)'), ('BSD', 'BSD (Bahamian Dollar)'), ('BTN', 'BTN (Ngultrum)'), ('BWP', 'BWP (Pula)'), ('BYR', 'BYR (Belarusian Ruble)'), ('BZD', 'BZD (Belize Dollar)'), ('CAD', 'CAD (Canadian Dollar)'), ('CDF', 'CDF (Congolese Franc)'), ('CHF', 'CHF (Swiss Franc)'), ('CLP', 'CLP (Chilean Peso)'), ('CNY', 'CNY (Yuan Renminbi)'), ('COP', 'COP (Colombian Peso)'), ('CRC', 'CRC (Costa Rican Colon)'), ('CUC', 'CUC (Peso Convertible)'), ('CUP', 'CUP (Cuban Peso)'), ('CVE', 'CVE (Cabo Verde Escudo)'), ('CZK', 'CZK (Czech Koruna)'), ('DJF', 'DJF (Djibouti Franc)'), ('DKK', 'DKK (Danish Krone)'), ('DOP', 'DOP (Dominican Peso)'), ('DZD', 'DZD (Algerian Dinar)'), ('EGP', 'EGP (Egyptian Pound)'), ('ERN', 'ERN (Nakfa)'), ('ETB', 'ETB (Ethiopian Birr)'), ('EUR', 'EUR (Euro)'), ('FJD', 'FJD (Fiji Dollar)'), ('FKP', 'FKP (Falkland Islands Pound)'), ('GBP', 'GBP (Pound Sterling)'), ('GEL', 'GEL (Lari)'), ('GHS', 'GHS (Ghana Cedi)'), ('GIP', 'GIP (Gibraltar Pound)'), ('GMD', 'GMD (Dalasi)'), ('GNF', 'GNF (Guinea Franc)'), ('GTQ', 'GTQ (Quetzal)'), ('GYD', 'GYD (Guyana Dollar)'), ('HKD', 'HKD (Hong Kong Dollar)'), ('HNL', 'HNL (Lempira)'), ('HRK', 'HRK (Kuna)'), ('HTG', 'HTG (Gourde)'), ('HUF', 'HUF (Forint)'), ('IDR', 'IDR (Rupiah)'), ('ILS', 'ILS (New Israeli Sheqel)'), ('INR', 'INR (Indian Rupee)'), ('IQD', 'IQD (Iraqi Dinar)'), ('IRR', 'IRR (Iranian Rial)'), ('ISK', 'ISK (Iceland Krona)'), ('JMD', 'JMD (Jamaican Dollar)'), ('JOD', 'JOD (Jordanian Dinar)'), ('JPY', 'JPY (Yen)'), ('KES', 'KES (Kenyan Shilling)'), ('KGS', 'KGS (Som)'), ('KHR', 'KHR (Riel)'), ('KMF', 'KMF (Comoro Franc)'), ('KPW', 'KPW (North Korean Won)'), ('KRW', 'KRW (Won)'), ('KWD', 'KWD (Kuwaiti Dinar)'), ('KYD', 'KYD (Cayman Islands Dollar)'), ('KZT', 'KZT (Tenge)'), ('LAK', 'LAK (Kip)'), ('LBP', 'LBP (Lebanese Pound)'), ('LKR', 'LKR (Sri Lanka Rupee)'), ('LRD', 'LRD (Liberian Dollar)'), ('LSL', 'LSL (Loti)'), ('LYD', 'LYD (Libyan Dinar)'), ('MAD', 'MAD (Moroccan Dirham)'), ('MDL', 'MDL (Moldovan Leu)'), ('MGA', 'MGA (Malagasy Ariary)'), ('MKD', 'MKD (Denar)'), ('MMK', 'MMK (Kyat)'), ('MNT', 'MNT (Tugrik)'), ('MOP', 'MOP (Pataca)'), ('MRO', 'MRO (Ouguiya)'), ('MUR', 'MUR (Mauritius Rupee)'), ('MVR', 'MVR (Rufiyaa)'), ('MWK', 'MWK (Malawi Kwacha)'), ('MXN', 'MXN (Mexican Peso)'), ('MYR', 'MYR (Malaysian Ringgit)'), ('MZN', 'MZN (Mozambique Metical)'), ('NAD', 'NAD (Namibia Dollar)'), ('NGN', 'NGN (Naira)'), ('NIO', 'NIO (Cordoba Oro)'), ('NOK', 'NOK (Norwegian Krone)'), ('NPR', 'NPR (Nepalese Rupee)'), ('NZD', 'NZD (New Zealand Dollar)'), ('OMR', 'OMR (Rial Omani)'), ('PAB', 'PAB (Balboa)'), ('PEN', 'PEN (Sol)'), ('PGK', 'PGK (Kina)'), ('PHP', 'PHP (Philippine Peso)'), ('PKR', 'PKR (Pakistan Rupee)'), ('PLN', 'PLN (Zloty)'), ('PYG', 'PYG (Guarani)'), ('QAR', 'QAR (Qatari Rial)'), ('RON', 'RON (Romanian Leu)'), ('RSD', 'RSD (Serbian Dinar)'), ('RUB', 'RUB (Russian Ruble)'), ('RWF', 'RWF (Rwanda Franc)'), ('SAR', 'SAR (Saudi Riyal)'), ('SBD', 'SBD (Solomon Islands Dollar)'), ('SCR', 'SCR (Seychelles Rupee)'), ('SDG', 'SDG (Sudanese Pound)'), ('SEK', 'SEK (Swedish Krona)'), ('SGD', 'SGD (Singapore Dollar)'), ('SHP', 'SHP (Saint Helena Pound)'), ('SLL', 'SLL (Leone)'), ('SOS', 'SOS (Somali Shilling)'), ('SRD', 'SRD (Surinam Dollar)'), ('SSP', 'SSP (South Sudanese Pound)'), ('STD', 'STD (Dobra)'), ('SVC', 'SVC (El Salvador Colon)'), ('SYP', 'SYP (Syrian Pound)'), ('SZL', 'SZL (Lilangeni)'), ('THB', 'THB (Baht)'), ('TJS', 'TJS (Somoni)'), ('TMT', 'TMT (Turkmenistan New Manat)'), ('TND', 'TND (Tunisian Dinar)'), ('TOP', 'TOP (Pa\u2019anga)'), ('TRY', 'TRY (Turkish Lira)'), ('TTD', 'TTD (Trinidad and Tobago Dollar)'), ('TWD', 'TWD (New Taiwan Dollar)'), ('TZS', 'TZS (Tanzanian Shilling)'), ('UAH', 'UAH (Hryvnia)'), ('UGX', 'UGX (Uganda Shilling)'), ('USD', 'USD (US Dollar)'), ('UYU', 'UYU (Peso Uruguayo)'), ('UZS', 'UZS (Uzbekistan Sum)'), ('VEF', 'VEF (Bol\xedvar)'), ('VND', 'VND (Dong)'), ('VUV', 'VUV (Vatu)'), ('WST', 'WST (Tala)'), ('XAF', 'XAF (CFA Franc BEAC)'), ('XAG', 'XAG (Silver)'), ('XAU', 'XAU (Gold)'), ('XBA', 'XBA (Bond Markets Unit European Composite Unit (EURCO))'), ('XBB', 'XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))'), ('XBC', 'XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))'), ('XBD', 'XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))'), ('XCD', 'XCD (East Caribbean Dollar)'), ('XDR', 'XDR (SDR (Special Drawing Right))'), ('XOF', 'XOF (CFA Franc BCEAO)'), ('XPD', 'XPD (Palladium)'), ('XPF', 'XPF (CFP Franc)'), ('XPT', 'XPT (Platinum)'), ('XSU', 'XSU (Sucre)'), ('XTS', 'XTS (Codes specifically reserved for testing purposes)'), ('XUA', 'XUA (ADB Unit of Account)'), ('XXX', 'XXX (The codes assigned for transactions where no currency is involved)'), ('YER', 'YER (Yemeni Rial)'), ('ZAR', 'ZAR (Rand)'), ('ZMW', 'ZMW (Zambian Kwacha)'), ('ZWL', 'ZWL (Zimbabwe Dollar)')])),
            ],
            options={
                'ordering': ['first_name', 'last_name', 'company'],
            },
        ),
        migrations.CreateModel(
            name='DocumentEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
                ('unit', models.CharField(max_length=1024, null=True, blank=True)),
                ('quantity', models.DecimalField(max_digits=19, decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('unit_price', models.DecimalField(max_digits=19, decimal_places=4)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('prorated', models.BooleanField(default=False)),
                ('invoice', models.ForeignKey(related_name='invoice_entries', blank=True, to='silver.BillingDocumentBase', null=True)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='MeteredFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The feature display name.', max_length=200, db_index=True)),
                ('unit', models.CharField(max_length=20)),
                ('price_per_unit', models.DecimalField(help_text=b'The price per unit.', max_digits=19, decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('included_units', models.DecimalField(help_text=b'The number of included units per plan interval.', max_digits=19, decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('included_units_during_trial', models.DecimalField(decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)], max_digits=19, blank=True, help_text=b'The number of included units during the trial period.', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MeteredFeatureUnitsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consumed_units', models.DecimalField(max_digits=19, decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('start_date', models.DateField(editable=False)),
                ('end_date', models.DateField(editable=False)),
                ('metered_feature', models.ForeignKey(related_name='consumed', to='silver.MeteredFeature')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_processor', models.CharField(max_length=256, choices=[(b'manual', b'manual'), (b'failing_void', b'failing_void'), (b'triggered', b'triggered')])),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', annoying.fields.JSONField(default={}, null=True, blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('valid_until', models.DateTimeField(null=True, blank=True)),
                ('display_info', models.CharField(max_length=256, null=True, blank=True)),
                ('customer', models.ForeignKey(to='silver.Customer')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('pdf_file', models.FileField(upload_to=silver.models.documents.pdf.get_upload_path, null=True, editable=False, blank=True)),
                ('dirty', models.PositiveIntegerField(default=0)),
                ('upload_path', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Display name of the plan.', max_length=200, db_index=True)),
                ('interval', models.CharField(default=b'month', help_text=b'The frequency with which a subscription should be billed.', max_length=12, choices=[(b'day', 'Day'), (b'week', 'Week'), (b'month', 'Month'), (b'year', 'Year')])),
                ('interval_count', models.PositiveIntegerField(help_text=b'The number of intervals between each subscription billing')),
                ('amount', models.DecimalField(help_text=b'The amount in the specified currency to be charged on the interval specified.', max_digits=19, decimal_places=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('currency', models.CharField(default=b'USD', help_text=b'The currency in which the subscription will be charged.', max_length=4, choices=[('AED', 'AED (UAE Dirham)'), ('AFN', 'AFN (Afghani)'), ('ALL', 'ALL (Lek)'), ('AMD', 'AMD (Armenian Dram)'), ('ANG', 'ANG (Netherlands Antillean Guilder)'), ('AOA', 'AOA (Kwanza)'), ('ARS', 'ARS (Argentine Peso)'), ('AUD', 'AUD (Australian Dollar)'), ('AWG', 'AWG (Aruban Florin)'), ('AZN', 'AZN (Azerbaijanian Manat)'), ('BAM', 'BAM (Convertible Mark)'), ('BBD', 'BBD (Barbados Dollar)'), ('BDT', 'BDT (Taka)'), ('BGN', 'BGN (Bulgarian Lev)'), ('BHD', 'BHD (Bahraini Dinar)'), ('BIF', 'BIF (Burundi Franc)'), ('BMD', 'BMD (Bermudian Dollar)'), ('BND', 'BND (Brunei Dollar)'), ('BOB', 'BOB (Boliviano)'), ('BRL', 'BRL (Brazilian Real)'), ('BSD', 'BSD (Bahamian Dollar)'), ('BTN', 'BTN (Ngultrum)'), ('BWP', 'BWP (Pula)'), ('BYR', 'BYR (Belarusian Ruble)'), ('BZD', 'BZD (Belize Dollar)'), ('CAD', 'CAD (Canadian Dollar)'), ('CDF', 'CDF (Congolese Franc)'), ('CHF', 'CHF (Swiss Franc)'), ('CLP', 'CLP (Chilean Peso)'), ('CNY', 'CNY (Yuan Renminbi)'), ('COP', 'COP (Colombian Peso)'), ('CRC', 'CRC (Costa Rican Colon)'), ('CUC', 'CUC (Peso Convertible)'), ('CUP', 'CUP (Cuban Peso)'), ('CVE', 'CVE (Cabo Verde Escudo)'), ('CZK', 'CZK (Czech Koruna)'), ('DJF', 'DJF (Djibouti Franc)'), ('DKK', 'DKK (Danish Krone)'), ('DOP', 'DOP (Dominican Peso)'), ('DZD', 'DZD (Algerian Dinar)'), ('EGP', 'EGP (Egyptian Pound)'), ('ERN', 'ERN (Nakfa)'), ('ETB', 'ETB (Ethiopian Birr)'), ('EUR', 'EUR (Euro)'), ('FJD', 'FJD (Fiji Dollar)'), ('FKP', 'FKP (Falkland Islands Pound)'), ('GBP', 'GBP (Pound Sterling)'), ('GEL', 'GEL (Lari)'), ('GHS', 'GHS (Ghana Cedi)'), ('GIP', 'GIP (Gibraltar Pound)'), ('GMD', 'GMD (Dalasi)'), ('GNF', 'GNF (Guinea Franc)'), ('GTQ', 'GTQ (Quetzal)'), ('GYD', 'GYD (Guyana Dollar)'), ('HKD', 'HKD (Hong Kong Dollar)'), ('HNL', 'HNL (Lempira)'), ('HRK', 'HRK (Kuna)'), ('HTG', 'HTG (Gourde)'), ('HUF', 'HUF (Forint)'), ('IDR', 'IDR (Rupiah)'), ('ILS', 'ILS (New Israeli Sheqel)'), ('INR', 'INR (Indian Rupee)'), ('IQD', 'IQD (Iraqi Dinar)'), ('IRR', 'IRR (Iranian Rial)'), ('ISK', 'ISK (Iceland Krona)'), ('JMD', 'JMD (Jamaican Dollar)'), ('JOD', 'JOD (Jordanian Dinar)'), ('JPY', 'JPY (Yen)'), ('KES', 'KES (Kenyan Shilling)'), ('KGS', 'KGS (Som)'), ('KHR', 'KHR (Riel)'), ('KMF', 'KMF (Comoro Franc)'), ('KPW', 'KPW (North Korean Won)'), ('KRW', 'KRW (Won)'), ('KWD', 'KWD (Kuwaiti Dinar)'), ('KYD', 'KYD (Cayman Islands Dollar)'), ('KZT', 'KZT (Tenge)'), ('LAK', 'LAK (Kip)'), ('LBP', 'LBP (Lebanese Pound)'), ('LKR', 'LKR (Sri Lanka Rupee)'), ('LRD', 'LRD (Liberian Dollar)'), ('LSL', 'LSL (Loti)'), ('LYD', 'LYD (Libyan Dinar)'), ('MAD', 'MAD (Moroccan Dirham)'), ('MDL', 'MDL (Moldovan Leu)'), ('MGA', 'MGA (Malagasy Ariary)'), ('MKD', 'MKD (Denar)'), ('MMK', 'MMK (Kyat)'), ('MNT', 'MNT (Tugrik)'), ('MOP', 'MOP (Pataca)'), ('MRO', 'MRO (Ouguiya)'), ('MUR', 'MUR (Mauritius Rupee)'), ('MVR', 'MVR (Rufiyaa)'), ('MWK', 'MWK (Malawi Kwacha)'), ('MXN', 'MXN (Mexican Peso)'), ('MYR', 'MYR (Malaysian Ringgit)'), ('MZN', 'MZN (Mozambique Metical)'), ('NAD', 'NAD (Namibia Dollar)'), ('NGN', 'NGN (Naira)'), ('NIO', 'NIO (Cordoba Oro)'), ('NOK', 'NOK (Norwegian Krone)'), ('NPR', 'NPR (Nepalese Rupee)'), ('NZD', 'NZD (New Zealand Dollar)'), ('OMR', 'OMR (Rial Omani)'), ('PAB', 'PAB (Balboa)'), ('PEN', 'PEN (Sol)'), ('PGK', 'PGK (Kina)'), ('PHP', 'PHP (Philippine Peso)'), ('PKR', 'PKR (Pakistan Rupee)'), ('PLN', 'PLN (Zloty)'), ('PYG', 'PYG (Guarani)'), ('QAR', 'QAR (Qatari Rial)'), ('RON', 'RON (Romanian Leu)'), ('RSD', 'RSD (Serbian Dinar)'), ('RUB', 'RUB (Russian Ruble)'), ('RWF', 'RWF (Rwanda Franc)'), ('SAR', 'SAR (Saudi Riyal)'), ('SBD', 'SBD (Solomon Islands Dollar)'), ('SCR', 'SCR (Seychelles Rupee)'), ('SDG', 'SDG (Sudanese Pound)'), ('SEK', 'SEK (Swedish Krona)'), ('SGD', 'SGD (Singapore Dollar)'), ('SHP', 'SHP (Saint Helena Pound)'), ('SLL', 'SLL (Leone)'), ('SOS', 'SOS (Somali Shilling)'), ('SRD', 'SRD (Surinam Dollar)'), ('SSP', 'SSP (South Sudanese Pound)'), ('STD', 'STD (Dobra)'), ('SVC', 'SVC (El Salvador Colon)'), ('SYP', 'SYP (Syrian Pound)'), ('SZL', 'SZL (Lilangeni)'), ('THB', 'THB (Baht)'), ('TJS', 'TJS (Somoni)'), ('TMT', 'TMT (Turkmenistan New Manat)'), ('TND', 'TND (Tunisian Dinar)'), ('TOP', 'TOP (Pa\u2019anga)'), ('TRY', 'TRY (Turkish Lira)'), ('TTD', 'TTD (Trinidad and Tobago Dollar)'), ('TWD', 'TWD (New Taiwan Dollar)'), ('TZS', 'TZS (Tanzanian Shilling)'), ('UAH', 'UAH (Hryvnia)'), ('UGX', 'UGX (Uganda Shilling)'), ('USD', 'USD (US Dollar)'), ('UYU', 'UYU (Peso Uruguayo)'), ('UZS', 'UZS (Uzbekistan Sum)'), ('VEF', 'VEF (Bol\xedvar)'), ('VND', 'VND (Dong)'), ('VUV', 'VUV (Vatu)'), ('WST', 'WST (Tala)'), ('XAF', 'XAF (CFA Franc BEAC)'), ('XAG', 'XAG (Silver)'), ('XAU', 'XAU (Gold)'), ('XBA', 'XBA (Bond Markets Unit European Composite Unit (EURCO))'), ('XBB', 'XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))'), ('XBC', 'XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))'), ('XBD', 'XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))'), ('XCD', 'XCD (East Caribbean Dollar)'), ('XDR', 'XDR (SDR (Special Drawing Right))'), ('XOF', 'XOF (CFA Franc BCEAO)'), ('XPD', 'XPD (Palladium)'), ('XPF', 'XPF (CFP Franc)'), ('XPT', 'XPT (Platinum)'), ('XSU', 'XSU (Sucre)'), ('XTS', 'XTS (Codes specifically reserved for testing purposes)'), ('XUA', 'XUA (ADB Unit of Account)'), ('XXX', 'XXX (The codes assigned for transactions where no currency is involved)'), ('YER', 'YER (Yemeni Rial)'), ('ZAR', 'ZAR (Rand)'), ('ZMW', 'ZMW (Zambian Kwacha)'), ('ZWL', 'ZWL (Zimbabwe Dollar)')])),
                ('trial_period_days', models.PositiveIntegerField(help_text=b'Number of trial period days granted when subscribing a customer to this plan.', null=True, verbose_name=b'Trial days', blank=True)),
                ('generate_documents_on_trial_end', models.NullBooleanField(help_text=b'If this is set to True, then billing documents will be generated when the subscription trial ends, instead of waiting for the end of the billing cycle.')),
                ('separate_cycles_during_trial', models.NullBooleanField(help_text=b'If this is set to True, then the trial period cycle will be split if it spans across multiple billing intervals.')),
                ('prebill_plan', models.NullBooleanField(help_text=b'If this is set to True, then the plan base amount will be billed at thebeginning of the billing cycle rather than after the end.')),
                ('generate_after', models.PositiveIntegerField(default=0, help_text=b'Number of seconds to wait after current billing cycle ends before generating the invoice. This can be used to allow systems to finish updating feature counters.')),
                ('cycle_billing_duration', models.DurationField(help_text=b"This can be used to ensure that the billing date doesn't pass a certain date.\nFor example if this field is set to 2 days, for a monthly subscription, the billing date will never surpass the 2nd day of the month. Billing documents can still be generated after that day during the billing cycle, but their billing date will appear to be the end of the cycle billing duration.", null=True, blank=True)),
                ('enabled', models.BooleanField(default=True, help_text=b'Whether to accept subscriptions.')),
                ('private', models.BooleanField(default=False, help_text=b'Indicates if a plan is private.')),
                ('metered_features', models.ManyToManyField(help_text=b"A list of the plan's metered features.", to='silver.MeteredFeature', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('company', models.CharField(max_length=128, null=True, blank=True)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, null=True, blank=True)),
                ('country', models.CharField(max_length=3, choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua and Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AX', '\xc5land Islands'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BL', 'Saint Barth\xe9lemy'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia, Plurinational State of'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CD', 'Congo, The Democratic Republic of the'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', "C\xf4te d'Ivoire"), ('CK', 'Cook Islands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cabo Verde'), ('CW', 'Cura\xe7ao'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia, Federated States of'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GA', 'Gabon'), ('GB', 'United Kingdom'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran, Islamic Republic of'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'Saint Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('ME', 'Montenegro'), ('MF', 'Saint Martin (French part)'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia, Republic of'), ('ML', 'Mali'), ('MM', 'Myanmar'), ('MN', 'Mongolia'), ('MO', 'Macao'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'Saint Pierre and Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PS', 'Palestine, State of'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'R\xe9union'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SI', 'Slovenia'), ('SJ', 'Svalbard and Jan Mayen'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SV', 'El Salvador'), ('SX', 'Sint Maarten (Dutch part)'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TR', 'Turkey'), ('TT', 'Trinidad and Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')])),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.CharField(max_length=254, null=True, blank=True)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=32, null=True, blank=True)),
                ('extra', models.TextField(help_text=b'Extra information to display on the invoice (markdown formatted).', null=True, blank=True)),
                ('meta', annoying.fields.JSONField(default={}, null=True, blank=True)),
                ('name', models.CharField(help_text=b'The name to be used for billing purposes.', max_length=128)),
                ('flow', models.CharField(default=b'proforma', help_text=b'One of the available workflows for generating proformas and invoices (see the documentation for more details).', max_length=10, choices=[(b'proforma', 'Proforma'), (b'invoice', 'Invoice')])),
                ('invoice_series', models.CharField(help_text=b'The series that will be used on every invoice generated by this provider.', max_length=20)),
                ('invoice_starting_number', models.PositiveIntegerField()),
                ('proforma_series', models.CharField(help_text=b'The series that will be used on every proforma generated by this provider.', max_length=20, null=True, blank=True)),
                ('proforma_starting_number', models.PositiveIntegerField(null=True, blank=True)),
                ('default_document_state', models.CharField(default=b'draft', help_text=b'The default state of the auto-generated documents.', max_length=10, choices=[(b'draft', 'Draft'), (b'issued', 'Issued')])),
                ('generate_documents_on_trial_end', models.BooleanField(default=True, help_text=b'If this is set to True, then billing documents will be generated when the subscription trial ends, instead of waiting for the end of the billing cycle.')),
                ('separate_cycles_during_trial', models.BooleanField(default=False, help_text=b'If this is set to True, then the trial period cycle will be split if it spans across multiple billing intervals.')),
                ('prebill_plan', models.BooleanField(default=True, help_text=b'If this is set to True, then the plan base amount will be billed at thebeginning of the billing cycle rather than after the end.')),
                ('cycle_billing_duration', models.DurationField(help_text=b"This can be used to ensure that the billing date doesn't pass a certain date.\nFor example if this field is set to 2 days, for a monthly subscription, the billing date will never surpass the 2nd day of the month. Billing documents can still be generated after that day during the billing cycle, but their billing date will appear to be the end of the cycle billing duration.", null=True, blank=True)),
            ],
            options={
                'ordering': ['name', 'company'],
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024, null=True, blank=True)),
                ('trial_end', models.DateField(help_text=b'The date at which the trial ends. If set, overrides the computed trial end date from the plan.', null=True, blank=True)),
                ('start_date', models.DateField(help_text=b'The starting date for the subscription.', null=True, blank=True)),
                ('cancel_date', models.DateField(help_text=b'The date when the subscription was canceled.', null=True, blank=True)),
                ('ended_at', models.DateField(help_text=b'The date when the subscription ended.', null=True, blank=True)),
                ('reference', models.CharField(blank=True, max_length=128, null=True, help_text=b"The subscription's reference in an external system.", validators=[django.core.validators.RegexValidator(regex=b'^[^,]*$', message='Reference must not contain commas.')])),
                ('state', django_fsm.FSMField(default=b'inactive', help_text=b'The state the subscription is in.', protected=True, max_length=12, choices=[(b'active', 'Active'), (b'inactive', 'Inactive'), (b'canceled', 'Canceled'), (b'ended', 'Ended')])),
                ('meta', annoying.fields.JSONField(null=True, blank=True)),
                ('customer', models.ForeignKey(related_name='subscriptions', to='silver.Customer', help_text=b'The customer who is subscribed to the plan.')),
                ('plan', models.ForeignKey(help_text=b'The plan the customer is subscribed to.', to='silver.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('currency', models.CharField(help_text=b'The currency used for billing.', max_length=4, choices=[('AED', 'AED (UAE Dirham)'), ('AFN', 'AFN (Afghani)'), ('ALL', 'ALL (Lek)'), ('AMD', 'AMD (Armenian Dram)'), ('ANG', 'ANG (Netherlands Antillean Guilder)'), ('AOA', 'AOA (Kwanza)'), ('ARS', 'ARS (Argentine Peso)'), ('AUD', 'AUD (Australian Dollar)'), ('AWG', 'AWG (Aruban Florin)'), ('AZN', 'AZN (Azerbaijanian Manat)'), ('BAM', 'BAM (Convertible Mark)'), ('BBD', 'BBD (Barbados Dollar)'), ('BDT', 'BDT (Taka)'), ('BGN', 'BGN (Bulgarian Lev)'), ('BHD', 'BHD (Bahraini Dinar)'), ('BIF', 'BIF (Burundi Franc)'), ('BMD', 'BMD (Bermudian Dollar)'), ('BND', 'BND (Brunei Dollar)'), ('BOB', 'BOB (Boliviano)'), ('BRL', 'BRL (Brazilian Real)'), ('BSD', 'BSD (Bahamian Dollar)'), ('BTN', 'BTN (Ngultrum)'), ('BWP', 'BWP (Pula)'), ('BYR', 'BYR (Belarusian Ruble)'), ('BZD', 'BZD (Belize Dollar)'), ('CAD', 'CAD (Canadian Dollar)'), ('CDF', 'CDF (Congolese Franc)'), ('CHF', 'CHF (Swiss Franc)'), ('CLP', 'CLP (Chilean Peso)'), ('CNY', 'CNY (Yuan Renminbi)'), ('COP', 'COP (Colombian Peso)'), ('CRC', 'CRC (Costa Rican Colon)'), ('CUC', 'CUC (Peso Convertible)'), ('CUP', 'CUP (Cuban Peso)'), ('CVE', 'CVE (Cabo Verde Escudo)'), ('CZK', 'CZK (Czech Koruna)'), ('DJF', 'DJF (Djibouti Franc)'), ('DKK', 'DKK (Danish Krone)'), ('DOP', 'DOP (Dominican Peso)'), ('DZD', 'DZD (Algerian Dinar)'), ('EGP', 'EGP (Egyptian Pound)'), ('ERN', 'ERN (Nakfa)'), ('ETB', 'ETB (Ethiopian Birr)'), ('EUR', 'EUR (Euro)'), ('FJD', 'FJD (Fiji Dollar)'), ('FKP', 'FKP (Falkland Islands Pound)'), ('GBP', 'GBP (Pound Sterling)'), ('GEL', 'GEL (Lari)'), ('GHS', 'GHS (Ghana Cedi)'), ('GIP', 'GIP (Gibraltar Pound)'), ('GMD', 'GMD (Dalasi)'), ('GNF', 'GNF (Guinea Franc)'), ('GTQ', 'GTQ (Quetzal)'), ('GYD', 'GYD (Guyana Dollar)'), ('HKD', 'HKD (Hong Kong Dollar)'), ('HNL', 'HNL (Lempira)'), ('HRK', 'HRK (Kuna)'), ('HTG', 'HTG (Gourde)'), ('HUF', 'HUF (Forint)'), ('IDR', 'IDR (Rupiah)'), ('ILS', 'ILS (New Israeli Sheqel)'), ('INR', 'INR (Indian Rupee)'), ('IQD', 'IQD (Iraqi Dinar)'), ('IRR', 'IRR (Iranian Rial)'), ('ISK', 'ISK (Iceland Krona)'), ('JMD', 'JMD (Jamaican Dollar)'), ('JOD', 'JOD (Jordanian Dinar)'), ('JPY', 'JPY (Yen)'), ('KES', 'KES (Kenyan Shilling)'), ('KGS', 'KGS (Som)'), ('KHR', 'KHR (Riel)'), ('KMF', 'KMF (Comoro Franc)'), ('KPW', 'KPW (North Korean Won)'), ('KRW', 'KRW (Won)'), ('KWD', 'KWD (Kuwaiti Dinar)'), ('KYD', 'KYD (Cayman Islands Dollar)'), ('KZT', 'KZT (Tenge)'), ('LAK', 'LAK (Kip)'), ('LBP', 'LBP (Lebanese Pound)'), ('LKR', 'LKR (Sri Lanka Rupee)'), ('LRD', 'LRD (Liberian Dollar)'), ('LSL', 'LSL (Loti)'), ('LYD', 'LYD (Libyan Dinar)'), ('MAD', 'MAD (Moroccan Dirham)'), ('MDL', 'MDL (Moldovan Leu)'), ('MGA', 'MGA (Malagasy Ariary)'), ('MKD', 'MKD (Denar)'), ('MMK', 'MMK (Kyat)'), ('MNT', 'MNT (Tugrik)'), ('MOP', 'MOP (Pataca)'), ('MRO', 'MRO (Ouguiya)'), ('MUR', 'MUR (Mauritius Rupee)'), ('MVR', 'MVR (Rufiyaa)'), ('MWK', 'MWK (Malawi Kwacha)'), ('MXN', 'MXN (Mexican Peso)'), ('MYR', 'MYR (Malaysian Ringgit)'), ('MZN', 'MZN (Mozambique Metical)'), ('NAD', 'NAD (Namibia Dollar)'), ('NGN', 'NGN (Naira)'), ('NIO', 'NIO (Cordoba Oro)'), ('NOK', 'NOK (Norwegian Krone)'), ('NPR', 'NPR (Nepalese Rupee)'), ('NZD', 'NZD (New Zealand Dollar)'), ('OMR', 'OMR (Rial Omani)'), ('PAB', 'PAB (Balboa)'), ('PEN', 'PEN (Sol)'), ('PGK', 'PGK (Kina)'), ('PHP', 'PHP (Philippine Peso)'), ('PKR', 'PKR (Pakistan Rupee)'), ('PLN', 'PLN (Zloty)'), ('PYG', 'PYG (Guarani)'), ('QAR', 'QAR (Qatari Rial)'), ('RON', 'RON (Romanian Leu)'), ('RSD', 'RSD (Serbian Dinar)'), ('RUB', 'RUB (Russian Ruble)'), ('RWF', 'RWF (Rwanda Franc)'), ('SAR', 'SAR (Saudi Riyal)'), ('SBD', 'SBD (Solomon Islands Dollar)'), ('SCR', 'SCR (Seychelles Rupee)'), ('SDG', 'SDG (Sudanese Pound)'), ('SEK', 'SEK (Swedish Krona)'), ('SGD', 'SGD (Singapore Dollar)'), ('SHP', 'SHP (Saint Helena Pound)'), ('SLL', 'SLL (Leone)'), ('SOS', 'SOS (Somali Shilling)'), ('SRD', 'SRD (Surinam Dollar)'), ('SSP', 'SSP (South Sudanese Pound)'), ('STD', 'STD (Dobra)'), ('SVC', 'SVC (El Salvador Colon)'), ('SYP', 'SYP (Syrian Pound)'), ('SZL', 'SZL (Lilangeni)'), ('THB', 'THB (Baht)'), ('TJS', 'TJS (Somoni)'), ('TMT', 'TMT (Turkmenistan New Manat)'), ('TND', 'TND (Tunisian Dinar)'), ('TOP', 'TOP (Pa\u2019anga)'), ('TRY', 'TRY (Turkish Lira)'), ('TTD', 'TTD (Trinidad and Tobago Dollar)'), ('TWD', 'TWD (New Taiwan Dollar)'), ('TZS', 'TZS (Tanzanian Shilling)'), ('UAH', 'UAH (Hryvnia)'), ('UGX', 'UGX (Uganda Shilling)'), ('USD', 'USD (US Dollar)'), ('UYU', 'UYU (Peso Uruguayo)'), ('UZS', 'UZS (Uzbekistan Sum)'), ('VEF', 'VEF (Bol\xedvar)'), ('VND', 'VND (Dong)'), ('VUV', 'VUV (Vatu)'), ('WST', 'WST (Tala)'), ('XAF', 'XAF (CFA Franc BEAC)'), ('XAG', 'XAG (Silver)'), ('XAU', 'XAU (Gold)'), ('XBA', 'XBA (Bond Markets Unit European Composite Unit (EURCO))'), ('XBB', 'XBB (Bond Markets Unit European Monetary Unit (E.M.U.-6))'), ('XBC', 'XBC (Bond Markets Unit European Unit of Account 9 (E.U.A.-9))'), ('XBD', 'XBD (Bond Markets Unit European Unit of Account 17 (E.U.A.-17))'), ('XCD', 'XCD (East Caribbean Dollar)'), ('XDR', 'XDR (SDR (Special Drawing Right))'), ('XOF', 'XOF (CFA Franc BCEAO)'), ('XPD', 'XPD (Palladium)'), ('XPF', 'XPF (CFP Franc)'), ('XPT', 'XPT (Platinum)'), ('XSU', 'XSU (Sucre)'), ('XTS', 'XTS (Codes specifically reserved for testing purposes)'), ('XUA', 'XUA (ADB Unit of Account)'), ('XXX', 'XXX (The codes assigned for transactions where no currency is involved)'), ('YER', 'YER (Yemeni Rial)'), ('ZAR', 'ZAR (Rand)'), ('ZMW', 'ZMW (Zambian Kwacha)'), ('ZWL', 'ZWL (Zimbabwe Dollar)')])),
                ('external_reference', models.CharField(max_length=256, null=True, blank=True)),
                ('data', annoying.fields.JSONField(default={}, null=True, blank=True)),
                ('state', django_fsm.FSMField(default=b'initial', max_length=8, choices=[(b'canceled', 'Canceled'), (b'refunded', 'Refunded'), (b'initial', 'Initial'), (b'failed', 'Failed'), (b'settled', 'Settled'), (b'pending', 'Pending')])),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('valid_until', models.DateTimeField(null=True, blank=True)),
                ('last_access', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', silver.utils.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('fail_code', models.CharField(blank=True, max_length=32, null=True, choices=[(b'transaction_declined_by_bank', b'transaction_declined_by_bank'), (b'transaction_hard_declined', b'transaction_hard_declined'), (b'invalid_payment_method', b'invalid_payment_method'), (b'expired_payment_method', b'expired_payment_method'), (b'default', b'default'), (b'invalid_card', b'invalid_card'), (b'insufficient_funds', b'insufficient_funds'), (b'transaction_declined', b'transaction_declined'), (b'expired_card', b'expired_card'), (b'transaction_hard_declined_by_bank', b'transaction_hard_declined_by_bank'), (b'limit_exceeded', b'limit_exceeded')])),
                ('refund_code', models.CharField(blank=True, max_length=32, null=True, choices=[(b'default', b'default')])),
                ('cancel_code', models.CharField(blank=True, max_length=32, null=True, choices=[(b'default', b'default')])),
                ('invoice', models.ForeignKey(related_name='invoice_transactions', blank=True, to='silver.BillingDocumentBase', null=True)),
                ('payment_method', models.ForeignKey(to='silver.PaymentMethod')),
                ('proforma', models.ForeignKey(related_name='proforma_transactions', blank=True, to='silver.BillingDocumentBase', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterIndexTogether(
            name='provider',
            index_together=set([('name', 'company')]),
        ),
        migrations.AddField(
            model_name='plan',
            name='product_code',
            field=models.ForeignKey(help_text=b'The product code for this plan.', to='silver.ProductCode'),
        ),
        migrations.AddField(
            model_name='plan',
            name='provider',
            field=models.ForeignKey(related_name='plans', to='silver.Provider', help_text=b'The provider which provides the plan.'),
        ),
        migrations.AddField(
            model_name='meteredfeatureunitslog',
            name='subscription',
            field=models.ForeignKey(related_name='mf_log_entries', to='silver.Subscription'),
        ),
        migrations.AddField(
            model_name='meteredfeature',
            name='product_code',
            field=silver.utils.models.UnsavedForeignKey(help_text=b'The product code for this plan.', to='silver.ProductCode'),
        ),
        migrations.AddField(
            model_name='documententry',
            name='product_code',
            field=models.ForeignKey(related_name='invoices', blank=True, to='silver.ProductCode', null=True),
        ),
        migrations.AddField(
            model_name='documententry',
            name='proforma',
            field=models.ForeignKey(related_name='proforma_entries', blank=True, to='silver.BillingDocumentBase', null=True),
        ),
        migrations.AlterIndexTogether(
            name='customer',
            index_together=set([('first_name', 'last_name', 'company')]),
        ),
        migrations.AddField(
            model_name='billinglog',
            name='subscription',
            field=models.ForeignKey(related_name='billing_log_entries', to='silver.Subscription'),
        ),
        migrations.AddField(
            model_name='billingdocumentbase',
            name='customer',
            field=models.ForeignKey(to='silver.Customer'),
        ),
        migrations.AddField(
            model_name='billingdocumentbase',
            name='pdf',
            field=models.ForeignKey(to='silver.PDF', null=True),
        ),
        migrations.AddField(
            model_name='billingdocumentbase',
            name='provider',
            field=models.ForeignKey(to='silver.Provider'),
        ),
        migrations.AddField(
            model_name='billingdocumentbase',
            name='related_document',
            field=models.ForeignKey(related_name='reverse_related_document', blank=True, to='silver.BillingDocumentBase', null=True),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('silver.billingdocumentbase',),
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('silver.billingdocumentbase',),
        ),
        migrations.AlterUniqueTogether(
            name='meteredfeatureunitslog',
            unique_together=set([('metered_feature', 'subscription', 'start_date', 'end_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='billingdocumentbase',
            unique_together=set([('kind', 'provider', 'series', 'number')]),
        ),
    ]
