import time, json, random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from random import randint
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import luu_function
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Green,Yellow,Red,Commands
from luu_function import driver

# Page



def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Approval------------------------------------------------------")
    driver.get(domain_name + "/approval/list/progress/ireq")
    time.sleep(5)
    Logging("1. Access Menu Approval successfully")
    Commands.Wait10s_ClickElement(data["approval"]["click_list_approval_progress_approval_v3"])
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval_v3"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin


def approval_write_all_form(domain_name):
    Logging("------------------------------------------------------Menu Approval------------------------------------------------------")
    time.sleep(2)
    Logging("---------------- Write All Form ------------------")

    try:
        Commands.Wait10s_ClickElement(data["approval"]["admin_approval_v3"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_all_form_v3"])
        time.sleep(5)
        Logging("2. Click All Forms successfully")
        totaltext=driver.find_element_by_xpath("//span[contains(.,'Total')]").text
        total = totaltext[int(6): int(totaltext.rfind("|"))]
        Logging("---  Total All Form before create new : " + total)
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["approval"]["icon_create_all_form_v3"])
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["approval"]["form_selection_v3"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["folder_approval_v3"])
        Logging("3. Click folder approval successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["agreement_route_v3"])
        Logging("4. Click Agreement Route successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_common_v3"])
        Logging("5. Click Common successfully") 
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["folder_approval_v3"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["hide_list_form_section_v3"])
        try:
            form_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_form_name_v3"])))
            form_name.send_keys(data["approval"]["form_name"])
            title_form_name=form_name.get_attribute("value")
            if(title_form_name==data["approval"]["form_name"]):
                Logging("6. Add Form Name =>pass")
            else:
                Logging("6. Add Form Name =>fail")
            Logging("7. Input Add Form Name successfully" + " :  " + data["approval"]["form_name"] )
            try:
                Commands.Wait10s_ClickElement(data["approval"]["icon_button_doc_no_v3"])
                time.sleep(1)
                Commands.Wait10s_ClickElement(data["approval"]["button_save_doc_no_v3"]) 
            except WebDriverException:
                Logging(" Doc No => ---- FAIL => Close Doc NO")
                Commands.Wait10s_ClickElement(data["approval"]["close_doc_no_all_form_admin_v3"])
            # time.sleep(1)
            # driver.execute_script("window.scrollTo(0, 100)")
            # time.sleep(3) 
            #editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
            #driver.switch_to.frame(editor_frame)
            #content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
            #content_input.send_keys(data["approval"]["content_form_name"])
            #driver.switch_to.default_content()
            
        except WebDriverException:
            Logging(" Create Form => ---- FAIL ")
            Commands.Wait10s_ClickElement(data["approval"]["close_all_form_admin_v3"]) 
           
        Commands.Wait10s_ClickElement(data["approval"]["click_button_next_all_form_v3"]) 
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["approval"]["click_button_save_all_form_v3"]) 
        time.sleep(4)
        Logging("8. Save All Form successfully")
        totaltext1=driver.find_element_by_xpath("//span[contains(.,'Total')]").text
        total1 = totaltext1[int(6): int(totaltext1.rfind("|"))]
        time.sleep(2)
        total=so(total)
        total1=so(total1)    
        Logging("---  Total all form after create : ")
        Logging(total1)
        time.sleep(1)
        if total1== total +1 :
            Logging(" ***  Total All Form displayed correctly")
            Logging(Green("Write All Form => ---------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["pass"])
        else:
            Logging(Red(" Write All Form => ---- FAIL "))
            ValidateFailResultAndSystem("<div>[Approval]2. Write All Form </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["fail"])
    except WebDriverException:
        Logging("8.Create Form Fail")

    Logging("-------------Delete All  Forms - Admin---------------")
    try:
        search_all_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_all_form_v3"])))
        search_all_form.send_keys(data["approval"]["title_search_all_form_v3"])
        search_all_form.send_keys(Keys.RETURN)
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["select_all_forms_delete_v3"])
        time.sleep(1)
        Logging("1. Click checkbox Delete All All Forms Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_delete_all_forms_v3"])
        time.sleep(1)
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_all_form_admin_v3"])
        Logging("3. Click button confirm successfully")
        Logging("=> Delete Default Approval Routes - Admin successfully")
    except WebDriverException:
        Logging("7.Delete All  Forms Fail")



def approval_write_all_official_form(domain_name):
    Logging("-------------- Write All Official Forms ------------------")  
    try:
        Commands.Wait10s_ClickElement(data["approval"]["all_official_form_v3"])
        Logging("1. Click All Official Forms successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["create_all_official_form_v3"])
        time.sleep(1)
        Logging("2. Click Create Write All Official Forms successfully")
        now = datetime.now()
        name_all_official_approval = "Generated by selenium at" +" " +str(now)
        input_name_all_official_approval = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_textbox_name_official_forms_v3"])))
        input_name_all_official_approval.send_keys(name_all_official_approval)
        time.sleep(2)
        Commands.SwitchToFrame_no(data["approval"]["input_editor_v3"])
        Commands.Wait10s_InputElement_return(data["approval"]["input_editor_tynmce_v3"],data["approval"]["content_form_name_official_forms_v3"])
        driver.switch_to.default_content()
        time.sleep(1)
        Logging("3. Input Content All Form successfully")
        Commands.Wait10s_ClickElement(data["approval"]["button_save_all_offcial_form_v3"])
        Logging("4. Save All Official Forms successfully")
        time.sleep(1)
        if 'Generated by' in driver.page_source :
            Logging(Green("=>  5. Write All Official Forms  PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["pass"])
        else:
            Logging(Red("=>  5. Write All Official Forms  FAIL"))
            ValidateFailResultAndSystem("<div>[Approval] Write All Official Forms  </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["fail"])


        Logging("-------------Delete All Official Forms - Admin---------------")
        search_official_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_official_form_v3"])))
        search_official_form.send_keys(data["approval"]["title_search_official_form_v3"])
        search_official_form.send_keys(Keys.RETURN)
        time.sleep(4)
        Commands.Wait10s_ClickElement(data["approval"]["select_official_forms_delete_v3"])
        time.sleep(1)
        Logging("1. Click checkbox Delete All Official Forms Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_delete_official_forms_v3"])
        time.sleep(1)
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_approval_routes_admin_v3"])
        Logging("3. Click button confirm successfully")
        Logging("=> Delete Default Approval Routes - Admin successfully")
    except WebDriverException:
        Logging("4.Write All Official Forms Fail")


def approval_view_all_approvals(domain_name):
   
    Logging("----------------- View All Approvals ------------------")
    try:
        #Commands.scroll_view(data["approval"]["all_approvals_v3"])
        Commands.Wait10s_ClickElement(data["approval"]["all_approvals_v3"])
        Logging("1. Click All Approvals successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_a_approval_v3"])
        try:
            Commands.Wait10s_InputElement(data["approval"]["txt_input_secrutity_pw_v3"],data["approval"]["secrutity_pw_v3"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_secrutity_pw_v3"])
            Logging(" Input Password successfully") 
        except WebDriverException:
            Logging("NOT SHOW Security Pasword ")
            
        Logging("2. View All Approvals successfully")
        if 'Approval Route' in driver.page_source :
            Logging(Green("=> 1.View All Approvals=> ---------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["pass"])
        else:
            Logging(Red("=> 1.View All Approvals =>---------- FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]2. View All Approvals </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["fail"])
    except WebDriverException:
        Logging("Not show View All Approvals")

    
def approval_view_official_documentation(domain_name):
    Logging("--------------- View Official Documentation ------------------")
    try:
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["official_documentation_archive_v3"])
        Logging("1. Click Official Documentation successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_official_documenttation_v3"])
        Logging("3. View Official Documentation successfully")
        time.sleep(1)
        if 'Print' in driver.page_source :
            Logging(Green(" => 1.View Official Documentation =>  PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["pass"])
        else:
            Logging(Red("=>1.View Official Documentation => FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]View Official Documentation </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["fail"])
    except WebDriverException:
        Logging("Not show data View Official Documentation  ")


def approval_arbitrary_decision(domain_name):
    Logging("-------------- Arbitrary Decision Settings -----------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["click_arbitrary_decision_v3"])
        Logging("1. Click Arbitrary Decision successfully")
        Commands.Wait10s_InputElement_return(data["approval"]["search_user_arbitrary_decision_v3"],data["approval"]["search_user_v3"])
        time.sleep(1)
        Logging("6. Search user successfully")
        try:
            Logging("-------------Show User Arbitrary Decision Settings ---------------")
            Commands.Wait10s_ClickElement(data["approval"]["select_user_arbitrary_decision_v3"])
            Logging("3. Select user successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["button_click_add_arbitrary_decision_v3"])
            Logging("3. Arbitrary Decision Settings successfully")
            Commands.Wait10s_ClickElement(data["approval"]["button_click_save_arbitrary_decision_v3"])
            Logging("3. Arbitrary Decision Settings successfully")
            Logging(Green("=> Arbitrary Decision Settings =>--------- PASS"))
        except WebDriverException:
            Logging("Not show User Arbitrary Decision Settings ")
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["pass"])
    except WebDriverException:
        Logging(Red("=> Arbitrary Decision Settings=>---------- FAIL"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["fail"])
    time.sleep(1)
    try:
        Logging("-------------Delete User Arbitrary Decision Settings ---------------")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_delete_arbitrary_decision_v3"])
        Logging("1. Click User Delete Change Approval Route successfully")
        Commands.Wait10s_ClickElement(data["approval"]["button_click_save_arbitrary_decision_v3"])
        Logging("2. Delete Change Approval Route successfully")
    except WebDriverException:
        Logging("Not show user Automationtest ")



    
def approval_default_approval_route(domain_name):
    Logging("------------- Default Approval Routes - Admin---------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["select_approval_step_management_admin_v3"])
        time.sleep(2)
        Logging("1. ClickApproval Step Management Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_create_approval_step_management_admin_v3"])
        time.sleep(2)
        Logging("2. Click Create a new approval Route successfully")
        now = datetime.now()
        name_default_approval_routes = "Generated by selenium at" +" " +str(now)
        input_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_approval_step_management_admin_v3"])))
        input_default_approval_routes.send_keys(name_default_approval_routes)
        Commands.Wait10s_ClickElement(data["approval"]["icon_org_default_approval_name_admin_v3"])
        Logging("5. Click Org successfully")
        try:
            Commands.Wait10s_ClickElement(data["approval"]["dept_defaul_approval_admin_v3"])
            Commands.Wait10s_ClickElement(data["approval"]["btn_add_defaul_approval_admin_v3"])
            time.sleep(2)
            try:
                Commands.Wait10s_ClickElement(data["approval"]["btn_ok_defaul_approval_admin_v3"])
                Logging("7. Show sub dept => Select user successfully")
            except WebDriverException:
                Logging("7. Not show pop up Sub Dept => Select user successfully")
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_org_defaul_approval_admin_v3"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_defaul_approval_admin_v3"])
            Logging("9. Save Default Approval Routes - Admin Pass")
        except WebDriverException:
            Logging("9. Save Default Approval Routes - Admin Fail")
            Commands.Wait10s_ClickElement(data["approval"]["btn_close_modal_org_defaul_approval_admin_v3"])
            Commands.Wait10s_ClickElement(data["approval"]["btn_close_modal_create_defaul_approval_admin_v3"])
        TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_admin"]["pass"])
    except WebDriverException:
        Logging("Default Approval Routes - Admin Fail ")
        TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_admin"]["fail"])

    Logging("-------------Delete Default Approval Routes - Admin---------------")
    try:
        #driver.execute_script("window.scrollTo(0, 100)")
        Commands.Wait10s_ClickElement(data["approval"]["check_defaul_approval_admin_admin_v3"])
        Logging("1. Click checkbox Delete Default Approval Routes Admin successfully")
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        try:
            Commands.Wait10s_ClickElement(data["approval"]["btn_delete_step_management_admin_v3"])
            Logging("2. Click button Delete successfully")
            Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_approval_step_management_admin_v3"])
            Logging("3. Click button confirm successfully")
            Logging("=> Delete Default Approval Routes - Admin successfully")
        except WebDriverException:
            Logging("Not show data delete")
    except WebDriverException:
        Logging("Delete Default Approval Routes - Admin => Fail")

    Logging("------------- Set Official Seal - Admin ---------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["select_value_set_official_seal_v3"])
        Logging("1. Click Set Official Seal successfully")
        time.sleep(1)
        txt_seal_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_txt_tel_set_official_seal_v3"])))
        txt_seal_name.send_keys(Keys.CONTROL + "a");
        txt_seal_name.send_keys(Keys.DELETE)
        txt_seal_name.send_keys(Keys.RETURN)
        txt_seal_name.send_keys(data["approval"]["input_txt_tel_set_official_seal_v3"])
        time.sleep(1)
        Commands.scroll_view(data["approval"]["click_button_save_set_official_seal_v3"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_button_save_set_official_seal_v3"])
        Logging("3. Click button Save Set Official Seal successfully")
        # get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["file_set_official_seal"])))
        # get_file.send_keys(luu_function.file_img)
        # Logging("2. Attch Signature Image successfully")
        # Commands.Wait10s_ClickElement(data["approval"]["btn_save_set_official_seal"])
        # Logging("3. Click button Save Set Official Seal successfully")
        TestCase_LogResult(**data["testcase_result"]["approval"]["set_official_seal _admin"]["pass"])
    except WebDriverException:
        Logging("Set Official Seal - Admin => Fail")
        TestCase_LogResult(**data["testcase_result"]["approval"]["set_official_seal _admin"]["fail"])
    


    Logging("------------- Search Discarded Documents - Admin ---------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["click_discarded_documents_v3"])
        Logging("1. Click Discarded Documents successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_title_discarded_documents_v3"])
        Logging("2. View Discarded Documents successfully")
        time.sleep(1)
        if 'Print' in driver.page_source :
            Logging(Green(" => 1.View Discarded Documents =>  PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_discarded_documents"]["pass"])
        else:
            Logging(Red("=>1.View Discarded Documents => FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]View Official Documentation </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_discarded_documents"]["fail"])
    except WebDriverException:
        Logging("Not show data Discarded Documents Documentation  ")

    Logging("------------- Change Approval Route - Admin ---------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["click_change_approval_route_v3"])
        Logging("1. Click Change Approval Route  successfully")
        Commands.Wait10s_InputElement_return(data["approval"]["search_user_arbitrary_decision_v3"],data["approval"]["search_user_v3"])
        time.sleep(1)
        Logging("6. Search user successfully")
        try:
            Commands.Wait10s_ClickElement(data["approval"]["select_user_change_approval_v3"])
            Logging("3. Select user successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["button_click_add_change_approval_v3"])
            Logging("3. Change Approval Route Admin successfully")
            Commands.Wait10s_ClickElement(data["approval"]["button_click_save_change_approval_v3"])
            Logging("3. Change Approval Route Admin successfully")
            Logging(Green("=> Change Approval Route Admin =>--------- PASS"))
        except WebDriverException:
            Logging("Not show User Change Approval Route Admin ")
        TestCase_LogResult(**data["testcase_result"]["approval"]["change_approval_route_admin"]["pass"])
    except WebDriverException:
        Logging("Not show data Change Approval Route Admin  ")
        TestCase_LogResult(**data["testcase_result"]["approval"]["change_approval_route_admin"]["fail"])

    try:
        Logging("-------------Delete User Change Approval Route Admin ---------------")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_delete_change_approval_v3"])
        Logging("1. Click User Delete Change Approval Route successfully")
        Commands.Wait10s_ClickElement(data["approval"]["button_click_save_change_approval_v3"])
        Logging("2. Delete Change Approval Route successfully")
    except WebDriverException:
        Logging("Not show user Automationtest ")

    Logging("------------- Admin-Setting Set the document numbering time ---------------")


    try:
        Commands.Wait10s_ClickElement(data["approval"]["click_admin-setting_v3"])
        Logging("1. Click Admin-Settings successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_set_number_time_submit_admin-setting_v3"])
        Logging("2. Click When submitting document successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_set_number_time_complete_admin-setting_v3"])
        Logging("3. When document is completed")
       
    except WebDriverException:
        Logging("Setting Set the document numbering time Fail  ")










def approval_default_approval_route_setting(domain_name):

    Logging("------------- Default Approval Routes - Default Approval Routes -Setting---------------")
    try:
        
        Commands.scroll_view(data["approval"]["click_sttings_approval"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["click_sttings_approval"])
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Logging("1. Click Settings successfully")
        #Commands.Wait10s_ClickElement(data["approval"]["select_default_approval_routes"])
        Commands.Wait10s_ClickElement(data["approval"]["select_default_approval_routes_setting"])
        time.sleep(2)
        Logging("2. Click Default Approval Route successfully")
        #time.sleep(5)
        Commands.Wait10s_ClickElement(data["approval"]["create_default_approval_routes"])
        time.sleep(5)
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        #Commands.Wait10s_ClickElement(data["approval"]["create_default_approval_routes"])
        
        Logging("3. Click button Create a new Approval Route successfully")
        now = datetime.now()
        name_default_approval_routes_setting = "Generated by selenium at" +" " +str(now)
        input_default_approval_routes_setting = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["input_appproval_route_name"])))
        input_default_approval_routes_setting.send_keys(name_default_approval_routes_setting)
        Commands.Wait10s_ClickElement(data["approval"]["click_org_default_approval_routes"])
        Logging("4. Click Org successfully")
        Commands.Wait10s_InputElement_return(data["approval"]["search_user_approval_in_org"],data["approval"]["user_search_org_approval"])
        time.sleep(2)
        Logging("5. Search user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_defaul_setting"])
        

        '''
        time.sleep(1)
        #select_dept_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_dept_defaul_setting"]))).click()
        time.sleep(1)
        select_user_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["user_reviewer_01"])))
        select_user_org_default_approval_routes.click()
        time.sleep(1)
        add_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_add_user"])))
        add_user_org_default_approval_routes.click()
        Logging("8. Add user successfully")
        time.sleep(2)
        try:
            check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
            if check_show_sub_dept.is_displayed():
                click_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_ok_select_sub_dept"]))).click()
                Logging("=> Select Sub Dept => --------PASS")
            else:
                Logging("=> Sub Dept not show  ")
                
        except WebDriverException:
            Logging("Not Show sub Dept ")
        '''

        time.sleep(1)
        Logging("6. Select user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["icon_add_user"])
        Logging("7. Add user successfully")
        try:
            check_add_user_share = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_user_org_default_approval_setting"])))
            Logging("8. Add User successfully")
            Commands.Wait10s_ClickElement(data["approval"]["button_save_reviewers_approval"])
            Logging("9. Save user successfully")
        except WebDriverException:
            Logging("Add User Share => Fail")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_default_approval_route"])
        Logging("10. Save Default Approval Routes successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_default_approval_route"])
        Logging("11. Close successfully")
        time.sleep(2)
        if 'Generated by' in driver.page_source :
            Logging(Green("=> 1. Default Approval Routes => ------------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["pass"])
        else:
            Logging(Red("=> 1. Default Approval Routes => ------------ FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]Default Approval Routes</div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["fail"])
    except WebDriverException:
        Logging("Default Approval Routes-Setting Fail ")

    try:
        Logging("-------------Delete Default Approval Routes-Setting---------------")
        Commands.Wait10s_ClickElement(data["approval"]["btn_check_all_approval_routes"])
        Logging("1. Click checkbox Delete Default Approval Routes successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_delete_approval_routes"])
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm"])
        Logging("3.Delete  Delete Default Approval Routes successfully")
    except WebDriverException:
        Logging("Delete Default Approval Routes-Setting => Fail")



def approval_manage_my_folder_setting(domain_name):
    Logging("------------- Manage My Folder---------------")
    try:
        #Commands.Wait10s_ClickElement(data["approval"]["setting_manager_my_folder"])
        Commands.Wait10s_ClickElement(data["approval"]["setting_manager_my_folder_personal"])
        Logging("1. Click Manage My Folder successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["select_my_folder"])
        Logging("2. Click My Folder successfully")
        time.sleep(1)
        #Commands.Wait10s_InputElement(data["approval"]["txt_folder_name_approval"],data["approval"]["folder_name_approval"])
        now = datetime.now()
        name_manage_my_folder_setting = "Generated by selenium at" +" " +str(now)
        input_name_manage_my_folder_setting = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_folder_name_approval"])))
        input_name_manage_my_folder_setting.send_keys(name_manage_my_folder_setting)
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_folder_approval"])
        Logging("4. Click Button Save Folder successfully")
        time.sleep(3)
        if 'Generated by' in driver.page_source :
            Logging(Green("=> 1. Add Manage My Folder => ------------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["pass"])
        else:
            Logging(Red("=> 1. Add Manage My Folder => ------------ FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]Manage My Folder</div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["fail"])
        Logging("-------------Delete Manage My Folder---------------")
        Commands.Wait10s_ClickElement(data["approval"]["select_my_folder_delete"])
        Logging("1. Click My Folder Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["icon_delete_my_folder"])
        Logging("2. Click icon Delete My Folder successfully")
        Logging("=> Delete My Folder successfully")
    except WebDriverException:
        Logging("Manage My Folder Fail ")



def approval_display_setting(domain_name):
    
    Logging("-------------Display Settings - Personal Settings ---------------")
    try:
        #Commands.scroll_view(data["approval"]["click_display_settings"])
        Commands.scroll_view(data["approval"]["click_display_pessonal_settings"])
        time.sleep(2)
        #Commands.Wait10s_ClickElement(data["approval"]["click_display_settings"])
        Commands.Wait10s_ClickElement(data["approval"]["click_display_pessonal_settings"])
        Logging("1. Click Display Settings successfully")
        
        '''
        click_org_elect_deputy_user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_org_select_deputy_user"]))).click()
        Logging("2. Click Select Deputy User successfully")
        search_org_user_deputy = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_deputy"])))
        search_org_user_deputy.send_keys(data["approval"]["user_search_org_approval"])
        search_org_user_deputy.send_keys(Keys.RETURN)
        time.sleep(1)
        Logging("3. Search user successfully")
        time.sleep(3)
        select_user_deputy = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_deputy"])))
        select_user_deputy.click()
        time.sleep(3)
        time.sleep(1)
        Logging("4. Select user Deputy successfully")
        '''

        Commands.Wait10s_ClickElement(data["approval"]["click_org_user_with_per_to_read"])
        Logging("2. Click Select Deputy User successfully")

        '''
        search_user_per_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_user_per_to_read"])))
        search_user_per_to_read.send_keys(data["approval"]["user_search_org_approval"])
        search_user_per_to_read.send_keys(Keys.RETURN)
        time.sleep(1)
        Logging("6. Search user Permission to read successfully")
        '''

        Commands.Wait10s_ClickElement(data["approval"]["select_dept_per_to_read"])
        Commands.Wait10s_ClickElement(data["approval"]["select_user_to_read"])
        Commands.Wait10s_ClickElement(data["approval"]["icon_add_user_per_to_read"])
        time.sleep(1)
        try:
            check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
            Commands.Wait10s_ClickElement(data["approval"]["click_ok_select_sub_dept"])
            Logging("=> Select Sub Dept => --------PASS") 
        except WebDriverException:
            Logging("Not Show sub Dept ")
        Logging("3. Add user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_add_user_to_read"])
        Logging("4. Save user successfully")
        get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_attach_signature_image"])))
        get_file.send_keys(luu_function.file_img)
        Logging("5. Attch Signature Image successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_signature_image"])
        Logging("6. Click Button save successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_signature"])
        Logging("7. Click Button Close successfully")
        time.sleep(1)
        Logging(Green("=> Change Signature Image  => --------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["pass"])
    except WebDriverException:
        Logging(Red("=> Change Signature Image  => --------FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]Change Signature Image</div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["fail"])


    try:
        Logging("-------------Delete Display Settings ----------------")
        Commands.Wait10s_ClickElement(data["approval"]["delete_signature_image"])
        Logging("1. Click Icon Delete successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_signature"])
        Logging("2. Click Button Confirm successfully")
        Logging("=> Delete Signature Image  => --------PASS")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_org_user_with_per_to_read"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_icon_delete_user_per"])
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_add_user_to_read"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_signature_image"])
        time.sleep(1)
        Logging("3. Click Button save successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_signature"])
        Logging("4. Click Button Close successfully")
        Logging("=> Delete Display Settings  => --------PASS")
    except WebDriverException:
        Logging("Delete Display Settings Fail ")




def access_menu_approval(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)

    
    if admin == True:
        try:
            approval_write_all_form(domain_name)
            Logging("Create all Form successfully")
        except WebDriverException:
            Logging("Fail to Create all Form")
        
    else:
        Logging("1.Write All Form => Account is not admin")
    

    if admin == True:
        try:
            approval_write_all_official_form(domain_name)
            Logging("Create All Official Form successfully")
        except WebDriverException:
            Logging("Fail to Create All Official Form")
        
    else:
        Logging("2.Write All Official Forms => Account is not admin")

    if admin == True:
        try:
            approval_view_all_approvals(domain_name)
            Logging("View All Approval  successfully")
        except WebDriverException:
            Logging("Fail to View All Approval ")
        
    else:
        Logging("3.View All Approvals => Account is not admin")

    if admin == True:
        try:
            approval_view_official_documentation(domain_name)
            Logging("View Official Documentation  successfully")
        except WebDriverException:
            Logging("Fail to Official Documentation ")
        
    else:
        Logging("4.View Official Documentation in Admin => Account is not admin")

    
    if admin == True:
        try:
            approval_arbitrary_decision(domain_name)
            Logging("Create Arbitrary Decision successfully")
        except WebDriverException:
            Logging("Fail to Arbitrary Decision ")
        
    else:
        Logging("5.Create Arbitrary Decision => Account is not admin")
    
    '''
    if admin == True:
        try:
            approval_change_approval_route(domain_name)
            Logging("Change Approval Route Admin successfully")
        except WebDriverException:
            Logging("Fail to Change Approval Route Admin ")
        
    else:
        Logging("6.Change Approval Route => Account is not admin")


    '''


    if admin == True:
        try:
            approval_default_approval_route(domain_name)
            Logging("Change Default Approval Routes Admin successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Admin ")
        
    else:
        Logging("7.Default Approval Routes in Admin => Account is not admin")


    if admin == True:
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")
        
    else:
        Logging("User Change Default Approval Routes")
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")



    if admin == True:
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")
        
    else:
        Logging("User create Manage My Folder")
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")


    if admin == True:
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")
        
    else:
        Logging("User create Display Settings ")
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")





    time.sleep(2)
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)
    
time.sleep(3)

def is_Displayed(driver,xpath):
    try:
        driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    
def so(total):
    num = re.sub(r'\D', "", total)
    return int(num)




'''
with open(os.path.dirname(Path(__file__).absolute())+'\\'+'luu_approval.txt','w') as approval:
    domain="http://qa.hanbiro.net"
    access_menu_approval(domain,approval)



result=open(os.path.dirname(Path(__file__).absolute())+'\\result.txt','r')
file_result=result.read()
Logging(file_result)
'''
  