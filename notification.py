from plyer import notification

education_title = "HERE WITH ME"
education_message = "Thank You I Don't Care"

notification.notify(
    title = education_title,
    message = education_message,
    app_icon = None,
    timeout = 10,
    toast = False
)
