# csci650-anti-aliasing

Repo for materials used during our presentation on anti-aliasing for CSCI 650.

### Addtional Information

Eric's SSAA script can be run by cloning this repository and installing dependencies with `pip install -r requirements.txt`. Usage is as follows:
```bash
python ssaa.py <input_image> <output_image> 
```
___
Line anti-aliasing slide uses information and images sourced from a CSCI 411 report on line drawing algorithms: https://github.com/szakal-byt3/line-drawing/tree/main.
___
Some of the images in the presentation are screenshots of a CSCI 566 assignment that was modified to disable/enable MSAA and use PCF. This code can be found under `webGL-example`. To run this, just open `gallery.html` with a browser that supports WebGL 1.0 or later. To load local files, you may need to either disable browser security or set up an HTTP server. For the latter option, Python can be used to easily do this if available. Simply navigate to the `webGL-example` directory, run `python -m http.server`, then go to `localhost:<PORT>` and click on `gallery.html`. 

Skybox images are by vladislavzh: https://opengameart.org/content/retro-skyboxes-pack. Models are my own.
