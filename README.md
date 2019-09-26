# serenytics-embedding-demo
Demo to embed a Serenytics dashboard in a web app (provides a frontend and a backend)

The documentation to securely embed a Serenytics dashboard in an app is here:
https://doc.serenytics.com/developer/template_dashboards/#back-end-mode

## backend
The backend is a Flask server. It provides a route to get an URL to embed a dashboard. You need a similar route in your own backend to enabled dashboard embedding in your app.

## frontend
The frontend is an Angular app. It embeds a dashboard in a iFrame.
