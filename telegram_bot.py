from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pandas as pd

# משתנה לאחסון נתונים
data = []

# הפקודה הראשונה שהבוט מגיב לה
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('שלום! שלח לי את הנתונים בפורמט הבא:\nצוות X\n5.56 - 2000\n7.62 - 5000')

# פונקציה לאיסוף נתונים
def collect_data(update: Update, context: CallbackContext) -> None:
    global data
    text = update.message.text
    data.append(text)
    update.message.reply_text('הנתונים נשמרו!')

# פונקציה ליצירת דוח
def generate_report(update: Update, context: CallbackContext) -> None:
    global data
    if data:
        # יצירת דוח
        rows = []
        for entry in data:
            lines = entry.split('\n')
            team = lines[0]
            for line in lines[1:]:
                weapon, quantity = line.split(' - ')
                rows.append({"Team": team, "Weapon": weapon.strip(), "Quantity": int(quantity.strip())})
        
        # יצירת קובץ Excel
        df = pd.DataFrame(rows)
        df.to_excel("daily_report.xlsx", index=False)
        
        # שליחת קובץ בחזרה
        update.message.reply_text("הדוח נוצר בהצלחה! שולח לך את הדוח...")
        update.message.reply_document(open("daily_report.xlsx", "rb"))
        
        # איפוס הנתונים
        data.clear()
    else:
        update.message.reply_text("אין נתונים לדוח.")

# פונקציה למחיקת נתונים
def clear_data(update: Update, context: CallbackContext) -> None:
    global data
    data.clear()
    update.message.reply_text("הנתונים נמחקו!")

# הפונקציה הראשית שמריצה את הבוט
def main():
    # ה-Token שלך מבוטפאדר
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher

    # הגדרת הפקודות
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, collect_data))
    dispatcher.add_handler(CommandHandler("report", generate_report))
    dispatcher.add_handler(CommandHandler("clear", clear_data))

    # התחלת הבוט
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
