from . import create_server
import signal

def main():
    try:
        server = create_server()
        print("SIGINT handler:", signal.getsignal(signal.SIGINT))
        server.run(host="0.0.0.0", port=5000, use_debugger=False, debug=server.config.get("DEBUG"), use_reloader=server.config.get("USE_RELOADER"))
    except KeyboardInterrupt:
        print("\nServer stopped by Ctrl+C")


if __name__ == "__main__":
    main()
    