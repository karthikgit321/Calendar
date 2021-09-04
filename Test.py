
import time
import uiautomator2 as u2
from datetime import datetime
import unittest
import element_identification

d = u2.connect()
d.app_start("com.android.calendar")

a=(d.device_info)
print(a)
print("--------------")
b=a.get('version')
print(b)
print(type(b))
c="8.1.0"

def calendar_reminder():
    a10=d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[6]
    print (a10)
    return a10

d.swipe_ext("up")
time.sleep(2)
d.swipe_ext("up")
#d(resourceId="com.android.calendar:id/new_event").click(timeout=3)
time.sleep(2)
#d.press("back")
#time.sleep(2)
#a=d(resourceId="com.android.calendar:id/scroll_view").child(className="android.widget.LinearLayout")[8]
a.click(timeout=3)
#d(resourceId="com.android.calendar:id/settings_button").click(timeout=3)
#d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[2].click(timeout=3)
#d(resourceId="com.android.calendar:id/horoscope_card_view_all").click(timeout=3)
#res=d(resourceId="com.android.calendar:id/change_zodiac_sign_title").exists(timeout=3)
#assert res

calendar_reminder().click(timeout=3)



'''
d(scrollable=True).scroll(steps=30)
a17 = d(resourceId="com.android.calendar:id/panchang_card_parent")
print(a17,a17.get_text())
a17.click()
'''

# e=element_identification.element_identification()
# d.app_start("com.android.calendar")
#e.menu().click(timeout=3)
#e.settings().click(timeout=3)
#e.calendar_holiday_enable().click(timeout=3)
#d.press("back")
#d ( scrollable = True ) .scroll(steps=5)
# d.swipe_ext("up")
# time.sleep(5)
# e.calendar_manageholidays().click(timeout=3)
# res=e.calendar_editholidays().exists(timeout=3)
# assert res


# mnu=d(resourceId="android:id/list").child(className="android.widget.LinearLayout")
# mnu=d(resourceId="android:id/text1")
'''mnu=d(text="Settings")
print(mnu.count,"mnu_count=")
for i, m in enumerate(mnu):
    print(i,m.get_text())
    if i==1:
        m.click()
        print("clicked")

print(mnu,"count=")
# d.swipe_ext("up")
# time.sleep(2)
# d(resourceId="android:id/list").child(className="android.widget.LinearLayout")[7].click(timeout=3)
'''