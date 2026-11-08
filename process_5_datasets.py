import os
import csv
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ambiguity_framework import AmbiguityPipeline
from run_pipeline import results_to_dataframe

# Define the 5 datasets text
DATASET_1_TEXT = """As a Data user, I want to have the 12-19-2017 deletions processed.
As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.
As a UI designer, I want to report to the Agencies about user testing, so that they are aware of their contributions to making Broker a better UX.
As a UI designer, I want to move on to round 2 of DABS or FABS landing page edits, so that I can get approvals from leadership.
As a UI designer, I want to move on to round 2 of Homepage edits, so that I can get approvals from leadership.
As a UI designer, I want to move on to round 3 of the Help page edits, so that I can get approvals from leadership.
As a Developer , I want to be able to log better, so that I can troubleshoot issues with particular submissions and functions.
As a Developer, I want to add the updates on a FABS submission to be modified when the publishStatus changes, so that I know when the status of the submission has changed.
As a DevOps engineer, I want New Relic to provide useful data across all applications.
As a UI designer,  I want to move on to round 2 of the Help page edits, so that I can get approvals from leadership.
As a UI designer, I want to move on to round 2 of Homepage edits, so that I can get approvals from leadership.
As a Broker user, I want to Upload and Validate the error message to have accurate text.
As a Broker user, I want the D1 file generation to be synced with the FPDS data load, so that I don't have to regenerate a file if no data has been updated.
As a Website user, I want to access published FABS files, so that I can see the new files as they come in.
As an owner, I want to be sure that USAspending only send grant records to my system.
As a Developer, I want to update the Broker validation rule table to account for the rule updates in DB-2213.
As a Developer, I want to add the GTAS window data to the database, so that I can ensure the site is locked down during the GTAS submission period.
As a Developer, I want D Files generation requests to be managed and cached, so that duplicate requests do not cause performance issues.
As a user, I want to access the raw agency published files from FABS via USAspending.
As an Agency user, I want to be able to include a large number of flexfields without performance impact.
As a Broker user, I want  to help create content mockups, so that I can submit my data efficiently.
As a UI designer, I want to track the issues that come up in Tech Thursday, so that I know what to test and what want s to be fixed.
As an Owner, I want to create a user testing summary from the UI SME, so that I can know what UI improvements we will follow through on.
As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.
As a UI designer, I want to schedule user testing, so that I can give the testers advanced notice to ensure buy-in.
As an Owner, I want to design a schedule from the UI SME, so that I know the potential timeline of the UI improvements wanted.
As an Owner, I want to design an audit from the UI SME, so that I know the potential scope of the UI improvements want ed.
As a Developer, I want to prevent users from double publishing FABS submissions after refreshing, so that there are no duplicates.
As an data user, I want to receive updates to FABS records.
As an Agency user, I want to be able to include a large number of flexfields without performance impact.
As a Developer , I want to update the FABS sample file to remove FundingAgencyCode after FABS is updated to no longer require the header.
As an agency user, I want to ensure that deleted FSRS records are not included in submissions.
As a website user, I want to see updated financial assistance data daily.
As a user, I want the publish button in FABS to deactivate after I click it while the derivations are happening, so that I cannot click it multiple times for the same submission.
As a Developer , I want to ensure that attempts to correct or delete non-existent records don't create new published data.
As an Owner, I want to reset the environment to only take Staging MAX permissions, so that I can ensure that the FABS testers no longer have access.
As a user, I want the flexfields in my submission file to appear in the warning and error files when the only error is a missing required element.
As a user, I want to have accurate and complete data related to PPoPCode and PPoPCongressionalDistrict.
As an agency user, I want the FABS validation rules to accept zero and blank for loan records.
As an Agency user, I want FABS deployed into production, so I can submit my Financial Assistance data.
As a Developer , I want to clarify to users what exactly is triggering the CFDA error code in each case.
As an agency user, I want to be confident that the data coming from SAM is complete.
As a Developer , I want my domain models to be indexed properly, so that I can get validation results back in a reasonable amount of time.
As an agency user, I want the FABS validation rules to accept zero and blank for non-loan records.
As a broker team member, I want to make some updates to the SQL codes for clarity.
As an agency user, I want to have all derived data elements derived properly.
As a broker team member, I want to add the 00***** and 00FORGN PPoPCode cases to the derivation logic.
As a data user, I want to see the office names derived from office codes, so that I can have appropriate context for understanding them.
As a broker user, I want the historical FABS loader to derive fields, so that my agency codes are correct in the PublishedAwardFinancialAssistance table.
As a broker team member, I want to ensure the Broker resources, validations, and P&P pages are updated appropriately for the launch of FABS and DAIMS v1.1.
As a Developer, I want the data loaded from historical FABS to include the FREC derivations, so that I can have consistent FREC data for USASpending.gov.
As a user, I don't want to see NASA grants displayed as contracts.
As a user, I want the DUNS validations to accept records whose ActionTypes are B, C, or D and the DUNS is registered in SAM, even though it may have expired.
As a user, I want the DUNS validations to accept records whose ActionDates are before the current registration date in SAM, but after the initial registration date.
As a broker team member, I want to derive FundingAgencyCode, so that the data quality and completeness improves.
As an agency user, I want the maximum length allowed for LegalEntityAddressLine3 to match Schema v1.1.
As an agency user, I want to use the schema v1.1 headers in my FABS file.
As a agency user, I want to map the FederalActionObligation properly to the Atom Feed.
As a Broker user, I want to have PPoPZIP+4 work the same as the Legal Entity ZIP validations.
As a FABS user, I want to link the SAMPLE FILE on the "What you want  to submit" dialog to point to the correct file, so that I have an accurate reference for my agency submissions.
As an Agency user, I want FPDS data to be up-to-date daily.
As a user, I want to access the raw agency published files from FABS via USAspending.
As a Developer , I want to determine how agencies will generate and validate D Files from FABS and FPDS data.
As a user, I want to generate and validate D Files from FABS and FPDS data.
As an Agency user, I want the header information box to show updated date AND time, so that I know when it was updated.
As an Agency user, I want to receive a more helpful file-level error when I upload a file with the wrong extension.
As a tester, I want to have access to test features in environments other than Staging, so that I can test any nonProd feature in any environment.
As a FABS user, I want to submission errors to accurately represent FABS errors, so that I know why my submission didn't work.
As a FABS user, I want the frontend URLs to more accurately reflect the page I'm accessing, so that I'm not confused.
As an Agency user, I want all historical Financial Assistance data loaded for FABS go-live.
As a Developer , I want the historical FPDS data loader to include both extracted historical data and FPDS feed data.
As an Agency user, I want historical FPDS data loaded.
As an Agency user, I want to accurately see who created a submission, so that I'm not confused about who last updated a submission.
As an agency user, I want to get File F in the correct format.
As an Agency user, I want to better understand my file-level errors.
As a Developer , I want to provide FABS groups that function under the FREC paradigm.
As a tester, I want to ensure that FABS is deriving fields properly through a robust test file plus a follow up check.
As an owner, I only want zero-padded fields, so that I can justify padding.
As a Broker user, I want to submit records for individual recipients without receiving a DUNS error.
As a user, I want more information about how many rows will be published prior to deciding whether to publish.
As a Developer, I want to prevent duplicate transactions from being published and deal with the time gap between validation and the publishing decision.
As a FABS user, I want to submit a citywide as a PPoPZIP and pass validations.
As a Broker user, I want to have updated error codes that accurately reflect the logic and provide enough information, so that I can fix my submission.
As an agency user, I want to leave off the last 4 digits of the ZIP without an error, so that I can complete my submissions.
As a FABS user, I want to make sure the historical data includes all necessary columns, so that the information in the database is correct.
As a data user, I want to access two additional fields from the FPDS data pull.
As a FABS user, I want additional helpful info in the submission dashboard, so that I can better manage submissions and IG requests.
As a FABS user, I want to download the uploaded FABS file, so that I can get the uploaded file.
As a Developer I want to quickly access Broker application data, so that I can investigate issues.
As a Developer , I want to determine the best way to load historical FPDS data, so that I can load all FPDS data since 2007.
As a FABS user, I want the language on FABS pages to be appropriate for me, so that I am not confused.
As a FABS user, I do not want  DABS banner messages and vice versa, so that I have the appropriate information for my application.
As a FABS user, I want to have read-only access to DABS, so that I can view DABS pages without wanting two sets of permissions.
As a FABS user, I want to have my validations run in a reasonable amount of time.
As a FABS user, I want to see correct status labels on the Submission Dashboard, so that I can quickly see my submission history.
As an agency user, I want to know when the submission periods start and end, so that I know when the submission starts and ends.
As an agency user, I want a landing page to navigate to either FABS or DABS pages, so that I can access both sides of the site.
As an agency user, I want to submit my data elements surrounded by quotation marks, so that Excel won't strip off leading and trailing zeroes."""

DATASET_2_TEXT = """As a Public User, I want to Search for Information, so that I can obtain publicly available information concerning properties, County services, processes and other general information.
As a ProspectiveApplicant, I want to research requirements and to select a service, so that I can find the relevant service and/or application type to initiate via the online portal.
As an Applicant, I want to Request PreApplication Assistance, so that I can receive a response to a request for a meeting or information that is a result of the preapplication assistance.
As a Customer, I want to Create a Customer Portal User Account, so that I can log on to the Customer Portal and perform transactions that first require user authentication.
As an Applicant, I want to Submit Application, so that I can provide my information, plans and/or documents to initiate a transaction with the County.
As an Applicant, I want to Submit Supporting Documentation, so that I can satisfy documentation requirements for my application.
As an Applicant, I want to Pay Fee, so that I can satisfy outstanding charge associated with the service requested or received from the County.
As an Applicant, I want to Check the Status of a transaction, so that I can understand where the provisioning of my service is in the process, such as information related to service levels, fees, plan review, permit, or inspection results.
As an Applicant, I want to Modify my Application, so that I can successfully change information on an application.
As a Staff member, I want to Perform a Completeness Review, so that I can validate when an application is complete and eligible for further technical review.
As a Staff member, I want to Record an Internal Note, so that I can share information with other Staff collaborating on the record.
As a Staff member, I want to Assign an Application for Detailed Review, so that I can review the for compliance and subsequently approved or denied.
As a Staff member, I want to Apply a Hold, so that I can prevent progression through the workflow or other actions in the system until the issue is resolved.
As a Staff member, I want to Remove a Hold, so that I can allow progression through the workflow or other actions in the system now that the issue has been resolved.
As a Staff member, I want to Send a Formal Response to Applicant, so that I can satisfy communication and records responsibilities.
As a Staff member, I want to Track  the Draft Proffers, so that I can preserve the history of draft proffer statements submitted by the Applicant.
As a Staff member, I want to Manage Approved Proffers, so that I can ensure compliance with and satisfaction of the proffer in the future.
As a Staff member, I want to Manage Ordinances, so that I can maintain accurate ordinance information in the System.
As a Staff member, I want to Schedule a Meeting, so that I can bring the required parties together at a specific date/time to address an issue.
As a staff member, I want to denote an application with a Final Action status. So that I can finish it.
As a Planning Staff member, I want to Conduct and Track Plan Amendments and Planning Studies, so that I can record work in process, outcome, and location-based information related to the Plan(s).
As a Planning Staff member, I want to Generate Planning-related Reports, so that I can access, analyze and/or export the needed information in the format I requested.
As a Planning Staff member, I want to Evaluate Consistency with the Comprehensive Plan, so that I can complete my required review of a plan set and/or application.
As a Staff member, I want to Perform a Staff Review, so that I can validate compliance of an application with the Zoning Ordinance and impact approval/denial of the application accordingly.
As a Zoning Staff member, I want to Process the Requests for Zoning Information, so that I can capture my response to the request in the system and also send a communication from the system to the Applicant.
As a Zoning Staff member, I want to Issue the Zoning-Related Permits, so that I can satisfy an Applicant's request for service that has proven to be eligible and in compliance with the Zoning Ordinance.
As a Staff member, I want to Develop a Staff Report, so that I can publish and distribute the report according to business rules.
As a Staff member, I want to Manage Hearing Calendars, so that I can track hearing-related activities and due dates.
As a Staff member, I want to Assign a Hearing Date, so that I can present the application to the appropriate governing body within the timelines dictated by the relevant County rules and procedures.
As a Staff member, I want to Manage Affidavits, so that I can ensure compliance with the requirements prior to the hearing.
As an Applicant, I want to Satisfy Hearing Requirements, so that I can ensure all pre-hearing requirements are satisfied in time for the hearing.
As a Staff member, I want to Prepare for and Support Hearing Execution, so that I can ensure all pre-hearing requirements are satisfied and staff and Applicant are ready for the hearing.
As a Staff member, I want to Capture a Hearing Decision, so that I can enforce the system.
As a Staff member, I want to Process the Appeals, so that I can track the outcome and record the impact on the relevant records.
As a Plan Review Staff member, I want to Assign Plans for Review, so that I can ensure plans have been assigned to the appropriate Plan Reviewer.
As a Plan Review Staff Supervisor, I want to Manage Plan Reviewer Workload, so that I can monitor and effectively adjust workload as necessary and ensure service levels are met
As an Applicant, I want to Request a Plan Review Meeting, so that I can meet with the Plan Review Staff regarding the plan review.
As a Plan Review Staff member, I want to successfully Conduct a Plan Review Meeting with the Applicant and record the outcome, so that I can listen to it again.
As a Plan Review Staff member, I want to Review Plans, so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant.
As an Applicant, I want to Resubmit Plans, so that I can review revised plans. 
As a Plan Review Staff Member, I want to Review the Code Modifications submitted by the Applicant, so that I can review the request and if approved, associate it with the appropriate project.
As a Plan Review Staff member, I want to Track the Completion of Required Plan Reviews, so that I can ensure all plan review tasks are completed, results have been sent to the Applicant and any downstream steps are initiated such has a final review or payment for permit issuance.
As a Development Staff member, I want to Issue a Development-related Permit, so that I can grant the request to the Applicant to begin work
As a Staff member, I want to Manage Bonds, so that I can track and manage bonds throughout the lifecycle of the project until release.
As an Applicant, I want to Complete Building Development Project, so that I can receive any posted bond and/or obtain occupancy.
As an Applicant, I want to Complete Building Development Project, so that I can receive any posted bond and/or obtain occupancy.
As a Customer, I want to Request Inspection, so that a County inspector is assigned to perform an inspection of my project.
As an Inspection Staff member, I want to Create an Inspection, so that I can schedule and assign the inspection.
As an Inspection Staff Supervisor, I want to Assign Inspections, so that I can make sure the appropriate Inspector receives the work.
As an Inspection Supervisor, I want to Manage Inspector Workload, so that I can meet service level and quality requirements.
As an Inspector, I want to Conduct Inspections, so that I can validate Customer compliance with code and regulations and provide results of the inspection to the Customer.
As an Enforcement Staff member, I want to Issue a Notice of Violation, so that I can provide formal communication to the responsible party.
As a l Staff member, I want to search for Property information, so that I can obtain all associated current and historic owners, permits, and applications.
As a Staff member, I need to be notified when Geospatial attributes change, so that I can ensure that I am reviewing the permit/application to the most current data and appropriate standards.
As a County Staff Member, I want to create a custom query/report outside of the common querying/reporting functionality, so that I can fulfill a request.
As a Staff member, I want to create each condo unit, so that I can associate it to the child parcel and address after the condominiums are recorded in the system.
As a Technical Staff member, I want to update the GIS Property Management, so that I can successfully update the transactional Parcel Pin to reference the GIS layer where the Split or Merged Parcel Pin exists.
As a Staff member, I want to Send or Post Citations and Fines, so that I can successfully send the Notice Of Violation document to the property owner and log information about the action."""

DATASET_3_TEXT = """As a user, I want to click on the address, so that it takes me to a new tab with Google Maps.
As a user, I want to be able to anonymously view public information, so that I know about recycling centers near me before creating an account.
As a user, I want to be able to enter my zip code and get a list of nearby recycling facilities, so that I can determine which ones I should consider.
As a user, I want to be able to get the hours of each recycling facility, so that I can arrange drop-offs on my off days or during after-work hours.
As a user, I want to have a flexible pick up time, so that I can more conveniently use the website.
As a user, I want to be able to select different types of recyclable waste, so I have and get a list of facilities that accept each type and their opening hours, so that I can find an optimal route and schedule.
As a user, I want to add donation centers as favorites on my profile, so that I can view them later.
As a user, I want to be able to give my email ID, so that I can receive notifications for new events as they are posted.
As a user, I want to be able to view a map display of the public recycling bins around my area.
As a user, I want to be able to view a map display of the special waste drop off sites around my area.
As a user, I want to be able to view the safe disposal events currently being organised around my area.
As a user, I want to choose a flexible pick up time, so that I can more conveniently use the website.
As a user, I want to view user documentation for the website, so that I know how to use the web app.
As a user, I want to get feedback when I enter an invalid zip code.
As a user, I want to be able to create an acocunt, so that I can create my own profile.
As an admin, I want to be able to add or remove recycling facilities' information, so that users get the most recent information.
As an admin, I want to be able to read users' feedback and complaints, so that we can add more features and keep improving the service we provide to them.
As a user, I want to be able to check transaction history and keep a record of it, so that I can go back when needed.
As a user, I want to have a great UI and UX from the sites, so that I have a pleasant experience when navigating through them.
As a user, I want to be able to access the site and do all the other stuffs on all of my electronic devices.
As an admin, I want to be able to block specific users based on IP address, so that I can prevent spamming on the websites.
As an admin, I want to view a dashboard that monitors all the sites' statuses, so that I can have a sense of what people are doing on our sites and know the service status.
As an admin, I want to have all data encrypted, so that important information will not be stolen during a server breach or an attack.
As an executive, I want to have full access to data related to my company, so that I can have a sense of my company's performance.
As an employee, I want to access the route planning system during work, so that I can be guided through the neighbourhood.
As an employee from the HR department, I want to have access to the full information of all employees working for this business.
As a developer, I want to access an API from the website, so that I can integrate it and implement certain features in my own iOS application.
As a user, I want to be able to receive tempting rewards, so that I have a reason to use the website.
As a user, I want to have my personal information kept securely in the database of the website, so that I will not suffer from identity theft or telephone harassment.
As an admin, I want to handle all users' activities, so that I can manage more efficiently.
As a company, I want to have a website that is easy to use, so that I can upload or delete stuff step by step.
As an employee, I want to get quick notifications, so that I can process cases the first time.
As a company accountant, I want to view all available activity fees online, so that I can easily create a bill statement.
As a developer, I want to use bootstrap in the process of developing, so that I can easily design my website.
As a developer, I want to attend some UI/UX lessons, so that I can develop an awesome and beautiful features website.
As a user, I want to view all locations of recycling centers on a map, so that I can check which routes to take to drop off waste.
As a user, I want to upload my week's schedule, so that I can get recommendations for recycling centers that best fit my availability.
As a user, I want to link my email account to my profile, so that I can get a temporary password in case I forget my own one.
As a user, I want to contact the administrators, so that I can give feedback or ask for help.
As an admin, I want to add recycling center information, so that I can keep the database up-to-date over time.
As an admin, I want to view user error logs, so that I can fix or review any issues that are being faced by users of the system.
As an admin, I want to onboard recycling centers on the platform, so that I can increase information accuracy.
As a superuser, I want to update the recycling center information, so that I can provide the latest information about the recycling center.
As a superuser, I want to view users' stats, so that I can view in real-time how many users have visited my recycling center information and their recyclable waste.
As a superuser, I want to reply to user questions, so that I can answer any questions about my recycling center.
As an admin, I want to be able to have a dashboard that shows usage stats and locations, so that I can identify the neighbourhoods with the largest number of drop-offs and to try getting more facilities involved.
As an admin, I want to be able to communicate directly with facilities, so that I can keep them updated about features we have on our website.
As a user, I want to be able to browse through the list of facolities and see which ones are environment-friendly, so that I can know for sure my waste is not going to leave a negative ecological footprint.
As a recyclingfacility representative, I want to be able to update my information and the type of material I accept, so that I can avoid any miscommunication with users.
As a recyclingfacility representative, I want to have access to user stats and schedules, so that I can adjust my hours and/or upgrade equipment and capacity in order to be able to accomodate larger amounts of recyclable materials.
As a recyclingfacility, I want to be able to communicate directly with the site admin and convey any issues or concerns I have, so that they fix them."""

DATASET_4_TEXT = """As a Data Publishing User, I want to be able to edit a dataset I have published, So that I can correct or enhance existing data.
As a Data Publishing User, I want to be able to edit the model of data I have already imported, So that I can fix bugs or make enhancements in the API built for my data.
As a Data Publishing User, I want to be able to delete a dataset I have published, So that I can remove unwanted data from OpenSpending.
As a Platform Administrator, I want to be able to Hide any dataset already added as Public, So that I can maintain Public/Hidden status for other users.
As a Platform Administrator, I want to have a view on all datasets published by all users, So that I can perform management actions on any dataset.
As a Platform Administrator, I want to be able to delete any dataset published, So that I can deal with takedown requests, or clean up test datasets.
As a Data Publishing User, I want to be able to edit the data source of data I have already imported, So that I can fix bugs or make enhancements in the API built for my data.
As a Data Publishing User, I want to have the Packager support Constants, So that I can model dimensions that may not exist in the source file.
As a Data Publishing User, I want to be able to import data in Excel, So that I do not have to convert data formats in order to use the data packager.
As a Data Publishing User, I want to know what my data needs to be able to be visualised on a map, So that I can visualise it on a map.
As a Data Publishing User, I want to be able to import data in JSON, So that I do not have to convert data formats in order to use the data packager.
As a Data Publishing User, I want to be able to import data from a Google Spreadsheet, So that I do not have to convert data formats in order to use the data packager.
As a Data Publishing User, I want to be able to import data from Fiscal Data Package descriptor file, So that I do not have to convert data formats in order to use the data packager.
As a Data Publishing User, I want to be able to provide the Platform Administrator with additional GeoJSON sources, So that I can improve the map-based visualisations of my data.
As a Data Consuming User, I want to be able to filter, sort and aggregate data by multiple dimensions and measures, So that I can get more granular views on the data.
As a Data Consuming User, I want to be able to download a CSV of the data that is used in any visualisation I am viewing, So that I can use the data in other tools.
As a Data Consuming User, I want to be able to change the display of all monetary measures across a set of currencies, So that I can understand localised amounts in non-localised figures.
As a Data Consuming User, I want to see textual descriptions that accompany embedded visualisations, So that I can more easily understand what I am viewing.
As a Data Consuming User, I want to be able to share a view state as a URL to social networks, So that I can share data that I have found with others.
As a Data Consuming User, I want to be able to download an image ofa particular view state, So that I can use it offline.
As a Data Consuming User, I want to be able to share an image of a particular view state to the social networks that support this, So that I can provide richer context in those communication channels for data I am sharing.
As a Data Consuming User, I want to be able to have stepped zoom on map visualisations, So that I can have better control over the navigation experience inside a map view.
As a Data Consuming User, I want to have consistent use of colour on map visualisations, So that I can better understand the visual logic of the map view.
As a Developer, I want to be able to customise the Brand Name and Icon, and Primary Color of all frontend Javascript apps, So that I can customise the branding for my own needs.
As an API User, I want to be able to understand if a user is a Publisher, So that I can offer functionality based on Dataset Publisher privileges.
As an API User, I want to be able to understand if a user is an Administrator, So that I can offer functionality based on Platform Administration privileges.
As an API User, I want to be able to get bordering regions|cities when I query a region|city, So that I can provider wider visual context for mapping visualisations.
As an API User, I want to be able to dynamically request polygons based on the query made, So that I can provide maps that match the query.
As an API User, I want to have a flexible API using HASC codes for countries, regions and cities, So that I can visualise budget data on maps.
As an API User, I want to be able to get a CSV output of any cube-based query, So that I can use work with tools that read CSV.
As an API User, I want to be able to get a set of monetary measures transferred to different currencies, So that I can use this in scenarios that might enable comparison by normalisation.
As an API User, I want to be able to use metadata to get results from multiple datasets, So that I can build user experiences based on more than one dataset more easily.
As an API User, I want to be able to use data to get results from multiple datasets, So that I can build user experiences based on more than one dataset more easily.
As an API User, I want to be able to normalise measures by population, So that I work with datasets in reference to their contextual constraints.
As an API User, I want to be able to normalise measures by geographical area, So that I work with datasets in reference to their contextual constraints.
As an API User, I want to be able to normalise measures by GDP, so I work with datasets in reference to their contextual constraints.
As an API User, I want to be able to normalise measures by GINI and related socioeconomic indexes, So that I work with datasets in reference to their contextual constraints.
As an API User, I want to be able to get a relative percentage of a measure to the total of the dataset it comes from, So that I can build alternative displays of the data.
As an API User, I want to be able to persistently store visualisation state in the database, So that such can be shared more easily and contribute to a visualisation gallery.
As a Data Publishing User, I want to have my dataset update automatically as the source file/files changes, So that OpenSpending always shows current data.
As an OpenSpending Community Member, I want to have a blog that highlights any and all projects in the open fiscal space, So that I can relate to openspending.org as the central hub of fiscal openness.
As a User, I want to be able to set my own username, So that my data is more easily discoverable.
As a Data Publishing User, I want to be able to add a dataset in a Hidden state, So that I can work on a dataset before having it discoverable via OpenSpending user interfaces.
As a Data Publishing User, I want to be able to Hide a dataset that I have already added as Public, So that I can fix my mistakes or have a dataset primarily for my own use.
As a Data Publishing User, I want to have a view on all the datasets I have published, So that I can perform management actions on my own datasets.
As a Data Publishing User, I want to have a functioning Python Client, So that I can add data to the datastore in bulk from the command line or my own programs.
As an OpenSpending Community Member, I want to have an app where I can find examples of use of fiscal data visualisations, So that I can find guidance in creating my own with Open Spending.
As a Data Publishing User, I want to know if my CSV file is valid, So that I can fix possible data issues before publishing it on Open Spending.
As a Data Consuming User, I want to be able to search any dataset published and publicly accessible by their title and metadata, So that I can find the datasets I'm interested in.
As a Data Consuming User, I want to visualize by default in treemap, bubble tree, map and pivot table the most recent year when my dataset contain multiple years, So that I'm not confused with the amounts.
As an API user, I want to be able to change the colors of the embedded visualisations in my own platform, So that I can customize the visualisations.
As an API user, I want to be able to change some of the styling of the embedded Viewer in my own platform, So that I can brand it to my own organisation's color scheme.
As a Platform administrator, I want to be able to translate the data types hierarchies of the Viewer while in embed mode, So that my users can understand the interface in their native language."""

DATASET_5_TEXT = """As a Developer, I want to get a Data Package into Node, so that I can start using the data for doing analysis and visualizations.
As a Researcher, I want to get a Data Package into Julia in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Publisher, I want to add type information to my data, so that it is more useful to others and can be used better with tools like visualization programs. 
As a Publisher, I want to be able to provide a visualization of data in the Data Package, so that I can provide my analysis and show my work to users of the data. 
As a Researcher, I want to be able to save new visualizations, so that I can share them with others or include them in the Data Package. 
As a ResearcherPublisher, I want to know that my data conforms to its Data Package profile, so that I can feel trust in the validity and usefulness of the data. 
As a ResearcherPublisher, I want to understand the ways in which my data is invalid, so that I can know how to fix it. 
As a Researcher, I want to get a Data Package into R in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Researcher, I want to get a Data Package into Excel in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Researcher, I want to get a Data Package into SPSS in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Researcher, I want to get a Data Package into STATA in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Researcher, I want to be able to translate my EML dataset to a Data Package, so that I can benefit from the wide array of tools available for Data Packages. 
As a Researcher, I want to get a Data Package into LibreOffice/OpenOffice in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Developer, I want to get a Data Package into Python in seconds, so that I can start using the data for doing analysis and visualizations. 
As a Developer, I want a jQuery plugin for Core Data Packages, so that I can use it to apply to form control that uses a core dataset for autocompletion. 
As a Researcher, I want to get my Excel spreadsheet into a Data Package, so that I can benefit from better tooling and standardization. 
As a Developer, I want to do exploratory data analysis in R and operationalize that analysis in Python, so that I can use the best tool for the job.
As a Developer, I want to get a Data Package into Clojure in seconds, so that I can start using the data in doing analysis and visualizations. 
As a Developer, I want to get a Data Package into Julia in seconds, so that I can start using the data in doing analysis and visualizations. 
As a Developer, I want to get a Data Package into C++ in seconds, so that I can start using the data in doing analysis and visualizations. 
As a Machine Learning expert, I would like to package ML datasets as data packages, so that I can easily import them into my ML platform, so that I can start using the data in doing analysis. 
As a Developer, I want an Elasticsearch integration, so that I can integrate data-packaged data with pipelines that use Elasticsearch. 
As a Developer, I want an SPSS integration, so that I can integrate data-packaged data with pipelines that use SPSS. 
As a Developer, I want an EPrints integration, so that I can integrate data-packaged data with pipelines that use EPrints. 
As a Developer, I want a Mongo integration, so that I can integrate data-packaged data with pipelines that use Mongo. 
As a Developer, I want a DAT integration, so that I can integrate data-packaged data with pipelines that use DAT. 
As a ResearcherGovernment Publisher, I want to add general reference data to my narrow dataset, so that my dataset is more useful. 
As a ResearcherGovernment Publisher, I want to add general country names to my dataset that only contains country codes, so that my dataset is more readable. 
As a ResearcherGovernment Publisher, I want to add reference data on inflation to my spending dataset, so that the spending lines in my dataset is more understandable. 
As a ResearcherGovernment Publisher, I want to map lines in my dataset using geographic data in my dataset, so that my dataset is more engaging for non-technical users. 
As a Researcher, I want to be able to reference a remote-controlled vocabulary for my dataset, so that I can be sure that column of my dataset are valid against a single shard list of terms. 
As a developer, I want an DSpace integration, so that I can integrate data-packaged data with pipelines that use Dspace. 
As a Developer, I want Feather integration, so that I can integrate data-packaged data with pipelines that use Feather. 
As a Developer, I want HDF5 integration, so that I can integrate data-packaged data with pipelines that use HDF5.
As a Researcher, working with data, I want an Microsoft Power BI integration, so that I can import datasets without downloading them locally. 
As a ResearcherPublisher, I want an integration with Zenodo, so that when I store my dataset in GitHub, I don’t have to retype descriptive information about my dataset. 
As a Publisher, I would like an integration with Open Refine, so that I can output cleaned Data Packages. 
As a ResearcherPublisher, I want to publish Data Packages to CKAN, so that my data is findable, and I can have a data API. 
As a ResearcherDeveloper, would like the ability import/export from MS-SQL, so that I can use Data Packages in workflows that involve MS-SQL. 
As a Researcher, working with data in NetCDF, I want NetCDF integration, so that I can store my data in plaintext while still retaining its metadata. 
As a Researcher, I want an integration with https://data.mendeley.com/, so that I can validate my data upon ingest to the service.
As a Publisher, I would like an integration with Excel, so that I can output cleaned Data Packages. 
As a Publisher, I want to store my data quickly and easily online. 
As a Repository Manager, I want a tool that makes it easy for researchers/ users to add basic metadata to their research data, so that it is more findable and therefore useful. 
As a ResearcherPublisher, I want validate my data with a minimum of clicks, so that I can feel trust in the validity and usefulness of the data. 
As a publisher, I want to be able to check that every time I update my data it is still good, so that I can catch errors early and store reliable data. 
As a DeveloperWrangler, I want to use a command line tool that allows met to validate data, so that I can feel trust in the validity and usefulness of the data quickly and in the context of my command line workflow. 
As a developer, I want an online service that is connected to my data repository that validates data on update, so that I can delegate data validation to a third party. 
As a government Publisher, I want to make it easy to prove that our published data is valid, so that I can claim that we are living up to our transparency commitments. 
As a Civic Tech Activist, I want to make it easy to assess the quality of data stored by the government, so that I can make sure that government is living up to its transparency commitments. 
As a publisher, I want to embed an interactive preview of my data on my site, so that users can be encouraged that this is the correct data for them. 
As a publisher, I want to embed a preview button on my site, so that users can preview the data and be encouraged that this is the correct data for them.
As a Publisher, I want to know how many users have previewed a dataset, so that I know how interest in a dataset relates to its actual download numbers. 
As a Developer, I want to customize an existing wizard for my specific type of data, so that I can give my users a great user experience.
As a Publisher, I want to add useful metadata or add in new data columns to make the dataset more useful. 
As a publisher, I want to package reproducible steps to get a certain data state, so my methodology is transparent and can be rerun by others. 
As a DeveloperDataWrangler, I want to store my Data Package in GitHub and have it automatically stored into CKAN, so that I get a data API and my dataset is listed in a relevant catalog. 
As a Researcher, I want a tool that can generate basic statistics about a dataset, so that I can get a quick preview of the data. 
As a DeveloperPublisher, I want a tool to create an embeddable data summary via iframe, so that I can embed data summaries across sites. 
As a Researcher, I want an app that generates an OpenRefine reconciliation API endpoint from a Tabular Data Package, so that I can use it to clean messy data. 
As a Researcher, I want an app that create proxy Data Packages for well know and reliable data, sources, so that I can load high quality data using Data Package tooling. 
As a RepositoryManagerResearcher, I want an app that acts as a match-making service for packaging data, so that owners are paired with data packagers. 
As a developer, I would like to create a web socket protocol for Frictionless data tools, so that I can easily use data packages with additional data analysis tools. 
As a Publisher, I would like a tool to check data availability persistence after publication. 
As a ResearcherPublisher, I want to specify the funding that contributed to the creation of a given dataset, so that funding agencies can identify the funding, source for a given dataset. 
As a ResearcherPublisher, I want to add a DOI to a dataset, so that I can cite it in papers stored  with the data."""

DATASETS = [
    {"id": "ds1_usaspending_broker", "title": "USASpending & Broker System", "text": DATASET_1_TEXT},
    {"id": "ds2_county_services", "title": "County & Municipal Services", "text": DATASET_2_TEXT},
    {"id": "ds3_recycling_app", "title": "Smart Recycling & Waste Management", "text": DATASET_3_TEXT},
    {"id": "ds4_open_spending", "title": "OpenSpending Fiscal Data Platform", "text": DATASET_4_TEXT},
    {"id": "ds5_data_packages", "title": "Data Packages & Frictionless Tooling", "text": DATASET_5_TEXT},
]

def save_datasets():
    os.makedirs("datasets", exist_ok=True)
    for ds in DATASETS:
        lines = [line.strip() for line in ds["text"].split("\n") if line.strip()]
        csv_path = os.path.join("datasets", f"{ds['id']}.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["requirement_sentence"])
            for line in lines:
                writer.writerow([line])
        print(f"Saved {len(lines)} sentences to {csv_path}")

def run_multi_dataset_pipeline():
    save_datasets()
    os.makedirs("outputs", exist_ok=True)
    
    pipeline = AmbiguityPipeline(ambiguity_threshold=0.0)
    all_sentences = []
    dataset_sentences_map = {}

    for ds in DATASETS:
        csv_path = os.path.join("datasets", f"{ds['id']}.csv")
        df = pd.read_csv(csv_path)
        col = 'requirement_sentence' if 'requirement_sentence' in df.columns else df.columns[0]
        sents = [s.strip() for s in df[col].dropna().astype(str).tolist() if len(s.strip()) >= 15]
        dataset_sentences_map[ds['id']] = sents
        all_sentences.extend(sents)

    print(f"Fitting pipeline shared TF-IDF vocabulary across all 5 datasets ({len(all_sentences)} total sentences)...")
    pipeline.fit_vocabulary(all_sentences)

    benchmark_summary = []

    # 1. Run per-dataset evaluation
    for ds in DATASETS:
        ds_id = ds["id"]
        ds_title = ds["title"]
        sents = dataset_sentences_map[ds_id]
        out_dir = os.path.join("outputs", ds_id)
        os.makedirs(out_dir, exist_ok=True)

        print(f"\n[Processing {ds_id}] ({len(sents)} sentences)...")
        results = pipeline.analyse_corpus(sents)
        df_res = results_to_dataframe(results)

        operating_threshold = float(df_res["ambiguity_score"].quantile(0.70))  # Top 30% percentile
        df_res["is_ambiguous"] = df_res["ambiguity_score"] >= operating_threshold
        df_res.loc[~df_res["is_ambiguous"], "ambiguity_type"] = "None"
        df_res.loc[~df_res["is_ambiguous"], ["top_sense_2_domain", "top_sense_2_gloss"]] = ""

        # Export CSVs
        df_res.to_csv(os.path.join(out_dir, "ambiguity_report_full.csv"), index=False)
        df_flagged = df_res[df_res["is_ambiguous"]].sort_values("ambiguity_score", ascending=False)
        df_flagged.to_csv(os.path.join(out_dir, "ambiguity_report_flagged.csv"), index=False)

        # Charts
        counts = df_res["ambiguity_type"].value_counts()
        plt.figure(figsize=(6, 4))
        counts.plot(kind="bar", color=["#2BC4B8", "#E8935A", "#6E7F91"])
        plt.title(f"Ambiguity Type Counts ({ds_title})")
        plt.ylabel("Count")
        plt.xlabel("Ambiguity Type")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "summary_ambiguity_type_counts.png"), dpi=150)
        plt.close()

        n_sents = len(sents)
        n_cands = len(df_res)
        n_flagged = int(df_res["is_ambiguous"].sum())
        n_inter = int((df_res["ambiguity_type"] == "Inter-Domain").sum())
        n_intra = int((df_res["ambiguity_type"] == "Intra-Domain").sum())
        top_words = df_res[df_res["is_ambiguous"]]["word"].value_counts().head(10).to_dict()

        summary_txt = (
            f"Dataset Title:                 {ds_title}\n"
            f"Dataset ID:                    {ds_id}\n"
            f"Operating Point:               Score >= {operating_threshold:.3f} (Top 30%)\n"
            f"Sentences Analysed:            {n_sents}\n"
            f"Candidate Word Instances:      {n_cands}\n"
            f"Flagged Ambiguous Instances:   {n_flagged} ({(n_flagged/n_cands*100 if n_cands else 0):.1f}%)\n"
            f"  - Inter-Domain:              {n_inter}\n"
            f"  - Intra-Domain:              {n_intra}\n"
            f"\nTop 10 Flagged Words:\n" + "\n".join([f"  {w}: {c}" for w, c in top_words.items()]) + "\n"
        )
        with open(os.path.join(out_dir, "summary.txt"), "w") as f:
            f.write(summary_txt)

        benchmark_summary.append({
            "dataset_id": ds_id,
            "dataset_title": ds_title,
            "sentences_count": n_sents,
            "candidate_words_count": n_cands,
            "flagged_count": n_flagged,
            "inter_domain_count": n_inter,
            "intra_domain_count": n_intra,
            "operating_threshold": round(operating_threshold, 3),
            "top_words": top_words
        })

    # 2. Run Combined Multi-Dataset Benchmark
    print("\n[Running Combined Multi-Dataset Cross-Domain Benchmark]...")
    out_dir_comb = os.path.join("outputs", "combined_all_datasets")
    os.makedirs(out_dir_comb, exist_ok=True)
    results_comb = pipeline.analyse_corpus(all_sentences)
    df_comb = results_to_dataframe(results_comb)

    threshold_comb = float(df_comb["ambiguity_score"].quantile(0.70))
    df_comb["is_ambiguous"] = df_comb["ambiguity_score"] >= threshold_comb
    df_comb.loc[~df_comb["is_ambiguous"], "ambiguity_type"] = "None"
    df_comb.loc[~df_comb["is_ambiguous"], ["top_sense_2_domain", "top_sense_2_gloss"]] = ""

    df_comb.to_csv(os.path.join(out_dir_comb, "ambiguity_report_full.csv"), index=False)
    df_comb[df_comb["is_ambiguous"]].sort_values("ambiguity_score", ascending=False).to_csv(os.path.join(out_dir_comb, "ambiguity_report_flagged.csv"), index=False)

    counts_c = df_comb["ambiguity_type"].value_counts()
    plt.figure(figsize=(6, 4))
    counts_c.plot(kind="bar", color=["#2BC4B8", "#E8935A", "#6E7F91"])
    plt.title("Combined Multi-Dataset Ambiguity Type Counts")
    plt.ylabel("Count")
    plt.xlabel("Ambiguity Type")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir_comb, "summary_ambiguity_type_counts.png"), dpi=150)
    plt.close()

    # Save benchmark overall JSON & CSV
    with open(os.path.join("outputs", "multi_dataset_benchmark_summary.json"), "w") as f:
        json.dump(benchmark_summary, f, indent=2)

    df_bench = pd.DataFrame(benchmark_summary)
    df_bench.to_csv(os.path.join("outputs", "multi_dataset_benchmark_summary.csv"), index=False)
    print("\nProcessing complete for all 5 datasets and combined benchmark!")

if __name__ == "__main__":
    run_multi_dataset_pipeline()
