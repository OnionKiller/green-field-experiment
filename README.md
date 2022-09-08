## Help in the thresholding question of fellow reddit user

This notebook was created to help fellow redditor `u/GrouchyAd4055` to threshold the playfield lines on a football field.

The original code used the opencv imshow utilities, but for test purposes I choose to use jupyter notebooks.
The notebook requires additional libraries to install, you can install it based on the pip freeze:
```bash
    $ pip install -r requirements.txt
```

The original idea was to create threshold parameters based on the green field, instead of the base colour of the white lines effectively setted by hand.
This in fact didn't work well based on the hsv colour space, so instead I present a somewhat bruteforce version based on adaptive thresholding, and perccentile based thresholding over the hsv colour space.

The resulting canny edges should be similary looking, altough more noisy.