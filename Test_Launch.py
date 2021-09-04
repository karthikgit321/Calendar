import os
import time
import unittest
from datetime import datetime

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
            self.d(resourceId="com.android.calendar:id/title").wait(timeout=2)
            self.e.take_shot("calendarlanguageselect_")
            self.e.select_ok().click(timeout=3)
            a2=self.e.new_event()
            assert a2
            self.e.take_shot('launch_')

        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar02_holiday_enable(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            self.e.calendar_holiday_enable().click(timeout=3)
            res=self.d(resourceId="android:id/checkbox")
            assert res
            self.e.take_shot('holidaysenable_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar03_manage(self):
        try:
            res=False
            self.d(scrollable=True).scroll(steps=15)
            self.e.calendar_manageholidays().click(timeout=3)
            res = self.e.calendar_editholidays().exists(timeout=3)
            assert res
            time.sleep(5)

            #h=self.e.calendar_manageholidays()
            #i=0
            #while not h and i<5:
             #  print (i)
             #  if h:
               #    h.click()
                #   res=True
                 #  break
               #else:
                #   i+=1
                 #  time.sleep(2)
                  # h = self.e.calendar_manageholidays()
            # res = self.e.calendar_editholidays().exists(timeout=3)

            assert res
            self.e.take_shot('calendarManage_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise
    def test_calendar04_panchang(self):
        try:
            self.d.scrollTextIntoView("Panchang")
            time.sleep(5)
            self.d(resourceId="com.android.calendar:id/panchang_card_parent").click(timeout=6)
            res = self.e.calendar_panchanginfo().exists(timeout=3)
            assert res
            self.e.take_shot('calendarpanchang_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise
    def test_calendar05_accounts(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            res=self.e.calendaraccounts().exists(timeout=3)
            assert res
            self.e.take_shot('calendaraccounts_')
            self.d.swipe_ext("up")
            self.e.take_shot('calendaraccounts1_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar05_acccountinfo(self):
        try:
            self.e.menu().click(timeout=3)
            time.sleep(2)
            self.e.settings().click(timeout=3)
            #a5 = self.d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[2]
            #print(a5)
            self.e.calendar_accountsdetails().click(timeout=3)
            res=self.e.calendar_addaccount().exists(timeout=3)
            assert res
            self.e.take_shot('calendaraddaccounts_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise


    def test_calendar06_startweek(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            self.e.calendar_startweek().click(timeout=3)
            res = self.e.calendar_starttitle().exists(timeout=3)
            assert res
            self.e.take_shot('calendarstartweek_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar07_reminder(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            #self.d.drag([0,709][720,805])
            self.d.swipe_ext("up")
            time.sleep(2)
            a10=self.e.calendar_reminder()
            a10.click(timeout=3)
            time.sleep(2)
            res=self.e.calendar_reminderinfo().exists(timeout=3)
            assert res
            self.e.take_shot('calendarreminder_')

        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar08_reminder_time(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            self.d.swipe_ext("up")
            time.sleep(2)
            a12=self.e.calendar_remindertime()
            a12.click(timeout=3)
            res=self.e.calendar_remindertimeinfo().exists(timeout=3)
            assert res
            self.e.take_shot('calendarremindertime_')

        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar09_reminder_default(self):
        try:
            self.e.menu().click(timeout=3)
            self.e.settings().click(timeout=3)
            self.d.swipe_ext("up")
            time.sleep(2)
            a13=self.e.calendar_reminderdefault()
            a13.click(timeout=3)
            res=self.e.calendar_reminderdefaultinfo().exists(timeout=3)
            assert res
            self.e.take_shot('calendarreminderdefault_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar10_day(self):
        try:
            self.d( scrollable = True ).scroll ( steps = 4 )
            res=self.e.calendar_birthdayremind().exists(timeout=3)
            assert res
            self.e.take_shot('calendarthisday_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise


    def test_calendar12_createevent(self):
        try:
            self.e.calendar_createevent().click(timeout=3)
            time.sleep(2)
            self.d.press("back")
            time.sleep(2)
            res=self.e.calendar_eventtitle().exists(timeout=3)
            assert res
            self.e.take_shot('createvent_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar13_repeat(self):
        try:
            self.e.calendar_createevent().click(timeout=3)
            time.sleep(2)
            self.d.press("back")
            time.sleep(2)
            self.e.calendar_repeat().click(timeout=3)
            res=self.e.calendar_repeatdetails().exists(timeout=3)
            assert res
            self.e.take_shot("repeat_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar14_Reminders(self):
        try:
            self.e.calendar_createevent().click(timeout=3)
            time.sleep(2)
            self.d.press("back")
            time.sleep(2)
            self.e.calendar_reminders().click(timeout=3)
            res = self.e.calendar_remindersdetails().exists(timeout=3)
            assert res
            self.e.take_shot("Remindersevent_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar15_accountevents(self):
        try:
            self.e.calendar_createevent().click(timeout=3)
            time.sleep(2)
            self.d.press("back")
            time.sleep(2)
            self.e.calendar_accountevents().click(timeout=3)
            res = self.e.calendar_accounteventsdetails().exists(timeout=3)
            assert res
            self.e.take_shot("accountevents_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar302_customize(self):
        try:
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.e.calendar_customize().click(timeout=2)
            res=self.e.calendar_customizeinfo().exists(timeout=2)
            assert res
            self.e.take_shot("calendarcustomize_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar402_customizesetting(self):
        try:
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.e.calendar_customize().click(timeout=3)
            self.e.calendar_settings().click(timeout=3)
            res=self.e.calendar_customizeinfo().exists(timeout=2)
            assert res
            self.e.take_shot("calendarcustomizesettings_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar02_panchangdemocard(self):
        try:
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.e.calendar_customize().click(timeout=3)
            self.e.calendar_panchangcustomizeinfo().click(timeout=3)
            res = self.e.calendar_panchanginfocard().exists(timeout=3)
            assert res
            self.e.take_shot("calendarpanchangdemo_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def test_calendar01_horoscopedemocard(self):
        try:
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.e.calendar_customize().click(timeout=3)
            self.e.calendar_horoscopecustomizeinfo().click(timeout=3)
            res=self.e.calendar_horoscopedemocard(self).exists(timeout=3)
            assert res
            self.e.take_shot("calendarhoroscopedemo_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise



    def test_calendar01_whatsappdemocard(self):
        try:
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(3)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.d.swipe_ext("up")
            time.sleep(2)
            self.e.calendar_customize().click(timeout=3)
            self.e.calendar_calendar_whatsappcustomizeinfo().click(timeout=3)
            res=self.e.calendar_whatsappdemocard(self).exists(timeout=3)
            assert res
            self.e.take_shot("calendarhoroscopedemo_")
        except Exception as error:
            self.e.take_shot('Error_')
            raise

    def tearDown(self):
        self.e.app_stop()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_title="Calendar Test Results",
                                                           report_name='Test Results',
                                                           output=os.getcwd()+'/reports'))
'''
    def test_calendar_drag(self):
        try:
           time.sleep(3)
           #self.d.drag(210,380,310,473,0.5)
           self.d.long_click (210,380,0.5 )
           time.sleep(5)
           self.d.drag(210,380,310,473,0.5)
           a3=self.e.new_event()
           assert a3
           self.e.take_shot('drag_')
        except Exception as error:
            self.e.take_shot('Error_')
            raise
'''