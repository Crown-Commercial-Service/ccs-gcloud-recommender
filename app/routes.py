from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Flask
from .forms import mainPageform, lot3Pageform, lot1Pageform, lot2Pageform
from .utils import sanitize_input, get_text_embeddings, search_service, convert_to_html_list, checkbox_filter, checkbox_findword_filter
import pandas as pd

main = Blueprint('main', __name__)


df = pd.DataFrame(columns=["id", "supplierName", "serviceName", "serviceDescription", "serviceBenefits", 
                           "serviceFeatures", "lotName", "standardsISOIEC27001", "standardsISO28000", "standardsCSASTAR", 
                           "standardsPCI", "standardsCyberEssentials", "standardsCyberEssentialsPlus", 
                           "emailOrTicketingSupport", "phoneSupport", "webChatSupport", "governmentSecurityClearances", 
                           "staffSecurityClearanceChecks", "resellingType", "educationPricing", "freeVersionTrialOption", "metricsHow", "score"])
query = ''
@main.route('/', methods = ['GET','POST'])
def index():
    global query
    global filter_df, No_filtter_df
    global results
    global lot_3_no, lot_1_no, lot_2_no

    form = mainPageform()
    filter_df = df.copy()
    No_filtter_df = df.copy()
    results = []
    filter_button = 0
    
    lot_1_no = lot_2_no = lot_3_no = 0 
    
    lot_1_name = 'Cloud hosting'
    lot_2_name = 'Cloud software'
    lot_3_name = 'Cloud support'

    if request.method == 'POST':
        print("Form submitted.")

        if form.SearchButton.data:
            # Example filter logic: Filter by education pricing
            print('Search button is pressed.')
            query = sanitize_input(form.Searchbar.data)
            No_filtter_df = pd.DataFrame(search_service(query))
            No_filtter_df = No_filtter_df.loc[No_filtter_df['score']>0.82, :]
            print(No_filtter_df.columns)
            #print(No_filtter_df.loc[0,'metricsHow'])
            filter_button = 1

            No_filtter_df["serviceFeatures"] = No_filtter_df["serviceFeatures"].apply(convert_to_html_list) 
            results = No_filtter_df.to_dict(orient='records')
            lot_1_no = No_filtter_df.loc[No_filtter_df['lotName']==lot_1_name,:].shape[0]
            lot_2_no = No_filtter_df.loc[No_filtter_df['lotName']==lot_2_name,:].shape[0]
            lot_3_no = No_filtter_df.loc[No_filtter_df['lotName']==lot_3_name,:].shape[0]

        elif form.ClearButton.data:
            print('Clear button is pressed. Filters reset.')
            query=''
            return redirect(url_for('main.index'))

        elif form.FilterButton.data:
            filter_df = No_filtter_df.copy()
            filter_button = 1

            # Mapping of form checkboxes to dataframe columns
            checkbox_column_map = {
                'Emailcheckbox': 'emailOrTicketingSupport',
                'Phonecheckbox': 'phoneSupport',
                'webchatcheckbox': 'webChatSupport',
                'standardsISOIEC27001checkbox': 'standardsISOIEC27001',
                'standardsISO28000checkbox': 'standardsISO28000',
                'standardsCSASTARcheckbox': 'standardsCSASTAR',
                'standardsPCIcheckbox': 'standardsPCI',
                'standardsCyberEssentialscheckbox': 'standardsCyberEssentials',
                'standardsCyberEssentialsPluscheckbox': 'standardsCyberEssentialsPlus',
                'educationPricingcheckbox': 'educationPricing',
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)

            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]
            
            # if form.apicheckbox.data:
            #     filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: type(x)==str and 'api' in x)]
            # if form.real_timecheckbox.data:
            #     filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: type(x)==str and 'real_time' in x)]
            # if form.regular_reportscheckbox.data:
            #     filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: type(x)==str and 'regular_reports' in x)]
            # if form.on_requestcheckbox.data:
            #     filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: type(x)==str and 'on_request' in x)]

            # check box mapping for metricsHow, metricsWhat, dataProtectionBetweenNetworks, dataProtectionWithinNetwork, dataStorageAndProcessingLocations, userAuthentication

                        
            

    # # metricsWhat
    # cpucheckbox = BooleanField('CPU')
    # diskcheckbox = BooleanField('Disk')
    # httpcheckbox = BooleanField('HTTP request and response status')
    # memorycheckbox = BooleanField('Memory')
    # networkcheckbox = BooleanField('Network')
    # num_instancescheckbox = BooleanField('Number of active instances')
    # othercheckbox = BooleanField('Other')

    # # scalingType
    # automaticcheckbox = BooleanField('Automatic')
    # user_interventioncheckbox = BooleanField('Manual')
            

            print('Filter button is pressed.')
            #filter_df["serviceFeatures"] = filter_df["serviceFeatures"].apply(convert_to_html_list) 
            results = filter_df.to_dict(orient='records')
            lot_1_no = filter_df.loc[filter_df['lotName']==lot_1_name,:].shape[0]
            lot_2_no = filter_df.loc[filter_df['lotName']==lot_2_name,:].shape[0]
            lot_3_no = filter_df.loc[filter_df['lotName']==lot_3_name,:].shape[0]

    return render_template('index.html', 
                           form = form, 
                           results = results, 
                           filter_df_len = len(results),
                           filter_button=filter_button, 
                           query=query,
                           lot_1_no = lot_1_no,
                           lot_2_no = lot_2_no,
                           lot_3_no = lot_3_no)

@main.route('/lot1', methods=['POST', 'GET'])
def lot1():
    global query, results
    global No_filtter_df
    global lot_3_no, lot_2_no, lot_1_no
    
    filter_df = No_filtter_df.copy()
    filter_df = filter_df.loc[filter_df['lotName']=='Cloud hosting', :]

    form = lot1Pageform()

    if request.method == 'POST':
        print("Form submitted.")

        if form.ClearButton.data:
            print('Clear button is pressed. Filters reset.')
            query=''
            return redirect(url_for('main.index'))

        elif form.FilterButton.data:

            # Mapping of form checkboxes to dataframe columns
            checkbox_column_map = {
                'Emailcheckbox': 'emailOrTicketingSupport',
                'Phonecheckbox': 'phoneSupport',
                'webchatcheckbox': 'webChatSupport',
                'standardsISOIEC27001checkbox': 'standardsISOIEC27001',
                'standardsISO28000checkbox': 'standardsISO28000',
                'standardsCSASTARcheckbox': 'standardsCSASTAR',
                'standardsPCIcheckbox': 'standardsPCI',
                'standardsCyberEssentialscheckbox': 'standardsCyberEssentials',
                'standardsCyberEssentialsPluscheckbox': 'standardsCyberEssentialsPlus',
                'educationPricingcheckbox': 'educationPricing',
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption',
                'usageNotificationscheckbox': 'usageNotifications',
                'backupcheckbox': 'backup'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)
            
            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]

            # metricHow
            metricsHow_checkbox_mapping = {'apicheckbox': 'api',
                                           'real_timecheckbox': 'real_time',
                                           'regular_reportscheckbox': 'regular_reports',
                                           'on_requestcheckbox': 'on_request'}
            filter_df = checkbox_findword_filter(form, metricsHow_checkbox_mapping, 'metricHow', filter_df)

            # metricWhat
            metricsWhat_checkbox_mapping = {'cpucheckbox': 'cpu',
                                           'diskcheckbox': 'disk',
                                           'memorycheckbox': 'memory',
                                           'httpcheckbox': 'http',
                                           'networkcheckbox': 'network',
                                           'num_instancescheckbox': 'num_instances',
                                           'othercheckbox': 'other'}
            filter_df = checkbox_findword_filter(form, metricsWhat_checkbox_mapping, 'metricWhat', filter_df)

            # scalingType
            scalingType_checkbox_mapping = {'automaticcheckbox': 'automatic',
                                           'user_interventioncheckbox': 'user_intervention'}
            filter_df = checkbox_findword_filter(form, scalingType_checkbox_mapping, 'scalingType', filter_df)

            # dataProtectionBetweenNetworks
            dataProtectionBetweenNetworks_checkbox_mapping = {'private_or_psncheckbox': 'private_or_psn',
                                           'tlscheckbox': 'tls',
                                           'ipsec_or_vpncheckbox': 'ipsec_or_vpn',
                                           'othercheckbox': 'other'}
            filter_df = checkbox_findword_filter(form, dataProtectionBetweenNetworks_checkbox_mapping, 'dataProtectionBetweenNetworks', filter_df)

            # dataProtectionWithinNetwork
            dataProtectionWithinNetwork_checkbox_mapping = {'tlsWINcheckbox': 'tls',
                                           'ipsec_or_vpnWINcheckbox': 'ipsec_or_vpn',
                                           'otherWINcheckbox': 'other'}
            filter_df = checkbox_findword_filter(form, dataProtectionWithinNetwork_checkbox_mapping, 'dataProtectionWithinNetwork', filter_df)

            # dataStorageAndProcessingLocations
            dataStorageAndProcessingLocations_checkbox_mapping = {'ukcheckbox': 'uk',
                                           'eeacheckbox': 'eea'}
            filter_df = checkbox_findword_filter(form, dataStorageAndProcessingLocations_checkbox_mapping, 'dataStorageAndProcessingLocations', filter_df)
            
            # userAuthentication
            userAuthentication_checkbox_mapping = {'two_factorcheckbox': 'two_factor',
                                           'pkacheckbox': 'pka',
                                           'dedicated_linkcheckbox': 'dedicated_link',
                                           'government_networkcheckbox': 'government_network',
                                           'identity_federationcheckbox': 'identity_federation',
                                           'username_or_passwordcheckbox': 'username_or_password'}
            filter_df = checkbox_findword_filter(form, userAuthentication_checkbox_mapping, 'userAuthentication', filter_df)

            # managementAccessAuthentication
            managementAccessAuthentication_checkbox_mapping = {'two_factorMMAcheckbox': 'two_factor',
                                           'public_keyMMAcheckbox': 'public_key',
                                           'dedicated_linkMMAcheckbox': 'dedicated_link',
                                           'government_networkMMAcheckbox': 'government_network',
                                           'identity_federationMMAcheckbox': 'identity_federation',
                                           'username_or_passwordMMAcheckbox': 'username_or_password'}
            filter_df = checkbox_findword_filter(form, managementAccessAuthentication_checkbox_mapping, 'managementAccessAuthentication', filter_df)

            # securityGovernanceStandards
            securityGovernanceStandards_checkbox_mapping = {'csa_ccmcheckbox': 'csa_ccm',
                                           'iso_iec_27001checkbox': 'iso_iec_27001'}
            filter_df = checkbox_findword_filter(form, securityGovernanceStandards_checkbox_mapping, 'securityGovernanceStandards', filter_df)

            print('Filter button is pressed.')

    lot_1_no = filter_df.loc[filter_df['lotName']=='Cloud hosting',:].shape[0]
            
    results = filter_df.to_dict(orient='records')

    return render_template('lot1.html', 
                           form = form,
                           query=query,
                           filter_df_len = len(results), 
                           lot_3_no=lot_3_no,
                           lot_2_no=lot_2_no,
                           lot_1_no=lot_1_no, 
                           results=results)

    

@main.route('/lot2', methods=['POST', 'GET'])
def lot2():
    global query, results
    global No_filtter_df
    global lot_3_no, lot_2_no, lot_1_no
    
    filter_df = No_filtter_df.copy()
    filter_df = filter_df.loc[filter_df['lotName']=='Cloud software', :]

    form = lot2Pageform()

    if request.method == 'POST':
        print("Form submitted.")

        if form.ClearButton.data:
            print('Clear button is pressed. Filters reset.')
            query=''
            return redirect(url_for('main.index'))

        elif form.FilterButton.data:

            # Mapping of form checkboxes to dataframe columns
            checkbox_column_map = {
                'Emailcheckbox': 'emailOrTicketingSupport',
                'Phonecheckbox': 'phoneSupport',
                'webchatcheckbox': 'webChatSupport',
                'standardsISOIEC27001checkbox': 'standardsISOIEC27001',
                'standardsISO28000checkbox': 'standardsISO28000',
                'standardsCSASTARcheckbox': 'standardsCSASTAR',
                'standardsPCIcheckbox': 'standardsPCI',
                'standardsCyberEssentialscheckbox': 'standardsCyberEssentials',
                'standardsCyberEssentialsPluscheckbox': 'standardsCyberEssentialsPlus',
                'educationPricingcheckbox': 'educationPricing',
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption',
                'supportMultiCloudcheckbox': 'supportMultiCloud'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)
            
            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]

            # metricHow
            metricsHow_checkbox_mapping = {'apicheckbox': 'api',
                                           'real_timecheckbox': 'real_time',
                                           'regular_reportscheckbox': 'regular_reports',
                                           'on_requestcheckbox': 'on_request'}
            filter_df = checkbox_findword_filter(form, metricsHow_checkbox_mapping, 'metricHow', filter_df)

            # dataProtectionBetweenNetworks
            dataProtectionBetweenNetworks_checkbox_mapping = {'private_or_psncheckbox': 'private_or_psn',
                                           'tlscheckbox': 'tls',
                                           'ipsec_or_vpncheckbox': 'ipsec_or_vpn',
                                           'othercheckbox': 'other'}
            filter_df = checkbox_findword_filter(form, dataProtectionBetweenNetworks_checkbox_mapping, 'dataProtectionBetweenNetworks', filter_df)

            # dataProtectionWithinNetwork
            dataProtectionWithinNetwork_checkbox_mapping = {'tlsWINcheckbox': 'tls',
                                           'ipsec_or_vpnWINcheckbox': 'ipsec_or_vpn',
                                           'otherWINcheckbox': 'other'}
            filter_df = checkbox_findword_filter(form, dataProtectionWithinNetwork_checkbox_mapping, 'dataProtectionWithinNetwork', filter_df)

            # dataStorageAndProcessingLocations
            dataStorageAndProcessingLocations_checkbox_mapping = {'ukcheckbox': 'uk',
                                           'eeacheckbox': 'eea'}
            filter_df = checkbox_findword_filter(form, dataStorageAndProcessingLocations_checkbox_mapping, 'dataStorageAndProcessingLocations', filter_df)
            
            # userAuthentication
            userAuthentication_checkbox_mapping = {'two_factorcheckbox': 'two_factor',
                                           'pkacheckbox': 'pka',
                                           'dedicated_linkcheckbox': 'dedicated_link',
                                           'government_networkcheckbox': 'government_network',
                                           'identity_federationcheckbox': 'identity_federation',
                                           'username_or_passwordcheckbox': 'username_or_password'}
            filter_df = checkbox_findword_filter(form, userAuthentication_checkbox_mapping, 'userAuthentication', filter_df)

            # managementAccessAuthentication
            managementAccessAuthentication_checkbox_mapping = {'two_factorMMAcheckbox': 'two_factor',
                                           'public_keyMMAcheckbox': 'public_key',
                                           'dedicated_linkMMAcheckbox': 'dedicated_link',
                                           'government_networkMMAcheckbox': 'government_network',
                                           'identity_federationMMAcheckbox': 'identity_federation',
                                           'username_or_passwordMMAcheckbox': 'username_or_password'}
            filter_df = checkbox_findword_filter(form, managementAccessAuthentication_checkbox_mapping, 'managementAccessAuthentication', filter_df)

            # securityGovernanceStandards
            securityGovernanceStandards_checkbox_mapping = {'csa_ccmcheckbox': 'csa_ccm',
                                           'iso_iec_27001checkbox': 'iso_iec_27001'}
            filter_df = checkbox_findword_filter(form, securityGovernanceStandards_checkbox_mapping, 'securityGovernanceStandards', filter_df)

            # cloudDeploymentModel
            cloudDeploymentModel_checkbox_mapping = {'publiccheckbox': 'public',
                                                'privatecheckbox': 'private',
                                                'hybridcheckbox': 'hybrid',
                                                'communitycheckbox': 'community'}
            filter_df = checkbox_findword_filter(form, cloudDeploymentModel_checkbox_mapping, 'cloudDeploymentModel', filter_df)

            # userSupportAccessibility - radiolist
            if form.USA_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['userSupportAccessibility'] == form.USA_RadioButtons.data]
    
            # serviceInterfaceAccessibility - radiolist
            if form.SIA_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['serviceInterfaceAccessibility'] == form.SIA_RadioButtons.data]
    
            # publicSectorNetworksTypes
            publicSectorNetworksTypes_checkbox_mapping = {'psncheckbox': 'psn',
                                                'pnncheckbox': 'pnn',
                                                'janetcheckbox': 'janet',
                                                'swancheckbox': 'swan',
                                                'hscncheckbox': 'hscn'}
            filter_df = checkbox_findword_filter(form, publicSectorNetworksTypes_checkbox_mapping, 'publicSectorNetworksTypes', filter_df)

            print('Filter button is pressed.')

             
    lot_2_no = filter_df.loc[filter_df['lotName']=='Cloud software',:].shape[0]
            
    results = filter_df.to_dict(orient='records')

    return render_template('lot2.html', 
                           form = form,
                           query=query, 
                           filter_df_len = len(results),
                           lot_3_no=lot_3_no,
                           lot_2_no=lot_2_no,
                           lot_1_no=lot_1_no, 
                           results=results)
    

@main.route('/lot3', methods=['POST', 'GET'])
def lot3():
    global query, results
    global No_filtter_df
    global lot_3_no, lot_2_no, lot_1_no
    form = lot3Pageform()
    
    filter_df = No_filtter_df.copy()
    filter_df = filter_df.loc[filter_df['lotName']=='Cloud support', :]

    if request.method == 'POST':
        print("Form submitted.")

        if form.ClearButton.data:
            print('Clear button is pressed. Filters reset.')
            query=''
            return redirect(url_for('main.index'))

        elif form.FilterButton.data:

            # Mapping of form checkboxes to dataframe columns
            checkbox_column_map = {
                'Emailcheckbox': 'emailOrTicketingSupport',
                'Phonecheckbox': 'phoneSupport',
                'webchatcheckbox': 'webChatSupport',
                'standardsISOIEC27001checkbox': 'standardsISOIEC27001',
                'standardsISO28000checkbox': 'standardsISO28000',
                'standardsCSASTARcheckbox': 'standardsCSASTAR',
                'standardsPCIcheckbox': 'standardsPCI',
                'standardsCyberEssentialscheckbox': 'standardsCyberEssentials',
                'standardsCyberEssentialsPluscheckbox': 'standardsCyberEssentialsPlus',
                'educationPricingcheckbox': 'educationPricing',
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)
            
            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]
            
                       
            print('Filter button is pressed.')

             
    lot_3_no = filter_df.loc[filter_df['lotName']=='Cloud support',:].shape[0]
            
    results = filter_df.to_dict(orient='records')

    return render_template('lot3.html', 
                           form = form,
                           query=query,
                           filter_df_len = len(results), 
                           lot_3_no=lot_3_no,
                           lot_2_no=lot_2_no,
                           lot_1_no=lot_1_no, 
                           results=results)


