import FW.Initialize.initialize_global_variables as iniVar
from UDFs.project_config import project_setup_paths as psp
import FW.Compare_Report.compare_report as cp
from FW.FW_logger import loggerPass, loggerInfo, get_from_reporting_dict, loggerDisplay
import FW.FW_Lib_Connect as dataConnection
import time, os, sys, threading
from FW.FW_tags import tags
from FW.FW_individual_script_runner import run_individual_script
import pandas as pd


#####################################################################################################################
@tags('random')
def test_main(test_name='Gagan'):
    psp.Globalinitialize();
    ls_refCols = ['Order ID']

######################################################################################################################################################################

    df_src = pd.read_csv(r"C:\Users\hp\Downloads\500000-Sales-Records (1)\Source.csv");
    df_trg = pd.read_csv(r"C:\Users\hp\Downloads\500000-Sales-Records (1)\Target.csv");

    ls_allCols_to_validate = df_src.columns.values
    cp.compare([df_src, ls_refCols, ls_allCols_to_validate], [df_trg, ls_refCols, ls_allCols_to_validate])

######################################################################################################################################################################

    # df_src = pd.read_csv(r"C:\Users\hp\Downloads\SampleCSVFile_2kb.csv");
    # df_trg = pd.read_csv(r"C:\Users\hp\Downloads\SampleCSVFile_2kb - Copy.csv");
    #
    # ls_allCols_to_validate = df_src.columns.values
    # cp.compare([df_src, ls_refCols, ls_allCols_to_validate], [df_trg, ls_refCols, ls_allCols_to_validate],report_tab_name="Gagan1")

######################################################################################################################################################################
# generate reports
def test_reporting(rptCnt=1, testName=None, Error=None, totaltestsCount=1):
    cp.prepareReport(rptCnt, testName, Error, totaltestsCount)


if __name__ == "__main__":
    #dry_run = False
    current_test_name = os.path.basename(sys.argv[0])
    run_individual_script(test_main, test_reporting, current_test_name, dry_run=False, verbose_debug=False)

