EXML WS23/24 Uni Bonn - Explainable Machine Learinig Seminar: Planet-V2
by Titus Henkelmann, Jakob Weigand and Adrian Weng in February 2024 

# Concept discovery of Planet-V2 using Superpixel and Sliding BlackBox

Beschreibung des Projektes goes here


# Requirements

We used the given model from [Kaggle](https://www.kaggle.com/models/google/planet-v2), which is free avaliable.

# Sliding BlackBox
Konzept erklären

# Superpixel
The idea behind superpixels is similar to that of the [Sliding BlackBox](https://github.com/s7jaweig/EXML-WS-23-24---Planet-V2/edit/main/README.md#sliding-blackbox). The image is first divided into superpixels. Superpixels are similar regions within an image, such as the sky, buildings or vegetation. A single image is divided into around 15 superpixels, the exact number depending on the context being displayed. The aim is to be able to make a statement about which region has a particularly strong influence on the final result.
The Planet is applied to the original image. The result is the geocell for which the output is maximum. The network is then applied to each superpixel. Only the geocell with the corresponding score for which the original image produced the maximum output is of interest as the output. The scores are scored to be compared. This makes it possible to determine which area of the image had a particularly large influence on the result of the original image. For a better understanding of the results, the score values of the superpixels are scaled to the range 0 to 255 and displayed in colour in the image. 

# Data
Worauf haben wir getestet vorstellen

# Ergebnisse
## Ergebnisse für BlackBox

## Ergebnisse für Superpixels

# Zusammenfassung

# Referenzen

* https://www.kaggle.com/models/google/planet-v2
* Weyand, T., Kostrikov, I., & Philbin, J. (2016). Planet-photo geolocation with convolutional neural networks. In Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part VIII 14 (pp. 37-55). Springer International Publishing.
  
