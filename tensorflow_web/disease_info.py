class DiseaseInfo(object):
    def __init__(self, disease):
        self.disease = disease

    def get_disease_info(self):
        disease_list_desc = {
            'apple frogeye spot': 'Frogeye leaf spot resembles a frog eye, as the name says, appearing as a light brown circular spot surrounded by a darker brown ring and a purple halo. The circles are usually 1/8 to 1/4 inch in diameter. Sometimes other fungi invade, enlarging the circles and causing them to look irregular. In older leaf spots, tiny reproductive centers, called pycnidia, emerge. In this case, observation through a magnifying glass reveals a tiny black pimple-like structure that contains more fungus spores, which will cause further infection.',
            'apple apple scab': 'Apple scab is a foliar fungal disease caused by Venturia inaequalis. It is not considered a serious threat to crabapple or apple trees; however, repeated annual apple scab infections can weaken the tree making it more susceptible to other insect or disease problems. Apple scab can seriously reduce the aesthetic quality of apple trees; heavy infections can reduce growth, vigor, flowering and apple yields. Apple scab is dependent on cool, wet weather to develop.',
            'apple cedar apple rust': 'Cedar-Apple Rust disease is a very common disease which affects cedar trees, junipers and apple trees. It is unique because in order for it to perpetuate itself, it must alternate between an apple tree and a cedar or juniper tree. It is therefore important to treat all apple trees, junipers and cedar trees in an area, regardless of whether they are yet showing symptoms.',
            'apple healthy': 'Your apple leaf is healthy. To learn more on how to take care and improve apple production, click the \'Learn more\' button below.',
            'blueberry healthy': 'Your blueberry leaf is healthy. To learn more on how to take care and improve blueberry production, click the \'Learn more\' button below.',
            'cherry including sour powdery mildew': 'Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface. Season long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard and consequently to protect developing fruit from accumulating spores on their surfaces.',
            'cherry including sour healthy': 'Your cherry leaf is healthy. To learn more on how to take care and improve cherry production, click the \'Learn more\' button below.',
            'corn maize cercospora leaf spot gray leaf spot': 'Symptoms of gray leaf spot are usually first noticed in the lower leaves. Initially, lesions of gray leaf spot begin as a small dot with a yellow halo. Lesions will elongate over time running parallel to the veins becoming pale brown to gray and rectangular in shape with blunt ends. These lesions can be described as having the appearance of a “matchstick”. Lesions may eventually coalesce killing the leaves. Leaves appear grayish in color due to the presence of fungal spores.',
            'corn maize common rust': 'Common rust of maize (P. sorghi) is characterized by the presence of golden-brown to cinnamon-brown pustules (uredinial) that can develop on any above-ground plant part including leaves, husks, tassels and stalks. The uredinia are circular to elongate, and develop with approximately equal frequency on the upper and lower leaf surfaces. The initial symptom is the formation of small chlorotic areas. As the uredinia develop they become erumpent, pushing up the epidermal tissue which eventually splits open to expose masses of powdery urediniospores. Spores often collect in and infect the whorls of the plants resulting in a band of infection across the leaf. On varieties containing genes for the production of anthocyanin pigments, the uredinia may be surrounded by a purple halo. When the disease is severe, large areas of the leaves and leaf sheaths can become first chlorotic then necrotic.',
            'corn maize northern leaf blight': 'Northern corn leaf blight (NCLB) is a foliar disease of corn (maize) caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica. With its characteristic cigar-shaped lesions, this disease can cause significant yield loss in susceptible corn hybrids. There are several host-specific forms of E. turcicum. The most economically important host is corn, but other forms may infect sorghum, Johnson grass, or sudangrass. The most common diagnostic symptom of the disease on corn is cigar-shaped or elliptical necrotic gray-green lesions on the leaves that range from one to seven inches long. These lesions may first appear as narrow, tan streaks that run parallel to the leaf veins. Fully developed lesions typically have a sooty appearance during humid weather, as a result of spore (conidia) formation.',
            'corn maize healthy': 'Your corn maize leaf is healthy. To learn more on how to take care and improve corn maize production, click the \'Learn more\' button below.',
            'grape black rot': 'Grape black rot is a fungal disease caused by an ascomycetous fungus, Guignardia bidwellii, that attacks grape vines during hot and humid weather. Grape black rot originated in eastern North America, but now occurs in portions of Europe, South America, and Asia. It can cause complete crop loss in warm, humid climates, but is virtually unknown in regions with arid summers. The name comes from the black fringe that borders growing brown patches on the leaves. The disease also attacks other parts of the plant, all green parts of the vine: the shoots, leaf and fruit stems, tendrils, and fruit. The most damaging effect is to the fruit.',
            'grape esca black measles': 'Grapevine measles, also called esca, black measles or Spanish measles, has long plagued grape growers with its cryptic expression of symptoms and, for a long time, a lack of identifiable causal organism(s). The name ‘measles’ refers to the superficial spots found on the fruit. During the season, the spots may coalesce over the skin surface, making berries black in appearance. Spotting can develop anytime between fruit set and a few days prior to harvest. Berries affected at fruit set tend not to mature and will shrivel and dry up. In addition to spotting, fruit affected later in the season will also have an acrid taste.',
            'grape leaf blight isariopsis leaf spot': 'On leaf surface we will see lesions which are irregularly shaped (2 to 25 mm in diameter). Initially lesions are dull red to brown in color turn black later. If disease is severe this lesions may coalesce. On berries we can see symptom similar to black rot but the entire clusters will collapse. Common in tropical and subtropical grapes. The disease appear late in the season. Cynthiana and Cabernet Sauvignon are susceptible to this pathogen.',
            'grape healthy': 'Your grape leaf is healthy. To learn more on how to take care and improve grape production, click the \'Learn more\' button below.',
            'orange haunglongbing citrus greening': 'Citrus greening disease (haunglongbìng or HLB), is a disease of citrus caused by a vector-transmitted pathogen. The causative agents are motile bacteria, Candidatus Liberibacter spp. The disease is vectored and transmitted by the Asian citrus psyllid, Diaphorina citri, and the African citrus psyllid, Trioza erytreae, also known as the two-spotted citrus psyllid. It has also been shown to be graft-transmissible. Three different types of HLB are currently known: The heat-tolerant Asian form, and the heat-sensitive African and American forms. The disease was first described in 1929 and first reported in China in 1943. The African variation was first reported in 1947 in South Africa, where it is still widespread. Eventually, it affected the United States, reaching Florida in 2005.',
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
            'strawberry healthy': 'Your strawberry leaf is healthy. To learn more on how to take care and improve strawberry production, click the \'Learn more\' button below.',
            'tomato bacterial spot': '',
            'tomato early blight': '',
            'tomato late blight': '',
            'tomato leaf mold': '',
            'tomato septoria leaf spot': '',
            'tomato spider mites two spotted spider mite': '',
            'tomato target spot': '',
            'tomato tomato yellow leaf curl virus': '',
            'tomato tomato mosaic virus': '',
            'tomato healthy': 'Your tomato leaf is healthy. To learn more on how to take care and improve tomato production, click the \'Learn more\' button below.',
        }

        disease_info = disease_list_desc.get(self.disease)

        return disease_info

    def get_disease_info_url(self):
        disease_list_url = {
            'apple frogeye spot': 'http://homeguides.sfgate.com/frogeye-leaf-spot-apple-trees-54984.html/',
            'apple apple scab': 'https://www.thetreegeek.com/problems/apple-scab/',
            'apple cedar apple rust': 'https://www.treehelp.com/cedar-apple-rust/',
            'apple healthy': 'https://content.ces.ncsu.edu/growing-apple-trees-in-the-home-garden/',
            'blueberry healthy': 'https://www.gardeningknowhow.com/edible/fruits/blueberries/growing-blueberry.htm/',
            'cherry including sour powdery mildew': 'http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/',
            'cherry including sour healthy': 'https://www.almanac.com/plant/cherries/',
            'corn maize cercospora leaf spot gray leaf spot': 'https://fieldcrops.cals.cornell.edu/corn/diseases-corn/gray-leaf-spot/',
            'corn maize common rust': 'https://www.plantwise.org/KnowledgeBank/Datasheet.aspx?dsid=45872',
            'corn maize northern leaf blight': 'https://www.pioneer.com/home/site/us/agronomy/crop-management/corn-insect-disease/northern-leaf-blight/',
            'corn maize healthy': 'https://www.thespruce.com/growing-garden-fresh-sweet-corn-1402816/',
            'grape black rot': 'https://grapesandwine.cals.cornell.edu/newsletters/appellation-cornell/2014-newsletters/issue-17/managing-black-rot/',
            'grape esca black measles': 'http://articles.extension.org/pages/64365/grapevine-measles/',
            'grape leaf blight isariopsis leaf spot': 'https://www.researchgate.net/publication/263317429_The_control_of_isariopsis_leaf_spot_and_downy_mildew_in_grapevine_cv_Isabel_with_the_essential_oil_of_lemon_grass_and_the_activity_of_defensive_enzymes_in_response_to_the_essential_oil/',
            'grape healthy': '',
            'orange haunglongbing citrus greening': 'http://www.crec.ifas.ufl.edu/extension/greening/index.shtml/',
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

        disease_info_url = disease_list_url.get(self.disease)

        return disease_info_url
