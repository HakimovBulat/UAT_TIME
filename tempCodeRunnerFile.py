    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(select_group))
    application.add_handler(CallbackQueryHandler(button_group))