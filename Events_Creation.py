import os
import time
import unittest
from datetime import datetime
import subprocess

import HtmlTestRunner
import uiautomator2 as u2
from element_identification import element_identification

class CalendarTestcases(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.d = u2.connect()
        self.e=element_identification()
        self.curDateTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.e.device_info()
        self.e.clear_app()

    def setUp(self):
        self.e.start_app()

    def test_calendar01_Launch(self):
        try:
            self.e.calendar_agree().click(timeout=3)
            self.e.calendar_access().click(timeout=3)
            self.e.select_ok().click(timeout=3)
            self.e.take_shot("homepageselect_")
            a2=self.e.new_event()
            assert a2
            self.e.take_shot('launch_')

        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar02_Event_creation(self):
        try:
            self.e.calendar_addevent().click(timeout=3)
            self.e.calendar_eventname().click(timeout=3)
            cmd = "adb shell input text Hello"
            subprocess.check_output(cmd)
            time.sleep(3)
            self.e.calendar_alldayenable().click(timeout=3)
            self.e.calendar_startdate().click(timeout=3)
            self.e.calendar_selectstartdate().click(timeout=3)
            self.e.calendar_enddate().click(timeout=3)
            self.e.calendar_selectstartdate().click(timeout=3)
            self.e.calendar_repeat1().click(timeout=3)
            self.e.calendar_selectrepeat().click(timeout=3)
            self.e.calendar_back().click(timeout=3)
            time.sleep(3)
            self.e.calendar_reminders().click(timeout=3)
            self.e.calendar_selectreminders().click(timeout=3)
            self.e.calendar_back().click(timeout=3)
            self.e.calendar_saveevent().click(timeout=3)
            self.e.take_shot("Event created_")
            time.sleep(3)
            a2=self.e.calendar_eventassert()
            assert a2
            self.e.take_shot('event_')
            self.e.calendar_selectview().click(timeout=3)
            self.e.calendar_selectagenda().click(timeout=3)
            time.sleep(3)
            a2 = self.e.calendar_eventassert()
            assert a2


        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar03_Birthday_event(self):
        try:
            self.e.calendar_addevent().click(timeout=3)
            self.e.calendar_Birthdayselection().click(timeout=3)
            self.e.calendar_eventname().click(timeout=3)
            cmd = "adb shell input text Test" + self.curDateTime
            subprocess.check_output(cmd)
            time.sleep(3)
            self.e.calendar_Birthdate().click(timeout=3)
            self.e.calendar_Birthdayselect().click(timeout=3)
            self.e.calendar_Remindertime().click(timeout=3)
            self.e.calendar_Birthdayselect().click(timeout=3)
            self.e.calendar_Birthdayagree().click(timeout=3)
            self.e.take_shot('event_')
            a2=cmd
            assert a2

        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def tearDown(self):
        self.e.app_stop()

