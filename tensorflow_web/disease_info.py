class DiseaseInfo(object):
    def __init__(self, disease):
        self.disease = disease

    def get_disease_info(self):
        disease_list = {
            'apple frogeye spot': 'Frogeye leaf spot resembles a frog eye, as the name says, appearing as a light brown circular spot surrounded by a darker brown ring and a purple halo. The circles are usually 1/8 to 1/4 inch in diameter. Sometimes other fungi invade, enlarging the circles and causing them to look irregular. In older leaf spots, tiny reproductive centers, called pycnidia, emerge. In this case, observation through a magnifying glass reveals a tiny black pimple-like structure that contains more fungus spores, which will cause further infection.',
            'apple apple scab': 'Apple scab is a foliar fungal disease caused by Venturia inaequalis. It is not considered a serious threat to crabapple or apple trees; however, repeated annual apple scab infections can weaken the tree making it more susceptible to other insect or disease problems. Apple scab can seriously reduce the aesthetic quality of apple trees; heavy infections can reduce growth, vigor, flowering and apple yields. Apple scab is dependent on cool, wet weather to develop.',
            'apple cedar apple rust': 'Cedar-Apple Rust disease is a very common disease which affects cedar trees, junipers and apple trees. It is unique because in order for it to perpetuate itself, it must alternate between an apple tree and a cedar or juniper tree. It is therefore important to treat all apple trees, junipers and cedar trees in an area, regardless of whether they are yet showing symptoms.',
            'apple healthy': 'Your apple leaf is healthy. To learn more on how to take care and improve apple production, click the \'Learn more\' button below.',
            'blueberry healthy': 'Your blueberry leaf is healthy. To learn more on how to take care and improve blueberry production, click the \'Learn more\' button below.',
            'cherry including sour powdery mildew': 'Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface. Season long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard and consequently to protect developing fruit from accumulating spores on their surfaces.',
            'cherry including sour healthy': 'Your cherry leaf is healthy. To learn more on how to take care and improve cherry production, click the \'Learn more\' button below.',
            'corn maize cercospora leaf spot gray leaf spot': '',
            'corn maize common rust': '',
            'corn maize northern leaf blight': '',
            'corn maize healthy': 'Your corn maize leaf is healthy. To learn more on how to take care and improve corn maize production, click the \'Learn more\' button below.',
            'grape black rot': '',
            'grape esca black measles': '',
            'grape leaf blight isariopsis leaf spot': '',
            'grape healthy': 'Your grape leaf is healthy. To learn more on how to take care and improve grape production, click the \'Learn more\' button below.',
            'orange haunglongbing citrus greening': '',
            'peach bacterial spot': '',
            'peach healthy': 'Your peach leaf is healthy. To learn more on how to take care and improve peach production, click the \'Learn more\' button below.',
            'pepper bell bacterial spot': '',
            'pepper bell healthy': 'Your pepper bell leaf is healthy. To learn more on how to take care and improve pepper bell production, click the \'Learn more\' button below.',
            'potato early blight': '',
            'potato late blight': '',
            'potato healthy': 'Your potato leaf is healthy. To learn more on how to take care and improve potato production, click the \'Learn more\' button below.',
            'raspberry healthy': '',
            'soybean healthy': 'Your soybean leaf is healthy. To learn more on how to take care and improve soybean production, click the \'Learn more\' button below.',
            'squash powdery mildew': '',
            'strawberry leaf scorch': '',
            'strawberry healthy': '',
            'tomato bacterial spot': '',
            'tomato early blight': '',
            'tomato late blight': '',
            'tomato leaf mold': '',
            'tomato septoria leaf spot': '',
            'tomato spider mites two spotted spider mite': '',
            'tomato target spot': '',
            'tomato tomato yellow leaf curl virus': '',
            'tomato tomato mosaic virus': '',
            'tomato healthy': '',
        }

        disease_info = disease_list.get(self.disease)

        return disease_info

    def get_disease_info_url(self):
        disease_list = {
            'apple frogeye spot': 'http://homeguides.sfgate.com/frogeye-leaf-spot-apple-trees-54984.html/',
            'apple apple scab': 'https://www.thetreegeek.com/problems/apple-scab/',
            'apple cedar apple rust': 'https://www.treehelp.com/cedar-apple-rust/',
            'apple healthy': 'https://content.ces.ncsu.edu/growing-apple-trees-in-the-home-garden/',
            'blueberry healthy': 'https://www.gardeningknowhow.com/edible/fruits/blueberries/growing-blueberry.htm/',
            'cherry including sour powdery mildew': 'http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/',
            'cherry including sour healthy': '',
            'corn maize cercospora leaf spot gray leaf spot': '',
            'corn maize common rust': '',
            'corn maize northern leaf blight': '',
            'corn maize healthy': 'https://www.thespruce.com/growing-garden-fresh-sweet-corn-1402816/',
            'grape black rot': '',
            'grape esca black measles': '',
            'grape leaf blight isariopsis leaf spot': '',
            'grape healthy': '',
            'orange haunglongbing citrus greening': '',
            'peach bacterial spot': '',
            'peach healthy': '',
            'pepper bell bacterial spot': '',
            'pepper bell healthy': '',
            'potato early blight': '',
            'potato late blight': '',
            'potato healthy': '',
            'raspberry healthy': '',
            'soybean healthy': 'https://www.gardeningknowhow.com/edible/vegetables/soybean/soybean-growing-information.htm/',
            'squash powdery mildew': '',
            'strawberry leaf scorch': '',
            'strawberry healthy': '',
            'tomato bacterial spot': '',
            'tomato early blight': '',
            'tomato late blight': '',
            'tomato leaf mold': '',
            'tomato septoria leaf spot': '',
            'tomato spider mites two spotted spider mite': '',
            'tomato target spot': '',
            'tomato tomato yellow leaf curl virus': '',
            'tomato tomato mosaic virus': '',
            'tomato healthy': '',
        }

        disease_info_url = disease_list.get(self.disease)

        return disease_info_url
