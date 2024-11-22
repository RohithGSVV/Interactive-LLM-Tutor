import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.join(os.path.dirname(__file__), '..', 'src'))))

from test_teams_notification import TeamsNotification

def test_teams_notification():
    tm = TeamsNotification()
    res = tm.send_message("Testing Notification Class") 
    assert res == 200, f"Failed to send notification: {res}"