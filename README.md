# 🐍 winsound Telephone

Simple python program that makes use of the `winsound` library to reproduce sounds on your computer, it allows for regular Windows alert sounds or custom ones, using .wav files. 🔊

I compiled the classic telephone dial tones in the sounds folder 📁, so you can test how dialing your own phone number would sound like with the `dial_up()` function!

![alt text](https://i.pinimg.com/originals/df/04/39/df04391732667b76d5291acf383329b1.gif)

The function `interval_reminder()` beeps after a certain amount of time is elapsed (interval) throughout the duration.

You can also create a .csv file with a list of frequency/duration pairs, that when called with the function `csv_to_sound()` reproduces the sounds specified.

Use `request_sound()` to test frequency/duration pairs, helpful for creating a good .csv file!  
