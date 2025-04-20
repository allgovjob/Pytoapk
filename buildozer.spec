[app]
title = BackgroundCommandRunner
package.name = bgcmdrunner
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,mysql-connector-python
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, CALL_PHONE
hide_title_bar = 1
log_level = 2
android.api = 31
android.minapi = 21
android.target = 31
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = 1
android.debug = 1
android.logcat_filters = *:S python:D
copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
