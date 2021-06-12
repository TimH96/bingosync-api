This is a fork of [@gamesdonequick/bingosync-api](https://github.com/GamesDoneQuick/bingosync-api). I forked said project to include non-spectator features and to fix the ``getNewSocketKey`` method that I could not longer get to work, specifically for a Windows Node.js application I wanted to build with it. Here is what changed:

+ Implemented joining as non-spectator, and consequently implemented methods for non-spectator features. The API allows you to tick/untick goals, change the players color and send chat messages.
+ Re-implemented ``getNewSocketKey`` to use the Node ``https`` module rather than ``ky``. I couldn't get the original implementation to work, and couldn't figure out why it was broken. My implementation does not support browsers, as far as I know.
+ Removed the local storage feature.
+ Massively streamlined the project. The original project was an NPM package and came with much of the assosciated professionalism, which however made it hard to work around its pipelines now that it, and some of its dependencies, are no longer on NPM. If you want the POST/PUT features from my code, I highly recommend you copy those and implement them in the original project instead, as I admittedly went the quick and dirty way to make this wrapper fit my specific needs.