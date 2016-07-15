Title: Neural Network for Object Detection
Date: 2016-7-13 15:14
Category: machine learning
Tags:
Slug: neural-network-for-object-detection
Authors:

For years, neural network has always been mystic to me and I never thought that I would do serious learning in this area until recently. I encountered an awesome book [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen. The book is written in an narrative way and quite interesting to read. After spending several days digesting most content from the book, I am equipped with essential tools to explore neural networks. Hence, in this blog let me discuss how to do object detection with neural networks and deep learning. 
<!-- PELICAN_END_SUMMARY -->

Foremost, big acknowledgment to [Michael Nielsen](http://michaelnielsen.org/) for enormous dedication to his book on [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) and generously making it freely accessible to everyone. To me, it is much more than a free book. Not quite like many other books you can find, it describes every classical element you need to know about neural networks in a way that it is made easiest possible for understanding. Before jumping into the content, please do checkout [What this book is about](http://neuralnetworksanddeeplearning.com/about.html) where you will also get an idea on the approaches adopted to help you understand the fundamentals both in theory and practice, and the philosophy advocated by the author:

> Technologies come and technologies go, but insight is forever.

####Neural networks for image recognition/classification
Not until recently, research and development in neural networks has proven powerful in solving vision problems like image classification. You probably heard that "deep" neural networks are great. While it's true that networks are usually deep for image classification, they also adopt a particular type of architecture different from the conventional one, which is called [convolutional networks](http://neuralnetworksanddeeplearning.com/chap6.html#introducing_convolutional_networks), or deep convolutional networks. 

In classifying handwritten digits from the MNIST data set, Michael showed that using one convolutional-pooling layer, accuracy rate is considerably improved to 98.78 percent versus 97.80 percent by a conventional shallow network. Furthermore, a second convolutional-pooling layer gets the accuracy to 99.06 percent. Some additional steps are found to yield even better results, that include using rectified linear units, expanding the training data, inserting an extra fully-connected layer and apply dropout, using an ensemble of networks. After all these steps, a 99.67 percent accuracy is achieved. Getting to a satisfying accuracy is more of an experimentation, and I am sure it helps to visit [Chapter 3 Improving the way neural networks learn](http://neuralnetworksanddeeplearning.com/chap3.html) back and forth. 

####Google's TensorFlow
You would be able to find some popular deep learning software. But according to Google senior fellow Jeff Dean, "There are currently 1500 repositories on GitHub which mention TensorFlow". I will choose TensorFlow for my image classification and object detection task. 

There are good tutorials about TensorFlow. To get hands on experience with constructing convolutional neural network, check out [Deep MNIST for Experts](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/pros/index.html#deep-mnist-for-experts). 
