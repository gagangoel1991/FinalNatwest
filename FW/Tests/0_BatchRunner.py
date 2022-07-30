# noinspection PyUnresolvedReferences
from UDFs.project_config import project_setup_paths as psp
from FW.FW_tags import tags, tests
import FW.FW_runner as runner

def getTestsList():
    #return ['test_1_2_th','test_2_5_th', 'test_2_3_th', 'test_2_6_th']
    #return [ 'test_2_1_th', 'test_2_2_th', 'test_2_3_th', 'test_2_4_th','test_2_6_th','test_1_1_th']
    #return [ 'test_1_2_th', 'test_1_1_th', 'test_2_1_th']
    #return [ 'test_1_2_th', 'test_1_1_th']
    #return [ 'test_1_1_th', 'test_1_2_th', 'test_2_1_th', 'test_2_2_th','test_2_3_th','test_2_4_th','test_2_5_th','test_2_6_th']
    #return tests.equals('test_demo1','test')
    #return tests.startswith("sun-prty_agree_t-GEND1ER", "test")
    #tags.containing('')
    #return [ 'test_demo1']
    #return [ 'test_demo1', 'test_demo', 'test_demo2']
    #return ['CLARICA-coverage_agreement_t-CURRENT_MINIMUM_PREMIUM_AMOUNT']
    return tags.containing('random')


if __name__ == '__main__': 
    psp.Globalinitialize()
    runner.runner(getTestsList(), "sequential" ) # multithread   sequential


    