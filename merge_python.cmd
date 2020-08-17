
set id=%1
set group=%2
set lecture=%3

%group:*"=set "group=%
%lecture:*"=set "lecture=%

copy/b ".\video_cache_all\%id%\%group%\%lecture%\*.ts" ".\video_cache_all\%id%\%group%\%lecture%.ts"