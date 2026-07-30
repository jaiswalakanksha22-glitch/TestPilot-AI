import os

SAMPLES = {
    "🔐 User Login": "login.txt",
    "👤 User Registration": "registration.txt",
    "💳 Payment": "payment.txt",
    "📅 Appointment Booking": "appointment.txt",
    "🌐 Login API": "api_login.txt"
}


def load_sample(display_name):

    filename = SAMPLES[display_name]

    path = os.path.join(
        "sample_requirements",
        filename
    )

    with open(path, "r", encoding="utf-8") as f:
        return f.read()