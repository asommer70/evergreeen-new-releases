;;#!/usr/local/bin/sbcl --script
;; (defvar *app* (make-instance 'ningle:<app>))

;; (setf (ningle:route *app* "/")
;;       "Welcome to ningle!")

;; (setf (ningle:route *app* "/login" :method :POST)
;;       #'(lambda (params)
;;           (if (authorize (cdr (assoc "username" params :test #'string=))
;;                          (cdr (assoc "password" params :test #'string=)))
;;               "Authorized!"
;;               "Failed...Try again.")))

;; (clack:clackup *app*)

(let ((quicklisp-init (merge-pathnames "quicklisp/setup.lisp" (user-homedir-pathname))))
  (when (probe-file quicklisp-init)
    (load quicklisp-init)))

(ql:quickload :wookie)


(Defpackage :my-website
  (:use :cl :wookie :wookie-plugin-export))
(in-package :my-website)

;; load Wookie's core plugins. much of Wookie's functionality is written as
;; plugins which can be enabled/disabled/overwritten it desired.
(load-plugins)

;; setup a simple homepage
(defroute (:get "/") (req res)
  (send-response res :body "<html><head><title>Test</title><head><body><h1>I've Got Worms...</h1></body></html>"))

;; setup a mapping for the url / to a local directory assets. a request for
;; 
;;   /images/background.jpg
;;
;; will load "./assets/images/background.jpg"
;;(def-directory-route "/" "./assets")

;; start the event loop that Wookie runs inside of
(as:with-event-loop ()
  ;; create a listener object, and pass it to start-server, which starts Wookie
  (let* ((listener (make-instance 'listener
                                  :bind nil  ; equivalent to "0.0.0.0" aka "don't care"
                                  :port 3000))
         ;; start it!! this passes back a cl-async server class
         (server (start-server listener)))
    ;; stop server on ctrl+c
    (as:signal-handler 2
      (lambda (sig)
        (declare (ignore sig))
        ;; remove our signal handler (or the event loop will just sit indefinitely)
        (as:free-signal-handler 2)
        ;; graceful stop...rejects all new connections, but lets current requests
        ;; finish.
        (as:close-tcp-server server)))))

;; (let ((blackbird:*debug-on-error* t)
;;       (wookie-config:*debug-on-error* t))
;;   ;; omit :catch-app-errors here
;;   (as:with-event-loop ()
;;     (wookie:start-server (make-instance 'wookie:listener
;;                                         :port 3000))))
