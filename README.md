# ai-zipper
ai-zipper offers numerous AI model(CNN) compression methods, also it is easy to embed into your own source code

## Version 0.0.1

### What is ai-zipper?
- ai-zipper offers several AI-Optimization and/or Model-Compression methods for CNN based networks
    - List of methods that will be offered later:
        - [ ] Quantization
        - [ ] Unstructured Pruning
        - [ ] Structured Pruning
        - [ ] Knowledge Distillation
        - [ ] ...and more

### Why Do I Need ai-zipper?
- You need ai-zipper when your model(network) is exceptionally slow, or too big to put into your system
- ai-zipper reduces the size of your convolutional network, and improves inference latency

### How does it work?
- List below shows which package is used for specific methods:
    - <b>Quantization:</b>
        - ai-zipper uses [Tensorflow Lite](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite) to offer Quantization
    - <b>Other methods will be posted later...</b>

### How Can I Use ai-zipper?
- Downloading through PyPI will be supported later...
- ai-zipper offers easy-to-import APIs for each methods.
    - It also gives one-shot method for beginners (which will be supported later)