#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on January 22, 2013, at 08:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
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
expName = 'TNT_test'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\eeglab\\Desktop\\Hangbin MRes\\final_version_with_trigger\\TNT_learning_lastrun.py',
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
    monitor='testMonitor', color=[-0.169,-0.169,-0.169], colorSpace='rgb',
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

# import stumuli
allData = data.importConditions(u'Stimuli_TNT.xlsx')
random.shuffle(allData)
cond_prac = []
cond_crat = []
for k in range(0,len(allData)):
    if allData[k]['cond'] == 'prac':
        cond_prac.append(allData[k])
    else:
        cond_crat.append(allData[k])
pss_learn = cond_prac[0:int(len(cond_prac)/2)] + cond_crat + cond_prac[int(len(cond_prac)/2):int(len(cond_prac))]

for dl in allData:
    scoreDict[dl[u'cue']] = 0

minCorrect = 1
loopIdx = -1

#Key parameter
win.mouseVisible = False
TextColour = 'white'
FontSize = 0.03

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_keyresp = keyboard.Keyboard()
welcome_title = visual.TextStim(win=win, name='welcome_title',
    text='Investigating the relationship between attention and memory',
    font='Open Sans',
    pos=(0, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color=TextColour, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcome_subtitle = visual.TextStim(win=win, name='welcome_subtitle',
    text='The University of Manchester',
    font='Open Sans',
    pos=(0, -0.0), height=0.04, wrapWidth=None, ori=0, 
    color=TextColour, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
welcome_names = visual.TextStim(win=win, name='welcome_names',
    text='Researcher: Hangbin Zhang\n\nSupervisors: Stephen Ball, Jason Taylor',
    font='Open Sans',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color=TextColour, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
welcome_prompt = visual.TextStim(win=win, name='welcome_prompt',
    text='press SPACE to begin the experiment',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color=TextColour, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
welcome_uomlogo = visual.ImageStim(
    win=win,
    name='welcome_uomlogo', 
    image='UoMLogo.jpg', mask=None,
    ori=0, pos=(0.5, 0.45), size=(0.24, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "IntroPhase1"
IntroPhase1Clock = core.Clock()
intro1_title = visual.TextStim(win=win, name='intro1_title',
    text='Welcome and thank you for agreeing to take part in this study.',
    font='Open Sans',
    pos=(0, 0.4), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro1_text = visual.TextStim(win=win, name='intro1_text',
    text='This study consists of three experiments designed to investigate how the brain processes memory and attention.\n\nThis will take around 2 hours.\n\nTo try and keep things varied we have split the experiments into shorter blocks. These blocks will be between 5-15 minutes long. You will be given regular short breaks during the blocks, and longer, self-timed breaks between them.\n\nEEG recording is very sensitive, and even small movements can create noise in the signal which makes analysis difficult. As such, it is important that you are seated comfortably, with your feet on the floor and hands on the desk. Please try to keep your head up and your eyes centred on the screen.\n\nThe researcher will regularly check on you during the session. If for any reason you want the researcher’s attention during the experiments or between check-ins, please knock on the glass window. \n\n\n\nPlease press SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
intro1_resp = keyboard.Keyboard()

# Initialize components for Routine "IntroPhase1_2"
IntroPhase1_2Clock = core.Clock()
intro_phase12 = visual.TextStim(win=win, name='intro_phase12',
    text='TNT - Study Phase\n\nIn this part of the experiment you will be shown 60 pairs of words once each.\n\nPlease try to remember all of the word pairs.\n\nWord pairs will be presented one pair at a time, one pair after another for 5 s.\n\nDo not worry if you think you cannot remember all of them at this stage. You will have a chance to remember these word pairs again. \n\nLater, your memory of these words will be tested. We will show you a word in each pair and ask you to recall the other paired word. \n\n\nPlease press SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_intro12 = keyboard.Keyboard()

# Initialize components for Routine "phase1_trial"
phase1_trialClock = core.Clock()
rep_pss_learn = len(pss_learn)
stim_disp = 'it does not work'
WordPairs_all = visual.TextStim(win=win, name='WordPairs_all',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dropIntro"
dropIntroClock = core.Clock()
Intro_drop = visual.TextStim(win=win, name='Intro_drop',
    text="Now, we start to learn these words again.\n\nIn this phase, you will be shown a word in each pair and you should recall the other paired word and say it aloud.\n\nAll the word pairs will be tested.\n\nThe word you responded to correctly will be removed automatically from the list. \n\nYou should continually respond and learn again if you can't remember and say the associate word correctly, until all pairs of words are removed. \n\n\nPlease press SPACE to continue\n",
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
int_drop_resp = keyboard.Keyboard()

# Initialize components for Routine "dropIntro_2"
dropIntro_2Clock = core.Clock()
Intro_drop2 = visual.TextStim(win=win, name='Intro_drop2',
    text='Please feel free if you cannot remember at first, the aim of this stage is to help you to learn the word pairs, so the accuracy in this stage will not be recorded.\n\n\nPlease press SPACE to continue\n\nGood luck!',
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intdrop_resp2 = keyboard.Keyboard()

# Initialize components for Routine "phase1_trial2"
phase1_trial2Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cue_stimili = visual.TextStim(win=win, name='cue_stimili',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
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
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "learningEnd"
learningEndClock = core.Clock()
EndLearning = visual.TextStim(win=win, name='EndLearning',
    text="Congratulations! You have completed the learning phase 1. \n\nNext, we will take a break and set up the EEG, preparing for the next phase!\n\nNow, please wait for the experimenter's coming. ",
    font='Open Sans',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0.0, 
    color=TextColour, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_resp = keyboard.Keyboard()

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

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_keyresp.keys = []
welcome_keyresp.rt = []
_welcome_keyresp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_keyresp, welcome_title, welcome_subtitle, welcome_names, welcome_prompt, welcome_uomlogo]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_keyresp* updates
    waitOnFlip = False
    if welcome_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_keyresp.frameNStart = frameN  # exact frame index
        welcome_keyresp.tStart = t  # local t and not account for scr refresh
        welcome_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_keyresp, 'tStartRefresh')  # time at next scr refresh
        welcome_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_keyresp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_keyresp_allKeys.extend(theseKeys)
        if len(_welcome_keyresp_allKeys):
            welcome_keyresp.keys = _welcome_keyresp_allKeys[-1].name  # just the last key pressed
            welcome_keyresp.rt = _welcome_keyresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *welcome_title* updates
    if welcome_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_title.frameNStart = frameN  # exact frame index
        welcome_title.tStart = t  # local t and not account for scr refresh
        welcome_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_title, 'tStartRefresh')  # time at next scr refresh
        welcome_title.setAutoDraw(True)
    
    # *welcome_subtitle* updates
    if welcome_subtitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_subtitle.frameNStart = frameN  # exact frame index
        welcome_subtitle.tStart = t  # local t and not account for scr refresh
        welcome_subtitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_subtitle, 'tStartRefresh')  # time at next scr refresh
        welcome_subtitle.setAutoDraw(True)
    
    # *welcome_names* updates
    if welcome_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_names.frameNStart = frameN  # exact frame index
        welcome_names.tStart = t  # local t and not account for scr refresh
        welcome_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_names, 'tStartRefresh')  # time at next scr refresh
        welcome_names.setAutoDraw(True)
    
    # *welcome_prompt* updates
    if welcome_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_prompt.frameNStart = frameN  # exact frame index
        welcome_prompt.tStart = t  # local t and not account for scr refresh
        welcome_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_prompt, 'tStartRefresh')  # time at next scr refresh
        welcome_prompt.setAutoDraw(True)
    
    # *welcome_uomlogo* updates
    if welcome_uomlogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_uomlogo.frameNStart = frameN  # exact frame index
        welcome_uomlogo.tStart = t  # local t and not account for scr refresh
        welcome_uomlogo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_uomlogo, 'tStartRefresh')  # time at next scr refresh
        welcome_uomlogo.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_keyresp.keys in ['', [], None]:  # No response was made
    welcome_keyresp.keys = None
thisExp.addData('welcome_keyresp.keys',welcome_keyresp.keys)
if welcome_keyresp.keys != None:  # we had a response
    thisExp.addData('welcome_keyresp.rt', welcome_keyresp.rt)
thisExp.addData('welcome_keyresp.started', welcome_keyresp.tStartRefresh)
thisExp.addData('welcome_keyresp.stopped', welcome_keyresp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('welcome_title.started', welcome_title.tStartRefresh)
thisExp.addData('welcome_title.stopped', welcome_title.tStopRefresh)
thisExp.addData('welcome_subtitle.started', welcome_subtitle.tStartRefresh)
thisExp.addData('welcome_subtitle.stopped', welcome_subtitle.tStopRefresh)
thisExp.addData('welcome_names.started', welcome_names.tStartRefresh)
thisExp.addData('welcome_names.stopped', welcome_names.tStopRefresh)
thisExp.addData('welcome_prompt.started', welcome_prompt.tStartRefresh)
thisExp.addData('welcome_prompt.stopped', welcome_prompt.tStopRefresh)
thisExp.addData('welcome_uomlogo.started', welcome_uomlogo.tStartRefresh)
thisExp.addData('welcome_uomlogo.stopped', welcome_uomlogo.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroPhase1"-------
continueRoutine = True
# update component parameters for each repeat
intro1_resp.keys = []
intro1_resp.rt = []
_intro1_resp_allKeys = []
# keep track of which components have finished
IntroPhase1Components = [intro1_title, intro1_text, intro1_resp]
for thisComponent in IntroPhase1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroPhase1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroPhase1"-------
while continueRoutine:
    # get current time
    t = IntroPhase1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroPhase1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1_title* updates
    if intro1_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_title.frameNStart = frameN  # exact frame index
        intro1_title.tStart = t  # local t and not account for scr refresh
        intro1_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_title, 'tStartRefresh')  # time at next scr refresh
        intro1_title.setAutoDraw(True)
    
    # *intro1_text* updates
    if intro1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_text.frameNStart = frameN  # exact frame index
        intro1_text.tStart = t  # local t and not account for scr refresh
        intro1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_text, 'tStartRefresh')  # time at next scr refresh
        intro1_text.setAutoDraw(True)
    
    # *intro1_resp* updates
    if intro1_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_resp.frameNStart = frameN  # exact frame index
        intro1_resp.tStart = t  # local t and not account for scr refresh
        intro1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_resp, 'tStartRefresh')  # time at next scr refresh
        intro1_resp.status = STARTED
        # keyboard checking is just starting
        intro1_resp.clock.reset()  # now t=0
    if intro1_resp.status == STARTED:
        theseKeys = intro1_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro1_resp_allKeys.extend(theseKeys)
        if len(_intro1_resp_allKeys):
            intro1_resp.keys = _intro1_resp_allKeys[-1].name  # just the last key pressed
            intro1_resp.rt = _intro1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroPhase1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroPhase1"-------
for thisComponent in IntroPhase1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro1_title.started', intro1_title.tStartRefresh)
thisExp.addData('intro1_title.stopped', intro1_title.tStopRefresh)
thisExp.addData('intro1_text.started', intro1_text.tStartRefresh)
thisExp.addData('intro1_text.stopped', intro1_text.tStopRefresh)
# check responses
if intro1_resp.keys in ['', [], None]:  # No response was made
    intro1_resp.keys = None
thisExp.addData('intro1_resp.keys',intro1_resp.keys)
if intro1_resp.keys != None:  # we had a response
    thisExp.addData('intro1_resp.rt', intro1_resp.rt)
thisExp.nextEntry()
# the Routine "IntroPhase1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroPhase1_2"-------
continueRoutine = True
# update component parameters for each repeat
resp_intro12.keys = []
resp_intro12.rt = []
_resp_intro12_allKeys = []
# keep track of which components have finished
IntroPhase1_2Components = [intro_phase12, resp_intro12]
for thisComponent in IntroPhase1_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroPhase1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroPhase1_2"-------
while continueRoutine:
    # get current time
    t = IntroPhase1_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroPhase1_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_phase12* updates
    if intro_phase12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_phase12.frameNStart = frameN  # exact frame index
        intro_phase12.tStart = t  # local t and not account for scr refresh
        intro_phase12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_phase12, 'tStartRefresh')  # time at next scr refresh
        intro_phase12.setAutoDraw(True)
    
    # *resp_intro12* updates
    if resp_intro12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_intro12.frameNStart = frameN  # exact frame index
        resp_intro12.tStart = t  # local t and not account for scr refresh
        resp_intro12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_intro12, 'tStartRefresh')  # time at next scr refresh
        resp_intro12.status = STARTED
        # keyboard checking is just starting
        resp_intro12.clock.reset()  # now t=0
    if resp_intro12.status == STARTED:
        theseKeys = resp_intro12.getKeys(keyList=['space'], waitRelease=False)
        _resp_intro12_allKeys.extend(theseKeys)
        if len(_resp_intro12_allKeys):
            resp_intro12.keys = _resp_intro12_allKeys[-1].name  # just the last key pressed
            resp_intro12.rt = _resp_intro12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroPhase1_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroPhase1_2"-------
for thisComponent in IntroPhase1_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp_intro12.keys in ['', [], None]:  # No response was made
    resp_intro12.keys = None
thisExp.addData('resp_intro12.keys',resp_intro12.keys)
if resp_intro12.keys != None:  # we had a response
    thisExp.addData('resp_intro12.rt', resp_intro12.rt)
thisExp.nextEntry()
# the Routine "IntroPhase1_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LearningPhase = data.TrialHandler(nReps=rep_pss_learn, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LearningPhase')
thisExp.addLoop(LearningPhase)  # add the loop to the experiment
thisLearningPhase = LearningPhase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearningPhase.rgb)
if thisLearningPhase != None:
    for paramName in thisLearningPhase:
        exec('{} = thisLearningPhase[paramName]'.format(paramName))

for thisLearningPhase in LearningPhase:
    currentLoop = LearningPhase
    # abbreviate parameter names if possible (e.g. rgb = thisLearningPhase.rgb)
    if thisLearningPhase != None:
        for paramName in thisLearningPhase:
            exec('{} = thisLearningPhase[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase1_trial"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    loopIdx += 1
    stim_text = pss_learn[loopIdx]
    stim_disp = stim_text['cue'] + '             ' + stim_text['target']
    WordPairs_all.setText(stim_disp)
    
    # keep track of which components have finished
    phase1_trialComponents = [WordPairs_all]
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
            if tThisFlipGlobal > WordPairs_all.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                WordPairs_all.tStop = t  # not accounting for scr refresh
                WordPairs_all.frameNStop = frameN  # exact frame index
                win.timeOnFlip(WordPairs_all, 'tStopRefresh')  # time at next scr refresh
                WordPairs_all.setAutoDraw(False)
        
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
    LearningPhase.addData('cue', pss_learn[loopIdx]['cue']) #where trials is the name of the loop
    LearningPhase.addData('target', pss_learn[loopIdx]['target']) #where trials is the name of the loop
    LearningPhase.addData('cond', pss_learn[loopIdx]['cond']) #where trials is the name of the loop
    thisExp.nextEntry()
    
# completed rep_pss_learn repeats of 'LearningPhase'


# ------Prepare to start Routine "dropIntro"-------
continueRoutine = True
# update component parameters for each repeat
int_drop_resp.keys = []
int_drop_resp.rt = []
_int_drop_resp_allKeys = []
# keep track of which components have finished
dropIntroComponents = [Intro_drop, int_drop_resp]
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
    
    # *int_drop_resp* updates
    if int_drop_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        int_drop_resp.frameNStart = frameN  # exact frame index
        int_drop_resp.tStart = t  # local t and not account for scr refresh
        int_drop_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(int_drop_resp, 'tStartRefresh')  # time at next scr refresh
        int_drop_resp.status = STARTED
        # keyboard checking is just starting
        int_drop_resp.clock.reset()  # now t=0
    if int_drop_resp.status == STARTED:
        theseKeys = int_drop_resp.getKeys(keyList=['space'], waitRelease=False)
        _int_drop_resp_allKeys.extend(theseKeys)
        if len(_int_drop_resp_allKeys):
            int_drop_resp.keys = _int_drop_resp_allKeys[-1].name  # just the last key pressed
            int_drop_resp.rt = _int_drop_resp_allKeys[-1].rt
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
if int_drop_resp.keys in ['', [], None]:  # No response was made
    int_drop_resp.keys = None
thisExp.addData('int_drop_resp.keys',int_drop_resp.keys)
if int_drop_resp.keys != None:  # we had a response
    thisExp.addData('int_drop_resp.rt', int_drop_resp.rt)
thisExp.nextEntry()
# the Routine "dropIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "dropIntro_2"-------
continueRoutine = True
# update component parameters for each repeat
intdrop_resp2.keys = []
intdrop_resp2.rt = []
_intdrop_resp2_allKeys = []
# keep track of which components have finished
dropIntro_2Components = [Intro_drop2, intdrop_resp2]
for thisComponent in dropIntro_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dropIntro_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "dropIntro_2"-------
while continueRoutine:
    # get current time
    t = dropIntro_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dropIntro_2Clock)
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
    
    # *intdrop_resp2* updates
    if intdrop_resp2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intdrop_resp2.frameNStart = frameN  # exact frame index
        intdrop_resp2.tStart = t  # local t and not account for scr refresh
        intdrop_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intdrop_resp2, 'tStartRefresh')  # time at next scr refresh
        intdrop_resp2.status = STARTED
        # keyboard checking is just starting
        intdrop_resp2.clock.reset()  # now t=0
    if intdrop_resp2.status == STARTED:
        theseKeys = intdrop_resp2.getKeys(keyList=['space'], waitRelease=False)
        _intdrop_resp2_allKeys.extend(theseKeys)
        if len(_intdrop_resp2_allKeys):
            intdrop_resp2.keys = _intdrop_resp2_allKeys[-1].name  # just the last key pressed
            intdrop_resp2.rt = _intdrop_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dropIntro_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dropIntro_2"-------
for thisComponent in dropIntro_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro_drop2.started', Intro_drop2.tStartRefresh)
thisExp.addData('Intro_drop2.stopped', Intro_drop2.tStopRefresh)
# check responses
if intdrop_resp2.keys in ['', [], None]:  # No response was made
    intdrop_resp2.keys = None
thisExp.addData('intdrop_resp2.keys',intdrop_resp2.keys)
if intdrop_resp2.keys != None:  # we had a response
    thisExp.addData('intdrop_resp2.rt', intdrop_resp2.rt)
thisExp.addData('intdrop_resp2.started', intdrop_resp2.tStart)
thisExp.addData('intdrop_resp2.stopped', intdrop_resp2.tStop)
thisExp.nextEntry()
# the Routine "dropIntro_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Dropoff_phase = data.TrialHandler(nReps=1000.0, method='random', 
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
        Dropoff_phase.addData('correct', 'LEARNED')
    elif resp_drop.keys: #make sure not empty, prevent list index error
        if 'f' in resp_drop.keys:
            msg = 'Correct'
            msgcolor = [-0.0039, 1.0000, -1.0000]
            Dropoff_phase.addData('correct', 1) #where trials is the name of the loop
            scoreDict[cue] += 1
        elif 'j' in resp_drop.keys:
            msg = 'Incorrect'
            msgcolor = [0.7255, -0.8431, -0.5294]
            Dropoff_phase.addData('correct', 0) #store for accuracy
    elif not resp_drop.keys:
        msg = 'Try to speak quickly.'
        msgcolor = [0.7255, -0.8431, -0.5294]
        Dropoff_phase.addData('correct', 'no resp') #store for accuracy
       
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
    
# completed 1000.0 repeats of 'Dropoff_phase'


# ------Prepare to start Routine "learningEnd"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
learningEndComponents = [EndLearning, end_resp]
for thisComponent in learningEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learningEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learningEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learningEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learningEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndLearning* updates
    if EndLearning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndLearning.frameNStart = frameN  # exact frame index
        EndLearning.tStart = t  # local t and not account for scr refresh
        EndLearning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndLearning, 'tStartRefresh')  # time at next scr refresh
        EndLearning.setAutoDraw(True)
    if EndLearning.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndLearning.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            EndLearning.tStop = t  # not accounting for scr refresh
            EndLearning.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndLearning, 'tStopRefresh')  # time at next scr refresh
            EndLearning.setAutoDraw(False)
    
    # *end_resp* updates
    if end_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        end_resp.clock.reset()  # now t=0
    if end_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_resp.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            end_resp.tStop = t  # not accounting for scr refresh
            end_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_resp, 'tStopRefresh')  # time at next scr refresh
            end_resp.status = FINISHED
    if end_resp.status == STARTED:
        theseKeys = end_resp.getKeys(keyList=['q'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learningEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learningEnd"-------
for thisComponent in learningEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndLearning.started', EndLearning.tStartRefresh)
thisExp.addData('EndLearning.stopped', EndLearning.tStopRefresh)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
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
