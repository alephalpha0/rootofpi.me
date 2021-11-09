---
title: "Building a CLI Flow 01"
date: 2020-11-10T22:14:04Z
draft: false
categories: ["blog"]
tags: ["geek me good", "command line gazing", "terminal blues"]
summary: "So, I feel like my grasp of scripting and pipelines is decent enough to cobble together a functioning bash script using programs and sources at my disposal that should take care of what I want to do. Namely, a locally saved, single file .html"
location: "the good ship starship shelled"
---


# Building a cli program flow in order to archive a single webpage or article.

### The problem to be solved: 
> I have a desire to be able to, through the command line, download a single webpage into a self-contained `.html` file with the option to convert it to (or save alongside) other formats such as `PDF`, `EPUB`, or even `md` if possible. There are **two** main use-cases I want to offer: 1) get the entire webpage, strip out the ads/useless shit, and save the new version locally & 2) for journal/website articles, blog entries, or tutorials: simply save the main content and discard every other element from the source. 
  
### The initial idea for solution: 
A bash script that takes in a URL and, through menu redirection, outputs the desired file(s) into a standard directory. 

### Why not use currently available methods: 
I've come across quite a few programs and scripts that seem like they would be perfect for what I want to do, but unfortunately I'm using termux on an Android and most of them do not work for one reason or the other in this enviromment.  
###### CLIs that I have tried with no luck to get working on Termux: 
+ `hget` - [hget](https://github.com/bevacqua/hget) 
+ `monolith` - [monolith](https://github.com/Y2Z/monolith)
+ `erised` - [erised](https://github.com/marvelm/erised) 
+ `percollate` - [percollate](https://github.com/danburzo/percollate)
+ `ferret` - [ferret](https://github.com/MontFerret/ferret) 

### The semi-focused detailing of my initial mind thoughts:   
So, I feel like my grasp of scripting and pipelines is decent enough to cobble together a functioning bash script using programs and sources at my disposal that should take care of what I want to do. Namely, a locally saved, single file `.html` and have the option/ability to convert to `PDF`, `md`, or `EPUB` if desired. In my mind, there will be several working pieces of this script that could and should be broken down into smaller modules\\functions . 

I'm designing and planning on a menu-driven interface so creating menu-building and menu-displaying functions will be two individual tasks. Directory checking, creation, and manipulation should be another set of tasks. Error handling, logging and graceful failures are another set. And finally, the actual downloading and parsing into files will be a set of functions. 
  
I'm aware that bash scripting might not be the optimal route to go with this idea, due to processing times, data handling and manipulation, and the fact that other languages come with the advantage of libraries and support modules that cover just about every detail and "feature" I could possibly come up against. However, it will serve as a basis for laying out the flow and main ideas of what I want my script to do as well as help prototype and get a working product to use as proof of concept. 

From the get-go, there are several options that I can and will be utilizing to achieve my end-goal. I'm hoping that using and offering several options of methods will not over-complicate the road ahead. The ability to write code that can be easily extended and has the ability to easily have options added to it is something that I am working towards. The thought that I should focus on one (one method for obtaining the webpage, one method for processing the downloaded data, one method for saving, and one method for file conversion) is there, and it has validity. However, I am blockheaded when it comes to ambitions, and throwing caution to the wind is the name of the game right now. 
###### Options in consideration for scraping/downloading/getting source: 
+ `wget` 
+ `cURL` 
+ `httpie` 
+ `ferret` 
+ `w3m` 

This is as far as I have gotten, planning and layout wise. The next part of this session of brain-vomitting will cover the logic trains, process flow, and possible ways of brainstorming the layout of the script. 

#### TODO:
+ research the methods of using `ferret` to scrape websites and obtain the contents. 
+ look into flags and options of `wget` `cURL` `httpie` and `w3m`. 
+ Sketch out the menus and brainstorm ways for it to work.
+ For processing... HTML2JSON? HTML2MD? HTML2????? 
+ File conversion should be PANDOC, but of course, the perfect tool doesn't work under termux. 
