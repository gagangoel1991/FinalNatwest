import FW.Initialize.initialize_global_variables as iniVar
import os

def Globalinitialize():
    v_current_project_path = r"C:\Users\hp\Documents\FinalNatwest\FW"

    v_current_project_root_path =os.path.abspath(os.path.join(v_current_project_path, os.pardir))
    v_current_project_test_path= v_current_project_path + r"\Tests"
    v_report_dict = {}
    
    iniVar.setupGlobalVariable(v_current_project_path, v_current_project_root_path, v_current_project_test_path, v_report_dict )
