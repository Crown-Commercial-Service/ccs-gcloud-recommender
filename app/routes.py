from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Flask
from .forms import mainPageform
from .utils import sanitize_input, get_text_embeddings, search_service
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
    form = mainPageform()
    filter_df = df.copy()
    filter_button = 0

    lot_1_no = 0
    lot_2_no = 0
    lot_3_no = 0 
    
    lot_1_name = 'Cloud hosting'
    lot_2_name = 'Cloud software'
    lot_3_name = 'Cloud support'

    if request.method == 'POST':
        print("Form submitted.")

        # if form.validate_on_submit():
        #     print("Form validated.")
        if form.SearchButton.data:
            # Example filter logic: Filter by education pricing
            print('Search button is pressed.')
            query = sanitize_input(form.Searchbar.data)
            filter_df = pd.DataFrame(search_service(query))
            filter_df = filter_df.loc[filter_df['score']>0.82, :]
            filter_button = 1

        elif form.ClearButton.data:
            print('Clear button is pressed. Filters reset.')
            query=''
            return redirect(url_for('main.index'))

        elif form.FilterButton.data:
            filter_df = pd.DataFrame(search_service(query))
            filter_df = filter_df.loc[filter_df['score']>0.82, :]
            filter_button = 1

            if form.Emailcheckbox.data:
                filter_df = filter_df[filter_df['emailOrTicketingSupport'] == True]
            if form.Phonecheckbox.data:
                filter_df = filter_df[filter_df['phoneSupport'] == True]
            if form.webchatcheckbox.data:
                filter_df = filter_df[filter_df['webChatSupport'] == True]
            if form.standardsISOIEC27001checkbox.data:
                filter_df = filter_df[filter_df['standardsISOIEC27001'] == True]
            if form.standardsISO28000checkbox.data:
                filter_df = filter_df[filter_df['standardsISO28000'] == True]
            if form.standardsCSASTARcheckbox.data:
                filter_df = filter_df[filter_df['standardsCSASTAR'] == True]
            if form.standardsPCIcheckbox.data:
                filter_df = filter_df[filter_df['standardsPCI'] == True]
            if form.standardsCyberEssentialscheckbox.data:
                filter_df = filter_df[filter_df['standardsCyberEssentials'] == True]
            if form.standardsCyberEssentialsPluscheckbox.data:
                filter_df = filter_df[filter_df['standardsCyberEssentialsPlus'] == True]
            if form.educationPricingcheckbox.data:
                filter_df = filter_df[filter_df['educationPricing'] == True]
            if form.freeVersionTrialOptioncheckbox.data:
                filter_df = filter_df[filter_df['freeVersionTrialOption'] == True]
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

            metricsHow_checkbox_mapping = {'apicheckbox': 'api',
                                           'real_timecheckbox': 'real_time',
                                           'regular_reportscheckbox': 'regular_reports',
                                           'on_requestcheckbox': 'on_request'}
            
            for checkbox, keyword in metricsHow_checkbox_mapping.items():
                if getattr(form, checkbox).data:
                    print(f'{checkbox} is selected.')
                    filter_df = filter_df[filter_df['metricsHow'].apply(lambda x: isinstance(x, str) and keyword in x)]            
            

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

             
    lot_1_no = filter_df.loc[filter_df['lotName']==lot_1_name,:].shape[0]
    lot_2_no = filter_df.loc[filter_df['lotName']==lot_2_name,:].shape[0]
    lot_3_no = filter_df.loc[filter_df['lotName']==lot_3_name,:].shape[0]

    results = filter_df.to_dict(orient='records')

    return render_template('index.html', 
                           form = form, 
                           results = results, 
                           filter_df_len = len(filter_df),
                           filter_button=filter_button, 
                           query=query,
                           lot_1_no = lot_1_no,
                           lot_2_no = lot_2_no,
                           lot_3_no = lot_3_no)


