#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on January 22, 2013, at 10:28
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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'FPVS'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\eeglab\\Desktop\\Hangbin MRes\\final_version_with_trigger\\FPVS_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
# Make random pool 
random_order = []
order_idx = 0
for i in range(1,7):
    random_order.append(i)
random.shuffle(random_order)
trial_order = random_order[order_idx]
hf_data = data.importConditions(u'Stimuli_hf_all.xlsx')[0:144]
length_hf = len(hf_data)
# generate random buffer
buffer_idx = -1
buffer_data = data.importConditions(u'Stimuli_hf_all.xlsx')
random.shuffle(buffer_data)
# randomize low frequency stimuli
length_trial = length_hf + 48
if trial_order == 1:
    nReps_cond1cue = length_trial
    nReps_cond2cue = 0
    nReps_cond3cue = 0
    nReps_cond1target = 0
    nReps_cond2target = 0
    nReps_cond3target = 0
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[0:16]
elif trial_order == 2:
    nReps_cond1cue = 0
    nReps_cond2cue = length_trial
    nReps_cond3cue = 0
    nReps_cond1target = 0
    nReps_cond2target = 0
    nReps_cond3target = 0
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[16:32]
elif trial_order == 3:
    nReps_cond1cue = 0
    nReps_cond2cue = 0
    nReps_cond3cue = length_trial
    nReps_cond1target = 0
    nReps_cond2target = 0
    nReps_cond3target = 0
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[32:48]
elif trial_order == 4:
    nReps_cond1cue = 0
    nReps_cond2cue = 0
    nReps_cond3cue = 0
    nReps_cond1target = length_trial
    nReps_cond2target = 0
    nReps_cond3target = 0
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[48:64]
elif trial_order == 5:
    nReps_cond1cue = 0
    nReps_cond2cue = 0
    nReps_cond3cue = 0
    nReps_cond1target = 0
    nReps_cond2target = length_trial
    nReps_cond3target = 0
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[64:80]
elif trial_order == 6:
    nReps_cond1cue = 0
    nReps_cond2cue = 0
    nReps_cond3cue = 0
    nReps_cond1target = 0
    nReps_cond2target = 0
    nReps_cond3target = length_trial
    lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[80:96]
# make a dictionary to hold stimulus texts

lf_data = lf_data + lf_data + lf_data

while True:
    random.shuffle(hf_data)
    judge = 0
    for i in range(0,(len(hf_data)-2)):
        if hf_data[i] == hf_data[i+1]:
            judge = judge + 1
    if judge == 0:
        break
        
while True:
    random.shuffle(lf_data)
    judge = 0
    for i in range(0,(len(lf_data)-2)):
        if lf_data[i] == lf_data[i+1]:
            judge = judge + 1
    if judge == 0:
        break

loopIdx_lf = -1
loopIdx_hf = -1

# remove cursor
win.mouseVisible = False

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelTex = visual.TextStim(win=win, name='WelTex',
    text='Welcome to the last FPVS task.\n\nYou should focus on the fixation, and press SPACE as quickly as possible if the color of the cross changes to red. Do not move your eyes away from the fixation cross, and keep your body relaxed and stable during the stimulus presentation.\n\nIf you see the resting instruction, you can have a rest, especially relaxing your eyes.\n\nPlease sit comfortablly and press SPACE to begin test',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_resp = keyboard.Keyboard()
start_recording = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "bufferBegin"
bufferBeginClock = core.Clock()
buf_bgin_txt = visual.TextStim(win=win, name='buf_bgin_txt',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
buf_bgin_fix = visual.TextStim(win=win, name='buf_bgin_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trigger_buffer = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "hF_trial"
hF_trialClock = core.Clock()
fixdetect_list = []
fixdetect_list2 = []
n = int(length_trial/8)
for i in range(0,n):
    m = (i*8) + random.randint(1,8)
    m2 = m + 1
    fixdetect_list.append(m)
    fixdetect_list2.append(m2)

fixdetect_list = fixdetect_list + fixdetect_list2

trial_currentn = -1
atten_detect = keyboard.Keyboard()
msg = 'why it cannot work?' # if this occurs, suggesting sth wrong
my_stimulus = visual.TextStim(win=win, name='my_stimulus',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
trigger_stimuli = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "buffuerEnd"
buffuerEndClock = core.Clock()
buf_end_txt = visual.TextStim(win=win, name='buf_end_txt',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
buf_end_fix = visual.TextStim(win=win, name='buf_end_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trigger_buffer_end = parallel.ParallelPort(address='0xD010')

# Initialize components for Routine "randomizer"
randomizerClock = core.Clock()

# Initialize components for Routine "rest"
restClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You can have a rest when you see this slide.\n\nRemembered, try to keep your body relaxed and stable while the words are presented.\n\nIf you are ready, press "SPACE" to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='Congratualations, you have finished all the experiment!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stop_recording = parallel.ParallelPort(address='0xD010')

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

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
start_resp.keys = []
start_resp.rt = []
_start_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [WelTex, start_resp, start_recording]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelTex* updates
    if WelTex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelTex.frameNStart = frameN  # exact frame index
        WelTex.tStart = t  # local t and not account for scr refresh
        WelTex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelTex, 'tStartRefresh')  # time at next scr refresh
        WelTex.setAutoDraw(True)
    
    # *start_resp* updates
    waitOnFlip = False
    if start_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp.frameNStart = frameN  # exact frame index
        start_resp.tStart = t  # local t and not account for scr refresh
        start_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp, 'tStartRefresh')  # time at next scr refresh
        start_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_resp.getKeys(keyList=['space'], waitRelease=False)
        _start_resp_allKeys.extend(theseKeys)
        if len(_start_resp_allKeys):
            start_resp.keys = _start_resp_allKeys[-1].name  # just the last key pressed
            start_resp.rt = _start_resp_allKeys[-1].rt
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
        if tThisFlipGlobal > start_recording.tStartRefresh + 0.1-frameTolerance:
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
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelTex.started', WelTex.tStartRefresh)
thisExp.addData('WelTex.stopped', WelTex.tStopRefresh)
# check responses
if start_resp.keys in ['', [], None]:  # No response was made
    start_resp.keys = None
thisExp.addData('start_resp.keys',start_resp.keys)
if start_resp.keys != None:  # we had a response
    thisExp.addData('start_resp.rt', start_resp.rt)
thisExp.addData('start_resp.started', start_resp.tStartRefresh)
thisExp.addData('start_resp.stopped', start_resp.tStopRefresh)
thisExp.nextEntry()
if start_recording.status == STARTED:
    win.callOnFlip(start_recording.setData, int(0))
thisExp.addData('start_recording.started', start_recording.tStartRefresh)
thisExp.addData('start_recording.stopped', start_recording.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
counterbalance = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='counterbalance')
thisExp.addLoop(counterbalance)  # add the loop to the experiment
thisCounterbalance = counterbalance.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCounterbalance.rgb)
if thisCounterbalance != None:
    for paramName in thisCounterbalance:
        exec('{} = thisCounterbalance[paramName]'.format(paramName))

for thisCounterbalance in counterbalance:
    currentLoop = counterbalance
    # abbreviate parameter names if possible (e.g. rgb = thisCounterbalance.rgb)
    if thisCounterbalance != None:
        for paramName in thisCounterbalance:
            exec('{} = thisCounterbalance[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    buffer_begin = data.TrialHandler(nReps=8.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='buffer_begin')
    thisExp.addLoop(buffer_begin)  # add the loop to the experiment
    thisBuffer_begin = buffer_begin.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBuffer_begin.rgb)
    if thisBuffer_begin != None:
        for paramName in thisBuffer_begin:
            exec('{} = thisBuffer_begin[paramName]'.format(paramName))
    
    for thisBuffer_begin in buffer_begin:
        currentLoop = buffer_begin
        # abbreviate parameter names if possible (e.g. rgb = thisBuffer_begin.rgb)
        if thisBuffer_begin != None:
            for paramName in thisBuffer_begin:
                exec('{} = thisBuffer_begin[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "bufferBegin"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        buffer_idx += 1
        buffer_begin_stim = buffer_data[buffer_idx]['stim']
        buf_bgin_txt.setText(buffer_begin_stim)
        
        #trigger_buffer_value = buffer_data[buffer_idx]['trigger_val']
        # keep track of which components have finished
        bufferBeginComponents = [buf_bgin_txt, buf_bgin_fix, trigger_buffer]
        for thisComponent in bufferBeginComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        bufferBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "bufferBegin"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = bufferBeginClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=bufferBeginClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *buf_bgin_txt* updates
            if buf_bgin_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buf_bgin_txt.frameNStart = frameN  # exact frame index
                buf_bgin_txt.tStart = t  # local t and not account for scr refresh
                buf_bgin_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buf_bgin_txt, 'tStartRefresh')  # time at next scr refresh
                buf_bgin_txt.setAutoDraw(True)
            if buf_bgin_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > buf_bgin_txt.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    buf_bgin_txt.tStop = t  # not accounting for scr refresh
                    buf_bgin_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(buf_bgin_txt, 'tStopRefresh')  # time at next scr refresh
                    buf_bgin_txt.setAutoDraw(False)
            
            # *buf_bgin_fix* updates
            if buf_bgin_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buf_bgin_fix.frameNStart = frameN  # exact frame index
                buf_bgin_fix.tStart = t  # local t and not account for scr refresh
                buf_bgin_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buf_bgin_fix, 'tStartRefresh')  # time at next scr refresh
                buf_bgin_fix.setAutoDraw(True)
            if buf_bgin_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > buf_bgin_fix.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    buf_bgin_fix.tStop = t  # not accounting for scr refresh
                    buf_bgin_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(buf_bgin_fix, 'tStopRefresh')  # time at next scr refresh
                    buf_bgin_fix.setAutoDraw(False)
            # *trigger_buffer* updates
            if trigger_buffer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_buffer.frameNStart = frameN  # exact frame index
                trigger_buffer.tStart = t  # local t and not account for scr refresh
                trigger_buffer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_buffer, 'tStartRefresh')  # time at next scr refresh
                trigger_buffer.status = STARTED
                win.callOnFlip(trigger_buffer.setData, int(8))
            if trigger_buffer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_buffer.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_buffer.tStop = t  # not accounting for scr refresh
                    trigger_buffer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_buffer, 'tStopRefresh')  # time at next scr refresh
                    trigger_buffer.status = FINISHED
                    win.callOnFlip(trigger_buffer.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bufferBeginComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "bufferBegin"-------
        for thisComponent in bufferBeginComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        buffer_begin.addData('buf_bgin_txt.started', buf_bgin_txt.tStartRefresh)
        buffer_begin.addData('buf_bgin_txt.stopped', buf_bgin_txt.tStopRefresh)
        buffer_begin.addData('buf_bgin_fix.started', buf_bgin_fix.tStartRefresh)
        buffer_begin.addData('buf_bgin_fix.stopped', buf_bgin_fix.tStopRefresh)
        if trigger_buffer.status == STARTED:
            win.callOnFlip(trigger_buffer.setData, int(0))
        buffer_begin.addData('trigger_buffer.started', trigger_buffer.tStartRefresh)
        buffer_begin.addData('trigger_buffer.stopped', trigger_buffer.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 8.0 repeats of 'buffer_begin'
    
    
    # set up handler to look after randomisation of conditions etc
    cond1cue = data.TrialHandler(nReps=nReps_cond1cue, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cond1cue')
    thisExp.addLoop(cond1cue)  # add the loop to the experiment
    thisCond1cue = cond1cue.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCond1cue.rgb)
    if thisCond1cue != None:
        for paramName in thisCond1cue:
            exec('{} = thisCond1cue[paramName]'.format(paramName))
    
    for thisCond1cue in cond1cue:
        currentLoop = cond1cue
        # abbreviate parameter names if possible (e.g. rgb = thisCond1cue.rgb)
        if thisCond1cue != None:
            for paramName in thisCond1cue:
                exec('{} = thisCond1cue[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for cond1cue (TrialHandler)
        cond1cue.addData('atten_detect.keys',atten_detect.keys)
        cond1cue.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            cond1cue.addData('atten_detect.rt', atten_detect.rt)
        cond1cue.addData('atten_detect.started', atten_detect.tStartRefresh)
        cond1cue.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        cond1cue.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        cond1cue.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        cond1cue.addData('fixation.started', fixation.tStartRefresh)
        cond1cue.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        cond1cue.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        cond1cue.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond1cue repeats of 'cond1cue'
    
    
    # set up handler to look after randomisation of conditions etc
    cond2cue = data.TrialHandler(nReps=nReps_cond2cue, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cond2cue')
    thisExp.addLoop(cond2cue)  # add the loop to the experiment
    thisCond2cue = cond2cue.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCond2cue.rgb)
    if thisCond2cue != None:
        for paramName in thisCond2cue:
            exec('{} = thisCond2cue[paramName]'.format(paramName))
    
    for thisCond2cue in cond2cue:
        currentLoop = cond2cue
        # abbreviate parameter names if possible (e.g. rgb = thisCond2cue.rgb)
        if thisCond2cue != None:
            for paramName in thisCond2cue:
                exec('{} = thisCond2cue[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for cond2cue (TrialHandler)
        cond2cue.addData('atten_detect.keys',atten_detect.keys)
        cond2cue.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            cond2cue.addData('atten_detect.rt', atten_detect.rt)
        cond2cue.addData('atten_detect.started', atten_detect.tStartRefresh)
        cond2cue.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        cond2cue.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        cond2cue.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        cond2cue.addData('fixation.started', fixation.tStartRefresh)
        cond2cue.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        cond2cue.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        cond2cue.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond2cue repeats of 'cond2cue'
    
    
    # set up handler to look after randomisation of conditions etc
    cond3cue = data.TrialHandler(nReps=nReps_cond3cue, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cond3cue')
    thisExp.addLoop(cond3cue)  # add the loop to the experiment
    thisCond3cue = cond3cue.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCond3cue.rgb)
    if thisCond3cue != None:
        for paramName in thisCond3cue:
            exec('{} = thisCond3cue[paramName]'.format(paramName))
    
    for thisCond3cue in cond3cue:
        currentLoop = cond3cue
        # abbreviate parameter names if possible (e.g. rgb = thisCond3cue.rgb)
        if thisCond3cue != None:
            for paramName in thisCond3cue:
                exec('{} = thisCond3cue[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for cond3cue (TrialHandler)
        cond3cue.addData('atten_detect.keys',atten_detect.keys)
        cond3cue.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            cond3cue.addData('atten_detect.rt', atten_detect.rt)
        cond3cue.addData('atten_detect.started', atten_detect.tStartRefresh)
        cond3cue.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        cond3cue.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        cond3cue.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        cond3cue.addData('fixation.started', fixation.tStartRefresh)
        cond3cue.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        cond3cue.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        cond3cue.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond3cue repeats of 'cond3cue'
    
    
    # set up handler to look after randomisation of conditions etc
    con1target = data.TrialHandler(nReps=nReps_cond1target, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='con1target')
    thisExp.addLoop(con1target)  # add the loop to the experiment
    thisCon1target = con1target.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCon1target.rgb)
    if thisCon1target != None:
        for paramName in thisCon1target:
            exec('{} = thisCon1target[paramName]'.format(paramName))
    
    for thisCon1target in con1target:
        currentLoop = con1target
        # abbreviate parameter names if possible (e.g. rgb = thisCon1target.rgb)
        if thisCon1target != None:
            for paramName in thisCon1target:
                exec('{} = thisCon1target[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for con1target (TrialHandler)
        con1target.addData('atten_detect.keys',atten_detect.keys)
        con1target.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            con1target.addData('atten_detect.rt', atten_detect.rt)
        con1target.addData('atten_detect.started', atten_detect.tStartRefresh)
        con1target.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        con1target.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        con1target.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        con1target.addData('fixation.started', fixation.tStartRefresh)
        con1target.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        con1target.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        con1target.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond1target repeats of 'con1target'
    
    
    # set up handler to look after randomisation of conditions etc
    cond2target = data.TrialHandler(nReps=nReps_cond2target, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cond2target')
    thisExp.addLoop(cond2target)  # add the loop to the experiment
    thisCond2target = cond2target.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCond2target.rgb)
    if thisCond2target != None:
        for paramName in thisCond2target:
            exec('{} = thisCond2target[paramName]'.format(paramName))
    
    for thisCond2target in cond2target:
        currentLoop = cond2target
        # abbreviate parameter names if possible (e.g. rgb = thisCond2target.rgb)
        if thisCond2target != None:
            for paramName in thisCond2target:
                exec('{} = thisCond2target[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for cond2target (TrialHandler)
        cond2target.addData('atten_detect.keys',atten_detect.keys)
        cond2target.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            cond2target.addData('atten_detect.rt', atten_detect.rt)
        cond2target.addData('atten_detect.started', atten_detect.tStartRefresh)
        cond2target.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        cond2target.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        cond2target.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        cond2target.addData('fixation.started', fixation.tStartRefresh)
        cond2target.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        cond2target.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        cond2target.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond2target repeats of 'cond2target'
    
    
    # set up handler to look after randomisation of conditions etc
    cond3target = data.TrialHandler(nReps=nReps_cond3target, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cond3target')
    thisExp.addLoop(cond3target)  # add the loop to the experiment
    thisCond3target = cond3target.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCond3target.rgb)
    if thisCond3target != None:
        for paramName in thisCond3target:
            exec('{} = thisCond3target[paramName]'.format(paramName))
    
    for thisCond3target in cond3target:
        currentLoop = cond3target
        # abbreviate parameter names if possible (e.g. rgb = thisCond3target.rgb)
        if thisCond3target != None:
            for paramName in thisCond3target:
                exec('{} = thisCond3target[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hF_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        trial_currentn += 1
        if trial_currentn in fixdetect_list:
            color = "red"
        else:
            color = "blue"
        atten_detect.keys = []
        atten_detect.rt = []
        _atten_detect_allKeys = []
        if ((trial_currentn + 1) % 4) == 0:
            loopIdx_lf += 1
            stim_text = lf_data[loopIdx_lf]
        else:
            loopIdx_hf += 1
            stim_text = hf_data[loopIdx_hf]
        
        trigger_stim_value = stim_text['trigger_val']
        my_stimulus.setText(stim_text['stim'])
        fixation.setColor(color, colorSpace='rgb')
        # keep track of which components have finished
        hF_trialComponents = [atten_detect, my_stimulus, fixation, trigger_stimuli]
        for thisComponent in hF_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hF_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hF_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hF_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hF_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *atten_detect* updates
            waitOnFlip = False
            if atten_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                atten_detect.frameNStart = frameN  # exact frame index
                atten_detect.tStart = t  # local t and not account for scr refresh
                atten_detect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(atten_detect, 'tStartRefresh')  # time at next scr refresh
                atten_detect.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(atten_detect.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(atten_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if atten_detect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > atten_detect.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    atten_detect.tStop = t  # not accounting for scr refresh
                    atten_detect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(atten_detect, 'tStopRefresh')  # time at next scr refresh
                    atten_detect.status = FINISHED
            if atten_detect.status == STARTED and not waitOnFlip:
                theseKeys = atten_detect.getKeys(keyList=['space'], waitRelease=False)
                _atten_detect_allKeys.extend(theseKeys)
                if len(_atten_detect_allKeys):
                    atten_detect.keys = _atten_detect_allKeys[-1].name  # just the last key pressed
                    atten_detect.rt = _atten_detect_allKeys[-1].rt
                    # was this correct?
                    if (atten_detect.keys == str("'space'")) or (atten_detect.keys == "'space'"):
                        atten_detect.corr = 1
                    else:
                        atten_detect.corr = 0
            
            # *my_stimulus* updates
            if my_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                my_stimulus.frameNStart = frameN  # exact frame index
                my_stimulus.tStart = t  # local t and not account for scr refresh
                my_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(my_stimulus, 'tStartRefresh')  # time at next scr refresh
                my_stimulus.setAutoDraw(True)
            if my_stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > my_stimulus.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    my_stimulus.tStop = t  # not accounting for scr refresh
                    my_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(my_stimulus, 'tStopRefresh')  # time at next scr refresh
                    my_stimulus.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            # *trigger_stimuli* updates
            if trigger_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_stimuli.frameNStart = frameN  # exact frame index
                trigger_stimuli.tStart = t  # local t and not account for scr refresh
                trigger_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_stimuli, 'tStartRefresh')  # time at next scr refresh
                trigger_stimuli.status = STARTED
                win.callOnFlip(trigger_stimuli.setData, int(trigger_stim_value))
            if trigger_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_stimuli.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_stimuli.tStop = t  # not accounting for scr refresh
                    trigger_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_stimuli, 'tStopRefresh')  # time at next scr refresh
                    trigger_stimuli.status = FINISHED
                    win.callOnFlip(trigger_stimuli.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hF_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hF_trial"-------
        for thisComponent in hF_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if atten_detect.keys in ['', [], None]:  # No response was made
            atten_detect.keys = None
            # was no response the correct answer?!
            if str("'space'").lower() == 'none':
               atten_detect.corr = 1;  # correct non-response
            else:
               atten_detect.corr = 0;  # failed to respond (incorrectly)
        # store data for cond3target (TrialHandler)
        cond3target.addData('atten_detect.keys',atten_detect.keys)
        cond3target.addData('atten_detect.corr', atten_detect.corr)
        if atten_detect.keys != None:  # we had a response
            cond3target.addData('atten_detect.rt', atten_detect.rt)
        cond3target.addData('atten_detect.started', atten_detect.tStartRefresh)
        cond3target.addData('atten_detect.stopped', atten_detect.tStopRefresh)
        counterbalance.addData('stim', stim_text['stim'])
        counterbalance.addData('category',  stim_text['category'])
        counterbalance.addData('type',  stim_text['type'])
        counterbalance.addData('trigger_value', stim_text['trigger_val'])
        counterbalance.addData('fixation_color', color)
        cond3target.addData('my_stimulus.started', my_stimulus.tStartRefresh)
        cond3target.addData('my_stimulus.stopped', my_stimulus.tStopRefresh)
        cond3target.addData('fixation.started', fixation.tStartRefresh)
        cond3target.addData('fixation.stopped', fixation.tStopRefresh)
        if trigger_stimuli.status == STARTED:
            win.callOnFlip(trigger_stimuli.setData, int(0))
        cond3target.addData('trigger_stimuli.started', trigger_stimuli.tStartRefresh)
        cond3target.addData('trigger_stimuli.stopped', trigger_stimuli.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps_cond3target repeats of 'cond3target'
    
    
    # set up handler to look after randomisation of conditions etc
    buffer_end = data.TrialHandler(nReps=8.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='buffer_end')
    thisExp.addLoop(buffer_end)  # add the loop to the experiment
    thisBuffer_end = buffer_end.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBuffer_end.rgb)
    if thisBuffer_end != None:
        for paramName in thisBuffer_end:
            exec('{} = thisBuffer_end[paramName]'.format(paramName))
    
    for thisBuffer_end in buffer_end:
        currentLoop = buffer_end
        # abbreviate parameter names if possible (e.g. rgb = thisBuffer_end.rgb)
        if thisBuffer_end != None:
            for paramName in thisBuffer_end:
                exec('{} = thisBuffer_end[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "buffuerEnd"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        buffer_idx += 1
        buffer_end_stim = buffer_data[buffer_idx]['stim']
        buf_end_txt.setText(buffer_end_stim)
        
        #trigger_buffer_end_value = buffer_data[buffer_idx]['trigger_val']
        # keep track of which components have finished
        buffuerEndComponents = [buf_end_txt, buf_end_fix, trigger_buffer_end]
        for thisComponent in buffuerEndComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        buffuerEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "buffuerEnd"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = buffuerEndClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=buffuerEndClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *buf_end_txt* updates
            if buf_end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buf_end_txt.frameNStart = frameN  # exact frame index
                buf_end_txt.tStart = t  # local t and not account for scr refresh
                buf_end_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buf_end_txt, 'tStartRefresh')  # time at next scr refresh
                buf_end_txt.setAutoDraw(True)
            if buf_end_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > buf_end_txt.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    buf_end_txt.tStop = t  # not accounting for scr refresh
                    buf_end_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(buf_end_txt, 'tStopRefresh')  # time at next scr refresh
                    buf_end_txt.setAutoDraw(False)
            
            # *buf_end_fix* updates
            if buf_end_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buf_end_fix.frameNStart = frameN  # exact frame index
                buf_end_fix.tStart = t  # local t and not account for scr refresh
                buf_end_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buf_end_fix, 'tStartRefresh')  # time at next scr refresh
                buf_end_fix.setAutoDraw(True)
            if buf_end_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > buf_end_fix.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    buf_end_fix.tStop = t  # not accounting for scr refresh
                    buf_end_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(buf_end_fix, 'tStopRefresh')  # time at next scr refresh
                    buf_end_fix.setAutoDraw(False)
            # *trigger_buffer_end* updates
            if trigger_buffer_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trigger_buffer_end.frameNStart = frameN  # exact frame index
                trigger_buffer_end.tStart = t  # local t and not account for scr refresh
                trigger_buffer_end.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trigger_buffer_end, 'tStartRefresh')  # time at next scr refresh
                trigger_buffer_end.status = STARTED
                win.callOnFlip(trigger_buffer_end.setData, int(9))
            if trigger_buffer_end.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trigger_buffer_end.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    trigger_buffer_end.tStop = t  # not accounting for scr refresh
                    trigger_buffer_end.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trigger_buffer_end, 'tStopRefresh')  # time at next scr refresh
                    trigger_buffer_end.status = FINISHED
                    win.callOnFlip(trigger_buffer_end.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in buffuerEndComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "buffuerEnd"-------
        for thisComponent in buffuerEndComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        buffer_end.addData('buf_end_txt.started', buf_end_txt.tStartRefresh)
        buffer_end.addData('buf_end_txt.stopped', buf_end_txt.tStopRefresh)
        buffer_end.addData('buf_end_fix.started', buf_end_fix.tStartRefresh)
        buffer_end.addData('buf_end_fix.stopped', buf_end_fix.tStopRefresh)
        if trigger_buffer_end.status == STARTED:
            win.callOnFlip(trigger_buffer_end.setData, int(0))
        buffer_end.addData('trigger_buffer_end.started', trigger_buffer_end.tStart)
        buffer_end.addData('trigger_buffer_end.stopped', trigger_buffer_end.tStop)
        thisExp.nextEntry()
        
    # completed 8.0 repeats of 'buffer_end'
    
    
    # ------Prepare to start Routine "randomizer"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_currentn = -1
    order_idx += 1
    if order_idx < 6:
        trial_order = random_order[order_idx]
    
    if trial_order == 1:
        nReps_cond1cue = length_trial
        nReps_cond2cue = 0
        nReps_cond3cue = 0
        nReps_cond1target = 0
        nReps_cond2target = 0
        nReps_cond3target = 0
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[0:16]
    elif trial_order == 2:
        nReps_cond1cue = 0
        nReps_cond2cue = length_trial
        nReps_cond3cue = 0
        nReps_cond1target = 0
        nReps_cond2target = 0
        nReps_cond3target = 0
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[16:32]
    elif trial_order == 3:
        nReps_cond1cue = 0
        nReps_cond2cue = 0
        nReps_cond3cue = length_trial
        nReps_cond1target = 0
        nReps_cond2target = 0
        nReps_cond3target = 0
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[32:48]
    elif trial_order == 4:
        nReps_cond1cue = 0
        nReps_cond2cue = 0
        nReps_cond3cue = 0
        nReps_cond1target = length_trial
        nReps_cond2target = 0
        nReps_cond3target = 0
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[48:64]
    elif trial_order == 5:
        nReps_cond1cue = 0
        nReps_cond2cue = 0
        nReps_cond3cue = 0
        nReps_cond1target = 0
        nReps_cond2target = length_trial
        nReps_cond3target = 0
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[64:80]
    elif trial_order == 6:
        nReps_cond1cue = 0
        nReps_cond2cue = 0
        nReps_cond3cue = 0
        nReps_cond1target = 0
        nReps_cond2target = 0
        nReps_cond3target = length_trial
        lf_data = data.importConditions(u'Stimuli_lf_all.xlsx')[80:96]
    lf_data = lf_data + lf_data + lf_data
    
    while True:
        random.shuffle(hf_data)
        judge = 0
        for i in range(0,(len(hf_data)-2)):
            if hf_data[i] == hf_data[i+1]:
                judge = judge + 1
        if judge == 0:
            break
            
    while True:
        random.shuffle(lf_data)
        judge = 0
        for i in range(0,(len(lf_data)-2)):
            if lf_data[i] == lf_data[i+1]:
                judge = judge + 1
        if judge == 0:
            break
    
    loopIdx_lf = -1
    loopIdx_hf = -1
    
    # reset buffer
    buffer_idx = -1
    random.shuffle(buffer_data)
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
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    restComponents = [text, key_resp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
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
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
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
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    counterbalance.addData('text.started', text.tStartRefresh)
    counterbalance.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    counterbalance.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        counterbalance.addData('key_resp.rt', key_resp.rt)
    counterbalance.addData('key_resp.started', key_resp.tStartRefresh)
    counterbalance.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'counterbalance'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [endText, stop_recording]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    if endText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endText.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            endText.tStop = t  # not accounting for scr refresh
            endText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endText, 'tStopRefresh')  # time at next scr refresh
            endText.setAutoDraw(False)
    # *stop_recording* updates
    if stop_recording.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_recording.frameNStart = frameN  # exact frame index
        stop_recording.tStart = t  # local t and not account for scr refresh
        stop_recording.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_recording, 'tStartRefresh')  # time at next scr refresh
        stop_recording.status = STARTED
        win.callOnFlip(stop_recording.setData, int(255))
    if stop_recording.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stop_recording.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            stop_recording.tStop = t  # not accounting for scr refresh
            stop_recording.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stop_recording, 'tStopRefresh')  # time at next scr refresh
            stop_recording.status = FINISHED
            win.callOnFlip(stop_recording.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
if stop_recording.status == STARTED:
    win.callOnFlip(stop_recording.setData, int(0))
thisExp.addData('stop_recording.started', stop_recording.tStartRefresh)
thisExp.addData('stop_recording.stopped', stop_recording.tStopRefresh)

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
