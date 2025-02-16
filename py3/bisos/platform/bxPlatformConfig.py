# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CmndSvc= for
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/platform/py3/bisos/platform/bxPlatformConfig.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bxPlatformConfig'], }
csInfo['version'] = '202502114408'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'bxPlatformConfig-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from bisos.common import bisosPolicy
from bisos.platform import bxPlatformThis

import os

####+BEGIN: b:py3:cs:orgItem/section :title "CSU-Lib Examples" :comment "-- Providing examples_csu"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CSU-Lib Examples* -- Providing examples_csu  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:icm:py3:section :title "CS-Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Commands*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bxPlatformConfig_libOverview" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxPlatformConfig_libOverview>>  =verify= argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxPlatformConfig_libOverview(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:

        moduleDescription = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
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

        print("NOTYET")
        return 

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print(each)
            if rtInv.outs:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

        """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""

# @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    #def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:


####+BEGIN: bx:cs:python:section :title "Obtain ICM-Package General Execution Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package General Execution Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "configBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /configBaseDir_obtain/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def configBaseDir_obtain():
####+END:
    return bxPlatformThis.pkgBase_configDir()

####+BEGIN: bx:cs:python:func :funcName "configPkgInfoBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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


####+BEGIN: bx:cs:python:func :funcName "configPkgInfoFpBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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

####+BEGIN: bx:cs:python:func :funcName "bisosUserName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bisosUserName")
    )

    
####+BEGIN: bx:cs:python:func :funcName "bisosGroupName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bisosGroupName")
    )

####+BEGIN: bx:cs:python:func :funcName "bystarUserName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /bystarUserName_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def bystarUserName_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()
        
    return(
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bystarsUserName")
    )

    
####+BEGIN: bx:cs:python:func :funcName "bystarGroupName_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /bystarGroupName_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def bystarGroupName_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="bystarGroupName")
    )


####+BEGIN: bx:cs:python:func :funcName "rootDir_provisioners_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /rootDir_provisioners_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def rootDir_provisioners_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_provisioners")
    )

####+BEGIN: bx:cs:python:func :funcName "rootDir_bisos_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_bisos")
    )

####+BEGIN: bx:cs:python:func :funcName "rootDir_bxo_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_bxo")
    )

####+BEGIN: bx:cs:python:func :funcName "rootDir_deRun_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_deRun")
    )

    

####+BEGIN: bx:cs:python:func :funcName "rootDir_foreignBxo_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
        b.fp.FileParamValueReadFrom(
            parRoot=os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
            parName="rootDir_foreignBxo")
    )


# ####+BEGIN: bx:cs:python:func :funcName "platformControlBaseDir_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
# """
# *  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /platformControlBaseDir_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
# """
# def platformControlBaseDir_fpObtain(
#     configBaseDir,
# ):
# ####+END:
#     if configBaseDir:
#         return(
#             b.fp.FileParamValueReadFrom(
#                 parRoot= os.path.abspath("{}/pkgInfo/fp".format(configBaseDir)),
#                 parName="platformControlBaseDir")
#         )
#     else:
#         b_io.eh.problem_usageError("Missing Argument")
#         return None
    


####+BEGIN: bx:dblock:python:section :title "Common Command Parameter Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Parameter Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "commonParamsSpecify" :funcType "void" :retType "bool" :deco "" :argsList "csParams"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-void      :: /commonParamsSpecify/ retType=bool argsList=(csParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    csParams,
):
####+END:
    
    # csParams.parDictAdd(
    #     parName='icmsPkgName',
    #     parDescription="ICMs Package Name",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["any"],
    #     parScope=cs.CmndParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--icmsPkgName',
    # )

    # csParams.parDictAdd(
    #     parName='platformControlBaseDir',
    #     parDescription="ICMs Package Run Environment -- A BaseDir for var/log/tmp (bxo=current bxo)",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["any"],
    #     parScope=cs.CmndParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--platformControlBaseDir',
    # )

    csParams.parDictAdd(
        parName='configBaseDir',
        parDescription="Root Of pkgInfo/fp from which file parameters will be read",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--configBaseDir',
    )
    
    csParams.parDictAdd(
        parName='bisosUserName',
        parDescription="BISOS Default UserName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bisosUserName',
    )
    
    csParams.parDictAdd(
        parName='bisosGroupName',
        parDescription="BISOS Default GroupName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bisosGroupName',
    )

    csParams.parDictAdd(
        parName='bystarUserName',
        parDescription="BYSTAR Default UserName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bystarUserName',
    )
    
    csParams.parDictAdd(
        parName='bystarGroupName',
        parDescription="BYSTAR Default GroupName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bystarGroupName',
    )
    
    csParams.parDictAdd(
        parName='rootDir_provisioners',
        parDescription="Root Dir For bisos (defaults to /opt/bisosProvisioner)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_provisioners',
    )
    
    csParams.parDictAdd(
        parName='rootDir_bisos',
        parDescription="Root Dir For bisos (defaults to /bisos)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_bisos',
    )

    csParams.parDictAdd(
        parName='rootDir_bxo',
        parDescription="Root Dir For BxO -- ByStar Objects (defaults to /bxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_bxo',
    )

    csParams.parDictAdd(
        parName='rootDir_deRun',
        parDescription="Root Dir For deRun -- ByStar Objects (defaults to /de/run)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_deRun',
    )

    csParams.parDictAdd(
        parName='rootDir_foreignBxo',
        parDescription="Root Dir For Foreign BxOs -- ByStar Objects (defaults to ~bisosUserName/foreignBxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rootDir_foreignBxo',
    )


####+BEGIN: bx:dblock:python:section :title "Common Command Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "examples_pkgInfoParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
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
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity,
                                                  comment='none', icmWrapper=None, icmName=None) # verbosity: 'little' 'basic' 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    cs.examples.menuChapter(' =FP Values=  *pkgInfo Get Parameters*')

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ; cps=cpsInit(); menuItem(verbosity='none')

    cs.examples.menuChapter(' =FP Values=  *PkgInfo Defaults ParsSet  --*')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /" ;
    cpsInit();  cps['configBaseDir'] = configBaseDir ;
    menuItem('little')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /tmp" ;
    cpsInit();  cps['configBaseDir'] = configBaseDir ;
    menuItem('none')
    
    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "foreignBxoPolicy /tmp" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; 
    cps['bystarUserName'] = "bystar" ; cps['bystarGroupName'] = "bisos"
    cps['rootDir_foreignBxo'] = "${HOME}/foreignBxo"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "externalPolicy" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; 
    cps['bisosUserName'] = "bisos" ; cps['bisosGroupName'] = "bisos" 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cs.examples.menuChapter(' =FP Values=  *PkgInfo ParsSet -- Set Parameters Explicitly*')
     
    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bisosUserName'] = "bisos"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bisosGroupName'] = "bisos"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bystarUserName'] = "bystar"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['bystarGroupName'] = "bisos"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_provisioners'] = "/opt/bisosProvisioner"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_bisos'] = "/bisos" 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_bxo'] = "/bxo" 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_deRun'] = "/de/run" 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['rootDir_foreignBxo'] = "${HOME}/foreignBxo" 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pkgInfoParsSet" ; cmndArgs = "" ;
    # cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['platformControlBaseDir'] = "${HOME}/bisosControl"
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pkgInfoParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pkgInfoParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')
    

####+BEGIN: bx:dblock:python:section :title "File Parameters Get/Set -- Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *File Parameters Get/Set -- Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "interactive fpBaseDir cmndOutcome"
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


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pkgInfoParsGet" :comment "" :parsMand "" :parsOpt "configBaseDir" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsGet>>  =verify= parsOpt=configBaseDir ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             configBaseDir: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'configBaseDir': configBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        configBaseDir = csParam.mappedValue('configBaseDir', configBaseDir)
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


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pkgInfoParsSet" :comment "" :parsMand "" :parsOpt "configBaseDir bisosUserName bisosGroupName bystarUserName bystarGroupName rootDir_provisioners rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo" :argsMin 0 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsSet>>  =verify= parsOpt=configBaseDir bisosUserName bisosGroupName bystarUserName bystarGroupName rootDir_provisioners rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', 'bisosUserName', 'bisosGroupName', 'bystarUserName', 'bystarGroupName', 'rootDir_provisioners', 'rootDir_bisos', 'rootDir_bxo', 'rootDir_deRun', 'rootDir_foreignBxo', ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             configBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             bisosUserName: typing.Optional[str]=None,  # Cs Optional Param
             bisosGroupName: typing.Optional[str]=None,  # Cs Optional Param
             bystarUserName: typing.Optional[str]=None,  # Cs Optional Param
             bystarGroupName: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_provisioners: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_bisos: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_bxo: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_deRun: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_foreignBxo: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'configBaseDir': configBaseDir, 'bisosUserName': bisosUserName, 'bisosGroupName': bisosGroupName, 'bystarUserName': bystarUserName, 'bystarGroupName': bystarGroupName, 'rootDir_provisioners': rootDir_provisioners, 'rootDir_bisos': rootDir_bisos, 'rootDir_bxo': rootDir_bxo, 'rootDir_deRun': rootDir_deRun, 'rootDir_foreignBxo': rootDir_foreignBxo, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        configBaseDir = csParam.mappedValue('configBaseDir', configBaseDir)
        bisosUserName = csParam.mappedValue('bisosUserName', bisosUserName)
        bisosGroupName = csParam.mappedValue('bisosGroupName', bisosGroupName)
        bystarUserName = csParam.mappedValue('bystarUserName', bystarUserName)
        bystarGroupName = csParam.mappedValue('bystarGroupName', bystarGroupName)
        rootDir_provisioners = csParam.mappedValue('rootDir_provisioners', rootDir_provisioners)
        rootDir_bisos = csParam.mappedValue('rootDir_bisos', rootDir_bisos)
        rootDir_bxo = csParam.mappedValue('rootDir_bxo', rootDir_bxo)
        rootDir_deRun = csParam.mappedValue('rootDir_deRun', rootDir_deRun)
        rootDir_foreignBxo = csParam.mappedValue('rootDir_foreignBxo', rootDir_foreignBxo)
####+END:
        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)

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
            
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=fpPath,
                parValue=valuePath,
            )

        def processEachArg(argStr):
            varNameValue = argStr.split('=')
            icm.b.fp.FileParamWriteToPath(
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
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bisosUserName",
                ),
                parValue=bisosUserName,
            )

        if bisosGroupName:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bisosGroupName",
                ),
                parValue=bisosGroupName,
            )
        if bystarUserName:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bystarUserName",
                ),
                parValue=bystarUserName,
            )

        if bystarGroupName:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bystarGroupName",
                ),
                parValue=bystarGroupName,
            )

        if rootDir_provisioners:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "rootDir_provisioners",
                ),
                parValue=rootDir_provisioners,
            )

        if rootDir_bisos:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "rootDir_bisos",
                ),
                parValue=rootDir_bisos,
            )

        if rootDir_bxo:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "rootDir_bxo",
                ),
                parValue=rootDir_bxo,
            )
           
        if rootDir_deRun:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "rootDir_deRun",
                ),
                parValue=rootDir_deRun,
            )
           
        if rootDir_foreignBxo:
            parNameFullPath = icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    configPkgInfoFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "rootDir_foreignBxo",
                ),
                parValue=rootDir_foreignBxo,
            )

        if rtInv.outs:
            parValue = b.fp.FileParamValueReadFromPath(parNameFullPath)
            b_io.ann.here("pkgInfoParsSet: {parValue} at {parNameFullPath}".
                         format(parValue=parValue, parNameFullPath=parNameFullPath))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return cmndArgsSpecDict

    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pkgInfoParsDefaultsSet" :comment "" :parsMand "" :parsOpt "configBaseDir bisosUserName bisosGroupName bystarUserName bystarGroupName rootDir_provisioners rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo" :argsMin 0 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsDefaultsSet>>  =verify= parsOpt=configBaseDir bisosUserName bisosGroupName bystarUserName bystarGroupName rootDir_provisioners rootDir_bisos rootDir_bxo rootDir_deRun rootDir_foreignBxo argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsDefaultsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', 'bisosUserName', 'bisosGroupName', 'bystarUserName', 'bystarGroupName', 'rootDir_provisioners', 'rootDir_bisos', 'rootDir_bxo', 'rootDir_deRun', 'rootDir_foreignBxo', ]
    cmndArgsLen = {'Min': 0, 'Max': 2,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             configBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             bisosUserName: typing.Optional[str]=None,  # Cs Optional Param
             bisosGroupName: typing.Optional[str]=None,  # Cs Optional Param
             bystarUserName: typing.Optional[str]=None,  # Cs Optional Param
             bystarGroupName: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_provisioners: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_bisos: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_bxo: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_deRun: typing.Optional[str]=None,  # Cs Optional Param
             rootDir_foreignBxo: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'configBaseDir': configBaseDir, 'bisosUserName': bisosUserName, 'bisosGroupName': bisosGroupName, 'bystarUserName': bystarUserName, 'bystarGroupName': bystarGroupName, 'rootDir_provisioners': rootDir_provisioners, 'rootDir_bisos': rootDir_bisos, 'rootDir_bxo': rootDir_bxo, 'rootDir_deRun': rootDir_deRun, 'rootDir_foreignBxo': rootDir_foreignBxo, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        configBaseDir = csParam.mappedValue('configBaseDir', configBaseDir)
        bisosUserName = csParam.mappedValue('bisosUserName', bisosUserName)
        bisosGroupName = csParam.mappedValue('bisosGroupName', bisosGroupName)
        bystarUserName = csParam.mappedValue('bystarUserName', bystarUserName)
        bystarGroupName = csParam.mappedValue('bystarGroupName', bystarGroupName)
        rootDir_provisioners = csParam.mappedValue('rootDir_provisioners', rootDir_provisioners)
        rootDir_bisos = csParam.mappedValue('rootDir_bisos', rootDir_bisos)
        rootDir_bxo = csParam.mappedValue('rootDir_bxo', rootDir_bxo)
        rootDir_deRun = csParam.mappedValue('rootDir_deRun', rootDir_deRun)
        rootDir_foreignBxo = csParam.mappedValue('rootDir_foreignBxo', rootDir_foreignBxo)
####+END:
        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        basesPolicy = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        rootPrefix = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)

        if basesPolicy == "bxoPolicy":
            if not bisosUserName:
                bisosUserName = bisosPolicy.bisosAccountName()
                
            if not bisosGroupName:
                bisosGroupName = bisosPolicy.bisosGroupName()

            if not bystarUserName:
                bystarUserName = bisosPolicy.bystarAccountName()
                
            if not bystarGroupName:
                bystarGroupName = bisosPolicy.bystarGroupName()
                
            if not rootDir_bisos:
                rootDir_bisos = os.path.join(rootPrefix, bisosPolicy.rootDir_bisos())

            if not rootDir_bxo:
                rootDir_bxo = os.path.join(rootPrefix, bisosPolicy.rootDir_bxo())

            if not rootDir_deRun:
                rootDir_deRun = os.path.join(rootPrefix, bisosPolicy.rootDir_deRun())

        elif basesPolicy == "foreignBxoPolicy":
            if not bisosUserName:
                return b_io.eh.problem_usageError("Missing bisosUserName")

            if not bisosGroupName:
                return b_io.eh.problem_usageError("Missing bisosGroupName")

            if not bystarUserName:
                return b_io.eh.problem_usageError("Missing bystarUserName")

            if not bystarGroupName:
                return b_io.eh.problem_usageError("Missing bystarGroupName")

            if not rootDir_foreignBxo:
                return b_io.eh.problem_usageError("Missing rootDir_foreignBxo")

            if not rootDir_provisioners:
                rootDir_provisioners = os.path.join(rootPrefix, bisosPolicy.rootDir_provisioners())

            if not rootDir_bisos:
                rootDir_bisos = os.path.join(rootPrefix, bisosPolicy.rootDir_bisos())

            if not rootDir_bxo:
                rootDir_bxo = os.path.join(rootPrefix, bisosPolicy.rootDir_bxo())

            if not rootDir_deRun:
                rootDir_deRun = os.path.join(rootPrefix, bisosPolicy.rootDir_deRun())
            
            
        elif basesPolicy == "externalPolicy":
            if not bisosUserName:
                return b_io.eh.problem_usageError("Missing bisosUserName")                

            if not bisosGroupName:
                return b_io.eh.problem_usageError("Missing bisosGroupName")

            if not bystarUserName:
                return b_io.eh.problem_usageError("Missing bystarUserName")                

            if not bystarGroupName:
                return b_io.eh.problem_usageError("Missing bystarGroupName")
            
            if not rootDir_foreignBxo:
                return b_io.eh.problem_usageError("Missing rootDir_foreignBxo")

            if not rootDir_provisioners:
                return b_io.eh.problem_usageError("Missing rootDir_provisioners")
            
            if not rootDir_bisos:
                return b_io.eh.problem_usageError("Missing rootDir_bisos")

            if not rootDir_bxo:
                return b_io.eh.problem_usageError("Missing rootDir_bxo")                

            if not rootDir_deRun:
                return b_io.eh.problem_usageError("Missing rootDir_deRun")                
            
            
        else:
            return b_io.eh.critical_oops("basesPolicy={}".format(basesPolicy))

        pkgInfoParsSet().cmnd(
            interactive=False,
            configBaseDir=configBaseDir,
            bisosUserName=bisosUserName,
            bisosGroupName=bisosGroupName,
            bystarUserName=bystarUserName,
            bystarGroupName=bystarGroupName,
            rootDir_foreignBxo=rootDir_foreignBxo,
            rootDir_provisioners=rootDir_provisioners,
            rootDir_bisos=rootDir_bisos,
            rootDir_bxo=rootDir_bxo,
            rootDir_deRun=rootDir_deRun,
        )

    def cmndDesc(): """
** Set File Parameters at ../pkgInfo/fp -- By default
** TODO NOTYET auto detect marme.dev -- marme.control and decide where they should be, perhaps in /var/
"""

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
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
    
    

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
