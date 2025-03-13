#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on มีนาคม 13, 2025, at 01:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Go No-Go'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1600, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Dell\\Downloads\\go_nogo_demoM\\Go No-Go_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='fill',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'fill'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_welcome') is None:
        # initialise key_welcome
        key_welcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_welcome',
        )
    if deviceManager.getDevice('key_Instructions') is None:
        # initialise key_Instructions
        key_Instructions = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_Instructions',
        )
    if deviceManager.getDevice('key_resp_t') is None:
        # initialise key_resp_t
        key_resp_t = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_t',
        )
    if deviceManager.getDevice('key_Instructions_2') is None:
        # initialise key_Instructions_2
        key_Instructions_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_Instructions_2',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_End') is None:
        # initialise key_resp_End
        key_resp_End = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_End',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    text_welcome = visual.TextStim(win=win, name='text_welcome',
        text='\nยินดีต้อนรับสู่ Go/No-go task\nกดปุ่ม Space เพื่อดำเนินการต่อ\n',
        font='Arial',
        pos=(0, 0.03), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_welcome = keyboard.Keyboard(deviceName='key_welcome')
    
    # --- Initialize components for Routine "Instructions" ---
    text_Instructions = visual.TextStim(win=win, name='text_Instructions',
        text='\nในเกมนี้จะมี แมว และ หนู โผล่มาให้ดูบนหน้าจอ\n\nโดยที่ ถ้าเห็นหนูบนหน้าจอ ให้กดปุ่ม Space เพื่อจับมัน\nแต่ ถ้าเห็นแมว ไม่ต้องกดปุ่มอะไร ให้ปล่อยมันไปจับหนู\n\nในตอนฝึกเล่น \nถ้าทำถูก จะมีการบอกว่า ถูกต้อง! \nถ้าทำผิด ก็จะมีการบอกว่า ผิด!\n\nกดปุ่ม Space เพื่อไปฝึกเล่น',
        font='Arial',
        pos=(0, 0.03), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_Instructions = keyboard.Keyboard(deviceName='key_Instructions')
    
    # --- Initialize components for Routine "countdown" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Fixation" ---
    text_Fixation = visual.TextStim(win=win, name='text_Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Tutorial" ---
    image_Tutorial = visual.ImageStim(
        win=win,
        name='image_Tutorial', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_Tutorial = visual.TextStim(win=win, name='text_Tutorial',
        text='\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_t = keyboard.Keyboard(deviceName='key_resp_t')
    
    # --- Initialize components for Routine "Feedback_Tutorial_2" ---
    text_feedback_Tutorial = visual.TextStim(win=win, name='text_feedback_Tutorial',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Instructions_2" ---
    text_Instructions_2 = visual.TextStim(win=win, name='text_Instructions_2',
        text='\nเมื่อเริ่มเล่นจริง จะไม่มีการบอกว่าถูกหรือผิด\n\nกดปุ่ม Space เพื่อไปเล่นจริง',
        font='Arial',
        pos=(0, 0.03), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_Instructions_2 = keyboard.Keyboard(deviceName='key_Instructions_2')
    
    # --- Initialize components for Routine "countdown" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Fixation" ---
    text_Fixation = visual.TextStim(win=win, name='text_Fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "GoNoGoTask" ---
    image_circle = visual.ImageStim(
        win=win,
        name='image_circle', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_gonogo_ITI = visual.TextStim(win=win, name='text_gonogo_ITI',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "End" ---
    text_end = visual.TextStim(win=win, name='text_end',
        text='ขอบคุณสำหรับการเข้าร่วม',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_End = keyboard.Keyboard(deviceName='key_resp_End')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[text_welcome, key_welcome],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_welcome
    key_welcome.keys = []
    key_welcome.rt = []
    _key_welcome_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_welcome* updates
        
        # if text_welcome is starting this frame...
        if text_welcome.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_welcome.frameNStart = frameN  # exact frame index
            text_welcome.tStart = t  # local t and not account for scr refresh
            text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_welcome.status = STARTED
            text_welcome.setAutoDraw(True)
        
        # if text_welcome is active this frame...
        if text_welcome.status == STARTED:
            # update params
            pass
        
        # *key_welcome* updates
        
        # if key_welcome is starting this frame...
        if key_welcome.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_welcome.frameNStart = frameN  # exact frame index
            key_welcome.tStart = t  # local t and not account for scr refresh
            key_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_welcome.status = STARTED
            # keyboard checking is just starting
            key_welcome.clock.reset()  # now t=0
        if key_welcome.status == STARTED:
            theseKeys = key_welcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_welcome_allKeys.extend(theseKeys)
            if len(_key_welcome_allKeys):
                key_welcome.keys = _key_welcome_allKeys[-1].name  # just the last key pressed
                key_welcome.rt = _key_welcome_allKeys[-1].rt
                key_welcome.duration = _key_welcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[text_Instructions, key_Instructions],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_Instructions
    key_Instructions.keys = []
    key_Instructions.rt = []
    _key_Instructions_allKeys = []
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Instructions* updates
        
        # if text_Instructions is starting this frame...
        if text_Instructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Instructions.frameNStart = frameN  # exact frame index
            text_Instructions.tStart = t  # local t and not account for scr refresh
            text_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Instructions.status = STARTED
            text_Instructions.setAutoDraw(True)
        
        # if text_Instructions is active this frame...
        if text_Instructions.status == STARTED:
            # update params
            pass
        
        # *key_Instructions* updates
        
        # if key_Instructions is starting this frame...
        if key_Instructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_Instructions.frameNStart = frameN  # exact frame index
            key_Instructions.tStart = t  # local t and not account for scr refresh
            key_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_Instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_Instructions.status = STARTED
            # keyboard checking is just starting
            key_Instructions.clock.reset()  # now t=0
        if key_Instructions.status == STARTED:
            theseKeys = key_Instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_Instructions_allKeys.extend(theseKeys)
            if len(_key_Instructions_allKeys):
                key_Instructions.keys = _key_Instructions_allKeys[-1].name  # just the last key pressed
                key_Instructions.rt = _key_Instructions_allKeys[-1].rt
                key_Instructions.duration = _key_Instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[text_3, text_2, text_1],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countdown" ---
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_1* updates
        
        # if text_1 is starting this frame...
        if text_1.status == NOT_STARTED and t >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_1.status = STARTED
            text_1.setAutoDraw(True)
        
        # if text_1 is active this frame...
        if text_1.status == STARTED:
            # update params
            pass
        
        # if text_1 is stopping this frame...
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.tStopRefresh = tThisFlipGlobal  # on global time
                text_1.frameNStop = frameN  # exact frame index
                # update status
                text_1.status = FINISHED
                text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            countdown.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if countdown.maxDurationReached:
        routineTimer.addTime(-countdown.maxDuration)
    elif countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    Play_t = data.TrialHandler2(
        name='Play_t',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Tutorial.csv'), 
        seed=None, 
    )
    thisExp.addLoop(Play_t)  # add the loop to the experiment
    thisPlay_t = Play_t.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPlay_t.rgb)
    if thisPlay_t != None:
        for paramName in thisPlay_t:
            globals()[paramName] = thisPlay_t[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPlay_t in Play_t:
        currentLoop = Play_t
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPlay_t.rgb)
        if thisPlay_t != None:
            for paramName in thisPlay_t:
                globals()[paramName] = thisPlay_t[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[text_Fixation],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Fixation* updates
            
            # if text_Fixation is starting this frame...
            if text_Fixation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Fixation.frameNStart = frameN  # exact frame index
                text_Fixation.tStart = t  # local t and not account for scr refresh
                text_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_Fixation.status = STARTED
                text_Fixation.setAutoDraw(True)
            
            # if text_Fixation is active this frame...
            if text_Fixation.status == STARTED:
                # update params
                pass
            
            # if text_Fixation is stopping this frame...
            if text_Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Fixation.tStop = t  # not accounting for scr refresh
                    text_Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_Fixation.frameNStop = frameN  # exact frame index
                    # update status
                    text_Fixation.status = FINISHED
                    text_Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Tutorial" ---
        # create an object to store info about Routine Tutorial
        Tutorial = data.Routine(
            name='Tutorial',
            components=[image_Tutorial, text_Tutorial, key_resp_t],
        )
        Tutorial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_Tutorial
        if(condition == 'go'):
            space_key = 'space'
        else:
            space_key = 'None'
        
        # ใน Begin Routine
        import random
        
        # สุ่มเวลาในช่วง 1 ถึง 3 วินาที (1000 ถึง 3000ms)
        min_time = 1.0  # นาทีต่ำสุด (วินาที)
        max_time = 3.0  # นาทีสูงสุด (วินาที)
        
        # สุ่มระยะเวลา
        random_time = random.uniform(min_time, max_time)
        
        # กำหนดเวลาที่สุ่มได้ให้เป็นตัวแปร
        thisExp.addData('random_time', random_time)
        
        # กำหนดให้ตัวแปรนี้จะใช้เป็นเวลาหยุดแสดงภาพ
        continueRoutine = True
        
        image_Tutorial.setImage(color)
        # create starting attributes for key_resp_t
        key_resp_t.keys = []
        key_resp_t.rt = []
        _key_resp_t_allKeys = []
        # store start times for Tutorial
        Tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Tutorial.tStart = globalClock.getTime(format='float')
        Tutorial.status = STARTED
        thisExp.addData('Tutorial.started', Tutorial.tStart)
        Tutorial.maxDuration = None
        # keep track of which components have finished
        TutorialComponents = Tutorial.components
        for thisComponent in Tutorial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Tutorial" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Tutorial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_Tutorial* updates
            
            # if image_Tutorial is starting this frame...
            if image_Tutorial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Tutorial.frameNStart = frameN  # exact frame index
                image_Tutorial.tStart = t  # local t and not account for scr refresh
                image_Tutorial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Tutorial, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_Tutorial.status = STARTED
                image_Tutorial.setAutoDraw(True)
            
            # if image_Tutorial is active this frame...
            if image_Tutorial.status == STARTED:
                # update params
                pass
            
            # if image_Tutorial is stopping this frame...
            if image_Tutorial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_Tutorial.tStartRefresh + duration
                -frameTolerance:
                    # keep track of stop time/frame for later
                    image_Tutorial.tStop = t  # not accounting for scr refresh
                    image_Tutorial.tStopRefresh = tThisFlipGlobal  # on global time
                    image_Tutorial.frameNStop = frameN  # exact frame index
                    # update status
                    image_Tutorial.status = FINISHED
                    image_Tutorial.setAutoDraw(False)
            
            # *text_Tutorial* updates
            
            # if text_Tutorial is starting this frame...
            if text_Tutorial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_Tutorial.frameNStart = frameN  # exact frame index
                text_Tutorial.tStart = t  # local t and not account for scr refresh
                text_Tutorial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Tutorial, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_Tutorial.status = STARTED
                text_Tutorial.setAutoDraw(True)
            
            # if text_Tutorial is active this frame...
            if text_Tutorial.status == STARTED:
                # update params
                pass
            
            # if text_Tutorial is stopping this frame...
            if text_Tutorial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Tutorial.tStartRefresh + duration2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Tutorial.tStop = t  # not accounting for scr refresh
                    text_Tutorial.tStopRefresh = tThisFlipGlobal  # on global time
                    text_Tutorial.frameNStop = frameN  # exact frame index
                    # update status
                    text_Tutorial.status = FINISHED
                    text_Tutorial.setAutoDraw(False)
            
            # *key_resp_t* updates
            waitOnFlip = False
            
            # if key_resp_t is starting this frame...
            if key_resp_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_t.frameNStart = frameN  # exact frame index
                key_resp_t.tStart = t  # local t and not account for scr refresh
                key_resp_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_t, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_t.started')
                # update status
                key_resp_t.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_t.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_t.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_t is stopping this frame...
            if key_resp_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_t.tStartRefresh + duration2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_t.tStop = t  # not accounting for scr refresh
                    key_resp_t.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_t.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_t.stopped')
                    # update status
                    key_resp_t.status = FINISHED
                    key_resp_t.status = FINISHED
            if key_resp_t.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_t.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_t_allKeys.extend(theseKeys)
                if len(_key_resp_t_allKeys):
                    key_resp_t.keys = _key_resp_t_allKeys[0].name  # just the first key pressed
                    key_resp_t.rt = _key_resp_t_allKeys[0].rt
                    key_resp_t.duration = _key_resp_t_allKeys[0].duration
                    # was this correct?
                    if (key_resp_t.keys == str(space_key)) or (key_resp_t.keys == space_key):
                        key_resp_t.corr = 1
                    else:
                        key_resp_t.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Tutorial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Tutorial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Tutorial" ---
        for thisComponent in Tutorial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Tutorial
        Tutorial.tStop = globalClock.getTime(format='float')
        Tutorial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Tutorial.stopped', Tutorial.tStop)
        # check responses
        if key_resp_t.keys in ['', [], None]:  # No response was made
            key_resp_t.keys = None
            # was no response the correct answer?!
            if str(space_key).lower() == 'none':
               key_resp_t.corr = 1;  # correct non-response
            else:
               key_resp_t.corr = 0;  # failed to respond (incorrectly)
        # store data for Play_t (TrialHandler)
        Play_t.addData('key_resp_t.keys',key_resp_t.keys)
        Play_t.addData('key_resp_t.corr', key_resp_t.corr)
        if key_resp_t.keys != None:  # we had a response
            Play_t.addData('key_resp_t.rt', key_resp_t.rt)
            Play_t.addData('key_resp_t.duration', key_resp_t.duration)
        # the Routine "Tutorial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback_Tutorial_2" ---
        # create an object to store info about Routine Feedback_Tutorial_2
        Feedback_Tutorial_2 = data.Routine(
            name='Feedback_Tutorial_2',
            components=[text_feedback_Tutorial],
        )
        Feedback_Tutorial_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_Feedback_Tutorial
        
        
        if(key_resp.corr == 1):
            feedback_text = "Correct"
        elif(key_resp.corr == 0):
            feedback_text = "Incorrect"
        
        #if(condition == 'go'):
        #    if(Play.key_resp.corr == 'space'):
        #        feedback_text = "Correct"
        #    else:
        #        feedback_text = "Incorrect"
        #if(condition == 'nogo'):
        #    if(Play.key_resp.corr == 'None'):
        #        feedback_text = "Correct"
        #    else:
        #        feedback_text = "Incorrect"
        
        text_feedback_Tutorial.setText(feedback_text)
        # store start times for Feedback_Tutorial_2
        Feedback_Tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback_Tutorial_2.tStart = globalClock.getTime(format='float')
        Feedback_Tutorial_2.status = STARTED
        Feedback_Tutorial_2.maxDuration = None
        # keep track of which components have finished
        Feedback_Tutorial_2Components = Feedback_Tutorial_2.components
        for thisComponent in Feedback_Tutorial_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback_Tutorial_2" ---
        # if trial has changed, end Routine now
        if isinstance(Play_t, data.TrialHandler2) and thisPlay_t.thisN != Play_t.thisTrial.thisN:
            continueRoutine = False
        Feedback_Tutorial_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_feedback_Tutorial* updates
            
            # if text_feedback_Tutorial is starting this frame...
            if text_feedback_Tutorial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_Tutorial.frameNStart = frameN  # exact frame index
                text_feedback_Tutorial.tStart = t  # local t and not account for scr refresh
                text_feedback_Tutorial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_Tutorial, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_feedback_Tutorial.status = STARTED
                text_feedback_Tutorial.setAutoDraw(True)
            
            # if text_feedback_Tutorial is active this frame...
            if text_feedback_Tutorial.status == STARTED:
                # update params
                pass
            
            # if text_feedback_Tutorial is stopping this frame...
            if text_feedback_Tutorial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_feedback_Tutorial.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_feedback_Tutorial.tStop = t  # not accounting for scr refresh
                    text_feedback_Tutorial.tStopRefresh = tThisFlipGlobal  # on global time
                    text_feedback_Tutorial.frameNStop = frameN  # exact frame index
                    # update status
                    text_feedback_Tutorial.status = FINISHED
                    text_feedback_Tutorial.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback_Tutorial_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_Tutorial_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback_Tutorial_2" ---
        for thisComponent in Feedback_Tutorial_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback_Tutorial_2
        Feedback_Tutorial_2.tStop = globalClock.getTime(format='float')
        Feedback_Tutorial_2.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback_Tutorial_2.maxDurationReached:
            routineTimer.addTime(-Feedback_Tutorial_2.maxDuration)
        elif Feedback_Tutorial_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Play_t'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Instructions_2" ---
    # create an object to store info about Routine Instructions_2
    Instructions_2 = data.Routine(
        name='Instructions_2',
        components=[text_Instructions_2, key_Instructions_2],
    )
    Instructions_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_Instructions_2
    key_Instructions_2.keys = []
    key_Instructions_2.rt = []
    _key_Instructions_2_allKeys = []
    # store start times for Instructions_2
    Instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_2.tStart = globalClock.getTime(format='float')
    Instructions_2.status = STARTED
    Instructions_2.maxDuration = None
    # keep track of which components have finished
    Instructions_2Components = Instructions_2.components
    for thisComponent in Instructions_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_2" ---
    Instructions_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Instructions_2* updates
        
        # if text_Instructions_2 is starting this frame...
        if text_Instructions_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Instructions_2.frameNStart = frameN  # exact frame index
            text_Instructions_2.tStart = t  # local t and not account for scr refresh
            text_Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instructions_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Instructions_2.status = STARTED
            text_Instructions_2.setAutoDraw(True)
        
        # if text_Instructions_2 is active this frame...
        if text_Instructions_2.status == STARTED:
            # update params
            pass
        
        # *key_Instructions_2* updates
        
        # if key_Instructions_2 is starting this frame...
        if key_Instructions_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_Instructions_2.frameNStart = frameN  # exact frame index
            key_Instructions_2.tStart = t  # local t and not account for scr refresh
            key_Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_Instructions_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_Instructions_2.status = STARTED
            # keyboard checking is just starting
            key_Instructions_2.clock.reset()  # now t=0
        if key_Instructions_2.status == STARTED:
            theseKeys = key_Instructions_2.getKeys(keyList=['r','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_Instructions_2_allKeys.extend(theseKeys)
            if len(_key_Instructions_2_allKeys):
                key_Instructions_2.keys = _key_Instructions_2_allKeys[-1].name  # just the last key pressed
                key_Instructions_2.rt = _key_Instructions_2_allKeys[-1].rt
                key_Instructions_2.duration = _key_Instructions_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_2" ---
    for thisComponent in Instructions_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_2
    Instructions_2.tStop = globalClock.getTime(format='float')
    Instructions_2.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[text_3, text_2, text_1],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countdown" ---
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_1* updates
        
        # if text_1 is starting this frame...
        if text_1.status == NOT_STARTED and t >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_1.status = STARTED
            text_1.setAutoDraw(True)
        
        # if text_1 is active this frame...
        if text_1.status == STARTED:
            # update params
            pass
        
        # if text_1 is stopping this frame...
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.tStopRefresh = tThisFlipGlobal  # on global time
                text_1.frameNStop = frameN  # exact frame index
                # update status
                text_1.status = FINISHED
                text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            countdown.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if countdown.maxDurationReached:
        routineTimer.addTime(-countdown.maxDuration)
    elif countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    Play = data.TrialHandler2(
        name='Play',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stimulus_Color.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(Play)  # add the loop to the experiment
    thisPlay = Play.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPlay.rgb)
    if thisPlay != None:
        for paramName in thisPlay:
            globals()[paramName] = thisPlay[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPlay in Play:
        currentLoop = Play
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPlay.rgb)
        if thisPlay != None:
            for paramName in thisPlay:
                globals()[paramName] = thisPlay[paramName]
        
        # --- Prepare to start Routine "Fixation" ---
        # create an object to store info about Routine Fixation
        Fixation = data.Routine(
            name='Fixation',
            components=[text_Fixation],
        )
        Fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Fixation
        Fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Fixation.tStart = globalClock.getTime(format='float')
        Fixation.status = STARTED
        Fixation.maxDuration = None
        # keep track of which components have finished
        FixationComponents = Fixation.components
        for thisComponent in Fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        # if trial has changed, end Routine now
        if isinstance(Play, data.TrialHandler2) and thisPlay.thisN != Play.thisTrial.thisN:
            continueRoutine = False
        Fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Fixation* updates
            
            # if text_Fixation is starting this frame...
            if text_Fixation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Fixation.frameNStart = frameN  # exact frame index
                text_Fixation.tStart = t  # local t and not account for scr refresh
                text_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_Fixation.status = STARTED
                text_Fixation.setAutoDraw(True)
            
            # if text_Fixation is active this frame...
            if text_Fixation.status == STARTED:
                # update params
                pass
            
            # if text_Fixation is stopping this frame...
            if text_Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Fixation.tStop = t  # not accounting for scr refresh
                    text_Fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_Fixation.frameNStop = frameN  # exact frame index
                    # update status
                    text_Fixation.status = FINISHED
                    text_Fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in Fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Fixation
        Fixation.tStop = globalClock.getTime(format='float')
        Fixation.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Fixation.maxDurationReached:
            routineTimer.addTime(-Fixation.maxDuration)
        elif Fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "GoNoGoTask" ---
        # create an object to store info about Routine GoNoGoTask
        GoNoGoTask = data.Routine(
            name='GoNoGoTask',
            components=[image_circle, text_gonogo_ITI, key_resp],
        )
        GoNoGoTask.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if(condition == 'go'):
            space_key = 'space'
        else:
            space_key = 'None'
        
        #condition = go -> space_key = 'space'
        #condition = nogo -> space_key = 'None'
        image_circle.setImage(color)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for GoNoGoTask
        GoNoGoTask.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        GoNoGoTask.tStart = globalClock.getTime(format='float')
        GoNoGoTask.status = STARTED
        thisExp.addData('GoNoGoTask.started', GoNoGoTask.tStart)
        GoNoGoTask.maxDuration = None
        # keep track of which components have finished
        GoNoGoTaskComponents = GoNoGoTask.components
        for thisComponent in GoNoGoTask.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "GoNoGoTask" ---
        # if trial has changed, end Routine now
        if isinstance(Play, data.TrialHandler2) and thisPlay.thisN != Play.thisTrial.thisN:
            continueRoutine = False
        GoNoGoTask.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_circle* updates
            
            # if image_circle is starting this frame...
            if image_circle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_circle.frameNStart = frameN  # exact frame index
                image_circle.tStart = t  # local t and not account for scr refresh
                image_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_circle, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_circle.status = STARTED
                image_circle.setAutoDraw(True)
            
            # if image_circle is active this frame...
            if image_circle.status == STARTED:
                # update params
                pass
            
            # if image_circle is stopping this frame...
            if image_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_circle.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_circle.tStop = t  # not accounting for scr refresh
                    image_circle.tStopRefresh = tThisFlipGlobal  # on global time
                    image_circle.frameNStop = frameN  # exact frame index
                    # update status
                    image_circle.status = FINISHED
                    image_circle.setAutoDraw(False)
            
            # *text_gonogo_ITI* updates
            
            # if text_gonogo_ITI is starting this frame...
            if text_gonogo_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_gonogo_ITI.frameNStart = frameN  # exact frame index
                text_gonogo_ITI.tStart = t  # local t and not account for scr refresh
                text_gonogo_ITI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_gonogo_ITI, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_gonogo_ITI.status = STARTED
                text_gonogo_ITI.setAutoDraw(True)
            
            # if text_gonogo_ITI is active this frame...
            if text_gonogo_ITI.status == STARTED:
                # update params
                pass
            
            # if text_gonogo_ITI is stopping this frame...
            if text_gonogo_ITI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_gonogo_ITI.tStartRefresh + duration2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_gonogo_ITI.tStop = t  # not accounting for scr refresh
                    text_gonogo_ITI.tStopRefresh = tThisFlipGlobal  # on global time
                    text_gonogo_ITI.frameNStop = frameN  # exact frame index
                    # update status
                    text_gonogo_ITI.status = FINISHED
                    text_gonogo_ITI.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + duration2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    key_resp.duration = _key_resp_allKeys[0].duration
                    # was this correct?
                    if (key_resp.keys == str(space_key)) or (key_resp.keys == space_key):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                GoNoGoTask.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GoNoGoTask.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "GoNoGoTask" ---
        for thisComponent in GoNoGoTask.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for GoNoGoTask
        GoNoGoTask.tStop = globalClock.getTime(format='float')
        GoNoGoTask.tStopRefresh = tThisFlipGlobal
        thisExp.addData('GoNoGoTask.stopped', GoNoGoTask.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(space_key).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for Play (TrialHandler)
        Play.addData('key_resp.keys',key_resp.keys)
        Play.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            Play.addData('key_resp.rt', key_resp.rt)
            Play.addData('key_resp.duration', key_resp.duration)
        # the Routine "GoNoGoTask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'Play'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[text_end, key_resp_End],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_End
    key_resp_End.keys = []
    key_resp_End.rt = []
    _key_resp_End_allKeys = []
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end* updates
        
        # if text_end is starting this frame...
        if text_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end.frameNStart = frameN  # exact frame index
            text_end.tStart = t  # local t and not account for scr refresh
            text_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_end.status = STARTED
            text_end.setAutoDraw(True)
        
        # if text_end is active this frame...
        if text_end.status == STARTED:
            # update params
            pass
        
        # *key_resp_End* updates
        
        # if key_resp_End is starting this frame...
        if key_resp_End.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_End.frameNStart = frameN  # exact frame index
            key_resp_End.tStart = t  # local t and not account for scr refresh
            key_resp_End.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_End, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_End.status = STARTED
            # keyboard checking is just starting
            key_resp_End.clock.reset()  # now t=0
        if key_resp_End.status == STARTED:
            theseKeys = key_resp_End.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_End_allKeys.extend(theseKeys)
            if len(_key_resp_End_allKeys):
                key_resp_End.keys = _key_resp_End_allKeys[-1].name  # just the last key pressed
                key_resp_End.rt = _key_resp_End_allKeys[-1].rt
                key_resp_End.duration = _key_resp_End_allKeys[-1].duration
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
