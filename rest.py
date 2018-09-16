#!/usr/bin/env python
import web

urls = (
    '/process/*', 'serve_requests',
    '/stats', 'list_stats'
)

app = web.application(urls, globals())

class serve_requests:        
    def GET(self):
        return "Get working"

    def POST(self):
        return "Get working"

    def PUT(self):
        return "Put working"

    def DELETE(self):
        return "delete working"


class list_stats:
    def GET(self):
        return "serving stats"


if __name__ == "__main__":
    app.run()
