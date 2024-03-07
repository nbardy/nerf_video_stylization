## Neural Video Stylization
A github repo to collect style nerf code, video nerf code, and add the devops to make it all runnable.

1) Add a style loss
2) Add a geometry loss
3) Use CLIP for style instead of VGG

Taking inspiration from below we train a pair of networks to do style and realistic rendering. We use propose to use a LORA to train the style output. We also use CLIP instead of VGG to add text guidance

https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136910701.pdf
Take: (Multiple Models)
Leave: Feature Matching, Copy the whole net(Use LORA)
Add: Use CLIP instead of VGG

2) Geometry Loss
- Add a loss for the Depth of the image matching the original with MIDAS
- Add a depth style loss for the style output that takes an input image or a tet and uses CLIP instead of VGG

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
