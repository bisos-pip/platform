# -*- coding: utf-8 -*-
"""\
* *[Summary]* ::  A /library/ to support icmsPkg facilities
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/bisos/platform/dev/bisos/platform/bxPlatformConfig.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "bxPlatformConfig"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805140708"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:icm:python:topControls 
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
* 
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
#import enum

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:

from bisos.common import bisosPolicy
from bisos.platform import bxPlatformThis

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bxPlatformConfig_libOverview" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /bxPlatformConfig_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxPlatformConfig_libOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:


####+BEGIN: bx:icm:python:section :title "Obtain ICM-Package General Execution Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package General Execution Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "configBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /configBaseDir_obtain/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def configBaseDir_obtain():
####+END:
    return bxPlatformThis.pkgBase_configDir()

####+BEGIN: bx:icm:python:func :funcName "configPkgInfoBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /configPkgInfoBaseDir_obtain/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def configPkgInfoBaseDir_obtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return os.path.abspath(
        "{}/pkgInfo".format(configBaseDir)
    )


####+BEGIN: bx:icm:python:func :funcName "configPkgInfoFpBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /configPkgInfoFpBaseDir_obtain/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def configPkgInfoFpBaseDir_obtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return os.path.abspath(
        "{}/pkgInfo/fp".format(configBaseDir)
    )

    
####+BEGIN: bx:dblock:python:section :title "File Parameters Obtain"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *File Parameters Obtain*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "bisosUserName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /bisosUserName_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def bisosUserName_fpObtain(
    configBaseDir=None,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()
        
    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bisosUserName")
    )

    
####+BEGIN: bx:icm:python:func :funcName "bisosGroupName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /bisosGroupName_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def bisosGroupName_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bisosGroupName")
    )

####+BEGIN: bx:icm:python:func :funcName "rootDir_bisos_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
()*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /rootDir_bisos_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def rootDir_bisos_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_bisos")
    )

####+BEGIN: bx:icm:python:func :funcName "rootDir_bxo_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /rootDir_bxo_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def rootDir_bxo_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_bxo")
    )

####+BEGIN: bx:icm:python:func :funcName "rootDir_deRun_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /rootDir_deRun_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def rootDir_deRun_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_deRun")
    )

    

####+BEGIN: bx:icm:python:func :funcName "rootDir_foreignBxo_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /rootDir_foreignBxo_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def rootDir_foreignBxo_fpObtain(
    configBaseDir=None,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()
        
    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_foreignBxo")
    )


# ####+BEGIN: bx:icm:python:func :funcName "platformControlBaseDir_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
# """
# *  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /platformControlBaseDir_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
# """
# def platformControlBaseDir_fpObtain(
#     configBaseDir,
# ):
# ####+END:
#     if configBaseDir:
#         return(
#             icm.FILE_ParamValueReadFrom(
#                 parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
#                 parName="platformControlBaseDir")
#         )
#     else:
#         icm.EH_problem_usageError("Missing Argument")
#         return None
    


####+BEGIN: bx:dblock:python:section :title "Common Command Parameter Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Parameter Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "void" :retType "bool" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-void      :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    
    # icmParams.parDictAdd(
    #     parName='icmsPkgName',
    #     parDescription="ICMs Package Name",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["any"],
    #     parScope=icm.ICM_ParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--icmsPkgName',
    # )

    # icmParams.parDictAdd(
    #     parName='platformControlBaseDir',
    #     parDescription="ICMs Package Run Environment -- A BaseDir for var/log/tmp (bxo=current bxo)",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["any"],
    #     parScope=icm.ICM_ParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--platformControlBaseDir',
    # )

    icmParams.parDictAdd(
        parName='configBaseDir',
        parDescription="Root Of pkgInfo/fp from which file parameters will be read",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--configBaseDir',
    )
    
    icmParams.parDictAdd(
        parName='bisosUserName',
        parDescription="BISOS Default UserName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bisosUserName',
    )
    
    icmParams.parDictAdd(
        parName='bisosGroupName',
        parDescription="BISOS Default GroupName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bisosGroupName',
    )
    
    icmParams.parDictAdd(
        parName='rootDir_bisos',
        parDescription="Root Dir For bisos (defaults to /bisos)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_bisos',
    )

    icmParams.parDictAdd(
        parName='rootDir_bxo',
        parDescription="Root Dir For BxO -- ByStar Objects (defaults to /bxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_bxo',
    )

    icmParams.parDictAdd(
        parName='rootDir_deRun',
        parDescription="Root Dir For deRun -- ByStar Objects (defaults to /de/run)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_deRun',
    )

    icmParams.parDictAdd(
        parName='rootDir_foreignBxo',
        parDescription="Root Dir For Foreign BxOs -- ByStar Objects (defaults to ~bisosUserName/foreignBxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_foreignBxo',
    )


####+BEGIN: bx:dblock:python:section :title "Common Command Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "examples_pkgInfoParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_pkgInfoParsFull/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def examples_pkgInfoParsFull(
    configBaseDir,
):
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity,
                                                  comment='none', icmWrapper=None, icmName=None) # verbosity: 'little' 'basic' 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    icm.cmndExampleMenuChapter(' =FP Values=  *pkgInfo Get Parameters*')

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ; cps=cpsInit(); menuItem(verbosity='none')

    icm.cmndExampleMenuChapter(' =FP Values=  *PkgInfo Defaults ParsSet  --*')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /" ;
    cpsInit();  cps['configBaseDir'] = configBaseDir ;
    menuItem('little')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /tmp" ;
    cpsInit();  cps['configBaseDir'] = configBaseDir ;
    menuItem('none')
    
    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "foreignBxoPolicy /tmp" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; 
    cps['bisosUserName'] = "lsipusr" ; cps['bisosGroupName'] = "employee"
    cps['rootDir_foreignBxo'] = "${HOME}/foreignBxo"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "externalPolicy" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; 
    cps['bisosUserName'] = "lsipusr" ; cps['bisosGroupName'] = "employee" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    icm.cmndExampleMenuChapter(' =FP Values=  *PkgInfo ParsSet -- Set Parameters Explicitly*')
     
    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bisosUserName'] = "lsipusr"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bisosGroupName'] = "employee" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_bisos'] = "/bisos" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_bxo'] = "/bxo" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_deRun'] = "/de/run" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_foreignBxo'] = "${HOME}/foreignBxo" 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    # cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['platformControlBaseDir'] = "${HOME}/bisosControl"
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pkgInfoParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')
    

####+BEGIN: bx:dblock:python:section :title "File Parameters Get/Set -- Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *File Parameters Get/Set -- Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "interactive fpBaseDir cmndOutcome"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /FP_readTreeAtBaseDir_CmndOutput/ retType=bool argsList=(interactive fpBaseDir cmndOutcome)  [[elisp:(org-cycle)][| ]]
"""
def FP_readTreeAtBaseDir_CmndOutput(
    interactive,
    fpBaseDir,
    cmndOutcome,
):
####+END:
    """Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only."""
    #
    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome
        
    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pkgInfoParsGet" :comment "" :parsMand "" :parsOpt "configBaseDir" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pkgInfoParsGet/ parsMand= parsOpt=configBaseDir argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pkgInfoParsGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'configBaseDir': configBaseDir, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']
####+END:

        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        FP_readTreeAtBaseDir_CmndOutput(
            interactive=interactive,
            fpBaseDir=configPkgInfoFpBaseDir_obtain(
                configBaseDir=configBaseDir,
            ),
            cmndOutcome=cmndOutcome,
        )

        return cmndOutcome


    def cmndDesc(): """
** Without --configBaseDir, it reads from ../pkgInfo/fp.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pkgInfoParsSet" :comment "" :parsMand "" :parsOpt "configBaseDir bisosUserName bisosGroupName rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo" :argsMin "0" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pkgInfoParsSet/ parsMand= parsOpt=configBaseDir bisosUserName bisosGroupName rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo argsMin=0 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pkgInfoParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', 'bisosUserName', 'bisosGroupName', 'rootDir_bisos', 'rootDir_bxo', 'rootDir_deRun', 'rootDir_foreignBxo', ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        bisosUserName=None,         # or Cmnd-Input
        bisosGroupName=None,         # or Cmnd-Input
        rootDir_bisos=None,         # or Cmnd-Input
        rootDir_bxo=None,         # or Cmnd-Input
        rootDir_deRun=None,         # or Cmnd-Input
        rootDir_foreignBxo=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, 'bisosUserName': bisosUserName, 'bisosGroupName': bisosGroupName, 'rootDir_bisos': rootDir_bisos, 'rootDir_bxo': rootDir_bxo, 'rootDir_deRun': rootDir_deRun, 'rootDir_foreignBxo': rootDir_foreignBxo, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']
        bisosUserName = callParamsDict['bisosUserName']
        bisosGroupName = callParamsDict['bisosGroupName']
        rootDir_bisos = callParamsDict['rootDir_bisos']
        rootDir_bxo = callParamsDict['rootDir_bxo']
        rootDir_deRun = callParamsDict['rootDir_deRun']
        rootDir_foreignBxo = callParamsDict['rootDir_foreignBxo']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        def createPathAndFpWrite(
                fpPath,
                valuePath,
        ):
            valuePath = os.path.abspath(valuePath)
            try:
                os.makedirs(valuePath)
            except OSError:
                if not os.path.isdir(valuePath):
                    raise
            
            icm.FILE_ParamWriteToPath(
                parNameFullPath=fpPath,
                parValue=valuePath,
            )

        def processEachArg(argStr):
            varNameValue=argStr.split('=')
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    varNameValue[0],
                ),
                parValue=varNameValue[1],
            )

        # Any number of Name=Value can be passed as args
        for each in cmndArgs:
            processEachArg(each)

        if bisosUserName:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bisosUserName",
                ),
                parValue=bisosUserName,
            )

        if bisosGroupName:
            icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "bisosGroupName",
                ),
                parValue=bisosGroupName,
            )

        if rootDir_bisos:
            icm.FILE_ParamWriteToPath(                
                parNameFullPath=os.path.join(configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "rootDir_bisos",
                ),
                parValue=rootDir_bisos,
            )

        if rootDir_bxo:
            icm.FILE_ParamWriteToPath(                
                parNameFullPath=os.path.join(configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "rootDir_bxo",
                ),
                parValue=rootDir_bxo,
            )
            
        if rootDir_deRun:
            icm.FILE_ParamWriteToPath(                
                parNameFullPath=os.path.join(configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "rootDir_deRun",
                ),
                parValue=rootDir_deRun,
            )
            
        if rootDir_foreignBxo:
            icm.FILE_ParamWriteToPath(                
                parNameFullPath=os.path.join(configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "rootDir_foreignBxo",
                ),
                parValue=rootDir_foreignBxo,
            )
            
            
        if interactive:
            icm.ANN_here("pkgInfoParsSet")

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return cmndArgsSpecDict

    

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pkgInfoParsDefaultsSet" :comment "" :parsMand "" :parsOpt "configBaseDir bisosUserName bisosGroupName rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo" :argsMin "0" :argsMax "2" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pkgInfoParsDefaultsSet/ parsMand= parsOpt=configBaseDir bisosUserName bisosGroupName rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo argsMin=0 argsMax=2 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pkgInfoParsDefaultsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', 'bisosUserName', 'bisosGroupName', 'rootDir_bisos', 'rootDir_bxo', 'rootDir_deRun', 'rootDir_foreignBxo', ]
    cmndArgsLen = {'Min': 0, 'Max': 2,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        bisosUserName=None,         # or Cmnd-Input
        bisosGroupName=None,         # or Cmnd-Input
        rootDir_bisos=None,         # or Cmnd-Input
        rootDir_bxo=None,         # or Cmnd-Input
        rootDir_deRun=None,         # or Cmnd-Input
        rootDir_foreignBxo=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, 'bisosUserName': bisosUserName, 'bisosGroupName': bisosGroupName, 'rootDir_bisos': rootDir_bisos, 'rootDir_bxo': rootDir_bxo, 'rootDir_deRun': rootDir_deRun, 'rootDir_foreignBxo': rootDir_foreignBxo, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']
        bisosUserName = callParamsDict['bisosUserName']
        bisosGroupName = callParamsDict['bisosGroupName']
        rootDir_bisos = callParamsDict['rootDir_bisos']
        rootDir_bxo = callParamsDict['rootDir_bxo']
        rootDir_deRun = callParamsDict['rootDir_deRun']
        rootDir_foreignBxo = callParamsDict['rootDir_foreignBxo']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        basesPolicy = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)
        rootPrefix = self.cmndArgsGet("1", cmndArgsSpecDict, effectiveArgsList)

        if basesPolicy == "bxoPolicy":
            if not bisosUserName:
                bisosUserName = bisosPolicy.bisosAccountName()
                
            if not bisosGroupName:
                bisosGroupName = bisosPolicy.bisosGroupName()

            if not rootDir_bisos:
                rootDir_bisos = os.path.join(rootPrefix, bisosPolicy.rootDir_bisos())

            if not rootDir_bxo:
                rootDir_bxo = os.path.join(rootPrefix, bisosPolicy.rootDir_bxo())

            if not rootDir_deRun:
                rootDir_deRun = os.path.join(rootPrefix, bisosPolicy.rootDir_deRun())

                
        elif basesPolicy == "foreignBxoPolicy":
            if not bisosUserName:
                return icm.EH_problem_usageError("Missing bisosUserName")                

            if not bisosGroupName:
                return icm.EH_problem_usageError("Missing bisosGroupName")

            if not rootDir_foreignBxo:
                return icm.EH_problem_usageError("Missing rootDir_foreignBxo")

            if not rootDir_bisos:
                rootDir_bisos = os.path.join(rootPrefix, bisosPolicy.rootDir_bisos())

            if not rootDir_bxo:
                rootDir_bxo = os.path.join(rootPrefix, bisosPolicy.rootDir_bxo())

            if not rootDir_deRun:
                rootDir_deRun = os.path.join(rootPrefix, bisosPolicy.rootDir_deRun())
            
            
        elif basesPolicy == "externalPolicy":
            if not bisosUserName:
                return icm.EH_problem_usageError("Missing bisosUserName")                

            if not bisosGroupName:
                return icm.EH_problem_usageError("Missing bisosGroupName")

            if not rootDir_foreignBxo:
                return icm.EH_problem_usageError("Missing rootDir_foreignBxo")

            if not rootDir_bisos:
                return icm.EH_problem_usageError("Missing rootDir_bisos")

            if not rootDir_bxo:
                return icm.EH_problem_usageError("Missing rootDir_bxo")                

            if not rootDir_deRun:
                return icm.EH_problem_usageError("Missing rootDir_deRun")                
            
            
        else:
            return icm.EH_critical_oops("basesPolicy={}".format(basesPolicy))

        pkgInfoParsSet().cmnd(
            interactive=False,
            configBaseDir=configBaseDir,
            bisosUserName=bisosUserName,
            bisosGroupName=bisosGroupName,
            rootDir_foreignBxo=rootDir_foreignBxo,
            rootDir_bisos=rootDir_bisos,
            rootDir_bxo=rootDir_bxo,
            rootDir_deRun=rootDir_deRun,
        )

    def cmndDesc(): """
** Set File Parameters at ../pkgInfo/fp -- By default
** TODO NOTYET auto detect marme.dev -- marme.control and decide where they should be, perhaps in /var/
"""

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:       
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="basesPolicy",
            argDefault="bxoPolicy",
            argChoices=['bxoPolicy', 'foreignBxoPolicy', 'externalPolicy'],
            argDescription="bxoPolicy: rundirs are per bxo/foreign. externalPolicy: Un-ByStar."
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="rootPrefix",
            argDefault="/",            
            argChoices='any',
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    
    

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
