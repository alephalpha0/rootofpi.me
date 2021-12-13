---
title: "Gif Making on the Command Line."
date: 2021-12-07T05:53:35Z
draft: true
categories: ["articles"]
tags: ["terminal kung fu", "termux"]
summary: "Tell what you're going to tell, how you're going to tell it. In less than 4 sentences."
---

# [CONCEPT](https://somecoolapp.io) - Tagline ne idiotic quip and we are good to go!

## Introduction to the problem I was trying to solve.
### Blahdy Blahdy blahdy

## `ffmpeg` and `gifski` combo-wombo.
[!Putting on a nice shade of Fuck You. Animated gif made with ffmpeg and gifski.](/img/gifs/fuckulipstick.gif)
### First step is going to be to use `ffmpeg` to explode a video file into `.png` images for each frame. In this example, I'm using a `.mp4` video file, but ffmpeg is hearty and can take just about anything thrown its way.

__Make sure you pay attention to the FPS in the metadata ofthe streams show by `ffmpeg`. Using this in the arguments given to `gifski` makes for a smoother gif.

```bash 
ffmpeg -i ${PATH_TO_VID}/${vid}.${ext} ${PATH_TO_FRAMES}/frame\%02d.png
``` 

### This will produce a set of `frame##.png` files in your specified directory. All set and ripe for the converting into a gif! So just `cd` into the holding directory and throw down the `gifski` command:

```bash
gifski -r 10 -Q XX -W 250 --repeat 0 frame*.png --output name_XX.gif
```
`-r` is the rate or fps of gif; `-Q` is the overall quality of gif processing; `-W` is the width of gif.


## `gifsicle` and ...
### Supporting details.

## Wrap up of points covered.
### Restate the points or steps or ruminations you have proclaimed. Add in one random link. 

## Sources & Resources & Knowledge.
* [navi tui cheatsheet](https://github.com/denisidoro/navi)
* `man ffmpeg`
* `gifski --help`
* [](https://)
