import Augmentor
p = Augmentor.Pipeline("C:\\Users\\Ehtisham Ali\\OneDrive\\Desktop\\Screenshots")
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.sample(500)
p.process()
