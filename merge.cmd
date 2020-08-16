set /p fileName=Input file name:

copy/b .\video_cache\*.ts ".\video_ready\%fileName%.ts"
del /Q .\video_cache\*.ts
pause