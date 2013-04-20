from SimpleCV import KNNClassifier
from SimpleCV import BOFFeatureExtractor
extractor = BOFFeatureExtractor()
classifier = KNNClassifier([extractor])
classifier.train(["training_dataset/2005__cabarnet_sauvignon__dry_creek_valley"],
                 ["2005__cabarnet_sauvignon__dry_creek_valley"])
