# make pdf
Make a searchable pdf via Google Cloud Vision OCR

## Compile

gcv2hocr.c : use MingW64.

gcvocr.py : use nuitka.
```
python -m nuitka gcvocr.py --standalone --recurse-none --remove-output --plugin-enable=qt-plugins --recurse-to=requests --recurse-to=urllib3 --recurse-to=chardet --recurse-to=certifi --recurse-to=idna --recurse-to=PIL
```
hocr-pdf.py : use nuitka.
```
python -m nuitka hocr-pdf.py --standalone --recurse-none --remove-output --plugin-enable=qt-plugins --recurse-to=reportlab --recurse-to=lxml --recurse-to=PIL
```
makepdfgui.py : use nuitka.
```
python -m nuitka makepdfgui.py --standalone --recurse-none --remove-output --plugin-enable=tk-inter
```
All output files put in the same folder together.

## Execute

Double click makepdfgui.exe.

Set Google API Key via press "Config" button.

Select input image file directry via press "Set IMG dir" button.

Wait until "Done" is shown.

## Requrements for image datas

.jpg file, image size is less than 1.5MB, and image height and width are less than 1500pixels.

## Source codes

gcv2hocr.c：https://github.com/dinosauria123/gcv2hocr/blob/master/main.c

hocr-pdf.py:https://github.com/tmbdev/hocr-tools/blob/master/hocr-pdf

gcvocr.py: shown at https://www.g104robo.com/entry/google-cloud-vision-api slightly modified.

## Windows binary download

https://onedrive.live.com/download.aspx/pub/makepdfGUI.zip?cid=563E2C9BCE80B408

## License

Licence for makepdfgui.py is CC.

Other files follow original source code licenses. 

2020.1.6 ENDO Michiaki
