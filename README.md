EXML WS23/24 Uni Bonn - Explainable Machine Learinig Seminar: Planet-V2
by Titus Henkelmann, Jakob Weigand and Adrian Weng in February 2024 

# Concept discovery of Planet-V2 using Superpixel and Sliding BlackBox

Beschreibung des Projektes goes here

# Workflow
![chart drawio](https://github.com/s7jaweig/EXML-WS-23-24---Planet-V2/assets/131247050/b0e1aa5c-247d-44a6-84dc-a50884da603d)


# Requirements

We used the given model from [Kaggle](https://www.kaggle.com/models/google/planet-v2), which is free avaliable.

# Sliding BlackBox
Konzept erklären

# Superpixel
The idea behind superpixels is similar to that of the [Sliding BlackBox](https://github.com/s7jaweig/EXML-WS-23-24---Planet-V2/tree/main?tab=readme-ov-file#sliding-blackbox). The image is first divided into superpixels. Superpixels are similar regions within an image, such as the sky, buildings or vegetation. A single image is divided into around 15 superpixels, the exact number depending on the context being displayed. The aim is to be able to make a statement about which region has a particularly strong influence on the final result.
The Planet is applied to the original image. The result is the geocell for which the output is maximum. The network is then applied to each superpixel. Only the geocell with the corresponding score for which the original image produced the maximum output is of interest as the output. The scores are scored to be compared. This makes it possible to determine which area of the image had a particularly large influence on the result of the original image. For a better understanding of the results, the score values of the superpixels are scaled to the range 0 to 255 and displayed in colour in the image. 

Alternativ:
The concept of superpixels is akin to that of the [Sliding BlackBox](https://github.com/s7jaweig/EXML-WS-23-24---Planet-V2/tree/main?tab=readme-ov-file#sliding-blackbox).  The image is initially partitioned into superpixels, which are regions of similarity within an image, such as the sky, buildings, or vegetation. Typically, an image is divided into approximately 15 superpixels, although the exact number depends on the context being depicted. The objective is to identify which region has a significant impact on the final outcome. The Planet is then applied to the original image.  The geocell with the highest output is identified and applied to each superpixel. Only the geocell with the corresponding score that produced the maximum output for the original image is of interest. The scores are then compared to determine which area of the image had a significant impact on the original image's result. To enhance comprehension of the results, the score values of the superpixels are scaled to a range of 0 to 255 and displayed in colour within the image.

# Data
Worauf haben wir getestet vorstellen

# Ergebnisse
## Ergebnisse für BlackBox

## Ergebnisse für Superpixels

# Zusammenfassung

# Referenzen

* https://www.kaggle.com/models/google/planet-v2
* Weyand, T., Kostrikov, I., & Philbin, J. (2016). Planet-photo geolocation with convolutional neural networks. In Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part VIII 14 (pp. 37-55). Springer International Publishing.
  
