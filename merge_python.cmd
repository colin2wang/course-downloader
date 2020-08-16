
set group=%1
set lecture=%2

%group:*"=set "group=%
%lecture:*"=set "lecture=%

copy/b ".\video_cache_all\%group%\%lecture%\*.ts" ".\video_cache_all\%group%\%lecture%.ts"