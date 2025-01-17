from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Flask
from .forms import mainPageform, lot3Pageform, lot1Pageform, lot2Pageform
from .utils import sanitize_input, get_text_embeddings, search_service, convert_to_html_list, checkbox_filter
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
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)
            
            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]

            metricsHow_checkbox_mapping = {'apicheckbox': 'api',
                                           'real_timecheckbox': 'real_time',
                                           'regular_reportscheckbox': 'regular_reports',
                                           'on_requestcheckbox': 'on_request'}
            
            for checkbox, keyword in metricsHow_checkbox_mapping.items():
                if getattr(form, checkbox).data:
                    print(f'{checkbox} is selected.')
                    filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: isinstance(x, str) and keyword in x)]            
                       
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
                'freeVersionTrialOptioncheckbox': 'freeVersionTrialOption'
            }

            filter_df= checkbox_filter(form, checkbox_column_map, filter_df)
            
            if form.MGSC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['governmentSecurityClearances'] == form.MGSC_RadioButtons.data]
            if form.SSCC_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['staffSecurityClearanceChecks'] == form.SSCC_RadioButtons.data]
            if form.Supplier_RadioButtons.data:
                filter_df = filter_df.loc[filter_df['resellingType'] == form.Supplier_RadioButtons.data]

            metricsHow_checkbox_mapping = {'apicheckbox': 'api',
                                           'real_timecheckbox': 'real_time',
                                           'regular_reportscheckbox': 'regular_reports',
                                           'on_requestcheckbox': 'on_request'}
            
            for checkbox, keyword in metricsHow_checkbox_mapping.items():
                if getattr(form, checkbox).data:
                    print(f'{checkbox} is selected.')
                    filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: isinstance(x, str) and keyword in x)]            
                       
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


