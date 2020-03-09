import tornado.ioloop
import tornado.web
import tornado.httpserver
import sys
import settings

from tornado.options import options


def main():
    try:
        print(f"Starting server at: {'http://' + options.host + ':' + str(options.port)}")
        options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(settings.application)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("Server got to stop.")
    except:
        import traceback
        print(traceback.print_exc())
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
