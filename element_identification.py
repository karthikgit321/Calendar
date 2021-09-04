import sys

import uiautomator2 as u2
import os
from datetime import datetime
import subprocess



class element_identification:
    def __init__(self):
        self.d=u2.connect()
        self.app_package="com.xiaomi.calendar"
        self.parent_dir = os.getcwd() + "\screenshots"
        self.curDate = datetime.now().strftime("%Y-%m-%d_%H-%M")
        self.curDateTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.save_path = os.path.join(self.parent_dir, self.curDate)
        self.c = "8.1.0"


    def create_dir(self):
        # Create the directory
        CHECK_FOLDER = os.path.isdir(self.save_path)
        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(self.save_path)
            print("created folder : ", self.save_path)

    def take_shot(self, name):
        self.name = name
        self.create_dir()
        self.d.screenshot(os.path.join(self.save_path, self.name + self.curDateTime + '.jpg'))

    def app_stop(self):
        self.d.app_stop(self.app_package)

    def start_app(self):
        self.d.app_start(self.app_package)

    def clear_app(self):
        self.d.app_clear(self.app_package)

    def device_info(self):
        a = (self.d.device_info)
        self.b = a.get('version')
        print(self.b)

    def select_ok(self):
        a1=self.d(resourceId="com.xiaomi.calendar:id/change_language")
        return a1

    def new_event(self):
        a2=self.d(resourceId="com.xiaomi.calendar:id/new_event").exists(timeout=3)
        return a2

    def drag_view(self):
        a3=self.d(resourceId="")

    def menu(self):
        a4=self.d(resourceId="com.android.calendar:id/settings_button")
        return a4

    def settings(self):
        a5=self.d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[2]
        print (a5)
        return a5

    def calendaraccounts(self):
        a6=self.d(resourceId="android:id/title")
        return a6

    def calendar_accountsdetails(self):
        a7=self.d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[0]
        return a7

    def calendar_addaccount(self):
        a8=self.d(resourceId="com.android.calendar:id/add_account")
        return a8

    def calendar_startweek(self):
        a7=self.d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[1]
        return a7

    def calendar_starttitle(self):
        a9=self.d(resourceId="miui:id/alertTitle")
        return a9

    def calendar_reminder(self):
        a10=self.d(text="Reminders")
        return a10

    def calendar_reminderinfo(self):
        a11=self.d(resourceId="miui:id/action_bar_title")
        return a11

    def calendar_remindertime(self):
        a12=self.d(text="Default all-day reminder time")
        return a12

    def calendar_remindertimeinfo(self):
        a13=self.d(resourceId="com.android.calendar:id/time")
        return a13

    def calendar_reminderdefault(self):
        a14=self.d(text="Default reminder time")
        return a14


    def calendar_reminderdefaultinfo(self):
        a15=self.d(resourceId="miui:id/alertTitle")
        return a15

    def calendar_birthdayremind(self):
        a16=self.d(resourceId="com.android.calendar:id/primary")
        return a16

    def calendar_manageholidays(self):
        a17=self.d(resourceId="com.android.calendar:id/long_holiday_item_one")
        return a17

    def calendar_editholidays(self):
        a18=self.d(resourceId="com.android.calendar:id/edit_your_holiday")
        return a18

    def calendar_manageinfo(self):
        a19=self.d(resourceId="com.android.calendar:id/week_holiday_title")
        return a19

    def calendar_holiday_enable(self):
        a20=self.d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[7]
        return a20

    def calendar_panchang(self):
        a21=self.d(resourceId="com.android.calendar:id/panchang_card_parent")
        return a21

    def calendar_panchanginfo(self):
        a22=self.d(resourceId="com.android.calendar:id/panchang_today_title")
        return a22

    def calendar_horoscope(self):
        a23=self.d(resourceId="com.android.calendar:id/horoscope_card_view_all")
        return a23

    def calendar_horoscopeinfo(self):
        a24=self.d(resourceId="com.android.calendar:id/change_zodiac_sign_title")
        return a24

    def calendar_createevent(self):
        a25=self.d(resourceId="com.android.calendar:id/new_event")
        return a25

    def calendar_eventtitle(self):
        a26=self.d(resourceId="com.android.calendar:id/title")
        return a26

    def calendar_repeat(self):
        a27=self.d(resourceId="com.android.calendar:id/scroll_view").child(className="android.widget.LinearLayout")[6]
        return a27

    def calendar_repeatdetails(self):
        a28=self.d(resourceId="android:id/title")
        return a28

    def calendar_remindersdetails(self):
        a30=self.d(resourceId="android:id/title")
        return a30

    def calendar_accountevents(self):
        a31 = self.d(resourceId="com.android.calendar:id/scroll_view").child(className="android.widget.LinearLayout")[8]
        return a31

    def calendar_accounteventsdetails(self):
        a32=self.d(resourceId="com.android.calendar:id/calendar_name")
        return a32

    def calendar_customize(self):
        a33=self.d(text="Customise your calendar")
        return a33

    def calendar_panchangcustomizeinfo(self):
        a34=self.d(resourceId="com.android.calendar:id/list").child(className="android.widget.ListView").child(className="android.widget.LinearLayout")[0]
        return a34

    def calendar_settings(self):
        a35=self.d(resourceId="com.android.calendar:id/setting_icon")
        return a35

    def calendar_panchanginfocard(self):
        a36=self.d(resourceId="com.android.calendar:id/panchang_card_parent")
        return a36

    def calendar_horoscopecustomizeinfo(self):
        a37 = self.d(resourceId="com.android.calendar:id/subscribe_channel_title_root")[1]
        return a37

    def calendar_horoscopedemocard(self):
        a38=self.d(resourceId="com.android.calendar:id/horoscope_title")
        return a38

    def calendar_whatsappcustomizeinfo(self):
        a39=(self.d(resourceId="com.android.calendar:id/list").child(className="android.widget.ListView").child(className="android.widget.LinearLayout"))[2]
        return a39

    def calendar_whatsappdemocard(self):
        a40=self.d(resourceId="com.android.calendar:id/click_layout")
        return a40

    def calendar_agree(self):
        a41=self.d(resourceId="android:id/button1")
        return a41

    def calendar_access(self):
        a42=self.d(resourceId="com.android.permissioncontroller:id/permission_allow_button")
        return a42

    def calendar_eventname(self):
        a43=self.d(resourceId="com.xiaomi.calendar:id/title")
        return a43

    def calendar_alldayenable(self):
        a44=self.d(resourceId="com.xiaomi.calendar:id/is_all_day")
        return a44

    def calendar_startdate(self):
        a45=self.d(resourceId="com.xiaomi.calendar:id/start_date")
        return a45

    def calendar_selectstartdate(self):
        a46=self.d(resourceId="android:id/button1")
        return a46

    def calendar_enddate(self):
        a47=self.d(resourceId="com.xiaomi.calendar:id/end_date")
        return a47

    def calendar_repeat1(self):
        a48=self.d(resourceId="android:id/text1")
        return a48

    def calendar_selectrepeat(self):
        a49=self.d(resourceId="android:id/list").child(className="android.widget.RelativeLayout")[1]
        return a49

    def calendar_back(self):
        a50=self.d(resourceId="miui:id/up")
        return a50

    def calendar_reminders(self):
        a51=self.d(resourceId="com.xiaomi.calendar:id/reminders")
        return a51

    def calendar_selectreminders(self):
        a52=self.d(resourceId="android:id/content")
        return a52

    def calendar_saveevent(self):
        a53=self.d(resourceId="com.xiaomi.calendar:id/action_done")
        return a53

    def calendar_eventassert(self):
        a54=self.d(text="Hello")
        return a54

    def calendar_addevent(self):
        a55=self.d(resourceId="com.xiaomi.calendar:id/new_event")
        return a55

    def calendar_selectview(self):
        a56=self.d(resourceId="com.xiaomi.calendar:id/tab_button")
        return a56

    def calendar_selectweek(self):
        a57=self.d(resourceId="com.xiaomi.calendar:id/tab_week")
        return a57

    def calendar_selectday(self):
        a58=self.d(resourceId="com.xiaomi.calendar:id/tab_day")
        return a58

    def calendar_selectagenda(self):
        a59=self.d(resourceId="com.xiaomi.calendar:id/tab_agenda")
        return a59

    def calendar_Birthdayselection(self):
        a60=self.d(resourceId="com.xiaomi.calendar:id/birthday_tab_container")
        return a60

    def calendar_Birthdate(self):
        a61=self.d(resourceId="com.xiaomi.calendar:id/birthday_date")
        return a61

    def calendar_Birthdayselect(self):
        a62=self.d(resourceId="android:id/button1")
        return a62

    def calendar_Remindertime(self):
        a63=self.d(resourceId="com.xiaomi.calendar:id/reminder_time")
        return a63

    def calendar_Birthdayagree(self):
        a64=self.d(resourceId="com.xiaomi.calendar:id/action_done")
        return a64