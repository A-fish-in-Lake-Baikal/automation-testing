import unittest,time,os,multiprocessing
import HTMLTestRunner


def creatsuit():
    casedir = []
    listaa = os.listdir(r'C:\Users\Administrator\Documents\GitHub\automation-testing\uiautomation')
    for x in listaa:
        if 'testcase' in x:
            casedir.append(x)

    suite = []
    for n in casedir:
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(n)
        print(discover)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        suite.append(testunit)
    print("===casedir:====", casedir)
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("!!!suite:!!!", suite)
    return suite, casedir

def EEEEEmultiRunCase(suite,casedir):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = os.path.dirname(os.path.abspath('.'))+'/test_report/'
    htmlfile = filename+now+"HTMLtemplate.html"
    fp = open(htmlfile, "wb")
    proclist=[]
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：'
        )
        proc = multiprocessing.Process(target=runner.run(i),args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist: proc.start()
    for proc in proclist: proc.join()
    fp.close()

if __name__ == "__main__":
    runtmp=creatsuit()
    EEEEEmultiRunCase(runtmp[0],runtmp[1])