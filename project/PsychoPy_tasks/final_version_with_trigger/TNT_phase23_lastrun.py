#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on January 29, 2013, at 14:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import random
acc = []


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'TNT_phase23'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\eeglab\\Desktop\\Hangbin MRes\\final_version_with_trigger\\TNT_phase23_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1493, 933], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=(0.0039, 0.0039, 0.0039), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setupExp"
setupExpClock = core.Clock()
# make a dictionary to hold scores for stimulus texts
scoreDict = {}
allData = data.importConditions(u'Stimuli_TNT.xlsx')
allData2 = data.importConditions(u'Stimuli_TNT2.xlsx')
minCorrect = 1
for dl in allData:
    scoreDict[dl[u'cue']] = 0
random.shuffle(allData)
random.shuffle(allData2)

SubjNum=float(expInfo['participant'])
if SubjNum%6 == 0:
    think = 'cond1'
    nothink = 'cond2'
    baseline = 'cond3'
    condition1 = 'think'
    condition2 = 'nothink'
    condition3 = 'baseline'
elif SubjNum%6 == 1:
    think = 'cond2'
    nothink = 'cond1'
    baseline = 'cond3'
    condition1 = 'nothink'
    condition2 = 'think'
    condition3 = 'baseline'
elif SubjNum%6 == 2:
    think = 'cond3'
    nothink = 'cond1'
    baseline = 'cond2'
    condition1 = 'nothink'
    condition2 = 'baseline'
    condition3 = 'think'
elif SubjNum%6 == 3:
    think = 'cond1'
    nothink = 'cond3'
    baseline = 'cond2'
    condition1 = 'think'
    condition2 = 'baseline'
    condition3 = 'nothink'
elif SubjNum%6 == 4:
    think = 'cond2'
    nothink = 'cond3'
    baseline = 'cond1'
    condition1 = 'baseline'
    condition2 = 'think'
    condition3 = 'nothink'
elif SubjNum%6 == 5:
    think = 'cond3'
    nothink = 'cond2'
    baseline = 'cond1'
    condition1 = 'baseline'
    condition2 = 'nothink'
    condition3 = 'think'

cond_prac = []
cond_think = []
cond_nothink = []
cond_base = []
cond_percp = []
for k in range(0,len(allData2)):
    if allData2[k]['cond'] in ['prac1','prac2']:
        cond_prac.append(allData2[k])
    elif allData2[k]['cond'] == 'percp':
        cond_percp.append(allData2[k])
    elif allData2[k]['cond'] == think:
        cond_think.append(allData2[k])
    elif allData2[k]['cond'] == nothink:
        cond_nothink.append(allData2[k])
    elif allData2[k]['cond'] == baseline:
        cond_base.append(allData2[k])

# set TNT stimulus
TNT_cond = cond_think + cond_nothink + cond_percp
block = TNT_cond + TNT_cond
rep_formal_TNT = len(block)

pool_fm = [x for x in (range(0,rep_formal_TNT))]
random.shuffle(pool_fm)

ind_test = cond_think + cond_nothink + cond_base
dep_test = cond_think + cond_nothink + cond_base
rep_indTest = len(ind_test)
rep_depTest = len(dep_test)

pool_test = [x for x in (range(0,rep_indTest))]
random.shuffle(pool_test)

# counterbalance final tests

rand_number = random.randint(1,2)
if rand_number == 1:
    random_indTest = 1
    random_depTest = 0
elif rand_number == 2:
    random_indTest = 0
    random_depTest = 1
# Key parameter
win.mouseVisible = False
TextColour = 'white'
FontSize = 0.03

# skip phase
resting_rep = 0 #default = 1
dropoff_rep = 0 #default = 1000
learnTest_rep = 0 #default = 1
prac_rep = 0 # default = 1000
TNT_rep = 5 # default = 5 (replicate 5 times/blocks)




# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome back to the test!\n\nNext, you will be tested with EEG recording.\n\nEEG recording is very sensitive, and even small movements can create noise in the signal which makes analysis difficult. As such, it is important that you are seated comfortably, with your feet on the floor and hands on the desk. Please try to keep your head up and your eyes centred on the screen.\n\n\npress SPACE to begin the experiment',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "rs_instruction"
rs_instructionClock = core.Clock()
rs_instr_title = visual.TextStim(win=win, name='rs_instr_title',
    text='Resting State Recording',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rs_instr_text = visual.TextStim(win=win, name='rs_instr_text',
    text="The part of this study involves taking a resting state recording. This simply involves sitting still for short period of time whilst we record your brain activity. During this time feel free to let your mind wander - it's not important to the experiment what you're thinking here\n\nWhen the recording begins you will be presented with a small + symbol in the middle of the screen. Please stare at this cross and continue to sit still until you see the next instruction. As blinking can make noise in the EEG signal, please try to blink as little as you comfortably can.",
    font='Open Sans',
    pos=(0, -0.0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rs_instr_resptext = visual.TextStim(win=win, name='rs_instr_resptext',
    text='Please press SPACE to begin',
    font='Open Sans',
    pos=(0, -0.3), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rs_instr_resp = keyboard.Keyboard()

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
countdown_text = visual.TextStim(win=win, name='countdown_text',
    text='Beginning task in...',
    font='Open Sans',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
timer_text_5 = visual.TextStim(win=win, name='timer_text_5',
    text='5',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
timer_text_4 = visual.TextStim(win=win, name='timer_text_4',
    text='4',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
timer_text_3 = visual.TextStim(win=win, name='timer_text_3',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
timer_text_2 = visual.TextStim(win=win, name='timer_text_2',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
timer_text_1 = visual.TextStim(win=win, name='timer_text_1',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "resting_state"
resting_stateClock = core.Clock()
rs_fixation = visual.ShapeStim(
    win=win, name='rs_fixation', vertices='cross',
    size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
rsEo_begin = parallel.ParallelPort(address='0xD010')
rsEO_end = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "dropIntro"
dropIntroClock = core.Clock()
Intro_drop = visual.TextStim(win=win, name='Intro_drop',
    text="Resting EEG recording ended. Now let's go back to the word pairs.\n\nIn case you have forgotten what you learned earlier, let's test and practice again.\n\nIn this phase, you will be shown a word from each pair. You should recall the other paired word and say it aloud.\n\nThe words you responded to correctly will be removed from the list. \n\nWe will repeat this until you have memorised every word pair.\n\nPlease press SPACE to continue\n",
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intDrop_resp = keyboard.Keyboard()

# Initialize components for Routine "dropintro12"
dropintro12Clock = core.Clock()
Intro_drop2 = visual.TextStim(win=win, name='Intro_drop2',
    text='The aim of this stage is to help you to learn all of the word pairs, so the accuracy in this stage will not be recorded.\n\n\nPlease press SPACE to continue\n\nGood luck!',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intDrop_resp2 = keyboard.Keyboard()

# Initialize components for Routine "phase1_trial2"
phase1_trial2Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cue_stimili = visual.TextStim(win=win, name='cue_stimili',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
msg='no message!'#if this comes up we forgot to update the msg!
msgcolor = 'white'
resp_drop = keyboard.Keyboard()

# Initialize components for Routine "drop_fdbk_3"
drop_fdbk_3Clock = core.Clock()
drop_fdbk_4 = visual.TextStim(win=win, name='drop_fdbk_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
drop_target2 = visual.TextStim(win=win, name='drop_target2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "LearningTestIntro"
LearningTestIntroClock = core.Clock()
LT_intro = visual.TextStim(win=win, name='LT_intro',
    text='Now, your memory of all these pairs will be tested. \n\nYou will be shown a word in each word pair, please try to recall the associate paired word.\n\nWhen you see the "SPEAK NOW" instruction, please say the associate word aloud. Please try to say as many word pairs as you can recall. Your accuracy will be recorded.\n\nNo feedback will be given at this stage.\n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LT_resp = keyboard.Keyboard()
start_recording = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "ISI_variable"
ISI_variableClock = core.Clock()
fix600 = visual.TextStim(win=win, name='fix600',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
variable_ISI = visual.TextStim(win=win, name='variable_ISI',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fix_trigger = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "phase1_trial"
phase1_trialClock = core.Clock()
say_instru = visual.TextStim(win=win, name='say_instru',
    text='',
    font='Open Sans',
    pos=(0, -0.05), height=0.025, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WordPairs_all = visual.TextStim(win=win, name='WordPairs_all',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
LearningTest = keyboard.Keyboard()
StudyTest_trigger = parallel.ParallelPort(address='0xD010')
StudyTest_WordNumber = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "test_accuracy"
test_accuracyClock = core.Clock()
phase1_acc = visual.TextStim(win=win, name='phase1_acc',
    text='',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
phase1_continue = visual.TextStim(win=win, name='phase1_continue',
    text='Press SPACE to continue',
    font='Open Sans',
    pos=(0, -0.05), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "IntroPhase2"
IntroPhase2Clock = core.Clock()
TNT_intro = visual.TextStim(win=win, name='TNT_intro',
    text="TNT: TNT phase\n\nIn this part of the experiment you will be completing the attention and memory task.\n\nYou are going to see the left-hand side members of the previously presented word pairs in different colors on the computer screen. \n\nIf you see a word in ‘Green’ font, try to recall the previously paired word with this presented word and keep the associate word in mind.\n\nIf you see a word in ‘Red’ font, try to prevent the previously paired word from coming into your mind.\n\nIf you see a word in 'Black' font, try to pay attention to it.\n\nPress SPACE to continue.",
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_intro2 = keyboard.Keyboard()

# Initialize components for Routine "introPhase22"
introPhase22Clock = core.Clock()
TNT_intro_2 = visual.TextStim(win=win, name='TNT_intro_2',
    text='After the end of cues, you need to answer if the associated word entered your mind in this trial by press "f" (yes) with your left index finger or "j" (no) with your right index finger. Please do not think too much and press it as quicky as possible based on your intuition.\n\nAfter reading a word presented in black font, do not respond.\n\nDuring this phase, please do fixate and concentrate on the word cue without looking away while the word is on screen.\n\nYou can have a break if you see a slide saying take a break.\n\nYou will have a chance to complete some practice examples before starting the experiment properly.\n\nPress SPACE to begin the practice.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_intro2_2 = keyboard.Keyboard()

# Initialize components for Routine "ISI_variable"
ISI_variableClock = core.Clock()
fix600 = visual.TextStim(win=win, name='fix600',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
variable_ISI = visual.TextStim(win=win, name='variable_ISI',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fix_trigger = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "phase2_trial_prac"
phase2_trial_pracClock = core.Clock()
rep_prac_TNT = len(cond_prac)
stim_disp = 'it does not work'
color = "white"
loopIdx = -1

cue_prac = visual.TextStim(win=win, name='cue_prac',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rate_awareness"
rate_awarenessClock = core.Clock()
ratePrac_instruText = visual.TextStim(win=win, name='ratePrac_instruText',
    text='Did the associated word come to mind, even briefly?',
    font='Open Sans',
    pos=(0, 0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ratePrac_text = visual.TextStim(win=win, name='ratePrac_text',
    text='Yes (press "f")                         No (press "j")',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ratePrac_resp = keyboard.Keyboard()

# Initialize components for Routine "TNT_prc_qs1"
TNT_prc_qs1Clock = core.Clock()
prc_qs_text = visual.TextStim(win=win, name='prc_qs_text',
    text='Please answer some questions about what you did earlier.\n\n1. When seeing the green word,  did you try to recall the paired word and keep it in mind?\n\nyes (press keyboard 1) \n\nno (press keyboard 0)',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
qs_resp1 = keyboard.Keyboard()

# Initialize components for Routine "TNT_prc_qs2"
TNT_prc_qs2Clock = core.Clock()
prc_qs_text2 = visual.TextStim(win=win, name='prc_qs_text2',
    text='2. When seeing the *red* word,  did you try to not think about the paired word?\n\nyes (press keyboard 1) \n\nno (press keyboard 0)',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
qs_resp2 = keyboard.Keyboard()

# Initialize components for Routine "TNT_prc_qs3"
TNT_prc_qs3Clock = core.Clock()
prc_qs_text3 = visual.TextStim(win=win, name='prc_qs_text3',
    text='3. When seeing the cue word,  did you think about any other unrelated information?\n\nyes (press keyboard 1) \n\nno (press keyboard 0)',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
qs_resp3 = keyboard.Keyboard()

# Initialize components for Routine "prac_end"
prac_endClock = core.Clock()
prc_end = visual.TextStim(win=win, name='prc_end',
    text='Remember, you are expected to try to think about the paired word if the cue word is green, and try to do *not* to think about the paired word if the cue word is red. \n\nPlease do not think about any unrelated information to distract you during the task, and please try not to move your eyes away from the central cross at any time while the cross and cue words are presented.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prc_end_resp = keyboard.Keyboard()

# Initialize components for Routine "prac_end2"
prac_end2Clock = core.Clock()
prc_end2 = visual.TextStim(win=win, name='prc_end2',
    text='Please make sure you understand the rules clearly, or your data would seriously harm the results of our experiment!\n\nPress "p" if you do not understand these rules very clearly and if you want to practice one more time.\n\nPress SPACE if you think you are clear and are ready to begin the formal session.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prc_end_resp2 = keyboard.Keyboard()

# Initialize components for Routine "prac_end3"
prac_end3Clock = core.Clock()

# Initialize components for Routine "fmIntro1"
fmIntro1Clock = core.Clock()
fmIntro_txt = visual.TextStim(win=win, name='fmIntro_txt',
    text='This section will take around 40 minutes to complete.\n\nDuring this phase, please follow the instructions you just learned: \n\ngreen font: recall and keep the paired word in mind \n\nred font: prevent the paired word from coming to mind \n\nblack font: simply pay attention to the cue word \n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fmIntro_resp = keyboard.Keyboard()

# Initialize components for Routine "fmIntro2"
fmIntro2Clock = core.Clock()
fmIntro_txt2 = visual.TextStim(win=win, name='fmIntro_txt2',
    text="Please fixate and concentrate on the word cue without looking away while the word appeared. \n\nIt's very important for our study!\n\nYou can have a rest when you see the resting instruction. \n\nNow, please choose a comfortable sitting position.\n\nPress SPACE to begin the task.",
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fmIntro_resp2 = keyboard.Keyboard()

# Initialize components for Routine "ISI_variable"
ISI_variableClock = core.Clock()
fix600 = visual.TextStim(win=win, name='fix600',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
variable_ISI = visual.TextStim(win=win, name='variable_ISI',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fix_trigger = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "phase2_trial_fm"
phase2_trial_fmClock = core.Clock()
stim_disp = 'it does not work'
color = "white"

trl_fm = -1
cue_fm = visual.TextStim(win=win, name='cue_fm',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TNT_trigger = parallel.ParallelPort(address='0xD010')
pair_mark = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "rate_awareness"
rate_awarenessClock = core.Clock()
ratePrac_instruText = visual.TextStim(win=win, name='ratePrac_instruText',
    text='Did the associated word come to mind, even briefly?',
    font='Open Sans',
    pos=(0, 0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ratePrac_text = visual.TextStim(win=win, name='ratePrac_text',
    text='Yes (press "f")                         No (press "j")',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ratePrac_resp = keyboard.Keyboard()

# Initialize components for Routine "short_break"
short_breakClock = core.Clock()
break10s = visual.TextStim(win=win, name='break10s',
    text='Take a break!\n\nYou can relax your eyes and body, and clear you throat at this moment.\n\nThe task will begin automatically in...',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
timer_10 = visual.TextStim(win=win, name='timer_10',
    text='10 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
var_9 = visual.TextStim(win=win, name='var_9',
    text='9 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
var_8 = visual.TextStim(win=win, name='var_8',
    text='8 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
var_7 = visual.TextStim(win=win, name='var_7',
    text='7 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
var_6 = visual.TextStim(win=win, name='var_6',
    text='6 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
var_5 = visual.TextStim(win=win, name='var_5',
    text='5 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
var_4 = visual.TextStim(win=win, name='var_4',
    text='4 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
var_3 = visual.TextStim(win=win, name='var_3',
    text='3 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
var_2 = visual.TextStim(win=win, name='var_2',
    text='2 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
var_1 = visual.TextStim(win=win, name='var_1',
    text='1 s',
    font='Open Sans',
    pos=(0, -0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "TNTrest"
TNTrestClock = core.Clock()
process_info = visual.TextStim(win=win, name='process_info',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
BreakIntro = visual.TextStim(win=win, name='BreakIntro',
    text='Take a break!\n\nPress SPACE to continue the experiment after at least 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
BreakEnd = keyboard.Keyboard()

# Initialize components for Routine "IntroIndTest"
IntroIndTestClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Different Probe Test\n\nIn this test, you will be given the category and the first letter of the paired word (right handed) you remember earlier. When you see the "SPEAK NOW" instruction, try to say this word aloud if you remember it.\n\nNote that you are expected to recall as of the words as you can regardless previous conditions.\n\nPress SPACE to begin test.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "indepTest"
indepTestClock = core.Clock()
say_intru_IT = visual.TextStim(win=win, name='say_intru_IT',
    text='SPEAK NOW',
    font='Open Sans',
    pos=(0, -0.05), height=0.025, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IT_screen = visual.TextStim(win=win, name='IT_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IT_resp = keyboard.Keyboard()
IT_trigger = parallel.ParallelPort(address='0xD010')
IT_WordNumber = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "IntroDepTest"
IntroDepTestClock = core.Clock()
intro_ind = visual.TextStim(win=win, name='intro_ind',
    text='Same Probe Test\n\nIn this test, you are expected to try your best to recall all the associate paired words of the presented cue. When you see the "SPEAK NOW" instruction, try to say this word aloud.\n\nNote that you need to say any words you can recall aloud regardless of the previous task.\n\nPress SPACE to begin test.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ind = keyboard.Keyboard()

# Initialize components for Routine "depTest"
depTestClock = core.Clock()
say_instruDT = visual.TextStim(win=win, name='say_instruDT',
    text='SPEAK NOW',
    font='Open Sans',
    pos=(0,-0.05), height=0.025, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DT_screen = visual.TextStim(win=win, name='DT_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
DT_resp = keyboard.Keyboard()
DT_trigger = parallel.ParallelPort(address='0xD010')
DT_WordNumber = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "randomizer"
randomizerClock = core.Clock()

# Initialize components for Routine "goodBye"
goodByeClock = core.Clock()
taskend = visual.TextStim(win=win, name='taskend',
    text='TNT finished. \n\nPlease wait for the experimenter.',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setupExp"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupExpComponents = []
for thisComponent in setupExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupExpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setupExp"-------
while continueRoutine:
    # get current time
    t = setupExpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupExpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupExp"-------
for thisComponent in setupExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setupExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [Welcome, key_resp]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rs_eeg = data.TrialHandler(nReps=resting_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rs_eeg')
thisExp.addLoop(rs_eeg)  # add the loop to the experiment
thisRs_eeg = rs_eeg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRs_eeg.rgb)
if thisRs_eeg != None:
    for paramName in thisRs_eeg:
        exec('{} = thisRs_eeg[paramName]'.format(paramName))

for thisRs_eeg in rs_eeg:
    currentLoop = rs_eeg
    # abbreviate parameter names if possible (e.g. rgb = thisRs_eeg.rgb)
    if thisRs_eeg != None:
        for paramName in thisRs_eeg:
            exec('{} = thisRs_eeg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rs_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    rs_instr_text.setHeight(FontSize)
    rs_instr_resptext.setHeight(FontSize)
    rs_instr_resp.keys = []
    rs_instr_resp.rt = []
    _rs_instr_resp_allKeys = []
    # keep track of which components have finished
    rs_instructionComponents = [rs_instr_title, rs_instr_text, rs_instr_resptext, rs_instr_resp]
    for thisComponent in rs_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rs_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rs_instruction"-------
    while continueRoutine:
        # get current time
        t = rs_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rs_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rs_instr_title* updates
        if rs_instr_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rs_instr_title.frameNStart = frameN  # exact frame index
            rs_instr_title.tStart = t  # local t and not account for scr refresh
            rs_instr_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rs_instr_title, 'tStartRefresh')  # time at next scr refresh
            rs_instr_title.setAutoDraw(True)
        
        # *rs_instr_text* updates
        if rs_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rs_instr_text.frameNStart = frameN  # exact frame index
            rs_instr_text.tStart = t  # local t and not account for scr refresh
            rs_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rs_instr_text, 'tStartRefresh')  # time at next scr refresh
            rs_instr_text.setAutoDraw(True)
        
        # *rs_instr_resptext* updates
        if rs_instr_resptext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rs_instr_resptext.frameNStart = frameN  # exact frame index
            rs_instr_resptext.tStart = t  # local t and not account for scr refresh
            rs_instr_resptext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rs_instr_resptext, 'tStartRefresh')  # time at next scr refresh
            rs_instr_resptext.setAutoDraw(True)
        
        # *rs_instr_resp* updates
        waitOnFlip = False
        if rs_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rs_instr_resp.frameNStart = frameN  # exact frame index
            rs_instr_resp.tStart = t  # local t and not account for scr refresh
            rs_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rs_instr_resp, 'tStartRefresh')  # time at next scr refresh
            rs_instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rs_instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rs_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rs_instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = rs_instr_resp.getKeys(keyList=['space'], waitRelease=False)
            _rs_instr_resp_allKeys.extend(theseKeys)
            if len(_rs_instr_resp_allKeys):
                rs_instr_resp.keys = _rs_instr_resp_allKeys[-1].name  # just the last key pressed
                rs_instr_resp.rt = _rs_instr_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rs_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rs_instruction"-------
    for thisComponent in rs_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rs_eeg.addData('rs_instr_title.started', rs_instr_title.tStartRefresh)
    rs_eeg.addData('rs_instr_title.stopped', rs_instr_title.tStopRefresh)
    rs_eeg.addData('rs_instr_text.started', rs_instr_text.tStartRefresh)
    rs_eeg.addData('rs_instr_text.stopped', rs_instr_text.tStopRefresh)
    rs_eeg.addData('rs_instr_resptext.started', rs_instr_resptext.tStartRefresh)
    rs_eeg.addData('rs_instr_resptext.stopped', rs_instr_resptext.tStopRefresh)
    # check responses
    if rs_instr_resp.keys in ['', [], None]:  # No response was made
        rs_instr_resp.keys = None
    rs_eeg.addData('rs_instr_resp.keys',rs_instr_resp.keys)
    if rs_instr_resp.keys != None:  # we had a response
        rs_eeg.addData('rs_instr_resp.rt', rs_instr_resp.rt)
    rs_eeg.addData('rs_instr_resp.started', rs_instr_resp.tStartRefresh)
    rs_eeg.addData('rs_instr_resp.stopped', rs_instr_resp.tStopRefresh)
    # the Routine "rs_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "countdown"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    countdownComponents = [countdown_text, timer_text_5, timer_text_4, timer_text_3, timer_text_2, timer_text_1]
    for thisComponent in countdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = countdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *countdown_text* updates
        if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_text.frameNStart = frameN  # exact frame index
            countdown_text.tStart = t  # local t and not account for scr refresh
            countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
            countdown_text.setAutoDraw(True)
        if countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown_text.tStop = t  # not accounting for scr refresh
                countdown_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown_text, 'tStopRefresh')  # time at next scr refresh
                countdown_text.setAutoDraw(False)
        
        # *timer_text_5* updates
        if timer_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text_5.frameNStart = frameN  # exact frame index
            timer_text_5.tStart = t  # local t and not account for scr refresh
            timer_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text_5, 'tStartRefresh')  # time at next scr refresh
            timer_text_5.setAutoDraw(True)
        if timer_text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_text_5.tStop = t  # not accounting for scr refresh
                timer_text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text_5, 'tStopRefresh')  # time at next scr refresh
                timer_text_5.setAutoDraw(False)
        
        # *timer_text_4* updates
        if timer_text_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text_4.frameNStart = frameN  # exact frame index
            timer_text_4.tStart = t  # local t and not account for scr refresh
            timer_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text_4, 'tStartRefresh')  # time at next scr refresh
            timer_text_4.setAutoDraw(True)
        if timer_text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_text_4.tStop = t  # not accounting for scr refresh
                timer_text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text_4, 'tStopRefresh')  # time at next scr refresh
                timer_text_4.setAutoDraw(False)
        
        # *timer_text_3* updates
        if timer_text_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text_3.frameNStart = frameN  # exact frame index
            timer_text_3.tStart = t  # local t and not account for scr refresh
            timer_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text_3, 'tStartRefresh')  # time at next scr refresh
            timer_text_3.setAutoDraw(True)
        if timer_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_text_3.tStop = t  # not accounting for scr refresh
                timer_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text_3, 'tStopRefresh')  # time at next scr refresh
                timer_text_3.setAutoDraw(False)
        
        # *timer_text_2* updates
        if timer_text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text_2.frameNStart = frameN  # exact frame index
            timer_text_2.tStart = t  # local t and not account for scr refresh
            timer_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text_2, 'tStartRefresh')  # time at next scr refresh
            timer_text_2.setAutoDraw(True)
        if timer_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_text_2.tStop = t  # not accounting for scr refresh
                timer_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text_2, 'tStopRefresh')  # time at next scr refresh
                timer_text_2.setAutoDraw(False)
        
        # *timer_text_1* updates
        if timer_text_1.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text_1.frameNStart = frameN  # exact frame index
            timer_text_1.tStart = t  # local t and not account for scr refresh
            timer_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text_1, 'tStartRefresh')  # time at next scr refresh
            timer_text_1.setAutoDraw(True)
        if timer_text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_text_1.tStop = t  # not accounting for scr refresh
                timer_text_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_text_1, 'tStopRefresh')  # time at next scr refresh
                timer_text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdown"-------
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rs_eeg.addData('countdown_text.started', countdown_text.tStartRefresh)
    rs_eeg.addData('countdown_text.stopped', countdown_text.tStopRefresh)
    rs_eeg.addData('timer_text_5.started', timer_text_5.tStartRefresh)
    rs_eeg.addData('timer_text_5.stopped', timer_text_5.tStopRefresh)
    rs_eeg.addData('timer_text_4.started', timer_text_4.tStartRefresh)
    rs_eeg.addData('timer_text_4.stopped', timer_text_4.tStopRefresh)
    rs_eeg.addData('timer_text_3.started', timer_text_3.tStartRefresh)
    rs_eeg.addData('timer_text_3.stopped', timer_text_3.tStopRefresh)
    rs_eeg.addData('timer_text_2.started', timer_text_2.tStartRefresh)
    rs_eeg.addData('timer_text_2.stopped', timer_text_2.tStopRefresh)
    rs_eeg.addData('timer_text_1.started', timer_text_1.tStartRefresh)
    rs_eeg.addData('timer_text_1.stopped', timer_text_1.tStopRefresh)
    
    # ------Prepare to start Routine "resting_state"-------
    continueRoutine = True
    routineTimer.add(305.000000)
    # update component parameters for each repeat
    rs_fixation.setSize(0.03)
    # keep track of which components have finished
    resting_stateComponents = [rs_fixation, rsEo_begin, rsEO_end]
    for thisComponent in resting_stateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resting_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resting_state"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = resting_stateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resting_stateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rs_fixation* updates
        if rs_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rs_fixation.frameNStart = frameN  # exact frame index
            rs_fixation.tStart = t  # local t and not account for scr refresh
            rs_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rs_fixation, 'tStartRefresh')  # time at next scr refresh
            rs_fixation.setAutoDraw(True)
        if rs_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rs_fixation.tStartRefresh + 305-frameTolerance:
                # keep track of stop time/frame for later
                rs_fixation.tStop = t  # not accounting for scr refresh
                rs_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rs_fixation, 'tStopRefresh')  # time at next scr refresh
                rs_fixation.setAutoDraw(False)
        # *rsEo_begin* updates
        if rsEo_begin.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rsEo_begin.frameNStart = frameN  # exact frame index
            rsEo_begin.tStart = t  # local t and not account for scr refresh
            rsEo_begin.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rsEo_begin, 'tStartRefresh')  # time at next scr refresh
            rsEo_begin.status = STARTED
            win.callOnFlip(rsEo_begin.setData, int(90))
        if rsEo_begin.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rsEo_begin.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                rsEo_begin.tStop = t  # not accounting for scr refresh
                rsEo_begin.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rsEo_begin, 'tStopRefresh')  # time at next scr refresh
                rsEo_begin.status = FINISHED
                win.callOnFlip(rsEo_begin.setData, int(0))
        # *rsEO_end* updates
        if rsEO_end.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
            # keep track of start time/frame for later
            rsEO_end.frameNStart = frameN  # exact frame index
            rsEO_end.tStart = t  # local t and not account for scr refresh
            rsEO_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rsEO_end, 'tStartRefresh')  # time at next scr refresh
            rsEO_end.status = STARTED
            win.callOnFlip(rsEO_end.setData, int(91))
        if rsEO_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rsEO_end.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                rsEO_end.tStop = t  # not accounting for scr refresh
                rsEO_end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rsEO_end, 'tStopRefresh')  # time at next scr refresh
                rsEO_end.status = FINISHED
                win.callOnFlip(rsEO_end.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resting_stateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resting_state"-------
    for thisComponent in resting_stateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rs_eeg.addData('rs_fixation.started', rs_fixation.tStartRefresh)
    rs_eeg.addData('rs_fixation.stopped', rs_fixation.tStopRefresh)
    if rsEo_begin.status == STARTED:
        win.callOnFlip(rsEo_begin.setData, int(0))
    rs_eeg.addData('rsEo_begin.started', rsEo_begin.tStart)
    rs_eeg.addData('rsEo_begin.stopped', rsEo_begin.tStop)
    if rsEO_end.status == STARTED:
        win.callOnFlip(rsEO_end.setData, int(0))
    rs_eeg.addData('rsEO_end.started', rsEO_end.tStartRefresh)
    rs_eeg.addData('rsEO_end.stopped', rsEO_end.tStopRefresh)
    thisExp.nextEntry()
    
# completed resting_rep repeats of 'rs_eeg'


# ------Prepare to start Routine "dropIntro"-------
continueRoutine = True
# update component parameters for each repeat
intDrop_resp.keys = []
intDrop_resp.rt = []
_intDrop_resp_allKeys = []
# keep track of which components have finished
dropIntroComponents = [Intro_drop, intDrop_resp]
for thisComponent in dropIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dropIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "dropIntro"-------
while continueRoutine:
    # get current time
    t = dropIntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dropIntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_drop* updates
    if Intro_drop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_drop.frameNStart = frameN  # exact frame index
        Intro_drop.tStart = t  # local t and not account for scr refresh
        Intro_drop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_drop, 'tStartRefresh')  # time at next scr refresh
        Intro_drop.setAutoDraw(True)
    
    # *intDrop_resp* updates
    waitOnFlip = False
    if intDrop_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intDrop_resp.frameNStart = frameN  # exact frame index
        intDrop_resp.tStart = t  # local t and not account for scr refresh
        intDrop_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intDrop_resp, 'tStartRefresh')  # time at next scr refresh
        intDrop_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intDrop_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intDrop_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intDrop_resp.status == STARTED and not waitOnFlip:
        theseKeys = intDrop_resp.getKeys(keyList=['space'], waitRelease=False)
        _intDrop_resp_allKeys.extend(theseKeys)
        if len(_intDrop_resp_allKeys):
            intDrop_resp.keys = _intDrop_resp_allKeys[-1].name  # just the last key pressed
            intDrop_resp.rt = _intDrop_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dropIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dropIntro"-------
for thisComponent in dropIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intDrop_resp.keys in ['', [], None]:  # No response was made
    intDrop_resp.keys = None
thisExp.addData('intDrop_resp.keys',intDrop_resp.keys)
if intDrop_resp.keys != None:  # we had a response
    thisExp.addData('intDrop_resp.rt', intDrop_resp.rt)
thisExp.nextEntry()
# the Routine "dropIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "dropintro12"-------
continueRoutine = True
# update component parameters for each repeat
intDrop_resp2.keys = []
intDrop_resp2.rt = []
_intDrop_resp2_allKeys = []
# keep track of which components have finished
dropintro12Components = [Intro_drop2, intDrop_resp2]
for thisComponent in dropintro12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dropintro12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "dropintro12"-------
while continueRoutine:
    # get current time
    t = dropintro12Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dropintro12Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_drop2* updates
    if Intro_drop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_drop2.frameNStart = frameN  # exact frame index
        Intro_drop2.tStart = t  # local t and not account for scr refresh
        Intro_drop2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_drop2, 'tStartRefresh')  # time at next scr refresh
        Intro_drop2.setAutoDraw(True)
    
    # *intDrop_resp2* updates
    waitOnFlip = False
    if intDrop_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intDrop_resp2.frameNStart = frameN  # exact frame index
        intDrop_resp2.tStart = t  # local t and not account for scr refresh
        intDrop_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intDrop_resp2, 'tStartRefresh')  # time at next scr refresh
        intDrop_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intDrop_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intDrop_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intDrop_resp2.status == STARTED and not waitOnFlip:
        theseKeys = intDrop_resp2.getKeys(keyList=['space'], waitRelease=False)
        _intDrop_resp2_allKeys.extend(theseKeys)
        if len(_intDrop_resp2_allKeys):
            intDrop_resp2.keys = _intDrop_resp2_allKeys[-1].name  # just the last key pressed
            intDrop_resp2.rt = _intDrop_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dropintro12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dropintro12"-------
for thisComponent in dropintro12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intDrop_resp2.keys in ['', [], None]:  # No response was made
    intDrop_resp2.keys = None
thisExp.addData('intDrop_resp2.keys',intDrop_resp2.keys)
if intDrop_resp2.keys != None:  # we had a response
    thisExp.addData('intDrop_resp2.rt', intDrop_resp2.rt)
thisExp.nextEntry()
# the Routine "dropintro12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Dropoff_phase = data.TrialHandler(nReps=dropoff_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli_TNT.xlsx'),
    seed=None, name='Dropoff_phase')
thisExp.addLoop(Dropoff_phase)  # add the loop to the experiment
thisDropoff_phase = Dropoff_phase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDropoff_phase.rgb)
if thisDropoff_phase != None:
    for paramName in thisDropoff_phase:
        exec('{} = thisDropoff_phase[paramName]'.format(paramName))

for thisDropoff_phase in Dropoff_phase:
    currentLoop = Dropoff_phase
    # abbreviate parameter names if possible (e.g. rgb = thisDropoff_phase.rgb)
    if thisDropoff_phase != None:
        for paramName in thisDropoff_phase:
            exec('{} = thisDropoff_phase[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase1_trial2"-------
    continueRoutine = True
    routineTimer.add(5.500000)
    # update component parameters for each repeat
    cue_stimili.setText(cue)
     ## Forces routine quit upon reaching criterion
    alreadyLearned = False
    if scoreDict[cue] >= minCorrect:
        continueRoutine = False
        alreadyLearned = True
    resp_drop.keys = []
    resp_drop.rt = []
    _resp_drop_allKeys = []
    # keep track of which components have finished
    phase1_trial2Components = [blank, cue_stimili, resp_drop]
    for thisComponent in phase1_trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase1_trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase1_trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = phase1_trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase1_trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # *cue_stimili* updates
        if cue_stimili.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            cue_stimili.frameNStart = frameN  # exact frame index
            cue_stimili.tStart = t  # local t and not account for scr refresh
            cue_stimili.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_stimili, 'tStartRefresh')  # time at next scr refresh
            cue_stimili.setAutoDraw(True)
        if cue_stimili.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_stimili.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                cue_stimili.tStop = t  # not accounting for scr refresh
                cue_stimili.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_stimili, 'tStopRefresh')  # time at next scr refresh
                cue_stimili.setAutoDraw(False)
        
        # *resp_drop* updates
        waitOnFlip = False
        if resp_drop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            resp_drop.frameNStart = frameN  # exact frame index
            resp_drop.tStart = t  # local t and not account for scr refresh
            resp_drop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_drop, 'tStartRefresh')  # time at next scr refresh
            resp_drop.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_drop.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_drop.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_drop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_drop.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                resp_drop.tStop = t  # not accounting for scr refresh
                resp_drop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_drop, 'tStopRefresh')  # time at next scr refresh
                resp_drop.status = FINISHED
        if resp_drop.status == STARTED and not waitOnFlip:
            theseKeys = resp_drop.getKeys(keyList=['f', 'j'], waitRelease=False)
            _resp_drop_allKeys.extend(theseKeys)
            if len(_resp_drop_allKeys):
                resp_drop.keys = _resp_drop_allKeys[-1].name  # just the last key pressed
                resp_drop.rt = _resp_drop_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase1_trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase1_trial2"-------
    for thisComponent in phase1_trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Dropoff_phase.addData('blank.started', blank.tStartRefresh)
    Dropoff_phase.addData('blank.stopped', blank.tStopRefresh)
    Dropoff_phase.addData('cue_stimili.started', cue_stimili.tStartRefresh)
    Dropoff_phase.addData('cue_stimili.stopped', cue_stimili.tStopRefresh)
    if alreadyLearned:
        Dropoff_phase.addData('response', 'LEARNED')
        Dropoff_phase.addData('correct', 'LEARNED')
        
    if resp_drop.keys: #make sure not empty, prevent list index error
        if 'f' in resp_drop.keys:
            msg = 'Correct'
            msgcolor = [-0.0039, 1.0000, -1.0000]
            scoreDict[cue] += 1
        elif 'j' in resp_drop.keys:
            msg = 'Incorrect'
            msgcolor = [0.7255, -0.8431, -0.5294]
    elif not resp_drop.keys:
        msg = 'Try to speak quickly.'
        msgcolor = [0.7255, -0.8431, -0.5294]
       
    # See if there are any words that 
    # have less than two correct
    haveTrialsLeft = False
    for st in scoreDict:
        if scoreDict[st] < minCorrect:
            haveTrialsLeft = True
            break
    
    if not haveTrialsLeft:
        Dropoff_phase.finished = True
    # check responses
    if resp_drop.keys in ['', [], None]:  # No response was made
        resp_drop.keys = None
    Dropoff_phase.addData('resp_drop.keys',resp_drop.keys)
    if resp_drop.keys != None:  # we had a response
        Dropoff_phase.addData('resp_drop.rt', resp_drop.rt)
    Dropoff_phase.addData('resp_drop.started', resp_drop.tStartRefresh)
    Dropoff_phase.addData('resp_drop.stopped', resp_drop.tStopRefresh)
    
    # ------Prepare to start Routine "drop_fdbk_3"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    drop_fdbk_4.setColor(msgcolor, colorSpace='rgb')
    drop_fdbk_4.setText(msg)
    drop_target2.setText(cue + '             ' + target)
    if alreadyLearned:
        continueRoutine = False
    # keep track of which components have finished
    drop_fdbk_3Components = [drop_fdbk_4, drop_target2]
    for thisComponent in drop_fdbk_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    drop_fdbk_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "drop_fdbk_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = drop_fdbk_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=drop_fdbk_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *drop_fdbk_4* updates
        if drop_fdbk_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            drop_fdbk_4.frameNStart = frameN  # exact frame index
            drop_fdbk_4.tStart = t  # local t and not account for scr refresh
            drop_fdbk_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(drop_fdbk_4, 'tStartRefresh')  # time at next scr refresh
            drop_fdbk_4.setAutoDraw(True)
        if drop_fdbk_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > drop_fdbk_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                drop_fdbk_4.tStop = t  # not accounting for scr refresh
                drop_fdbk_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(drop_fdbk_4, 'tStopRefresh')  # time at next scr refresh
                drop_fdbk_4.setAutoDraw(False)
        
        # *drop_target2* updates
        if drop_target2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            drop_target2.frameNStart = frameN  # exact frame index
            drop_target2.tStart = t  # local t and not account for scr refresh
            drop_target2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(drop_target2, 'tStartRefresh')  # time at next scr refresh
            drop_target2.setAutoDraw(True)
        if drop_target2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > drop_target2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                drop_target2.tStop = t  # not accounting for scr refresh
                drop_target2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(drop_target2, 'tStopRefresh')  # time at next scr refresh
                drop_target2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in drop_fdbk_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "drop_fdbk_3"-------
    for thisComponent in drop_fdbk_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Dropoff_phase.addData('drop_fdbk_4.started', drop_fdbk_4.tStartRefresh)
    Dropoff_phase.addData('drop_fdbk_4.stopped', drop_fdbk_4.tStopRefresh)
    Dropoff_phase.addData('drop_target2.started', drop_target2.tStartRefresh)
    Dropoff_phase.addData('drop_target2.stopped', drop_target2.tStopRefresh)
    thisExp.nextEntry()
    
# completed dropoff_rep repeats of 'Dropoff_phase'


# ------Prepare to start Routine "LearningTestIntro"-------
continueRoutine = True
# update component parameters for each repeat
LT_resp.keys = []
LT_resp.rt = []
_LT_resp_allKeys = []
# keep track of which components have finished
LearningTestIntroComponents = [LT_intro, LT_resp, start_recording]
for thisComponent in LearningTestIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LearningTestIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LearningTestIntro"-------
while continueRoutine:
    # get current time
    t = LearningTestIntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LearningTestIntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LT_intro* updates
    if LT_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LT_intro.frameNStart = frameN  # exact frame index
        LT_intro.tStart = t  # local t and not account for scr refresh
        LT_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LT_intro, 'tStartRefresh')  # time at next scr refresh
        LT_intro.setAutoDraw(True)
    
    # *LT_resp* updates
    waitOnFlip = False
    if LT_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LT_resp.frameNStart = frameN  # exact frame index
        LT_resp.tStart = t  # local t and not account for scr refresh
        LT_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LT_resp, 'tStartRefresh')  # time at next scr refresh
        LT_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(LT_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(LT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if LT_resp.status == STARTED and not waitOnFlip:
        theseKeys = LT_resp.getKeys(keyList=['space'], waitRelease=False)
        _LT_resp_allKeys.extend(theseKeys)
        if len(_LT_resp_allKeys):
            LT_resp.keys = _LT_resp_allKeys[-1].name  # just the last key pressed
            LT_resp.rt = _LT_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *start_recording* updates
    if start_recording.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_recording.frameNStart = frameN  # exact frame index
        start_recording.tStart = t  # local t and not account for scr refresh
        start_recording.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_recording, 'tStartRefresh')  # time at next scr refresh
        start_recording.status = STARTED
        win.callOnFlip(start_recording.setData, int(254))
    if start_recording.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_recording.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            start_recording.tStop = t  # not accounting for scr refresh
            start_recording.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_recording, 'tStopRefresh')  # time at next scr refresh
            start_recording.status = FINISHED
            win.callOnFlip(start_recording.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LearningTestIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LearningTestIntro"-------
for thisComponent in LearningTestIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('LT_intro.started', LT_intro.tStartRefresh)
thisExp.addData('LT_intro.stopped', LT_intro.tStopRefresh)
# check responses
if LT_resp.keys in ['', [], None]:  # No response was made
    LT_resp.keys = None
thisExp.addData('LT_resp.keys',LT_resp.keys)
if LT_resp.keys != None:  # we had a response
    thisExp.addData('LT_resp.rt', LT_resp.rt)
thisExp.nextEntry()
if start_recording.status == STARTED:
    win.callOnFlip(start_recording.setData, int(0))
thisExp.addData('start_recording.started', start_recording.tStartRefresh)
thisExp.addData('start_recording.stopped', start_recording.tStopRefresh)
# the Routine "LearningTestIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learning_test = data.TrialHandler(nReps=learnTest_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli_TNT.xlsx'),
    seed=None, name='learning_test')
thisExp.addLoop(learning_test)  # add the loop to the experiment
thisLearning_test = learning_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning_test.rgb)
if thisLearning_test != None:
    for paramName in thisLearning_test:
        exec('{} = thisLearning_test[paramName]'.format(paramName))

for thisLearning_test in learning_test:
    currentLoop = learning_test
    # abbreviate parameter names if possible (e.g. rgb = thisLearning_test.rgb)
    if thisLearning_test != None:
        for paramName in thisLearning_test:
            exec('{} = thisLearning_test[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISI_variable"-------
    continueRoutine = True
    # update component parameters for each repeat
    ISI = random.choice([p/5 for p in range(5, 13)])
    # keep track of which components have finished
    ISI_variableComponents = [fix600, variable_ISI, fix_trigger]
    for thisComponent in ISI_variableComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISI_variableClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI_variable"-------
    while continueRoutine:
        # get current time
        t = ISI_variableClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISI_variableClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix600* updates
        if fix600.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix600.frameNStart = frameN  # exact frame index
            fix600.tStart = t  # local t and not account for scr refresh
            fix600.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix600, 'tStartRefresh')  # time at next scr refresh
            fix600.setAutoDraw(True)
        if fix600.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix600.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                fix600.tStop = t  # not accounting for scr refresh
                fix600.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix600, 'tStopRefresh')  # time at next scr refresh
                fix600.setAutoDraw(False)
        
        # *variable_ISI* updates
        if variable_ISI.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
            # keep track of start time/frame for later
            variable_ISI.frameNStart = frameN  # exact frame index
            variable_ISI.tStart = t  # local t and not account for scr refresh
            variable_ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(variable_ISI, 'tStartRefresh')  # time at next scr refresh
            variable_ISI.setAutoDraw(True)
        if variable_ISI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > variable_ISI.tStartRefresh + ISI-frameTolerance:
                # keep track of stop time/frame for later
                variable_ISI.tStop = t  # not accounting for scr refresh
                variable_ISI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(variable_ISI, 'tStopRefresh')  # time at next scr refresh
                variable_ISI.setAutoDraw(False)
        # *fix_trigger* updates
        if fix_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_trigger.frameNStart = frameN  # exact frame index
            fix_trigger.tStart = t  # local t and not account for scr refresh
            fix_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_trigger, 'tStartRefresh')  # time at next scr refresh
            fix_trigger.status = STARTED
            win.callOnFlip(fix_trigger.setData, int(250))
        if fix_trigger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_trigger.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                fix_trigger.tStop = t  # not accounting for scr refresh
                fix_trigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_trigger, 'tStopRefresh')  # time at next scr refresh
                fix_trigger.status = FINISHED
                win.callOnFlip(fix_trigger.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_variableComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_variable"-------
    for thisComponent in ISI_variableComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning_test.addData('fix600.started', fix600.tStartRefresh)
    learning_test.addData('fix600.stopped', fix600.tStopRefresh)
    learning_test.addData('variable_ISI.started', variable_ISI.tStartRefresh)
    learning_test.addData('variable_ISI.stopped', variable_ISI.tStopRefresh)
    if fix_trigger.status == STARTED:
        win.callOnFlip(fix_trigger.setData, int(0))
    learning_test.addData('fix_trigger.started', fix_trigger.tStartRefresh)
    learning_test.addData('fix_trigger.stopped', fix_trigger.tStopRefresh)
    # the Routine "ISI_variable" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "phase1_trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    say_instru.setText('SPEAK NOW')
    WordPairs_all.setText(cue)
    LearningTest.keys = []
    LearningTest.rt = []
    _LearningTest_allKeys = []
    tiral_nall = learning_test.nTotal
    if learning_test.thisN == 0:
        number_correct = 0
    # keep track of which components have finished
    phase1_trialComponents = [say_instru, WordPairs_all, LearningTest, StudyTest_trigger, StudyTest_WordNumber]
    for thisComponent in phase1_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase1_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase1_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = phase1_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase1_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *say_instru* updates
        if say_instru.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            say_instru.frameNStart = frameN  # exact frame index
            say_instru.tStart = t  # local t and not account for scr refresh
            say_instru.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(say_instru, 'tStartRefresh')  # time at next scr refresh
            say_instru.setAutoDraw(True)
        if say_instru.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > say_instru.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                say_instru.tStop = t  # not accounting for scr refresh
                say_instru.frameNStop = frameN  # exact frame index
                win.timeOnFlip(say_instru, 'tStopRefresh')  # time at next scr refresh
                say_instru.setAutoDraw(False)
        
        # *WordPairs_all* updates
        if WordPairs_all.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WordPairs_all.frameNStart = frameN  # exact frame index
            WordPairs_all.tStart = t  # local t and not account for scr refresh
            WordPairs_all.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WordPairs_all, 'tStartRefresh')  # time at next scr refresh
            WordPairs_all.setAutoDraw(True)
        if WordPairs_all.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > WordPairs_all.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                WordPairs_all.tStop = t  # not accounting for scr refresh
                WordPairs_all.frameNStop = frameN  # exact frame index
                win.timeOnFlip(WordPairs_all, 'tStopRefresh')  # time at next scr refresh
                WordPairs_all.setAutoDraw(False)
        
        # *LearningTest* updates
        waitOnFlip = False
        if LearningTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LearningTest.frameNStart = frameN  # exact frame index
            LearningTest.tStart = t  # local t and not account for scr refresh
            LearningTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LearningTest, 'tStartRefresh')  # time at next scr refresh
            LearningTest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LearningTest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LearningTest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LearningTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LearningTest.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                LearningTest.tStop = t  # not accounting for scr refresh
                LearningTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LearningTest, 'tStopRefresh')  # time at next scr refresh
                LearningTest.status = FINISHED
        if LearningTest.status == STARTED and not waitOnFlip:
            theseKeys = LearningTest.getKeys(keyList=['f', 'j'], waitRelease=False)
            _LearningTest_allKeys.extend(theseKeys)
            if len(_LearningTest_allKeys):
                LearningTest.keys = _LearningTest_allKeys[-1].name  # just the last key pressed
                LearningTest.rt = _LearningTest_allKeys[-1].rt
                # was this correct?
                if (LearningTest.keys == str("'f'")) or (LearningTest.keys == "'f'"):
                    LearningTest.corr = 1
                else:
                    LearningTest.corr = 0
        # *StudyTest_trigger* updates
        if StudyTest_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyTest_trigger.frameNStart = frameN  # exact frame index
            StudyTest_trigger.tStart = t  # local t and not account for scr refresh
            StudyTest_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyTest_trigger, 'tStartRefresh')  # time at next scr refresh
            StudyTest_trigger.status = STARTED
            win.callOnFlip(StudyTest_trigger.setData, int(trigger_val))
        if StudyTest_trigger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyTest_trigger.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                StudyTest_trigger.tStop = t  # not accounting for scr refresh
                StudyTest_trigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(StudyTest_trigger, 'tStopRefresh')  # time at next scr refresh
                StudyTest_trigger.status = FINISHED
                win.callOnFlip(StudyTest_trigger.setData, int(0))
        # *StudyTest_WordNumber* updates
        if StudyTest_WordNumber.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            StudyTest_WordNumber.frameNStart = frameN  # exact frame index
            StudyTest_WordNumber.tStart = t  # local t and not account for scr refresh
            StudyTest_WordNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyTest_WordNumber, 'tStartRefresh')  # time at next scr refresh
            StudyTest_WordNumber.status = STARTED
            win.callOnFlip(StudyTest_WordNumber.setData, int(word_number))
        if StudyTest_WordNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyTest_WordNumber.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                StudyTest_WordNumber.tStop = t  # not accounting for scr refresh
                StudyTest_WordNumber.frameNStop = frameN  # exact frame index
                win.timeOnFlip(StudyTest_WordNumber, 'tStopRefresh')  # time at next scr refresh
                StudyTest_WordNumber.status = FINISHED
                win.callOnFlip(StudyTest_WordNumber.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase1_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase1_trial"-------
    for thisComponent in phase1_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning_test.addData('say_instru.started', say_instru.tStartRefresh)
    learning_test.addData('say_instru.stopped', say_instru.tStopRefresh)
    learning_test.addData('WordPairs_all.started', WordPairs_all.tStartRefresh)
    learning_test.addData('WordPairs_all.stopped', WordPairs_all.tStopRefresh)
    # check responses
    if LearningTest.keys in ['', [], None]:  # No response was made
        LearningTest.keys = None
        # was no response the correct answer?!
        if str("'f'").lower() == 'none':
           LearningTest.corr = 1;  # correct non-response
        else:
           LearningTest.corr = 0;  # failed to respond (incorrectly)
    # store data for learning_test (TrialHandler)
    learning_test.addData('LearningTest.keys',LearningTest.keys)
    learning_test.addData('LearningTest.corr', LearningTest.corr)
    if LearningTest.keys != None:  # we had a response
        learning_test.addData('LearningTest.rt', LearningTest.rt)
    learning_test.addData('LearningTest.started', LearningTest.tStartRefresh)
    learning_test.addData('LearningTest.stopped', LearningTest.tStopRefresh)
    if LearningTest.keys is not None:
        if 'f' in LearningTest.keys:
            number_correct = number_correct + 1
    acc = round(number_correct*100/tiral_nall,2)
    if (learning_test.thisN + 1) == tiral_nall:
        if acc >= 0.75:
            masg= "Your Accuracy = " + str(acc) + "%. Please press 'space' to continue"
        elif acc < 0.75:
            masg = "Your accuracy is low, please do *not* press any button and wait to learn again."
    
    learning_test.addData('condition1', condition1)
    learning_test.addData('condition2', condition2)
    learning_test.addData('condition3', condition3)
    if StudyTest_trigger.status == STARTED:
        win.callOnFlip(StudyTest_trigger.setData, int(0))
    learning_test.addData('StudyTest_trigger.started', StudyTest_trigger.tStartRefresh)
    learning_test.addData('StudyTest_trigger.stopped', StudyTest_trigger.tStopRefresh)
    if StudyTest_WordNumber.status == STARTED:
        win.callOnFlip(StudyTest_WordNumber.setData, int(0))
    learning_test.addData('StudyTest_WordNumber.started', StudyTest_WordNumber.tStartRefresh)
    learning_test.addData('StudyTest_WordNumber.stopped', StudyTest_WordNumber.tStopRefresh)
    thisExp.nextEntry()
    
# completed learnTest_rep repeats of 'learning_test'


# ------Prepare to start Routine "test_accuracy"-------
continueRoutine = True
# update component parameters for each repeat
if not acc:
    masg = 'no info passed'
phase1_acc.setText(masg)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
test_accuracyComponents = [phase1_acc, phase1_continue, key_resp_2]
for thisComponent in test_accuracyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_accuracyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_accuracy"-------
while continueRoutine:
    # get current time
    t = test_accuracyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_accuracyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *phase1_acc* updates
    if phase1_acc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        phase1_acc.frameNStart = frameN  # exact frame index
        phase1_acc.tStart = t  # local t and not account for scr refresh
        phase1_acc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(phase1_acc, 'tStartRefresh')  # time at next scr refresh
        phase1_acc.setAutoDraw(True)
    
    # *phase1_continue* updates
    if phase1_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        phase1_continue.frameNStart = frameN  # exact frame index
        phase1_continue.tStart = t  # local t and not account for scr refresh
        phase1_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(phase1_continue, 'tStartRefresh')  # time at next scr refresh
        phase1_continue.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_accuracyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_accuracy"-------
for thisComponent in test_accuracyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('phase1_continue.started', phase1_continue.tStartRefresh)
thisExp.addData('phase1_continue.stopped', phase1_continue.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "test_accuracy" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Prac_rep = data.TrialHandler(nReps=prac_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Prac_rep')
thisExp.addLoop(Prac_rep)  # add the loop to the experiment
thisPrac_rep = Prac_rep.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_rep.rgb)
if thisPrac_rep != None:
    for paramName in thisPrac_rep:
        exec('{} = thisPrac_rep[paramName]'.format(paramName))

for thisPrac_rep in Prac_rep:
    currentLoop = Prac_rep
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_rep.rgb)
    if thisPrac_rep != None:
        for paramName in thisPrac_rep:
            exec('{} = thisPrac_rep[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "IntroPhase2"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_intro2.keys = []
    resp_intro2.rt = []
    _resp_intro2_allKeys = []
    # keep track of which components have finished
    IntroPhase2Components = [TNT_intro, resp_intro2]
    for thisComponent in IntroPhase2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IntroPhase2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "IntroPhase2"-------
    while continueRoutine:
        # get current time
        t = IntroPhase2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IntroPhase2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TNT_intro* updates
        if TNT_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TNT_intro.frameNStart = frameN  # exact frame index
            TNT_intro.tStart = t  # local t and not account for scr refresh
            TNT_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TNT_intro, 'tStartRefresh')  # time at next scr refresh
            TNT_intro.setAutoDraw(True)
        
        # *resp_intro2* updates
        waitOnFlip = False
        if resp_intro2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_intro2.frameNStart = frameN  # exact frame index
            resp_intro2.tStart = t  # local t and not account for scr refresh
            resp_intro2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_intro2, 'tStartRefresh')  # time at next scr refresh
            resp_intro2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_intro2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_intro2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_intro2.status == STARTED and not waitOnFlip:
            theseKeys = resp_intro2.getKeys(keyList=['space'], waitRelease=False)
            _resp_intro2_allKeys.extend(theseKeys)
            if len(_resp_intro2_allKeys):
                resp_intro2.keys = _resp_intro2_allKeys[-1].name  # just the last key pressed
                resp_intro2.rt = _resp_intro2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntroPhase2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "IntroPhase2"-------
    for thisComponent in IntroPhase2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('TNT_intro.started', TNT_intro.tStartRefresh)
    Prac_rep.addData('TNT_intro.stopped', TNT_intro.tStopRefresh)
    # check responses
    if resp_intro2.keys in ['', [], None]:  # No response was made
        resp_intro2.keys = None
    Prac_rep.addData('resp_intro2.keys',resp_intro2.keys)
    if resp_intro2.keys != None:  # we had a response
        Prac_rep.addData('resp_intro2.rt', resp_intro2.rt)
    Prac_rep.addData('resp_intro2.started', resp_intro2.tStartRefresh)
    Prac_rep.addData('resp_intro2.stopped', resp_intro2.tStopRefresh)
    # the Routine "IntroPhase2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "introPhase22"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_intro2_2.keys = []
    resp_intro2_2.rt = []
    _resp_intro2_2_allKeys = []
    # keep track of which components have finished
    introPhase22Components = [TNT_intro_2, resp_intro2_2]
    for thisComponent in introPhase22Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introPhase22Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "introPhase22"-------
    while continueRoutine:
        # get current time
        t = introPhase22Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introPhase22Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TNT_intro_2* updates
        if TNT_intro_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TNT_intro_2.frameNStart = frameN  # exact frame index
            TNT_intro_2.tStart = t  # local t and not account for scr refresh
            TNT_intro_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TNT_intro_2, 'tStartRefresh')  # time at next scr refresh
            TNT_intro_2.setAutoDraw(True)
        
        # *resp_intro2_2* updates
        waitOnFlip = False
        if resp_intro2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_intro2_2.frameNStart = frameN  # exact frame index
            resp_intro2_2.tStart = t  # local t and not account for scr refresh
            resp_intro2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_intro2_2, 'tStartRefresh')  # time at next scr refresh
            resp_intro2_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_intro2_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_intro2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_intro2_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_intro2_2.getKeys(keyList=['space'], waitRelease=False)
            _resp_intro2_2_allKeys.extend(theseKeys)
            if len(_resp_intro2_2_allKeys):
                resp_intro2_2.keys = _resp_intro2_2_allKeys[-1].name  # just the last key pressed
                resp_intro2_2.rt = _resp_intro2_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introPhase22Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "introPhase22"-------
    for thisComponent in introPhase22Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('TNT_intro_2.started', TNT_intro_2.tStartRefresh)
    Prac_rep.addData('TNT_intro_2.stopped', TNT_intro_2.tStopRefresh)
    # check responses
    if resp_intro2_2.keys in ['', [], None]:  # No response was made
        resp_intro2_2.keys = None
    Prac_rep.addData('resp_intro2_2.keys',resp_intro2_2.keys)
    if resp_intro2_2.keys != None:  # we had a response
        Prac_rep.addData('resp_intro2_2.rt', resp_intro2_2.rt)
    Prac_rep.addData('resp_intro2_2.started', resp_intro2_2.tStartRefresh)
    Prac_rep.addData('resp_intro2_2.stopped', resp_intro2_2.tStopRefresh)
    # the Routine "introPhase22" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    TNT_prac_loop = data.TrialHandler(nReps=rep_prac_TNT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TNT_prac_loop')
    thisExp.addLoop(TNT_prac_loop)  # add the loop to the experiment
    thisTNT_prac_loop = TNT_prac_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNT_prac_loop.rgb)
    if thisTNT_prac_loop != None:
        for paramName in thisTNT_prac_loop:
            exec('{} = thisTNT_prac_loop[paramName]'.format(paramName))
    
    for thisTNT_prac_loop in TNT_prac_loop:
        currentLoop = TNT_prac_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTNT_prac_loop.rgb)
        if thisTNT_prac_loop != None:
            for paramName in thisTNT_prac_loop:
                exec('{} = thisTNT_prac_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI_variable"-------
        continueRoutine = True
        # update component parameters for each repeat
        ISI = random.choice([p/5 for p in range(5, 13)])
        # keep track of which components have finished
        ISI_variableComponents = [fix600, variable_ISI, fix_trigger]
        for thisComponent in ISI_variableComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISI_variableClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI_variable"-------
        while continueRoutine:
            # get current time
            t = ISI_variableClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISI_variableClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix600* updates
            if fix600.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix600.frameNStart = frameN  # exact frame index
                fix600.tStart = t  # local t and not account for scr refresh
                fix600.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix600, 'tStartRefresh')  # time at next scr refresh
                fix600.setAutoDraw(True)
            if fix600.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix600.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    fix600.tStop = t  # not accounting for scr refresh
                    fix600.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix600, 'tStopRefresh')  # time at next scr refresh
                    fix600.setAutoDraw(False)
            
            # *variable_ISI* updates
            if variable_ISI.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                variable_ISI.frameNStart = frameN  # exact frame index
                variable_ISI.tStart = t  # local t and not account for scr refresh
                variable_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(variable_ISI, 'tStartRefresh')  # time at next scr refresh
                variable_ISI.setAutoDraw(True)
            if variable_ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > variable_ISI.tStartRefresh + ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    variable_ISI.tStop = t  # not accounting for scr refresh
                    variable_ISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(variable_ISI, 'tStopRefresh')  # time at next scr refresh
                    variable_ISI.setAutoDraw(False)
            # *fix_trigger* updates
            if fix_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_trigger.frameNStart = frameN  # exact frame index
                fix_trigger.tStart = t  # local t and not account for scr refresh
                fix_trigger.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_trigger, 'tStartRefresh')  # time at next scr refresh
                fix_trigger.status = STARTED
                win.callOnFlip(fix_trigger.setData, int(250))
            if fix_trigger.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_trigger.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_trigger.tStop = t  # not accounting for scr refresh
                    fix_trigger.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_trigger, 'tStopRefresh')  # time at next scr refresh
                    fix_trigger.status = FINISHED
                    win.callOnFlip(fix_trigger.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI_variableComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI_variable"-------
        for thisComponent in ISI_variableComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNT_prac_loop.addData('fix600.started', fix600.tStartRefresh)
        TNT_prac_loop.addData('fix600.stopped', fix600.tStopRefresh)
        TNT_prac_loop.addData('variable_ISI.started', variable_ISI.tStartRefresh)
        TNT_prac_loop.addData('variable_ISI.stopped', variable_ISI.tStopRefresh)
        if fix_trigger.status == STARTED:
            win.callOnFlip(fix_trigger.setData, int(0))
        TNT_prac_loop.addData('fix_trigger.started', fix_trigger.tStartRefresh)
        TNT_prac_loop.addData('fix_trigger.stopped', fix_trigger.tStopRefresh)
        # the Routine "ISI_variable" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "phase2_trial_prac"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        loopIdx += 1
        stim_disp = cond_prac[loopIdx]['cue']
        cue_prac.setText(stim_disp)
        if cond_prac[loopIdx]['cond'] == 'prac1':
            color = "red"
        else :
            color = "green"
        
        
        
        cue_prac.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        phase2_trial_pracComponents = [cue_prac]
        for thisComponent in phase2_trial_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        phase2_trial_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "phase2_trial_prac"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = phase2_trial_pracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=phase2_trial_pracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cue_prac* updates
            if cue_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cue_prac.frameNStart = frameN  # exact frame index
                cue_prac.tStart = t  # local t and not account for scr refresh
                cue_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_prac, 'tStartRefresh')  # time at next scr refresh
                cue_prac.setAutoDraw(True)
            if cue_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_prac.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_prac.tStop = t  # not accounting for scr refresh
                    cue_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cue_prac, 'tStopRefresh')  # time at next scr refresh
                    cue_prac.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in phase2_trial_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "phase2_trial_prac"-------
        for thisComponent in phase2_trial_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNT_prac_loop.addData('cue', cond_prac[loopIdx]['cue']) #where trials is the name of the loop
        
        # ------Prepare to start Routine "rate_awareness"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        ratePrac_resp.keys = []
        ratePrac_resp.rt = []
        _ratePrac_resp_allKeys = []
        # keep track of which components have finished
        rate_awarenessComponents = [ratePrac_instruText, ratePrac_text, ratePrac_resp]
        for thisComponent in rate_awarenessComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rate_awarenessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rate_awareness"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rate_awarenessClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rate_awarenessClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ratePrac_instruText* updates
            if ratePrac_instruText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_instruText.frameNStart = frameN  # exact frame index
                ratePrac_instruText.tStart = t  # local t and not account for scr refresh
                ratePrac_instruText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_instruText, 'tStartRefresh')  # time at next scr refresh
                ratePrac_instruText.setAutoDraw(True)
            if ratePrac_instruText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_instruText.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_instruText.tStop = t  # not accounting for scr refresh
                    ratePrac_instruText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_instruText, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_instruText.setAutoDraw(False)
            
            # *ratePrac_text* updates
            if ratePrac_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_text.frameNStart = frameN  # exact frame index
                ratePrac_text.tStart = t  # local t and not account for scr refresh
                ratePrac_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_text, 'tStartRefresh')  # time at next scr refresh
                ratePrac_text.setAutoDraw(True)
            if ratePrac_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_text.tStop = t  # not accounting for scr refresh
                    ratePrac_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_text, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_text.setAutoDraw(False)
            
            # *ratePrac_resp* updates
            waitOnFlip = False
            if ratePrac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_resp.frameNStart = frameN  # exact frame index
                ratePrac_resp.tStart = t  # local t and not account for scr refresh
                ratePrac_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_resp, 'tStartRefresh')  # time at next scr refresh
                ratePrac_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ratePrac_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ratePrac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ratePrac_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_resp.tStop = t  # not accounting for scr refresh
                    ratePrac_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_resp, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_resp.status = FINISHED
            if ratePrac_resp.status == STARTED and not waitOnFlip:
                theseKeys = ratePrac_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _ratePrac_resp_allKeys.extend(theseKeys)
                if len(_ratePrac_resp_allKeys):
                    ratePrac_resp.keys = _ratePrac_resp_allKeys[-1].name  # just the last key pressed
                    ratePrac_resp.rt = _ratePrac_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rate_awarenessComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rate_awareness"-------
        for thisComponent in rate_awarenessComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNT_prac_loop.addData('ratePrac_instruText.started', ratePrac_instruText.tStartRefresh)
        TNT_prac_loop.addData('ratePrac_instruText.stopped', ratePrac_instruText.tStopRefresh)
        TNT_prac_loop.addData('ratePrac_text.started', ratePrac_text.tStartRefresh)
        TNT_prac_loop.addData('ratePrac_text.stopped', ratePrac_text.tStopRefresh)
        # check responses
        if ratePrac_resp.keys in ['', [], None]:  # No response was made
            ratePrac_resp.keys = None
        TNT_prac_loop.addData('ratePrac_resp.keys',ratePrac_resp.keys)
        if ratePrac_resp.keys != None:  # we had a response
            TNT_prac_loop.addData('ratePrac_resp.rt', ratePrac_resp.rt)
        TNT_prac_loop.addData('ratePrac_resp.started', ratePrac_resp.tStartRefresh)
        TNT_prac_loop.addData('ratePrac_resp.stopped', ratePrac_resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed rep_prac_TNT repeats of 'TNT_prac_loop'
    
    
    # ------Prepare to start Routine "TNT_prc_qs1"-------
    continueRoutine = True
    # update component parameters for each repeat
    qs_resp1.keys = []
    qs_resp1.rt = []
    _qs_resp1_allKeys = []
    # keep track of which components have finished
    TNT_prc_qs1Components = [prc_qs_text, qs_resp1]
    for thisComponent in TNT_prc_qs1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TNT_prc_qs1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TNT_prc_qs1"-------
    while continueRoutine:
        # get current time
        t = TNT_prc_qs1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TNT_prc_qs1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prc_qs_text* updates
        if prc_qs_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_qs_text.frameNStart = frameN  # exact frame index
            prc_qs_text.tStart = t  # local t and not account for scr refresh
            prc_qs_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_qs_text, 'tStartRefresh')  # time at next scr refresh
            prc_qs_text.setAutoDraw(True)
        
        # *qs_resp1* updates
        waitOnFlip = False
        if qs_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            qs_resp1.frameNStart = frameN  # exact frame index
            qs_resp1.tStart = t  # local t and not account for scr refresh
            qs_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(qs_resp1, 'tStartRefresh')  # time at next scr refresh
            qs_resp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(qs_resp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(qs_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if qs_resp1.status == STARTED and not waitOnFlip:
            theseKeys = qs_resp1.getKeys(keyList=['0', '1'], waitRelease=False)
            _qs_resp1_allKeys.extend(theseKeys)
            if len(_qs_resp1_allKeys):
                qs_resp1.keys = _qs_resp1_allKeys[-1].name  # just the last key pressed
                qs_resp1.rt = _qs_resp1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TNT_prc_qs1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TNT_prc_qs1"-------
    for thisComponent in TNT_prc_qs1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('prc_qs_text.started', prc_qs_text.tStartRefresh)
    Prac_rep.addData('prc_qs_text.stopped', prc_qs_text.tStopRefresh)
    # check responses
    if qs_resp1.keys in ['', [], None]:  # No response was made
        qs_resp1.keys = None
    Prac_rep.addData('qs_resp1.keys',qs_resp1.keys)
    if qs_resp1.keys != None:  # we had a response
        Prac_rep.addData('qs_resp1.rt', qs_resp1.rt)
    Prac_rep.addData('qs_resp1.started', qs_resp1.tStartRefresh)
    Prac_rep.addData('qs_resp1.stopped', qs_resp1.tStopRefresh)
    # the Routine "TNT_prc_qs1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TNT_prc_qs2"-------
    continueRoutine = True
    # update component parameters for each repeat
    qs_resp2.keys = []
    qs_resp2.rt = []
    _qs_resp2_allKeys = []
    # keep track of which components have finished
    TNT_prc_qs2Components = [prc_qs_text2, qs_resp2]
    for thisComponent in TNT_prc_qs2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TNT_prc_qs2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TNT_prc_qs2"-------
    while continueRoutine:
        # get current time
        t = TNT_prc_qs2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TNT_prc_qs2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prc_qs_text2* updates
        if prc_qs_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_qs_text2.frameNStart = frameN  # exact frame index
            prc_qs_text2.tStart = t  # local t and not account for scr refresh
            prc_qs_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_qs_text2, 'tStartRefresh')  # time at next scr refresh
            prc_qs_text2.setAutoDraw(True)
        
        # *qs_resp2* updates
        waitOnFlip = False
        if qs_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            qs_resp2.frameNStart = frameN  # exact frame index
            qs_resp2.tStart = t  # local t and not account for scr refresh
            qs_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(qs_resp2, 'tStartRefresh')  # time at next scr refresh
            qs_resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(qs_resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(qs_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if qs_resp2.status == STARTED and not waitOnFlip:
            theseKeys = qs_resp2.getKeys(keyList=['0', '1'], waitRelease=False)
            _qs_resp2_allKeys.extend(theseKeys)
            if len(_qs_resp2_allKeys):
                qs_resp2.keys = _qs_resp2_allKeys[-1].name  # just the last key pressed
                qs_resp2.rt = _qs_resp2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TNT_prc_qs2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TNT_prc_qs2"-------
    for thisComponent in TNT_prc_qs2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('prc_qs_text2.started', prc_qs_text2.tStartRefresh)
    Prac_rep.addData('prc_qs_text2.stopped', prc_qs_text2.tStopRefresh)
    # check responses
    if qs_resp2.keys in ['', [], None]:  # No response was made
        qs_resp2.keys = None
    Prac_rep.addData('qs_resp2.keys',qs_resp2.keys)
    if qs_resp2.keys != None:  # we had a response
        Prac_rep.addData('qs_resp2.rt', qs_resp2.rt)
    Prac_rep.addData('qs_resp2.started', qs_resp2.tStartRefresh)
    Prac_rep.addData('qs_resp2.stopped', qs_resp2.tStopRefresh)
    # the Routine "TNT_prc_qs2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TNT_prc_qs3"-------
    continueRoutine = True
    # update component parameters for each repeat
    qs_resp3.keys = []
    qs_resp3.rt = []
    _qs_resp3_allKeys = []
    # keep track of which components have finished
    TNT_prc_qs3Components = [prc_qs_text3, qs_resp3]
    for thisComponent in TNT_prc_qs3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TNT_prc_qs3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TNT_prc_qs3"-------
    while continueRoutine:
        # get current time
        t = TNT_prc_qs3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TNT_prc_qs3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prc_qs_text3* updates
        if prc_qs_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_qs_text3.frameNStart = frameN  # exact frame index
            prc_qs_text3.tStart = t  # local t and not account for scr refresh
            prc_qs_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_qs_text3, 'tStartRefresh')  # time at next scr refresh
            prc_qs_text3.setAutoDraw(True)
        
        # *qs_resp3* updates
        waitOnFlip = False
        if qs_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            qs_resp3.frameNStart = frameN  # exact frame index
            qs_resp3.tStart = t  # local t and not account for scr refresh
            qs_resp3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(qs_resp3, 'tStartRefresh')  # time at next scr refresh
            qs_resp3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(qs_resp3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(qs_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if qs_resp3.status == STARTED and not waitOnFlip:
            theseKeys = qs_resp3.getKeys(keyList=['0', '1'], waitRelease=False)
            _qs_resp3_allKeys.extend(theseKeys)
            if len(_qs_resp3_allKeys):
                qs_resp3.keys = _qs_resp3_allKeys[-1].name  # just the last key pressed
                qs_resp3.rt = _qs_resp3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TNT_prc_qs3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TNT_prc_qs3"-------
    for thisComponent in TNT_prc_qs3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('prc_qs_text3.started', prc_qs_text3.tStartRefresh)
    Prac_rep.addData('prc_qs_text3.stopped', prc_qs_text3.tStopRefresh)
    # check responses
    if qs_resp3.keys in ['', [], None]:  # No response was made
        qs_resp3.keys = None
    Prac_rep.addData('qs_resp3.keys',qs_resp3.keys)
    if qs_resp3.keys != None:  # we had a response
        Prac_rep.addData('qs_resp3.rt', qs_resp3.rt)
    Prac_rep.addData('qs_resp3.started', qs_resp3.tStartRefresh)
    Prac_rep.addData('qs_resp3.stopped', qs_resp3.tStopRefresh)
    # the Routine "TNT_prc_qs3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prac_end"-------
    continueRoutine = True
    # update component parameters for each repeat
    prc_end_resp.keys = []
    prc_end_resp.rt = []
    _prc_end_resp_allKeys = []
    # keep track of which components have finished
    prac_endComponents = [prc_end, prc_end_resp]
    for thisComponent in prac_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_end"-------
    while continueRoutine:
        # get current time
        t = prac_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prc_end* updates
        if prc_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_end.frameNStart = frameN  # exact frame index
            prc_end.tStart = t  # local t and not account for scr refresh
            prc_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_end, 'tStartRefresh')  # time at next scr refresh
            prc_end.setAutoDraw(True)
        
        # *prc_end_resp* updates
        waitOnFlip = False
        if prc_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_end_resp.frameNStart = frameN  # exact frame index
            prc_end_resp.tStart = t  # local t and not account for scr refresh
            prc_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_end_resp, 'tStartRefresh')  # time at next scr refresh
            prc_end_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prc_end_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prc_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prc_end_resp.status == STARTED and not waitOnFlip:
            theseKeys = prc_end_resp.getKeys(keyList=['space'], waitRelease=False)
            _prc_end_resp_allKeys.extend(theseKeys)
            if len(_prc_end_resp_allKeys):
                prc_end_resp.keys = _prc_end_resp_allKeys[-1].name  # just the last key pressed
                prc_end_resp.rt = _prc_end_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_end"-------
    for thisComponent in prac_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('prc_end.started', prc_end.tStartRefresh)
    Prac_rep.addData('prc_end.stopped', prc_end.tStopRefresh)
    # check responses
    if prc_end_resp.keys in ['', [], None]:  # No response was made
        prc_end_resp.keys = None
    Prac_rep.addData('prc_end_resp.keys',prc_end_resp.keys)
    if prc_end_resp.keys != None:  # we had a response
        Prac_rep.addData('prc_end_resp.rt', prc_end_resp.rt)
    Prac_rep.addData('prc_end_resp.started', prc_end_resp.tStartRefresh)
    Prac_rep.addData('prc_end_resp.stopped', prc_end_resp.tStopRefresh)
    # the Routine "prac_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prac_end2"-------
    continueRoutine = True
    # update component parameters for each repeat
    prc_end_resp2.keys = []
    prc_end_resp2.rt = []
    _prc_end_resp2_allKeys = []
    # keep track of which components have finished
    prac_end2Components = [prc_end2, prc_end_resp2]
    for thisComponent in prac_end2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_end2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_end2"-------
    while continueRoutine:
        # get current time
        t = prac_end2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_end2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prc_end2* updates
        if prc_end2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_end2.frameNStart = frameN  # exact frame index
            prc_end2.tStart = t  # local t and not account for scr refresh
            prc_end2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_end2, 'tStartRefresh')  # time at next scr refresh
            prc_end2.setAutoDraw(True)
        
        # *prc_end_resp2* updates
        waitOnFlip = False
        if prc_end_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prc_end_resp2.frameNStart = frameN  # exact frame index
            prc_end_resp2.tStart = t  # local t and not account for scr refresh
            prc_end_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prc_end_resp2, 'tStartRefresh')  # time at next scr refresh
            prc_end_resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prc_end_resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prc_end_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prc_end_resp2.status == STARTED and not waitOnFlip:
            theseKeys = prc_end_resp2.getKeys(keyList=['p', 'space'], waitRelease=False)
            _prc_end_resp2_allKeys.extend(theseKeys)
            if len(_prc_end_resp2_allKeys):
                prc_end_resp2.keys = _prc_end_resp2_allKeys[-1].name  # just the last key pressed
                prc_end_resp2.rt = _prc_end_resp2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_end2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_end2"-------
    for thisComponent in prac_end2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_rep.addData('prc_end2.started', prc_end2.tStartRefresh)
    Prac_rep.addData('prc_end2.stopped', prc_end2.tStopRefresh)
    # check responses
    if prc_end_resp2.keys in ['', [], None]:  # No response was made
        prc_end_resp2.keys = None
    Prac_rep.addData('prc_end_resp2.keys',prc_end_resp2.keys)
    if prc_end_resp2.keys != None:  # we had a response
        Prac_rep.addData('prc_end_resp2.rt', prc_end_resp2.rt)
    Prac_rep.addData('prc_end_resp2.started', prc_end_resp2.tStartRefresh)
    Prac_rep.addData('prc_end_resp2.stopped', prc_end_resp2.tStopRefresh)
    # the Routine "prac_end2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prac_end3"-------
    continueRoutine = True
    # update component parameters for each repeat
    loopIdx = -1
    random.shuffle(cond_prac)
    if prc_end_resp2.keys == 'space':
        Prac_rep.finished = True
    # keep track of which components have finished
    prac_end3Components = []
    for thisComponent in prac_end3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_end3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_end3"-------
    while continueRoutine:
        # get current time
        t = prac_end3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_end3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_end3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_end3"-------
    for thisComponent in prac_end3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_end3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed prac_rep repeats of 'Prac_rep'


# ------Prepare to start Routine "fmIntro1"-------
continueRoutine = True
# update component parameters for each repeat
fmIntro_resp.keys = []
fmIntro_resp.rt = []
_fmIntro_resp_allKeys = []
# keep track of which components have finished
fmIntro1Components = [fmIntro_txt, fmIntro_resp]
for thisComponent in fmIntro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fmIntro1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fmIntro1"-------
while continueRoutine:
    # get current time
    t = fmIntro1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fmIntro1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fmIntro_txt* updates
    if fmIntro_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fmIntro_txt.frameNStart = frameN  # exact frame index
        fmIntro_txt.tStart = t  # local t and not account for scr refresh
        fmIntro_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fmIntro_txt, 'tStartRefresh')  # time at next scr refresh
        fmIntro_txt.setAutoDraw(True)
    
    # *fmIntro_resp* updates
    waitOnFlip = False
    if fmIntro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fmIntro_resp.frameNStart = frameN  # exact frame index
        fmIntro_resp.tStart = t  # local t and not account for scr refresh
        fmIntro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fmIntro_resp, 'tStartRefresh')  # time at next scr refresh
        fmIntro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fmIntro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fmIntro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fmIntro_resp.status == STARTED and not waitOnFlip:
        theseKeys = fmIntro_resp.getKeys(keyList=['space'], waitRelease=False)
        _fmIntro_resp_allKeys.extend(theseKeys)
        if len(_fmIntro_resp_allKeys):
            fmIntro_resp.keys = _fmIntro_resp_allKeys[-1].name  # just the last key pressed
            fmIntro_resp.rt = _fmIntro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fmIntro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fmIntro1"-------
for thisComponent in fmIntro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fmIntro_txt.started', fmIntro_txt.tStartRefresh)
thisExp.addData('fmIntro_txt.stopped', fmIntro_txt.tStopRefresh)
# check responses
if fmIntro_resp.keys in ['', [], None]:  # No response was made
    fmIntro_resp.keys = None
thisExp.addData('fmIntro_resp.keys',fmIntro_resp.keys)
if fmIntro_resp.keys != None:  # we had a response
    thisExp.addData('fmIntro_resp.rt', fmIntro_resp.rt)
thisExp.addData('fmIntro_resp.started', fmIntro_resp.tStartRefresh)
thisExp.addData('fmIntro_resp.stopped', fmIntro_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "fmIntro1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fmIntro2"-------
continueRoutine = True
# update component parameters for each repeat
fmIntro_resp2.keys = []
fmIntro_resp2.rt = []
_fmIntro_resp2_allKeys = []
# keep track of which components have finished
fmIntro2Components = [fmIntro_txt2, fmIntro_resp2]
for thisComponent in fmIntro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fmIntro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fmIntro2"-------
while continueRoutine:
    # get current time
    t = fmIntro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fmIntro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fmIntro_txt2* updates
    if fmIntro_txt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fmIntro_txt2.frameNStart = frameN  # exact frame index
        fmIntro_txt2.tStart = t  # local t and not account for scr refresh
        fmIntro_txt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fmIntro_txt2, 'tStartRefresh')  # time at next scr refresh
        fmIntro_txt2.setAutoDraw(True)
    
    # *fmIntro_resp2* updates
    waitOnFlip = False
    if fmIntro_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fmIntro_resp2.frameNStart = frameN  # exact frame index
        fmIntro_resp2.tStart = t  # local t and not account for scr refresh
        fmIntro_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fmIntro_resp2, 'tStartRefresh')  # time at next scr refresh
        fmIntro_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fmIntro_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fmIntro_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fmIntro_resp2.status == STARTED and not waitOnFlip:
        theseKeys = fmIntro_resp2.getKeys(keyList=['space'], waitRelease=False)
        _fmIntro_resp2_allKeys.extend(theseKeys)
        if len(_fmIntro_resp2_allKeys):
            fmIntro_resp2.keys = _fmIntro_resp2_allKeys[-1].name  # just the last key pressed
            fmIntro_resp2.rt = _fmIntro_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fmIntro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fmIntro2"-------
for thisComponent in fmIntro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fmIntro_txt2.started', fmIntro_txt2.tStartRefresh)
thisExp.addData('fmIntro_txt2.stopped', fmIntro_txt2.tStopRefresh)
# check responses
if fmIntro_resp2.keys in ['', [], None]:  # No response was made
    fmIntro_resp2.keys = None
thisExp.addData('fmIntro_resp2.keys',fmIntro_resp2.keys)
if fmIntro_resp2.keys != None:  # we had a response
    thisExp.addData('fmIntro_resp2.rt', fmIntro_resp2.rt)
thisExp.addData('fmIntro_resp2.started', fmIntro_resp2.tStartRefresh)
thisExp.addData('fmIntro_resp2.stopped', fmIntro_resp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "fmIntro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TNTphase = data.TrialHandler(nReps=TNT_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TNTphase')
thisExp.addLoop(TNTphase)  # add the loop to the experiment
thisTNTphase = TNTphase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTNTphase.rgb)
if thisTNTphase != None:
    for paramName in thisTNTphase:
        exec('{} = thisTNTphase[paramName]'.format(paramName))

for thisTNTphase in TNTphase:
    currentLoop = TNTphase
    # abbreviate parameter names if possible (e.g. rgb = thisTNTphase.rgb)
    if thisTNTphase != None:
        for paramName in thisTNTphase:
            exec('{} = thisTNTphase[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    TNTPhase_block = data.TrialHandler(nReps=rep_formal_TNT, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TNTPhase_block')
    thisExp.addLoop(TNTPhase_block)  # add the loop to the experiment
    thisTNTPhase_block = TNTPhase_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTNTPhase_block.rgb)
    if thisTNTPhase_block != None:
        for paramName in thisTNTPhase_block:
            exec('{} = thisTNTPhase_block[paramName]'.format(paramName))
    
    for thisTNTPhase_block in TNTPhase_block:
        currentLoop = TNTPhase_block
        # abbreviate parameter names if possible (e.g. rgb = thisTNTPhase_block.rgb)
        if thisTNTPhase_block != None:
            for paramName in thisTNTPhase_block:
                exec('{} = thisTNTPhase_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI_variable"-------
        continueRoutine = True
        # update component parameters for each repeat
        ISI = random.choice([p/5 for p in range(5, 13)])
        # keep track of which components have finished
        ISI_variableComponents = [fix600, variable_ISI, fix_trigger]
        for thisComponent in ISI_variableComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISI_variableClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI_variable"-------
        while continueRoutine:
            # get current time
            t = ISI_variableClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISI_variableClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix600* updates
            if fix600.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix600.frameNStart = frameN  # exact frame index
                fix600.tStart = t  # local t and not account for scr refresh
                fix600.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix600, 'tStartRefresh')  # time at next scr refresh
                fix600.setAutoDraw(True)
            if fix600.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix600.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    fix600.tStop = t  # not accounting for scr refresh
                    fix600.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix600, 'tStopRefresh')  # time at next scr refresh
                    fix600.setAutoDraw(False)
            
            # *variable_ISI* updates
            if variable_ISI.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                variable_ISI.frameNStart = frameN  # exact frame index
                variable_ISI.tStart = t  # local t and not account for scr refresh
                variable_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(variable_ISI, 'tStartRefresh')  # time at next scr refresh
                variable_ISI.setAutoDraw(True)
            if variable_ISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > variable_ISI.tStartRefresh + ISI-frameTolerance:
                    # keep track of stop time/frame for later
                    variable_ISI.tStop = t  # not accounting for scr refresh
                    variable_ISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(variable_ISI, 'tStopRefresh')  # time at next scr refresh
                    variable_ISI.setAutoDraw(False)
            # *fix_trigger* updates
            if fix_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_trigger.frameNStart = frameN  # exact frame index
                fix_trigger.tStart = t  # local t and not account for scr refresh
                fix_trigger.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_trigger, 'tStartRefresh')  # time at next scr refresh
                fix_trigger.status = STARTED
                win.callOnFlip(fix_trigger.setData, int(250))
            if fix_trigger.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_trigger.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_trigger.tStop = t  # not accounting for scr refresh
                    fix_trigger.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_trigger, 'tStopRefresh')  # time at next scr refresh
                    fix_trigger.status = FINISHED
                    win.callOnFlip(fix_trigger.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI_variableComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI_variable"-------
        for thisComponent in ISI_variableComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNTPhase_block.addData('fix600.started', fix600.tStartRefresh)
        TNTPhase_block.addData('fix600.stopped', fix600.tStopRefresh)
        TNTPhase_block.addData('variable_ISI.started', variable_ISI.tStartRefresh)
        TNTPhase_block.addData('variable_ISI.stopped', variable_ISI.tStopRefresh)
        if fix_trigger.status == STARTED:
            win.callOnFlip(fix_trigger.setData, int(0))
        TNTPhase_block.addData('fix_trigger.started', fix_trigger.tStartRefresh)
        TNTPhase_block.addData('fix_trigger.stopped', fix_trigger.tStopRefresh)
        # the Routine "ISI_variable" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "phase2_trial_fm"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        trl_fm += 1
        loopIdx_fm = pool_fm[trl_fm]
        stim_disp = block[loopIdx_fm]['cue']
        cue_fm.setText(stim_disp)
        trigger_value = block[loopIdx_fm]['trigger_val']
        word_number = block[loopIdx_fm]['word_number']
        if block[loopIdx_fm]['cond'] == nothink:
            color = 'red'
        elif block[loopIdx_fm]['cond'] == think:
            color = 'green'
        else:
            color = 'black'
        cue_fm.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        phase2_trial_fmComponents = [cue_fm, TNT_trigger, pair_mark]
        for thisComponent in phase2_trial_fmComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        phase2_trial_fmClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "phase2_trial_fm"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = phase2_trial_fmClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=phase2_trial_fmClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cue_fm* updates
            if cue_fm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cue_fm.frameNStart = frameN  # exact frame index
                cue_fm.tStart = t  # local t and not account for scr refresh
                cue_fm.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_fm, 'tStartRefresh')  # time at next scr refresh
                cue_fm.setAutoDraw(True)
            if cue_fm.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_fm.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_fm.tStop = t  # not accounting for scr refresh
                    cue_fm.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cue_fm, 'tStopRefresh')  # time at next scr refresh
                    cue_fm.setAutoDraw(False)
            # *TNT_trigger* updates
            if TNT_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TNT_trigger.frameNStart = frameN  # exact frame index
                TNT_trigger.tStart = t  # local t and not account for scr refresh
                TNT_trigger.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TNT_trigger, 'tStartRefresh')  # time at next scr refresh
                TNT_trigger.status = STARTED
                win.callOnFlip(TNT_trigger.setData, int(trigger_value))
            if TNT_trigger.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TNT_trigger.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    TNT_trigger.tStop = t  # not accounting for scr refresh
                    TNT_trigger.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TNT_trigger, 'tStopRefresh')  # time at next scr refresh
                    TNT_trigger.status = FINISHED
                    win.callOnFlip(TNT_trigger.setData, int(0))
            # *pair_mark* updates
            if pair_mark.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                pair_mark.frameNStart = frameN  # exact frame index
                pair_mark.tStart = t  # local t and not account for scr refresh
                pair_mark.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pair_mark, 'tStartRefresh')  # time at next scr refresh
                pair_mark.status = STARTED
                win.callOnFlip(pair_mark.setData, int(word_number))
            if pair_mark.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pair_mark.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pair_mark.tStop = t  # not accounting for scr refresh
                    pair_mark.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pair_mark, 'tStopRefresh')  # time at next scr refresh
                    pair_mark.status = FINISHED
                    win.callOnFlip(pair_mark.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in phase2_trial_fmComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "phase2_trial_fm"-------
        for thisComponent in phase2_trial_fmComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNTPhase_block.addData('cue', block[loopIdx_fm]['cue']) #where trials is the name of the loop
        TNTPhase_block.addData('color', color) #where trials is the name of the loop
        TNTPhase_block.addData('cond', block[loopIdx_fm]['cond']) #where trials is the name of the loop
        TNTPhase_block.addData('target', block[loopIdx_fm]['target']) #where trials is the name of the loop
        if TNT_trigger.status == STARTED:
            win.callOnFlip(TNT_trigger.setData, int(0))
        TNTPhase_block.addData('TNT_trigger.started', TNT_trigger.tStartRefresh)
        TNTPhase_block.addData('TNT_trigger.stopped', TNT_trigger.tStopRefresh)
        if pair_mark.status == STARTED:
            win.callOnFlip(pair_mark.setData, int(0))
        TNTPhase_block.addData('pair_mark.started', pair_mark.tStartRefresh)
        TNTPhase_block.addData('pair_mark.stopped', pair_mark.tStopRefresh)
        
        # ------Prepare to start Routine "rate_awareness"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        ratePrac_resp.keys = []
        ratePrac_resp.rt = []
        _ratePrac_resp_allKeys = []
        # keep track of which components have finished
        rate_awarenessComponents = [ratePrac_instruText, ratePrac_text, ratePrac_resp]
        for thisComponent in rate_awarenessComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rate_awarenessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rate_awareness"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rate_awarenessClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rate_awarenessClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ratePrac_instruText* updates
            if ratePrac_instruText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_instruText.frameNStart = frameN  # exact frame index
                ratePrac_instruText.tStart = t  # local t and not account for scr refresh
                ratePrac_instruText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_instruText, 'tStartRefresh')  # time at next scr refresh
                ratePrac_instruText.setAutoDraw(True)
            if ratePrac_instruText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_instruText.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_instruText.tStop = t  # not accounting for scr refresh
                    ratePrac_instruText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_instruText, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_instruText.setAutoDraw(False)
            
            # *ratePrac_text* updates
            if ratePrac_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_text.frameNStart = frameN  # exact frame index
                ratePrac_text.tStart = t  # local t and not account for scr refresh
                ratePrac_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_text, 'tStartRefresh')  # time at next scr refresh
                ratePrac_text.setAutoDraw(True)
            if ratePrac_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_text.tStop = t  # not accounting for scr refresh
                    ratePrac_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_text, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_text.setAutoDraw(False)
            
            # *ratePrac_resp* updates
            waitOnFlip = False
            if ratePrac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratePrac_resp.frameNStart = frameN  # exact frame index
                ratePrac_resp.tStart = t  # local t and not account for scr refresh
                ratePrac_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratePrac_resp, 'tStartRefresh')  # time at next scr refresh
                ratePrac_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ratePrac_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ratePrac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ratePrac_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ratePrac_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ratePrac_resp.tStop = t  # not accounting for scr refresh
                    ratePrac_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ratePrac_resp, 'tStopRefresh')  # time at next scr refresh
                    ratePrac_resp.status = FINISHED
            if ratePrac_resp.status == STARTED and not waitOnFlip:
                theseKeys = ratePrac_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _ratePrac_resp_allKeys.extend(theseKeys)
                if len(_ratePrac_resp_allKeys):
                    ratePrac_resp.keys = _ratePrac_resp_allKeys[-1].name  # just the last key pressed
                    ratePrac_resp.rt = _ratePrac_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rate_awarenessComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rate_awareness"-------
        for thisComponent in rate_awarenessComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNTPhase_block.addData('ratePrac_instruText.started', ratePrac_instruText.tStartRefresh)
        TNTPhase_block.addData('ratePrac_instruText.stopped', ratePrac_instruText.tStopRefresh)
        TNTPhase_block.addData('ratePrac_text.started', ratePrac_text.tStartRefresh)
        TNTPhase_block.addData('ratePrac_text.stopped', ratePrac_text.tStopRefresh)
        # check responses
        if ratePrac_resp.keys in ['', [], None]:  # No response was made
            ratePrac_resp.keys = None
        TNTPhase_block.addData('ratePrac_resp.keys',ratePrac_resp.keys)
        if ratePrac_resp.keys != None:  # we had a response
            TNTPhase_block.addData('ratePrac_resp.rt', ratePrac_resp.rt)
        TNTPhase_block.addData('ratePrac_resp.started', ratePrac_resp.tStartRefresh)
        TNTPhase_block.addData('ratePrac_resp.stopped', ratePrac_resp.tStopRefresh)
        
        # ------Prepare to start Routine "short_break"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        if (trl_fm+1)%20 is not 0:
            continueRoutine = False
        # keep track of which components have finished
        short_breakComponents = [break10s, timer_10, var_9, var_8, var_7, var_6, var_5, var_4, var_3, var_2, var_1]
        for thisComponent in short_breakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        short_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "short_break"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = short_breakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=short_breakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break10s* updates
            if break10s.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break10s.frameNStart = frameN  # exact frame index
                break10s.tStart = t  # local t and not account for scr refresh
                break10s.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break10s, 'tStartRefresh')  # time at next scr refresh
                break10s.setAutoDraw(True)
            if break10s.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > break10s.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    break10s.tStop = t  # not accounting for scr refresh
                    break10s.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(break10s, 'tStopRefresh')  # time at next scr refresh
                    break10s.setAutoDraw(False)
            
            # *timer_10* updates
            if timer_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_10.frameNStart = frameN  # exact frame index
                timer_10.tStart = t  # local t and not account for scr refresh
                timer_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_10, 'tStartRefresh')  # time at next scr refresh
                timer_10.setAutoDraw(True)
            if timer_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_10.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_10.tStop = t  # not accounting for scr refresh
                    timer_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_10, 'tStopRefresh')  # time at next scr refresh
                    timer_10.setAutoDraw(False)
            
            # *var_9* updates
            if var_9.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                var_9.frameNStart = frameN  # exact frame index
                var_9.tStart = t  # local t and not account for scr refresh
                var_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_9, 'tStartRefresh')  # time at next scr refresh
                var_9.setAutoDraw(True)
            if var_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_9.tStop = t  # not accounting for scr refresh
                    var_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_9, 'tStopRefresh')  # time at next scr refresh
                    var_9.setAutoDraw(False)
            
            # *var_8* updates
            if var_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                var_8.frameNStart = frameN  # exact frame index
                var_8.tStart = t  # local t and not account for scr refresh
                var_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_8, 'tStartRefresh')  # time at next scr refresh
                var_8.setAutoDraw(True)
            if var_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_8.tStop = t  # not accounting for scr refresh
                    var_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_8, 'tStopRefresh')  # time at next scr refresh
                    var_8.setAutoDraw(False)
            
            # *var_7* updates
            if var_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                var_7.frameNStart = frameN  # exact frame index
                var_7.tStart = t  # local t and not account for scr refresh
                var_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_7, 'tStartRefresh')  # time at next scr refresh
                var_7.setAutoDraw(True)
            if var_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_7.tStop = t  # not accounting for scr refresh
                    var_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_7, 'tStopRefresh')  # time at next scr refresh
                    var_7.setAutoDraw(False)
            
            # *var_6* updates
            if var_6.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                var_6.frameNStart = frameN  # exact frame index
                var_6.tStart = t  # local t and not account for scr refresh
                var_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_6, 'tStartRefresh')  # time at next scr refresh
                var_6.setAutoDraw(True)
            if var_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_6.tStop = t  # not accounting for scr refresh
                    var_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_6, 'tStopRefresh')  # time at next scr refresh
                    var_6.setAutoDraw(False)
            
            # *var_5* updates
            if var_5.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                var_5.frameNStart = frameN  # exact frame index
                var_5.tStart = t  # local t and not account for scr refresh
                var_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_5, 'tStartRefresh')  # time at next scr refresh
                var_5.setAutoDraw(True)
            if var_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_5.tStop = t  # not accounting for scr refresh
                    var_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_5, 'tStopRefresh')  # time at next scr refresh
                    var_5.setAutoDraw(False)
            
            # *var_4* updates
            if var_4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                var_4.frameNStart = frameN  # exact frame index
                var_4.tStart = t  # local t and not account for scr refresh
                var_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_4, 'tStartRefresh')  # time at next scr refresh
                var_4.setAutoDraw(True)
            if var_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_4.tStop = t  # not accounting for scr refresh
                    var_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_4, 'tStopRefresh')  # time at next scr refresh
                    var_4.setAutoDraw(False)
            
            # *var_3* updates
            if var_3.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                var_3.frameNStart = frameN  # exact frame index
                var_3.tStart = t  # local t and not account for scr refresh
                var_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_3, 'tStartRefresh')  # time at next scr refresh
                var_3.setAutoDraw(True)
            if var_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_3.tStop = t  # not accounting for scr refresh
                    var_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_3, 'tStopRefresh')  # time at next scr refresh
                    var_3.setAutoDraw(False)
            
            # *var_2* updates
            if var_2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                var_2.frameNStart = frameN  # exact frame index
                var_2.tStart = t  # local t and not account for scr refresh
                var_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_2, 'tStartRefresh')  # time at next scr refresh
                var_2.setAutoDraw(True)
            if var_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_2.tStop = t  # not accounting for scr refresh
                    var_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_2, 'tStopRefresh')  # time at next scr refresh
                    var_2.setAutoDraw(False)
            
            # *var_1* updates
            if var_1.status == NOT_STARTED and tThisFlip >= 9-frameTolerance:
                # keep track of start time/frame for later
                var_1.frameNStart = frameN  # exact frame index
                var_1.tStart = t  # local t and not account for scr refresh
                var_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_1, 'tStartRefresh')  # time at next scr refresh
                var_1.setAutoDraw(True)
            if var_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > var_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    var_1.tStop = t  # not accounting for scr refresh
                    var_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(var_1, 'tStopRefresh')  # time at next scr refresh
                    var_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in short_breakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "short_break"-------
        for thisComponent in short_breakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TNTPhase_block.addData('break10s.started', break10s.tStartRefresh)
        TNTPhase_block.addData('break10s.stopped', break10s.tStopRefresh)
        thisExp.nextEntry()
        
    # completed rep_formal_TNT repeats of 'TNTPhase_block'
    
    
    # ------Prepare to start Routine "TNTrest"-------
    continueRoutine = True
    # update component parameters for each repeat
    TNT_process = (TNTphase.thisN+1)/TNT_rep
    TNT_process_left = 1-TNT_process
    process_disply = f"You have completed {format(TNT_process,'.2%')}\n{format(TNT_process_left,'.2%')} remains"
    
    process_info.setText(process_disply)
    BreakEnd.keys = []
    BreakEnd.rt = []
    _BreakEnd_allKeys = []
    # keep track of which components have finished
    TNTrestComponents = [process_info, BreakIntro, BreakEnd]
    for thisComponent in TNTrestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TNTrestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TNTrest"-------
    while continueRoutine:
        # get current time
        t = TNTrestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TNTrestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *process_info* updates
        if process_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            process_info.frameNStart = frameN  # exact frame index
            process_info.tStart = t  # local t and not account for scr refresh
            process_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(process_info, 'tStartRefresh')  # time at next scr refresh
            process_info.setAutoDraw(True)
        
        # *BreakIntro* updates
        if BreakIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BreakIntro.frameNStart = frameN  # exact frame index
            BreakIntro.tStart = t  # local t and not account for scr refresh
            BreakIntro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BreakIntro, 'tStartRefresh')  # time at next scr refresh
            BreakIntro.setAutoDraw(True)
        
        # *BreakEnd* updates
        waitOnFlip = False
        if BreakEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BreakEnd.frameNStart = frameN  # exact frame index
            BreakEnd.tStart = t  # local t and not account for scr refresh
            BreakEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BreakEnd, 'tStartRefresh')  # time at next scr refresh
            BreakEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(BreakEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(BreakEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if BreakEnd.status == STARTED and not waitOnFlip:
            theseKeys = BreakEnd.getKeys(keyList=['space'], waitRelease=False)
            _BreakEnd_allKeys.extend(theseKeys)
            if len(_BreakEnd_allKeys):
                BreakEnd.keys = _BreakEnd_allKeys[-1].name  # just the last key pressed
                BreakEnd.rt = _BreakEnd_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TNTrestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TNTrest"-------
    for thisComponent in TNTrestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    random.shuffle(pool_fm)
    trl_fm = -1
    TNTphase.addData('process_info.started', process_info.tStartRefresh)
    TNTphase.addData('process_info.stopped', process_info.tStopRefresh)
    TNTphase.addData('BreakIntro.started', BreakIntro.tStartRefresh)
    TNTphase.addData('BreakIntro.stopped', BreakIntro.tStopRefresh)
    # check responses
    if BreakEnd.keys in ['', [], None]:  # No response was made
        BreakEnd.keys = None
    TNTphase.addData('BreakEnd.keys',BreakEnd.keys)
    if BreakEnd.keys != None:  # we had a response
        TNTphase.addData('BreakEnd.rt', BreakEnd.rt)
    TNTphase.addData('BreakEnd.started', BreakEnd.tStartRefresh)
    TNTphase.addData('BreakEnd.stopped', BreakEnd.tStopRefresh)
    # the Routine "TNTrest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed TNT_rep repeats of 'TNTphase'


# set up handler to look after randomisation of conditions etc
random_test = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='random_test')
thisExp.addLoop(random_test)  # add the loop to the experiment
thisRandom_test = random_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRandom_test.rgb)
if thisRandom_test != None:
    for paramName in thisRandom_test:
        exec('{} = thisRandom_test[paramName]'.format(paramName))

for thisRandom_test in random_test:
    currentLoop = random_test
    # abbreviate parameter names if possible (e.g. rgb = thisRandom_test.rgb)
    if thisRandom_test != None:
        for paramName in thisRandom_test:
            exec('{} = thisRandom_test[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    indepTest_trial = data.TrialHandler(nReps=random_indTest, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='indepTest_trial')
    thisExp.addLoop(indepTest_trial)  # add the loop to the experiment
    thisIndepTest_trial = indepTest_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIndepTest_trial.rgb)
    if thisIndepTest_trial != None:
        for paramName in thisIndepTest_trial:
            exec('{} = thisIndepTest_trial[paramName]'.format(paramName))
    
    for thisIndepTest_trial in indepTest_trial:
        currentLoop = indepTest_trial
        # abbreviate parameter names if possible (e.g. rgb = thisIndepTest_trial.rgb)
        if thisIndepTest_trial != None:
            for paramName in thisIndepTest_trial:
                exec('{} = thisIndepTest_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "IntroIndTest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        trl_test = -1
        random.shuffle(pool_test)
        # keep track of which components have finished
        IntroIndTestComponents = [text, key_resp_3]
        for thisComponent in IntroIndTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IntroIndTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "IntroIndTest"-------
        while continueRoutine:
            # get current time
            t = IntroIndTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IntroIndTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IntroIndTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "IntroIndTest"-------
        for thisComponent in IntroIndTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        indepTest_trial.addData('text.started', text.tStartRefresh)
        indepTest_trial.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        indepTest_trial.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            indepTest_trial.addData('key_resp_3.rt', key_resp_3.rt)
        indepTest_trial.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        indepTest_trial.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "IntroIndTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        indepTest_loop = data.TrialHandler(nReps=rep_indTest, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='indepTest_loop')
        thisExp.addLoop(indepTest_loop)  # add the loop to the experiment
        thisIndepTest_loop = indepTest_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisIndepTest_loop.rgb)
        if thisIndepTest_loop != None:
            for paramName in thisIndepTest_loop:
                exec('{} = thisIndepTest_loop[paramName]'.format(paramName))
        
        for thisIndepTest_loop in indepTest_loop:
            currentLoop = indepTest_loop
            # abbreviate parameter names if possible (e.g. rgb = thisIndepTest_loop.rgb)
            if thisIndepTest_loop != None:
                for paramName in thisIndepTest_loop:
                    exec('{} = thisIndepTest_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "indepTest"-------
            continueRoutine = True
            routineTimer.add(6.000000)
            # update component parameters for each repeat
            IT_resp.keys = []
            IT_resp.rt = []
            _IT_resp_allKeys = []
            trl_test += 1
            loopIdx_test = pool_test[trl_test]
            stim_cat = ind_test[loopIdx_test]['category']
            stim_firstletter = ind_test[loopIdx_test]['firstL']
            stim_disp = stim_cat + '             ' + stim_firstletter + '__'
            IT_screen.setText(stim_disp)
            trigger_value = ind_test[loopIdx_test]['trigger_val']+20
            word_number = ind_test[loopIdx_test]['word_number'] - 100
            # keep track of which components have finished
            indepTestComponents = [say_intru_IT, IT_screen, IT_resp, IT_trigger, IT_WordNumber]
            for thisComponent in indepTestComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            indepTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "indepTest"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = indepTestClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=indepTestClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *say_intru_IT* updates
                if say_intru_IT.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    say_intru_IT.frameNStart = frameN  # exact frame index
                    say_intru_IT.tStart = t  # local t and not account for scr refresh
                    say_intru_IT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(say_intru_IT, 'tStartRefresh')  # time at next scr refresh
                    say_intru_IT.setAutoDraw(True)
                if say_intru_IT.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > say_intru_IT.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        say_intru_IT.tStop = t  # not accounting for scr refresh
                        say_intru_IT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(say_intru_IT, 'tStopRefresh')  # time at next scr refresh
                        say_intru_IT.setAutoDraw(False)
                
                # *IT_screen* updates
                if IT_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    IT_screen.frameNStart = frameN  # exact frame index
                    IT_screen.tStart = t  # local t and not account for scr refresh
                    IT_screen.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(IT_screen, 'tStartRefresh')  # time at next scr refresh
                    IT_screen.setAutoDraw(True)
                if IT_screen.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > IT_screen.tStartRefresh + 6.0-frameTolerance:
                        # keep track of stop time/frame for later
                        IT_screen.tStop = t  # not accounting for scr refresh
                        IT_screen.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(IT_screen, 'tStopRefresh')  # time at next scr refresh
                        IT_screen.setAutoDraw(False)
                
                # *IT_resp* updates
                waitOnFlip = False
                if IT_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    IT_resp.frameNStart = frameN  # exact frame index
                    IT_resp.tStart = t  # local t and not account for scr refresh
                    IT_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(IT_resp, 'tStartRefresh')  # time at next scr refresh
                    IT_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(IT_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(IT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if IT_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > IT_resp.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        IT_resp.tStop = t  # not accounting for scr refresh
                        IT_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(IT_resp, 'tStopRefresh')  # time at next scr refresh
                        IT_resp.status = FINISHED
                if IT_resp.status == STARTED and not waitOnFlip:
                    theseKeys = IT_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _IT_resp_allKeys.extend(theseKeys)
                    if len(_IT_resp_allKeys):
                        IT_resp.keys = _IT_resp_allKeys[-1].name  # just the last key pressed
                        IT_resp.rt = _IT_resp_allKeys[-1].rt
                        # was this correct?
                        if (IT_resp.keys == str("'f'")) or (IT_resp.keys == "'f'"):
                            IT_resp.corr = 1
                        else:
                            IT_resp.corr = 0
                # *IT_trigger* updates
                if IT_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    IT_trigger.frameNStart = frameN  # exact frame index
                    IT_trigger.tStart = t  # local t and not account for scr refresh
                    IT_trigger.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(IT_trigger, 'tStartRefresh')  # time at next scr refresh
                    IT_trigger.status = STARTED
                    win.callOnFlip(IT_trigger.setData, int(trigger_value))
                if IT_trigger.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > IT_trigger.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        IT_trigger.tStop = t  # not accounting for scr refresh
                        IT_trigger.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(IT_trigger, 'tStopRefresh')  # time at next scr refresh
                        IT_trigger.status = FINISHED
                        win.callOnFlip(IT_trigger.setData, int(0))
                # *IT_WordNumber* updates
                if IT_WordNumber.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    IT_WordNumber.frameNStart = frameN  # exact frame index
                    IT_WordNumber.tStart = t  # local t and not account for scr refresh
                    IT_WordNumber.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(IT_WordNumber, 'tStartRefresh')  # time at next scr refresh
                    IT_WordNumber.status = STARTED
                    win.callOnFlip(IT_WordNumber.setData, int(word_number))
                if IT_WordNumber.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > IT_WordNumber.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        IT_WordNumber.tStop = t  # not accounting for scr refresh
                        IT_WordNumber.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(IT_WordNumber, 'tStopRefresh')  # time at next scr refresh
                        IT_WordNumber.status = FINISHED
                        win.callOnFlip(IT_WordNumber.setData, int(0))
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in indepTestComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "indepTest"-------
            for thisComponent in indepTestComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            indepTest_loop.addData('say_intru_IT.started', say_intru_IT.tStartRefresh)
            indepTest_loop.addData('say_intru_IT.stopped', say_intru_IT.tStopRefresh)
            indepTest_loop.addData('IT_screen.started', IT_screen.tStartRefresh)
            indepTest_loop.addData('IT_screen.stopped', IT_screen.tStopRefresh)
            # check responses
            if IT_resp.keys in ['', [], None]:  # No response was made
                IT_resp.keys = None
                # was no response the correct answer?!
                if str("'f'").lower() == 'none':
                   IT_resp.corr = 1;  # correct non-response
                else:
                   IT_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for indepTest_loop (TrialHandler)
            indepTest_loop.addData('IT_resp.keys',IT_resp.keys)
            indepTest_loop.addData('IT_resp.corr', IT_resp.corr)
            if IT_resp.keys != None:  # we had a response
                indepTest_loop.addData('IT_resp.rt', IT_resp.rt)
            indepTest_loop.addData('IT_resp.started', IT_resp.tStartRefresh)
            indepTest_loop.addData('IT_resp.stopped', IT_resp.tStopRefresh)
            indepTest_loop.addData('cue', ind_test[loopIdx_test]['cue'])
            indepTest_loop.addData('target', ind_test[loopIdx_test]['target'])
            indepTest_loop.addData('cond', ind_test[loopIdx_test]['cond'])
            if IT_trigger.status == STARTED:
                win.callOnFlip(IT_trigger.setData, int(0))
            indepTest_loop.addData('IT_trigger.started', IT_trigger.tStartRefresh)
            indepTest_loop.addData('IT_trigger.stopped', IT_trigger.tStopRefresh)
            if IT_WordNumber.status == STARTED:
                win.callOnFlip(IT_WordNumber.setData, int(0))
            indepTest_loop.addData('IT_WordNumber.started', IT_WordNumber.tStartRefresh)
            indepTest_loop.addData('IT_WordNumber.stopped', IT_WordNumber.tStopRefresh)
            thisExp.nextEntry()
            
        # completed rep_indTest repeats of 'indepTest_loop'
        
        thisExp.nextEntry()
        
    # completed random_indTest repeats of 'indepTest_trial'
    
    
    # set up handler to look after randomisation of conditions etc
    depTest_trial = data.TrialHandler(nReps=random_depTest, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='depTest_trial')
    thisExp.addLoop(depTest_trial)  # add the loop to the experiment
    thisDepTest_trial = depTest_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDepTest_trial.rgb)
    if thisDepTest_trial != None:
        for paramName in thisDepTest_trial:
            exec('{} = thisDepTest_trial[paramName]'.format(paramName))
    
    for thisDepTest_trial in depTest_trial:
        currentLoop = depTest_trial
        # abbreviate parameter names if possible (e.g. rgb = thisDepTest_trial.rgb)
        if thisDepTest_trial != None:
            for paramName in thisDepTest_trial:
                exec('{} = thisDepTest_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "IntroDepTest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_ind.keys = []
        key_resp_ind.rt = []
        _key_resp_ind_allKeys = []
        trl_test = -1
        random.shuffle(pool_test)
        # keep track of which components have finished
        IntroDepTestComponents = [intro_ind, key_resp_ind]
        for thisComponent in IntroDepTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IntroDepTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "IntroDepTest"-------
        while continueRoutine:
            # get current time
            t = IntroDepTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IntroDepTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intro_ind* updates
            if intro_ind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_ind.frameNStart = frameN  # exact frame index
                intro_ind.tStart = t  # local t and not account for scr refresh
                intro_ind.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_ind, 'tStartRefresh')  # time at next scr refresh
                intro_ind.setAutoDraw(True)
            
            # *key_resp_ind* updates
            waitOnFlip = False
            if key_resp_ind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_ind.frameNStart = frameN  # exact frame index
                key_resp_ind.tStart = t  # local t and not account for scr refresh
                key_resp_ind.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_ind, 'tStartRefresh')  # time at next scr refresh
                key_resp_ind.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_ind.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_ind.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_ind.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_ind.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_ind_allKeys.extend(theseKeys)
                if len(_key_resp_ind_allKeys):
                    key_resp_ind.keys = _key_resp_ind_allKeys[-1].name  # just the last key pressed
                    key_resp_ind.rt = _key_resp_ind_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IntroDepTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "IntroDepTest"-------
        for thisComponent in IntroDepTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        depTest_trial.addData('intro_ind.started', intro_ind.tStartRefresh)
        depTest_trial.addData('intro_ind.stopped', intro_ind.tStopRefresh)
        # check responses
        if key_resp_ind.keys in ['', [], None]:  # No response was made
            key_resp_ind.keys = None
        depTest_trial.addData('key_resp_ind.keys',key_resp_ind.keys)
        if key_resp_ind.keys != None:  # we had a response
            depTest_trial.addData('key_resp_ind.rt', key_resp_ind.rt)
        depTest_trial.addData('key_resp_ind.started', key_resp_ind.tStartRefresh)
        depTest_trial.addData('key_resp_ind.stopped', key_resp_ind.tStopRefresh)
        # the Routine "IntroDepTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        depTest_loop = data.TrialHandler(nReps=rep_depTest, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='depTest_loop')
        thisExp.addLoop(depTest_loop)  # add the loop to the experiment
        thisDepTest_loop = depTest_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDepTest_loop.rgb)
        if thisDepTest_loop != None:
            for paramName in thisDepTest_loop:
                exec('{} = thisDepTest_loop[paramName]'.format(paramName))
        
        for thisDepTest_loop in depTest_loop:
            currentLoop = depTest_loop
            # abbreviate parameter names if possible (e.g. rgb = thisDepTest_loop.rgb)
            if thisDepTest_loop != None:
                for paramName in thisDepTest_loop:
                    exec('{} = thisDepTest_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "depTest"-------
            continueRoutine = True
            routineTimer.add(6.000000)
            # update component parameters for each repeat
            DT_resp.keys = []
            DT_resp.rt = []
            _DT_resp_allKeys = []
            trl_test += 1
            loopIdx_test = pool_test[trl_test]
            stim_disp = dep_test[loopIdx_test]['cue']
            DT_screen.setText(stim_disp)
            
            trigger_value = dep_test[loopIdx_test]['trigger_val']+10
            word_number = dep_test[loopIdx_test]['word_number']
            # keep track of which components have finished
            depTestComponents = [say_instruDT, DT_screen, DT_resp, DT_trigger, DT_WordNumber]
            for thisComponent in depTestComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            depTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "depTest"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = depTestClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=depTestClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *say_instruDT* updates
                if say_instruDT.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    say_instruDT.frameNStart = frameN  # exact frame index
                    say_instruDT.tStart = t  # local t and not account for scr refresh
                    say_instruDT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(say_instruDT, 'tStartRefresh')  # time at next scr refresh
                    say_instruDT.setAutoDraw(True)
                if say_instruDT.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > say_instruDT.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        say_instruDT.tStop = t  # not accounting for scr refresh
                        say_instruDT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(say_instruDT, 'tStopRefresh')  # time at next scr refresh
                        say_instruDT.setAutoDraw(False)
                
                # *DT_screen* updates
                if DT_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    DT_screen.frameNStart = frameN  # exact frame index
                    DT_screen.tStart = t  # local t and not account for scr refresh
                    DT_screen.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DT_screen, 'tStartRefresh')  # time at next scr refresh
                    DT_screen.setAutoDraw(True)
                if DT_screen.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DT_screen.tStartRefresh + 6.0-frameTolerance:
                        # keep track of stop time/frame for later
                        DT_screen.tStop = t  # not accounting for scr refresh
                        DT_screen.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DT_screen, 'tStopRefresh')  # time at next scr refresh
                        DT_screen.setAutoDraw(False)
                
                # *DT_resp* updates
                waitOnFlip = False
                if DT_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    DT_resp.frameNStart = frameN  # exact frame index
                    DT_resp.tStart = t  # local t and not account for scr refresh
                    DT_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DT_resp, 'tStartRefresh')  # time at next scr refresh
                    DT_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(DT_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(DT_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if DT_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DT_resp.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        DT_resp.tStop = t  # not accounting for scr refresh
                        DT_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DT_resp, 'tStopRefresh')  # time at next scr refresh
                        DT_resp.status = FINISHED
                if DT_resp.status == STARTED and not waitOnFlip:
                    theseKeys = DT_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _DT_resp_allKeys.extend(theseKeys)
                    if len(_DT_resp_allKeys):
                        DT_resp.keys = _DT_resp_allKeys[-1].name  # just the last key pressed
                        DT_resp.rt = _DT_resp_allKeys[-1].rt
                        # was this correct?
                        if (DT_resp.keys == str("'f'")) or (DT_resp.keys == "'f'"):
                            DT_resp.corr = 1
                        else:
                            DT_resp.corr = 0
                # *DT_trigger* updates
                if DT_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    DT_trigger.frameNStart = frameN  # exact frame index
                    DT_trigger.tStart = t  # local t and not account for scr refresh
                    DT_trigger.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DT_trigger, 'tStartRefresh')  # time at next scr refresh
                    DT_trigger.status = STARTED
                    win.callOnFlip(DT_trigger.setData, int(trigger_value))
                if DT_trigger.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DT_trigger.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        DT_trigger.tStop = t  # not accounting for scr refresh
                        DT_trigger.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DT_trigger, 'tStopRefresh')  # time at next scr refresh
                        DT_trigger.status = FINISHED
                        win.callOnFlip(DT_trigger.setData, int(0))
                # *DT_WordNumber* updates
                if DT_WordNumber.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    DT_WordNumber.frameNStart = frameN  # exact frame index
                    DT_WordNumber.tStart = t  # local t and not account for scr refresh
                    DT_WordNumber.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DT_WordNumber, 'tStartRefresh')  # time at next scr refresh
                    DT_WordNumber.status = STARTED
                    win.callOnFlip(DT_WordNumber.setData, int(word_number))
                if DT_WordNumber.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DT_WordNumber.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        DT_WordNumber.tStop = t  # not accounting for scr refresh
                        DT_WordNumber.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DT_WordNumber, 'tStopRefresh')  # time at next scr refresh
                        DT_WordNumber.status = FINISHED
                        win.callOnFlip(DT_WordNumber.setData, int(0))
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in depTestComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "depTest"-------
            for thisComponent in depTestComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            depTest_loop.addData('say_instruDT.started', say_instruDT.tStartRefresh)
            depTest_loop.addData('say_instruDT.stopped', say_instruDT.tStopRefresh)
            depTest_loop.addData('DT_screen.started', DT_screen.tStartRefresh)
            depTest_loop.addData('DT_screen.stopped', DT_screen.tStopRefresh)
            # check responses
            if DT_resp.keys in ['', [], None]:  # No response was made
                DT_resp.keys = None
                # was no response the correct answer?!
                if str("'f'").lower() == 'none':
                   DT_resp.corr = 1;  # correct non-response
                else:
                   DT_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for depTest_loop (TrialHandler)
            depTest_loop.addData('DT_resp.keys',DT_resp.keys)
            depTest_loop.addData('DT_resp.corr', DT_resp.corr)
            if DT_resp.keys != None:  # we had a response
                depTest_loop.addData('DT_resp.rt', DT_resp.rt)
            depTest_loop.addData('DT_resp.started', DT_resp.tStartRefresh)
            depTest_loop.addData('DT_resp.stopped', DT_resp.tStopRefresh)
            depTest_loop.addData('cue', dep_test[loopIdx_test]['cue'])
            depTest_loop.addData('target', dep_test[loopIdx_test]['target'])
            depTest_loop.addData('cond', dep_test[loopIdx_test]['cond'])
            if DT_trigger.status == STARTED:
                win.callOnFlip(DT_trigger.setData, int(0))
            depTest_loop.addData('DT_trigger.started', DT_trigger.tStartRefresh)
            depTest_loop.addData('DT_trigger.stopped', DT_trigger.tStopRefresh)
            if DT_WordNumber.status == STARTED:
                win.callOnFlip(DT_WordNumber.setData, int(0))
            depTest_loop.addData('DT_WordNumber.started', DT_WordNumber.tStartRefresh)
            depTest_loop.addData('DT_WordNumber.stopped', DT_WordNumber.tStopRefresh)
            thisExp.nextEntry()
            
        # completed rep_depTest repeats of 'depTest_loop'
        
        thisExp.nextEntry()
        
    # completed random_depTest repeats of 'depTest_trial'
    
    
    # ------Prepare to start Routine "randomizer"-------
    continueRoutine = True
    # update component parameters for each repeat
    temp = random_indTest
    random_indTest = random_depTest
    random_depTest = temp
    
    # keep track of which components have finished
    randomizerComponents = []
    for thisComponent in randomizerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    randomizerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "randomizer"-------
    while continueRoutine:
        # get current time
        t = randomizerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=randomizerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in randomizerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "randomizer"-------
    for thisComponent in randomizerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "randomizer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'random_test'


# ------Prepare to start Routine "goodBye"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
key_resp_end.keys = []
key_resp_end.rt = []
_key_resp_end_allKeys = []
# keep track of which components have finished
goodByeComponents = [taskend, key_resp_end]
for thisComponent in goodByeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodByeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodBye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = goodByeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodByeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *taskend* updates
    if taskend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        taskend.frameNStart = frameN  # exact frame index
        taskend.tStart = t  # local t and not account for scr refresh
        taskend.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(taskend, 'tStartRefresh')  # time at next scr refresh
        taskend.setAutoDraw(True)
    if taskend.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > taskend.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            taskend.tStop = t  # not accounting for scr refresh
            taskend.frameNStop = frameN  # exact frame index
            win.timeOnFlip(taskend, 'tStopRefresh')  # time at next scr refresh
            taskend.setAutoDraw(False)
    
    # *key_resp_end* updates
    waitOnFlip = False
    if key_resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.tStart = t  # local t and not account for scr refresh
        key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_end.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_end.tStop = t  # not accounting for scr refresh
            key_resp_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_end, 'tStopRefresh')  # time at next scr refresh
            key_resp_end.status = FINISHED
    if key_resp_end.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_end.getKeys(keyList=['q'], waitRelease=False)
        _key_resp_end_allKeys.extend(theseKeys)
        if len(_key_resp_end_allKeys):
            key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
            key_resp_end.rt = _key_resp_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodByeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodBye"-------
for thisComponent in goodByeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('taskend.started', taskend.tStartRefresh)
thisExp.addData('taskend.stopped', taskend.tStopRefresh)
# check responses
if key_resp_end.keys in ['', [], None]:  # No response was made
    key_resp_end.keys = None
thisExp.addData('key_resp_end.keys',key_resp_end.keys)
if key_resp_end.keys != None:  # we had a response
    thisExp.addData('key_resp_end.rt', key_resp_end.rt)
thisExp.addData('key_resp_end.started', key_resp_end.tStartRefresh)
thisExp.addData('key_resp_end.stopped', key_resp_end.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
