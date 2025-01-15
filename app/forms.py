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
    private_or_psncheckbox = BooleanField('Private network or public sector network')

    
# ['private_or_psn', 'tls', 'ipsec_or_vpn', 'other']

# ['private_or_psn', 'tls', 'legacy_ssl', 'other']
    
# Private network or public sector network

# TLS (version 1.2 or above)

# 

# Bonded fibre optic connections
    
#     # dataProtectionWithinNetwork

    
# TLS (version 1.2 or above)

# IPsec or TLS VPN gateway

#     # dataStorageAndProcessingLocations
#     ['uk', 'eea']

# United Kingdom

# European Economic Area (EEA)

#     # userAuthentication
    
# ['pka', 'government_network', 'dedicated_link', 'username_or_password']

# managementAccessAuthentication
# ['two_factor', 'public_key', 'identity_federation', 'dedicated_link', 'username_or_password']


# 2-factor authentication

# Public key authentication (including by TLS client certificate)

# Identity federation with existing provider (for example Google Apps)

# Limited access network (for example PSN)

# Dedicated link (for example VPN)

# Username or password

# securityGovernanceStandards
# ['iso_iec_27001']


# CSA CCM version 3.0

# ISO/IEC 27001

# datacentreSecurityStandards

# supportMultiCloud
# boolean

# cloudDeploymentModel
# ['public', 'private']

# Public cloud

# Private cloud

# Community cloud

# Hybrid cloud

# userSupportAccessibility
# radiolist


# WCAG 2.1 AAA

# WCAG 2.1 AA or EN 301 549

# WCAG 2.1 A

# None or don’t know

# serviceInterfaceAccessibility

# WCAG 2.1 AAA

# WCAG 2.1 AA or EN 301 549

# WCAG 2.1 A

# None or don’t know

# publicSectorNetworksTypes
# ['psn', 'pnn', 'n3', 'janet', 'swan', 'hscn']

# Public Services Network (PSN)

# Police National Network (PNN)

# Joint Academic Network (JANET)

# Scottish Wide Area Network (SWAN)

# Health and Social Care Network (HSCN)






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




# Lot 1 filters
# Metrics reporting
# Infrastructure or application metrics

# Scaling
# Usage notifications
# Backup and recovery
# Data protection between buyer and supplier networks
# Data protection within supplier network
# Data storage and processing locations
# User authentication
# Management access authentication
# Security governance standards
# Datacentre security standard

# Lot 2 filters:
# Multi cloud support
# Cloud deployment model
# Supplier type
# User support
# User support accessibility
# Service interface accessibility
# Using the service
# Metrics reporting
# Connected public sector networks
# Data protection between buyer and supplier networks
# Data protection within supplier network
# Data storage and processing locations
# User authentication
# Management access authentication
# Security governance standards
# Datacentre security standard

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