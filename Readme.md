## Neural Video Stylization
A github repo with two goals:
1. Add the devops to Make NERFs easy to generate with a single 
2. Add stylization code from other NERF repos


### Plan
#### Devops Code [1]:
Get three apple neumann scripts working to preprocess, train, and render.
(Should run on modal or colab to be easily reusable and avoid dependancy issues)


#### Style Code [2]:
1) Add a style loss
2) Add a geometry loss
3) Use CLIP for style instead of VGG

Taking inspiration from ARF[1] we train a pair of networks to do style and realistic rendering. We use a LORA to train the style output instead of a new model.

[1] https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136910701.pdf

2) Geometry Loss
- Add a loss for the Depth of the image matching the original with MIDAS
- Add a depth style loss with CLIP

Reference:
https://hyblue.github.io/geo-srf/

### Progress:
#### Fullstack/Devops Code
- [🚧] apple Neumann preprocessing working on Modal
- [ ] Train running on modal
- [ ] Inference running on modal
### Research Code
- [ ] Add Style Loss
- [ ] Add Geometry/Depth Loss
