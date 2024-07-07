from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '7029103499:AAGTuXTGfx4pMiDZH_GJPvb1vMMXgP5Z9FI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_text(
        f'سلام {update.effective_user.first_name} عزیز \n'
        'به ربات ایساتیس پویا خوش آمدید.\n'
        'می‌توانید جهت اطلاع از فعالیت‌های شرکت‌ها، به کانال‌ شرکت مورد نظرتون بپیوندید و از آخرین اخبار و فعالیت‌ها مطلع شوید. '
        'لطفاً کانال مد نظر خود را از منوی زیر انتخاب کرده و جوین شوید.',
        reply_markup=reply_markup
    )
    

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_text(
         'لطفاً شرکت  مد نظر خود را از منوی زیر انتخاب کرده.',
        reply_markup=reply_markup
    )
    


async def show_submenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text=='گروه مالی و سرمایه گذاری ایساتیس پویا' :
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatispooya.png', caption='گروه مالی ایساتیس پویا\n 🌐 https://isatispooya.com/' , reply_to_message_id=update.message.id) 

# Visa
        
    if text == 'سرمایه گذاری':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['سبدگردانی', 'کارگزاری','ویسا'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )

    elif text == 'کارگزاری':
        # await update.message.reply_text('اینجا لینک سایت رسمی گروه مالی و سرمایه گذاری ایساتیس پویا قرار می‌گیرد.')
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\ipb.png', caption='کارگزاری ایساتیس پویا\n 🌐 https://ipb.ir/' , reply_to_message_id=update.message.id) 
 
    elif text == 'ویسا':
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatisvisa.png', caption='سرمایه گذاری ایساتیس پویا\n 🌐 https://visa.isatispooya.ir/' , reply_to_message_id=update.message.id) 

    elif text == 'سبدگردانی':
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatispm.png', caption='سبدگردانی ایساتیس پویا\n 🌐 https://isatispm.ir/' , reply_to_message_id=update.message.id) 

    elif text == 'بازگشت به منوی اصلی':
        await back(update, context)

# Bours

    if text == 'بورس':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['خرید سهام'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'خرید سهام':
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatisvisa.png', caption='خرید سهام\n 🌐 https://isatiscrowd.ir/' , reply_to_message_id=update.message.id) 



# Insurance

    if text == 'بیمه':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['بیمه زندگی','کارگزاری بیمه'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'بیمه زندگی':
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\insurance.png', caption='بیمه زندگی \n 🌐 https://insurance.isatispooya.com/' , reply_to_message_id=update.message.id) 

    elif text == 'کارگزاری بیمه':
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\ipin.png', caption='کارگزاری بیمه\n 🌐 https://ipin.ir/' , reply_to_message_id=update.message.id) 


# Isatispm

    if text == 'سبدگردان':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['سبدگردانی اختصاصی'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'سبدگردانی اختصاصی':
     await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatispm.png', caption='سبدگردانی ایساتیس پویا\n 🌐 https://isatispm.ir/' , reply_to_message_id=update.message.id) 



# Sabad

    if text == 'ابزارهای مالی':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['صندوق سرمایه گذاری ترمه','صندوق سرمایه گذاری خاتم','صندوق بازارگردانی'],
            ['صندوق سرمایه‌گذاری مشترک','صندوق سرمایه گذاری خصوصی اکسیر زیست پارسیان'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )




# Ipmill

    if text == 'صنایع مفتول':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\ipmill.png', caption='صنایع مفتول ایساتیس پویا\n 🌐 https://ipmill.isatispooya.com/' , reply_to_message_id=update.message.id) 

# Atieh

    if text == 'آتیه سازان کویر یزدان':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\isatisatieh.png', caption='آتیه سازان کویر یزدان\n 🌐 https://atieh.isatispooya.com/' , reply_to_message_id=update.message.id) 
# Pardisan

    if text == 'عمرانی سفیران پردیسان':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\pardisan.png', caption='عمرانی سفیران پردیسان یزد\n 🌐 https://pardisan.isatispooya.com/' , reply_to_message_id=update.message.id) 

# Isatis-crowd

    if text == 'پلتفرم تامین مالی':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_photo(photo='D:\Abouei\TelegramBot\image\crowd.png', caption='پلتفرم تامین مالی ایساتیس پویا\n 🌐 https://isatiscrowd.ir/' , reply_to_message_id=update.message.id) 

async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(f'{update.effective_user.first_name}عزیز\n ممنون که با ما همراه بودید\nگروه مالی ایساتیس پویا ')



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", goodbye))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_submenu))
app.run_polling()
