from ipaddress import ip_address, ip_network
from flask import Flask, request, render_template, make_response, \
                  send_from_directory, redirect, url_for
from flask_limiter import Limiter
import redis


# GLOBAL VARIABLES
REDIS_HOST = "redis"
REDIS_PORT = 6379
IP_LIMIT = 3
AGE_OFF = 5  # in minutes
WHITELISTED_SUBNET = "10.24.85.0/24"
AUTHORIZED_AGENT = "Papa"
CHAT_KEY = "5466334579"

with open("flag.txt") as f:
    FLAG = f.read().strip()

redisclient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


MESSAGES = [
    ("handler", "Welcome Agent. Thank you for verifying your identity and location."),
    ("handler", "This is a security chat system with U.S. Military Grade Encryption."),
    ("handler", "Please provide the secret pin provided to retrieve details about your next mission.")
]


def get_client_ip_address():
    """
    Returns the IP address from the header X-Real-IP
    or the client address passed from the request object.

    :input request: flask.Request object
    :return str: IP address
    """

    return request.headers.get("X-Real-IP") or request.remote_addr


def get_blocked_ips():
    """
    Returns the blocked IP and the default IP limit for
    each blocked IP from the Redis database.

    :return list: tuple of (IP, IP_LIMIT)
    """

    blocked_ip_stats = []
    for key in redisclient.scan_iter("LIMITER*"):
        value = int(redisclient.get(key))
        key = key.decode().split("/")[1]
        if value > IP_LIMIT:
            blocked_ip_stats.append((key, IP_LIMIT))
    return blocked_ip_stats

# Initialize app and extension applications
app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_client_ip_address,
    default_limits=[f"{IP_LIMIT} per {AGE_OFF} minutes"],
    storage_uri=f"redis://{REDIS_HOST}:{REDIS_PORT}",
    strategy="fixed-window"
)

@app.errorhandler(429)
def handler_rate_limited(e):
    """
    Return a Rate Limited page with stats of all blocked IPs.
    """

    return make_response(render_template("rate-limited.html", blocked_ips=get_blocked_ips(), time=AGE_OFF))

@app.errorhandler(404)
def handler_not_found(e):
    """
    Return a default 404 page for a page Not Found.
    """

    return render_template("404.html"), 404


@app.route("/robots.txt")
@limiter.exempt
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/chat", methods=["GET", "POST"])
@limiter.exempt
def chat():
    useragent = request.headers.get("User-Agent", "")
    remoteip = get_client_ip_address()

    # Right UA, Right IP
    if ip_address(remoteip) not in ip_network(WHITELISTED_SUBNET) and useragent != AUTHORIZED_AGENT:
        return redirect(url_for("index"))

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        print(message)

        if message:
            global MESSAGES
            MESSAGES.append(("agent", message))

            if message == CHAT_KEY:
                MESSAGES.append(("handler", "Thank you for providing the secret pin, Agent Papa."))
                MESSAGES.append(("handler", f"Your next mission is: {FLAG}"))
            else:
                MESSAGES.append(("handler", "Invalid secret pin, Agent. Are you sure you're not an impostor? Try again."))
    return render_template("chat.html", messages=MESSAGES)


# Index view
@app.route('/', methods=["GET"])
def index():
    useragent = request.headers.get("User-Agent", "")
    remoteip = get_client_ip_address()

    # Right UA, Right IP
    if ip_address(remoteip) in ip_network(WHITELISTED_SUBNET) and useragent == AUTHORIZED_AGENT:
        return redirect(url_for("chat"))
    # Wrong UA, Wrong IP
    elif ip_address(remoteip) not in ip_network(WHITELISTED_SUBNET) and useragent != AUTHORIZED_AGENT:
        return render_template("unauthorized-agent.html")
    # Right UA, Wrong IP
    elif ip_address(remoteip) not in ip_network(WHITELISTED_SUBNET) and useragent == AUTHORIZED_AGENT:
        return render_template("authorized-agent.html", authorized_agent=AUTHORIZED_AGENT, whitelisted_subnet=WHITELISTED_SUBNET, chat_key=CHAT_KEY)
