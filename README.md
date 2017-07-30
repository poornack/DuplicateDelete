# Duplicate Delete

This application can be used to find duplicate files in a folder. Currently, the file extention it finds are hard coded to find .jpg and .mts files. Support for all other file extentions is progress

### To do:
- Add command line arguments
- Add support for all file formats
- Add the option to delete duplicate files
- Add logging
- Add progress. Helpful for long operations.

**How it works:** The CRC of each file in the directory is read and compared with the other files' CRC. The file name does not have to be similar.

**Note:** This has only been tested with MacOS. There may be issues when running on Window. Feel free to send me bugs you find and any other feedback
