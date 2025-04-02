# Random Number Picker
This is a random number picker I developed specifically to give me a truly random number from a list for my 100 day/100 song karaoke challenge (posting soon). feel free to use and fork however you like (with attribution)

# Virustotal is showing false positives
**[More info](#2)**
Since version 0.1.7, A lot of antiviruses on virustotal are marking the compiled binaries as viruses. These are false positives caused by the switch to a new python compiler, [Check out the virustotal results for version 0.1.7 here](https://www.virustotal.com/gui/file/10ac50465a5dc8811d631a341b35874fdc9918aa7cc2f2e6bfdc7337aa64d76e/detection)

# How to use
Simply change the data in the '[data.json](./data.json)' file and add your own data. A tool for this will be developed soon

add your entries to '[data.json](./data.json), seperated by a comma, such as in [example.json](./example.json). For automatically opening links, copy paste the data under 'data', make sure that any numbers are in quotes, add a colon after the data but before the comma, and set the value to `null` if you do not want the selection to open a link or put your links in quotes after the colon

change settings in config.json

# Future plans
- [X] Integrate with OBS using text and webhooks
- [X] Allow the automatically opening a URL after choosing a song
- [ ] Create an easier, seperate program that appends data to the .json file for easier editing

I currently don't plan to support this project in the future, outside of the items above, ~~however I *MAY* add support for something other than numbers~~
Update: I did add support for something other than numbers

# NO SUPPORT
This project comes with no support as it is a personal project. If you would like a feature to be added, fork this repository and add it. No pull requests will be merged into this repository

# License
This project is licensed under the [GPL-3.0 License](./LICENSE). Read LICENSE for more information
