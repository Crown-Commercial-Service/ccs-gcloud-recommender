from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, RadioField

class mainPageform(FlaskForm):
    Searchbar = StringField('Search')
    Emailcheckbox = BooleanField('Email support')
    Phonecheckbox = BooleanField('Phone support')
    webchatcheckbox = BooleanField('Webchat support')
    standardsISOIEC27001checkbox = BooleanField('ISO/IEC 27001 (service security)')
    standardsISO28000checkbox = BooleanField('ISO 28000:2007 (supply chain security)')
    standardsCSASTARcheckbox = BooleanField('CSA STAR (service security)')
    standardsPCIcheckbox = BooleanField('PCI DSS (payment card security)')
    standardsCyberEssentialscheckbox = BooleanField('Cyber essentials')
    standardsCyberEssentialsPluscheckbox = BooleanField('Cyber essentials plus')
    educationPricingcheckbox = BooleanField('Discount for Educational org')
    freeVersionTrialOptioncheckbox = BooleanField('Free trial')
    
    MGSC_RadioButtons=RadioField('Minimum Government Secuirty Clearance', 
                                 choices=[('dv','Developed Vetting (DV)'),
                                          ('sc','Security Clearance (SC)'),
                                          ('bpss','Baseline Personnel Security Standard (BPSS)'),
                                          ('none','none')])
    Supplier_RadioButtons = RadioField('Supplier Type', 
                                       choices=[('not_reseller','Not a reseller'),
                                                ('reseller_extra_features_and_support','Reseller providing extra features and support'),
                                                ('reseller_extra_support','Reseller providing extra support'),
                                                ('reseller_no_extras','Reseller (no extras)')])
    SSCC_RadioButtons = RadioField('Staff Security Clearance Checks',
                                   choices=[('staff_screening_to_bs7858_2019','Conforms to BS7858:2019'),
                                            ('staff_screening_not_bs7858_2019','No to BS7858:2019'),
                                            ('none','none')])

    SearchButton = SubmitField('Search')
    FilterButton = SubmitField('Filter')
    ClearButton = SubmitField('Clear')


class lot1Pageform(FlaskForm):
    Searchbar = StringField('Search')
    Emailcheckbox = BooleanField('Email support')
    Phonecheckbox = BooleanField('Phone support')
    webchatcheckbox = BooleanField('Webchat support')
    standardsISOIEC27001checkbox = BooleanField('ISO/IEC 27001 (service security)')
    standardsISO28000checkbox = BooleanField('ISO 28000:2007 (supply chain security)')
    standardsCSASTARcheckbox = BooleanField('CSA STAR (service security)')
    standardsPCIcheckbox = BooleanField('PCI DSS (payment card security)')
    standardsCyberEssentialscheckbox = BooleanField('Cyber essentials')
    standardsCyberEssentialsPluscheckbox = BooleanField('Cyber essentials plus')
    educationPricingcheckbox = BooleanField('Discount for Educational org')
    freeVersionTrialOptioncheckbox = BooleanField('Free trial')
    
    # metricsHow
    apicheckbox = BooleanField('API access')
    real_timecheckbox = BooleanField('Real-time dashboards')
    regular_reportscheckbox = BooleanField('Regular reports')
    on_requestcheckbox = BooleanField('Reports on request')

    # metricsWhat
    cpucheckbox = BooleanField('CPU')
    diskcheckbox = BooleanField('Disk')
    httpcheckbox = BooleanField('HTTP request and response status')
    memorycheckbox = BooleanField('Memory')
    networkcheckbox = BooleanField('Network')
    num_instancescheckbox = BooleanField('Number of active instances')
    othercheckbox = BooleanField('Other')

    # scalingType
    automaticcheckbox = BooleanField('Automatic')
    user_interventioncheckbox = BooleanField('Manual')

    # usageNotifications
    usageNotificationscheckbox = BooleanField('Notifies users if usage nears service limits')

    # backup
    backupcheckbox = BooleanField('Backup and recovery is available')

    # dataProtectionBetweenNetworks
    private_or_psncheckbox = BooleanField('Private network or public sector network')
    tlscheckbox = BooleanField('TLS (version 1.2 or above)')
    ipsec_or_vpncheckbox = BooleanField('IPsec or TLS VPN gateway')
    othercheckbox = BooleanField('Other')

    # dataProtectionWithinNetwork
    tlsWINcheckbox = BooleanField('TLS (version 1.2 or above)')
    ipsec_or_vpnWINcheckbox = BooleanField('IPsec or TLS VPN gateway')
    otherWINcheckbox = BooleanField('Other')

    # dataStorageAndProcessingLocations
    ukcheckbox = BooleanField('United Kingdom')
    eeacheckbox = BooleanField('European Economic Area (EEA)')

    # userAuthentication
    two_factorcheckbox = BooleanField('2-factor authentication')
    pkacheckbox = BooleanField('Public key authentication (including by TLS client certificate)')
    dedicated_linkcheckbox = BooleanField('Dedicated link (for example VPN)')
    government_networkcheckbox = BooleanField('Limited access network (for example PSN)')
    identity_federationcheckbox = BooleanField('Identity federation with existing provider (for example Google apps)')
    username_or_passwordcheckbox =BooleanField('Username or password')

    # managementAccessAuthentication
    two_factorMMAcheckbox = BooleanField('2-factor authentication')
    public_keyMMAcheckbox = BooleanField('Public key authentication (including by TLS client certificate)')
    dedicated_linkMMAcheckbox = BooleanField('Dedicated link (for example VPN)')
    government_networkMMAcheckbox = BooleanField('Limited access network (for example PSN)')
    identity_federationMMAcheckbox = BooleanField('Identity federation with existing provider (for example Google apps)')
    username_or_passwordMMAcheckbox =BooleanField('Username or password')

    # securityGovernanceStandards
    csa_ccmcheckbox = BooleanField('CSA CCM version 3.0')
    iso_iec_27001checkbox = BooleanField('ISO/IEC 27001')

    # datacentreSecurityStandards
    recognised_standardcheckbox = BooleanField('Complies with a recognised standard (for example CSA CCM version 3.0)')

    MGSC_RadioButtons=RadioField('Minimum Government Secuirty Clearance', 
                                 choices=[('dv','Developed Vetting (DV)'),
                                          ('sc','Security Clearance (SC)'),
                                          ('bpss','Baseline Personnel Security Standard (BPSS)'),
                                          ('none','none')])
    Supplier_RadioButtons = RadioField('Supplier Type', 
                                       choices=[('not_reseller','Not a reseller'),
                                                ('reseller_extra_features_and_support','Reseller providing extra features and support'),
                                                ('reseller_extra_support','Reseller providing extra support'),
                                                ('reseller_no_extras','Reseller (no extras)')])
    SSCC_RadioButtons = RadioField('Staff Security Clearance Checks',
                                   choices=[('staff_screening_to_bs7858_2019','Conforms to BS7858:2019'),
                                            ('staff_screening_not_bs7858_2019','No to BS7858:2019'),
                                            ('none','none')])


    SearchButton = SubmitField('Search')
    FilterButton = SubmitField('Filter')
    ClearButton = SubmitField('Clear')

class lot2Pageform(FlaskForm):
    Searchbar = StringField('Search')
    Emailcheckbox = BooleanField('Email support')
    Phonecheckbox = BooleanField('Phone support')
    webchatcheckbox = BooleanField('Webchat support')
    standardsISOIEC27001checkbox = BooleanField('ISO/IEC 27001 (service security)')
    standardsISO28000checkbox = BooleanField('ISO 28000:2007 (supply chain security)')
    standardsCSASTARcheckbox = BooleanField('CSA STAR (service security)')
    standardsPCIcheckbox = BooleanField('PCI DSS (payment card security)')
    standardsCyberEssentialscheckbox = BooleanField('Cyber essentials')
    standardsCyberEssentialsPluscheckbox = BooleanField('Cyber essentials plus')
    educationPricingcheckbox = BooleanField('Discount for Educational org')
    freeVersionTrialOptioncheckbox = BooleanField('Free trial')
    
    # metricsHow
    apicheckbox = BooleanField('API access')
    real_timecheckbox = BooleanField('Real-time dashboards')
    regular_reportscheckbox = BooleanField('Regular reports')
    on_requestcheckbox = BooleanField('Reports on request')

    # dataProtectionBetweenNetworks
    private_or_psncheckbox = BooleanField('Private network or public sector network')
    tlscheckbox = BooleanField('TLS (version 1.2 or above)')
    ipsec_or_vpncheckbox = BooleanField('IPsec or TLS VPN gateway')
    othercheckbox = BooleanField('Other')

    # dataProtectionWithinNetwork
    tlsWINcheckbox = BooleanField('TLS (version 1.2 or above)')
    ipsec_or_vpnWINcheckbox = BooleanField('IPsec or TLS VPN gateway')
    otherWINcheckbox = BooleanField('Other')

    # dataStorageAndProcessingLocations
    ukcheckbox = BooleanField('United Kingdom')
    eeacheckbox = BooleanField('European Economic Area (EEA)')

    # userAuthentication
    two_factorcheckbox = BooleanField('2-factor authentication')
    pkacheckbox = BooleanField('Public key authentication (including by TLS client certificate)')
    dedicated_linkcheckbox = BooleanField('Dedicated link (for example VPN)')
    government_networkcheckbox = BooleanField('Limited access network (for example PSN)')
    identity_federationcheckbox = BooleanField('Identity federation with existing provider (for example Google apps)')
    username_or_passwordcheckbox =BooleanField('Username or password')

    # managementAccessAuthentication
    two_factorMMAcheckbox = BooleanField('2-factor authentication')
    public_keyMMAcheckbox = BooleanField('Public key authentication (including by TLS client certificate)')
    dedicated_linkMMAcheckbox = BooleanField('Dedicated link (for example VPN)')
    government_networkMMAcheckbox = BooleanField('Limited access network (for example PSN)')
    identity_federationMMAcheckbox = BooleanField('Identity federation with existing provider (for example Google apps)')
    username_or_passwordMMAcheckbox =BooleanField('Username or password')

    # securityGovernanceStandards
    csa_ccmcheckbox = BooleanField('CSA CCM version 3.0')
    iso_iec_27001checkbox = BooleanField('ISO/IEC 27001')

    # datacentreSecurityStandards
    recognised_standardcheckbox = BooleanField('Complies with a recognised standard (for example CSA CCM version 3.0)')

    # cloudDeploymentModel
    publiccheckbox = BooleanField('Public cloud')
    privatecheckbox = BooleanField('Private cloud')
    hybridcheckbox = BooleanField('Hybrid cloud')
    communitycheckbox = BooleanField('Community cloud')

    # userSupportAccessibility - radiolist
    USA_RadioButtons=RadioField('User Support Accessibility', 
                                 choices=[('wcag_aaa','WCAG 2.1 AAA'),
                                          ('wcag_aa','WCAG 2.1 AA or EN 301 549'),
                                          ('wcag_a','WCAG 2.1 A'),
                                          ('none','None or don’t know')])
    
    # serviceInterfaceAccessibility - radiolist
    SIA_RadioButtons=RadioField('Service interface accessibility', 
                                 choices=[('wcag_aaa','WCAG 2.1 AAA'),
                                          ('wcag_aa','WCAG 2.1 AA or EN 301 549'),
                                          ('wcag_a','WCAG 2.1 A'),
                                          ('none','None or don’t know')])
    
    # publicSectorNetworksTypes
    psncheckbox = BooleanField('Public Services Network (PSN)')
    pnncheckbox = BooleanField('Police National Network (PNN)')
    janetcheckbox = BooleanField('Joint Academic Network (JANET)')
    swancheckbox = BooleanField('Scottish Wide Area Network (SWAN)')
    hscncheckbox = BooleanField('Health and Social Care Network (HSCN)')

    # supportMultiCloud True or False
    supportMultiCloudcheckbox = BooleanField('Multi cloud support')

    MGSC_RadioButtons=RadioField('Minimum Government Secuirty Clearance', 
                                 choices=[('dv','Developed Vetting (DV)'),
                                          ('sc','Security Clearance (SC)'),
                                          ('bpss','Baseline Personnel Security Standard (BPSS)'),
                                          ('none','none')])
    Supplier_RadioButtons = RadioField('Supplier Type', 
                                       choices=[('not_reseller','Not a reseller'),
                                                ('reseller_extra_features_and_support','Reseller providing extra features and support'),
                                                ('reseller_extra_support','Reseller providing extra support'),
                                                ('reseller_no_extras','Reseller (no extras)')])
    SSCC_RadioButtons = RadioField('Staff Security Clearance Checks',
                                   choices=[('staff_screening_to_bs7858_2019','Conforms to BS7858:2019'),
                                            ('staff_screening_not_bs7858_2019','No to BS7858:2019'),
                                            ('none','none')])


    SearchButton = SubmitField('Search')
    FilterButton = SubmitField('Filter')
    ClearButton = SubmitField('Clear')


class lot3Pageform(FlaskForm):
    Searchbar = StringField('Search')
    Emailcheckbox = BooleanField('Email support')
    Phonecheckbox = BooleanField('Phone support')
    webchatcheckbox = BooleanField('Webchat support')
    standardsISOIEC27001checkbox = BooleanField('ISO/IEC 27001 (service security)')
    standardsISO28000checkbox = BooleanField('ISO 28000:2007 (supply chain security)')
    standardsCSASTARcheckbox = BooleanField('CSA STAR (service security)')
    standardsPCIcheckbox = BooleanField('PCI DSS (payment card security)')
    standardsCyberEssentialscheckbox = BooleanField('Cyber essentials')
    standardsCyberEssentialsPluscheckbox = BooleanField('Cyber essentials plus')
    educationPricingcheckbox = BooleanField('Discount for Educational org')
    freeVersionTrialOptioncheckbox = BooleanField('Free trial')
    MGSC_RadioButtons=RadioField('Minimum Government Secuirty Clearance', 
                                 choices=[('dv','Developed Vetting (DV)'),
                                          ('sc','Security Clearance (SC)'),
                                          ('bpss','Baseline Personnel Security Standard (BPSS)'),
                                          ('none','none')])
    Supplier_RadioButtons = RadioField('Supplier Type', 
                                       choices=[('not_reseller','Not a reseller'),
                                                ('reseller_extra_features_and_support','Reseller providing extra features and support'),
                                                ('reseller_extra_support','Reseller providing extra support'),
                                                ('reseller_no_extras','Reseller (no extras)')])
    SSCC_RadioButtons = RadioField('Staff Security Clearance Checks',
                                   choices=[('staff_screening_to_bs7858_2019','Conforms to BS7858:2019'),
                                            ('staff_screening_not_bs7858_2019','No to BS7858:2019'),
                                            ('none','none')])
    SearchButton = SubmitField('Search')
    FilterButton = SubmitField('Filter')
    ClearButton = SubmitField('Clear')