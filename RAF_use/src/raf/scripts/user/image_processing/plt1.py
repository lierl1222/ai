#coding = utf-8
from dis import dis
import json
from re import S, T
import re
import rospy 
import math
import numpy as np
import cv2
import os


from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from tf_transformations import euler_from_quaternion



dlist = []

bflag = 0
flag = 0
res0 = {'x': [-4.905355364876086, -4.9052892078750165, -4.905171536379684, -4.905011307386576, -4.90476488382697, -4.904372123272603, -4.903827844951368, -4.903058945601719, -4.90202982927209, -4.90058569182865, -4.898755638190207, -4.8965234853584025, -4.893824136948747, -4.890764785095461, -4.887271307751793, -4.883340473849883, -4.879324024451644, -4.874817791442478, -4.869486473739313, -4.863934913208057, -4.8579712338764445, -4.851424282388534, -4.844635597151159, -4.83744110669612, -4.8296244727773665, -4.8216372862267916, -4.813280335651304, -4.804295827838447, -4.7952432486487995, -4.785868548806197, -4.775863435877771, -4.765940645463962, -4.755840140959174, -4.744887122506459, -4.733757726487652, -4.722400547867101, -4.710497876199959, -4.698610127239891, -4.686412249770103, -4.673613640987796, -4.660956024443632, -4.648043369596967, -4.634382609771926, -4.62074727399384, -4.60705610326557, -4.592645397360908, -4.578294409018474, -4.563749885666227, -4.548656208702876, -4.5338870119738495, -4.518816676117319, -4.503097671481142, -4.487680301562302, -4.472189269628147, -4.456163262942214, -4.4405275606064265, -4.424797016234383, -4.408510006148772, -4.392399277965912, -4.376108224410916, -4.3593846094919355, -4.343152998245634, -4.326777498800567, -4.309917626989703, -4.293551448792997, -4.277052631215328, -4.2600375016062575, -4.243502600473069, -4.226912792724432, -4.2098700308343115, -4.1933605430072225, -4.177070866880792, -4.160170674419772, -4.14387437328939, -4.127594158071501, -4.110889391797991, -4.094850721423588, -4.078863493998059, -4.062583742592521, -4.046947130822918, -4.031416811005523, -4.015557825789079, -4.000242079710595, -3.9850203572296343, -3.969435837439351, -3.954692681323747, -3.94015566792592, -3.9253348837367934, -3.9110844312746953, -3.896862420783392, -3.8824758497134604, -3.868947308310946, -3.855760580515901, -3.8424478545876584, -3.829735914735617, -3.817515893119402, -3.805228102494385, -3.793485465660547, -3.781853335012512, -3.7702761900239343, -3.759389310052198, -3.7488708542868014, -3.738383569480857, -3.7284313594925442, -3.7187356667453475, -3.7091770593608318, -3.7003360623735535, -3.691888114497649, -3.6835267283630837, -3.6758024418548776, -3.6684071556538305, -3.661156109566366, -3.654437511540362, -3.64805480284795, -3.6420694032661682, -3.6366664201672916, -3.6316049242377466, -3.6268208426950173, -3.622580049439736, -3.618753918452039, -3.615199881600271, -3.612196997832705, -3.609624124288791, -3.6073937736735617, -3.605663722566685, -3.6043270046089173, -3.6033840553705834, -3.602839285559544, -3.6024992641063194, -3.6026617231044917, -3.6034107546061453, -3.6046164395090576, -3.6062979678957174, -3.608294302097561, -3.6107119296578625, -3.6136736622641683, -3.616981437391857, -3.6205863751448137, -3.624704831152768, -3.629094697721126, -3.6338883678684764, -3.6393785796362894, -3.645093579631331, -3.6509612160201317, -3.6572632977540316, -3.663874992247427, -3.6712426981328887, -3.679103794129809, -3.6869170950821397, -3.695233146240264, -3.704302185919847, -3.7134171554012982, -3.7227173904713022, -3.7325159105764976, -3.742570666531533, -3.752999500522855, -3.764123086832357, -3.775332469691625, -3.7866623614446566, -3.798546760689565, -3.8102871062337087, -3.822570763458704, -3.8355421422264615, -3.8483342581886806, -3.861420259612851, -3.8751774290573406, -3.888837235142369, -3.902708877591277, -3.917056935168881, -3.9310866148897, -3.945404888102761, -3.9605045326088235, -3.97549747051691, -3.990619984835758, -4.006237972459674, -4.021492494088077, -4.036939204448249, -4.053074515424783, -4.068812660087164, -4.084576583612214, -4.1010022962018295, -4.117150543886461, -4.1334120227806075, -4.150180951964153, -4.1663825787518, -4.182566536312178, -4.199371740539709, -4.215829754282518, -4.23236486448594, -4.249315643172542, -4.265707961209748, -4.281948229924442, -4.298721917919408, -4.314978487394956, -4.331225598602523, -4.347965042895064, -4.364126338443309, -4.380246064488823, -4.396803359368052, -4.412817796488946, -4.42880079918482, -4.445133059035184, -4.4608242367710345, -4.47635453907315, -4.492197005995214, -4.507375324396945, -4.5223693542549395, -4.537580661658515, -4.552135732291162, -4.566488083538404, -4.581078978231415, -4.595039673252831, -4.608894007267187, -4.6227055414629445, -4.635918512078167, -4.648983063866818, -4.662160459606666, -4.674591388632758, -4.686765399685335, -4.698989295060248, -4.710510118710494, -4.721741915524509, -4.732971923930952, -4.743586563832117, -4.7540226673158, -4.764521943141555, -4.774165936767026, -4.783352082092223, -4.79243643657284, -4.800910277815859, -4.808978623018882, -4.81690027025689, -4.824201159661007, -4.831111414717645, -4.837829893635986, -4.843920066051357, -4.849624507078254, -4.855114922948077, -4.860035167158501, -4.8646337919492755, -4.869155449833713, -4.873038291667717, -4.876261561592185, -4.879163358969575, -4.881556402887636, -4.8835259820857475, -4.885120689493925, -4.886290406188784, -4.887029619778728, -4.887384028032549, -4.8873015450891435, -4.886682553968106, -4.885623353384132, -4.884170583466028, -4.88228990988743, -4.880009486422694, -4.877412583616943, -4.874237165631314, -4.870504355707961], 'y': [1.4616016874930515, 1.4739405948254416, 1.4868359678820784, 1.5007479399919426, 1.514742445803881, 1.5290784899831595, 1.5439592165287157, 1.5585686360533646, 1.5737268436489884, 1.5898816212000844, 1.6060231390789774, 1.6222001614864747, 1.6389615011254213, 1.6552551381920872, 1.6715134761321566, 1.6882816657831023, 1.7044113475597773, 1.7204199129633968, 1.7367405907612328, 1.7524022902070144, 1.7679594447990294, 1.7838069829427692, 1.7990269895032596, 1.8140926386832308, 1.8293949200345223, 1.844069836758421, 1.8585431531541354, 1.873175086639423, 1.887167197764007, 1.900898782041432, 1.9148000074086244, 1.9281599196425399, 1.9413545786660997, 1.9545692078349834, 1.9669746955804324, 1.9790635363693352, 1.9912453204333522, 2.0027069358483054, 2.0138464959561597, 2.025004855450517, 2.0354813742647337, 2.045704013652878, 2.0559045319095457, 2.065429022164096, 2.074688779942181, 2.0837020129181547, 2.0922500364892653, 2.1005811532568677, 2.108709154468375, 2.1160577540812535, 2.1229824373303625, 2.129719782220047, 2.1358285998597055, 2.1415986042784754, 2.1471103638183435, 2.152059133836465, 2.1567064354214995, 2.161117453872066, 2.1648773446638585, 2.168305213094535, 2.1715221231684327, 2.174161625598057, 2.1764222932823296, 2.178259000421311, 2.179613496279972, 2.1804782696391025, 2.1809070883134347, 2.180879495326319, 2.1804193242891583, 2.1796124105791903, 2.1783220358948374, 2.1767343985361167, 2.1749011018897324, 2.172615014570213, 2.1696885644828656, 2.1663359490890413, 2.1627006004596008, 2.15872880031083, 2.1541028014144965, 2.1492224155912587, 2.1438896680700568, 2.1379630431365126, 2.131793054212086, 2.125194504473334, 2.118090776559401, 2.1107724017141742, 2.1030272419216987, 2.094860106450737, 2.0867057111183533, 2.0781202261096645, 2.068721564992498, 2.059094890672527, 2.049281653787056, 2.0387920675648186, 2.0281852499387916, 2.017452278812442, 2.006166971618317, 1.9949416685392956, 1.9832181823012736, 1.9707320422924568, 1.9583317112835823, 1.9456970858449316, 1.932500572863495, 1.9195155514848872, 1.9064030571897916, 1.892395398727571, 1.8784914630100813, 1.864453296878487, 1.849728406938731, 1.8352444894780355, 1.8205131527465686, 1.805163364387618, 1.7902449327974586, 1.7752577973259214, 1.7595871298016494, 1.7440705297038257, 1.7282420273809338, 1.711919585960592, 1.6960978921100456, 1.6802572441899122, 1.6637688988035868, 1.6475740386038202, 1.6313843017812757, 1.6147258446924142, 1.5984029614774786, 1.5819438294020558, 1.5649287524440672, 1.548517537454469, 1.5322128358050109, 1.5154341043336037, 1.4990527162840195, 1.4825968196678516, 1.4656318208500763, 1.4493155203546988, 1.4331199564784314, 1.416496271676924, 1.4004605924665048, 1.3845053540662247, 1.368105571717472, 1.352267787635296, 1.3364969910102356, 1.3204499657969861, 1.3050608041056695, 1.2898019214505527, 1.2742457637244045, 1.2592241369559285, 1.24435148268563, 1.2293435275239712, 1.2149411242647394, 1.2007720602902028, 1.1864829310073302, 1.172864736561228, 1.1595337447233174, 1.1459280983346598, 1.1329244157906162, 1.1201942454718101, 1.1074094964132233, 1.0953304422039387, 1.0835838400919668, 1.0717230697545266, 1.060440351426325, 1.0495059900547166, 1.038668454014301, 1.0285054936262468, 1.0186475815016798, 1.008847511049549, 0.999637593801929, 0.9907670098284685, 0.9819242920963206, 0.9736731407412349, 0.9659669441804081, 0.9584219588836049, 0.9514419126795955, 0.9448425442484966, 0.9384665694262808, 0.9326723086477002, 0.9272202241351516, 0.9220538577471418, 0.9174630713465739, 0.913284628058098, 0.9094158326832479, 0.9060510083712227, 0.9031003686233693, 0.9004394081597084, 0.8980806185303158, 0.896227491173584, 0.8949033731331203, 0.8940693393816889, 0.8936534994184403, 0.8936310760725266, 0.8939980094859399, 0.8948022922696023, 0.896109040057697, 0.8977872206402454, 0.8998266397388328, 0.902393177447385, 0.9053373363012218, 0.9087730196301788, 0.9127385643954335, 0.9168633894290574, 0.9213272867129427, 0.926597144901187, 0.9321644403751695, 0.9381045313227033, 0.94466564643573, 0.9514031129868421, 0.9585351858069991, 0.9661464775868193, 0.9738286428496368, 0.9817222363627583, 0.9903630364206435, 0.9991990246583466, 1.0082988762506515, 1.0181834632412563, 1.0281035818327346, 1.038348063722558, 1.049328835967723, 1.0604328797308724, 1.0718934868781, 1.084014607477549, 1.0960602233370202, 1.1083579619423345, 1.1212854864643829, 1.134062680726954, 1.1469561995699047, 1.160458404167299, 1.1740404458672185, 1.187929680160004, 1.2024721834587482, 1.216800223011619, 1.231362296818922, 1.2466286354455407, 1.2616454169887608, 1.276847658835928, 1.292700864382657, 1.3082132654636258, 1.3238741697874663, 1.3401176889979438, 1.3560068232892089, 1.371993315408887, 1.3884837361950568, 1.4046559556318097, 1.4210125262655084, 1.437920756032028, 1.4543964187054603, 1.4708629329893368, 1.4878456719680448, 1.504342031002066, 1.5208680912114887, 1.537918702865396, 1.5545238901905631, 1.5711353655936529, 1.5882730349053957, 1.6048732338640586, 1.6214435951839843, 1.6384433921115944, 1.6548986073127903, 1.6712744185673654, 1.6880848272073445]}

res1={'x': [-2.0136285245896195, -2.0204615126972927, -2.0275011065994586, -2.0352832823987077, -2.0442242944322984, -2.053623312631424, -2.063545287607474, -2.0744749899181216, -2.0857878165686845, -2.0976625712726014, -2.11019077432331, -2.1226706106029902, -2.135478918620066, -2.1492469850980145, -2.163189529519841, -2.17751757203039, -2.192395845137311, -2.20709469456237, -2.2223100954581785, -2.2386180055151326, -2.254870327620361, -2.27119457075822, -2.288141144534158, -2.3046258850356844, -2.3210628280410837, -2.3381202119198603, -2.3546256344407643, -2.371015814870123, -2.387856184353576, -2.4041241840777547, -2.420304189769445, -2.4368622251206777, -2.4527776886460257, -2.468573048305705, -2.4846995156217653, -2.5002195329226193, -2.515564850549446, -2.53114868028725, -2.5461186159791893, -2.5608571770909436, -2.5758695230177877, -2.5903592741928243, -2.6046284404318, -2.619012785457204, -2.6326512965331217, -2.6460308298999293, -2.659581281213824, -2.6724116224230166, -2.684985379786761, -2.6976556263132276, -2.709625004050984, -2.7213149164944825, -2.732985775087208, -2.7440070790730244, -2.754751046943492, -2.7654639403630688, -2.775588072111116, -2.7854654323808377, -2.795230517797135, -2.804196168745558, -2.8127973970232256, -2.821274205013282, -2.8290971470150437, -2.8365489600171205, -2.8438760460326487, -2.850625901912873, -2.8570159746177617, -2.863203609482843, -2.868681596638651, -2.8738223288023215, -2.8786296828729117, -2.8829163829241584, -2.8868510515723695, -2.8904574441020774, -2.893452855563454, -2.8959855544875976, -2.89815441870941, -2.8998159952468514, -2.9010576855911583, -2.901950372565895, -2.902400104667632, -2.9024436361374537, -2.902232558015854, -2.90146333189328, -2.9001836905742313, -2.8985057282476374, -2.8963553925703382, -2.8937634622825663, -2.890748512576598, -2.8873826720698648, -2.883574522240444, -2.879208849507581, -2.87455268697244, -2.8694343348914257, -2.863874272361227, -2.8580883853781685, -2.851872506738374, -2.8453051098975877, -2.838684635963921, -2.8314843425551204, -2.8234707099725194, -2.81529659245486, -2.806731885543735, -2.797602282960828, -2.7883310671150277, -2.7788459823236225, -2.7686862058615587, -2.758491402776459, -2.7479325364682246, -2.7366346907095345, -2.7254865646950885, -2.714007632552587, -2.701902085096941, -2.6899457296064333, -2.6776683989241015, -2.6645548350316544, -2.65154031413749, -2.6382529623490716, -2.6242884891172635, -2.6105406537976643, -2.5965358130323244, -2.5819616577786957, -2.567694029477321, -2.5532469546104326, -2.5379749991515155, -2.5230386765616557, -2.507931561918415, -2.492242782836429, -2.476840885546214, -2.4612913061861392, -2.4451142292891612, -2.4292463766099868, -2.413223241537411, -2.396593210828233, -2.380406081043412, -2.3641374883513975, -2.34726702955381, -2.330872038692727, -2.314430322091963, -2.2973448723460166, -2.2807283374768237, -2.2642028733454014, -2.2471819114310625, -2.230775250706398, -2.2143612926829284, -2.1974051269944592, -2.181069800354265, -2.164702559458111, -2.1478830511895954, -2.1316452571307125, -2.115425507753075, -2.098883310740711, -2.0829221743440374, -2.067078513031275, -2.0507268498499025, -2.03502747279146, -2.019417968842065, -2.0036040194643996, -1.9884181588054841, -1.9734544832705725, -1.9582359212507408, -1.9437906313474247, -1.929487246431124, -1.9150272644077668, -1.9009998175130862, -1.8872582007528107, -1.87332232961041, -1.8600839424537963, -1.847144856205168, -1.8340825969131993, -1.8215483381570485, -1.809354678066694, -1.7971606484378921, -1.7855840116446757, -1.7742714993602422, -1.7630468673132949, -1.7524661641513433, -1.74218914367375, -1.7318646723512627, -1.7221448168142053, -1.712822958818049, -1.7036122394088982, -1.6950811028396813, -1.686961505199448, -1.6788962331439545, -1.671395561734437, -1.664255710867107, -1.6573781120571245, -1.6511258855691726, -1.6452211965236205, -1.6395904921515858, -1.6344897524456978, -1.6298817662432754, -1.6254584644697019, -1.621368288232467, -1.6178180147728185, -1.6146442507895677, -1.6120519297825928, -1.6098885679053871, -1.6080694262916673, -1.6067159289968305, -1.6057746886660011, -1.6052854766249867, -1.605240410538506, -1.6056010119012645, -1.6064681032477786, -1.607563143725497, -1.6091782247247117, -1.6111972813519593, -1.6133543336251812, -1.615919555101001, -1.6192024660585669, -1.622977285697442, -1.6271061505161264, -1.6316010974992627, -1.6364979698892104, -1.641903869643664, -1.647792274129854, -1.6538223712771953, -1.6601951939157842, -1.6672591612587755, -1.6745356301336007, -1.6820842655147863, -1.6904531490156451, -1.698818346484883, -1.70743346845961, -1.7166571421498302, -1.7261949942128192, -1.7361564701984311, -1.7468322949540878, -1.7575650116274442, -1.7686146574715194, -1.7802460534980251, -1.791784998721549, -1.8034609663154055, -1.8158168941250161, -1.8283533154554743, -1.84116504504515, -1.8546253252557656, -1.868010104817735, -1.8815902531201976, -1.8959060403423518, -1.9100358544309683, -1.924411545550665, -1.939450357362994, -1.954218559393167, -1.9691802128057323, -1.9847178023522027, -1.9999498938047493, -2.015247865156501, -2.031099447584042, -2.0467584239484475, -2.0626797908869414, -2.07919859037573, -2.0953472630812513, -2.1115895312910955, -2.12844411395824], 'y': [-2.6048137964595024, -2.6053474842348905, -2.6059059325232723, -2.6065264781683766, -2.6072213881118125, -2.6080302633083052, -2.608932847719627, -2.6099738688178014, -2.611099650378434, -2.612316388161767, -2.613566851768041, -2.6148787958664137, -2.6162237616786146, -2.6176263195145832, -2.6189560506750946, -2.6201854781285334, -2.621298269323548, -2.622213196865926, -2.6229339570916643, -2.6233933540909953, -2.6234728961461355, -2.6232116563816814, -2.622488638907269, -2.621375100045994, -2.619907095600894, -2.6179435182911757, -2.6157568107514573, -2.6130189988449275, -2.609638300119991, -2.6059518899165606, -2.6018582931295215, -2.597184460210497, -2.5922304295976675, -2.586863927988794, -2.5809012227833765, -2.574696494640318, -2.568147377928642, -2.56095303759494, -2.5535855886362886, -2.5459026017892716, -2.537620170084776, -2.5293790517635575, -2.5209338324512602, -2.511583161856764, -2.5019670347406513, -2.492068286339657, -2.48145498197181, -2.470803908986422, -2.4598137054386453, -2.4481729066300644, -2.436548836858766, -2.4246464603480984, -2.412072549955382, -2.399568092398852, -2.38683021956078, -2.3734277353735997, -2.3601273675920944, -2.346758268826318, -2.332687124975796, -2.3186216096449015, -2.3042754374115226, -2.2892699349014025, -2.274527987115525, -2.259590173866785, -2.2440542409462796, -2.228780848894684, -2.2133672577266137, -2.197376093420328, -2.18167901032858, -2.165836834830431, -2.149364099193418, -2.133270772068389, -2.1171089122824926, -2.100352769416225, -2.083945037358079, -2.067423526871036, -2.0503315224290724, -2.033731939623259, -2.0171032129303126, -1.999948121354705, -1.983302345856154, -1.9666137286803784, -1.949438494822542, -1.9328040015545573, -1.9161724089249905, -1.8991879590042127, -1.8826855791876331, -1.866272575492354, -1.8494856294949216, -1.8331699572802354, -1.8169696220759666, -1.8003550898234704, -1.7843443896460145, -1.7684806234044015, -1.752270213612294, -1.736818157106654, -1.7214476658653977, -1.7056921372617677, -1.690534089223899, -1.6755640748122462, -1.660420913539031, -1.6459629347896705, -1.6317098146186664, -1.6173000301309182, -1.603543642211481, -1.5900946756651237, -1.5764415427994802, -1.5633779607737106, -1.550566783456708, -1.5377308975159538, -1.5256266739832096, -1.5137770962534884, -1.5018302851152339, -1.4903889275527598, -1.4792113221901444, -1.468266733347493, -1.4579651705047862, -1.4480343004455745, -1.4382027385850853, -1.4289623795395356, -1.4201152042960867, -1.4113216761201717, -1.4030395614691966, -1.395101371423003, -1.3873631721308466, -1.3803231563745064, -1.3736936379991025, -1.3672268663905325, -1.3612774225782056, -1.3556566994566248, -1.3503464308544568, -1.3457290716772026, -1.3415168406294307, -1.3376035809486135, -1.3341970279248065, -1.331220556609378, -1.328641172023166, -1.326442806674339, -1.3244608292634157, -1.322997638322145, -1.322173088871876, -1.3216767251968249, -1.3216531043799558, -1.3219785061981706, -1.322736882920972, -1.3239506242545451, -1.3256135357284744, -1.3275963902242958, -1.3299815129635968, -1.332879304574996, -1.3361839440021357, -1.3399843156852715, -1.3441490529260536, -1.3485222448325827, -1.3533315759591642, -1.3586031704751258, -1.364399124346322, -1.3707687428042294, -1.377157630522144, -1.3840082693572118, -1.3915259603333552, -1.3990925158908203, -1.4068601220397234, -1.4151890489333299, -1.423827634580692, -1.4327248271620623, -1.442305059955568, -1.4521810572927245, -1.4622663383131742, -1.4728031337112133, -1.483429179201049, -1.49453278393208, -1.5064150063305317, -1.5181939172940535, -1.5302173318053016, -1.542995039600056, -1.5556648174323646, -1.5685508349025723, -1.581950517659234, -1.5952284051998096, -1.6089260137306252, -1.6231731988259355, -1.637337902563487, -1.65163651834283, -1.666533644792948, -1.6810644370186776, -1.69588879891896, -1.7115159833369589, -1.726743371176103, -1.7419745497595525, -1.7579360374944977, -1.773583517228068, -1.7893961821975803, -1.8057810493023212, -1.821736118422951, -1.837949539413286, -1.854770913633912, -1.8710953931292673, -1.8874670196417394, -1.9043852216657586, -1.9208778737831906, -1.937327689459215, -1.954303441183475, -1.9708443325809568, -1.9874185486578864, -2.004459298294405, -2.0208511546897077, -2.037246454041954, -2.0540482505734685, -2.070304699915294, -2.086366137153501, -2.10298755101355, -2.1190842293011194, -2.135017297660987, -2.1513493577602945, -2.1670372938266724, -2.1826732270089266, -2.198583455834734, -2.213834600779654, -2.228981677686425, -2.244410035525142, -2.2592821510986845, -2.273934764010812, -2.2887912292728, -2.3029791303424116, -2.3169844901287386, -2.3311378436042145, -2.3446753773466833, -2.3579270622703405, -2.3713310410771298, -2.3840518576047898, -2.396539716149222, -2.4090830937418146, -2.420976111210116, -2.432640090173649, -2.4444273675629975, -2.4554026499965107, -2.4660366773813696, -2.4766281835940345, -2.4866056801038847, -2.4962221664397717, -2.505747922510483, -2.51461905732932, -2.523132964288223, -2.5315262279736808, -2.5392582787073703, -2.5466259807576073, -2.55383330678435, -2.5604212700935345, -2.566752794559222, -2.5730822515725973, -2.5786950052257747, -2.5836632392887595, -2.588396232521927, -2.5925798646918516, -2.59628960874755, -2.599678602127216]}


def dist(x,y):
    return math.sqrt(x**2+y**2)

class PID():
    def __init__(self):
        self.kp = 3.8
        self.ki = 0.0
        self.kd = 0.6
        self.now = 0
        self.last = 0
        self.incont = 0
        self.dcont = 0

    def con(self,yaw,theta):
        f = theta - yaw
        leng = math.sin(f)
        print('leng:',leng)
        self.last = self.now
        self.now = leng
        self.incont += self.now
        if self.incont > 10:
            self.incont = 10
        elif self.incont < -10:
            self.incont = -10
        self.dcont   = self.now - self.last
        return self.now*self.kp + self.dcont*self.kd + self.incont*self.ki
        

class Trace:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = 0
        self.high_speed = 0.50
        self.low_speed = 0.50
        self.speed_flag = 0
        self.img_flag = 0

        self.aflag = 0
        self.labelflag = 0

        self.check = 0
        self.img_label = 0
        self.xl =[]
        self.yl =[]

        self.vel = Twist()
        self.vel.linear.x = self.high_speed
        self.pid = PID()
        self.yaw = 0
        rospy.Subscriber('/odom',Odometry,self.odom_sub)
        rospy.Subscriber("/camera/rgb/image_raw", Image, self.img_sub)
        rospy.Subscriber("/imu",Imu,self.imu_sub)
        self.vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=5)

    def  odom_sub(self,data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
        dist_list = list(dist(self.x - res['x'][i], self.y - res['y'][i]) for i in range(len(res['x'])))
        print('dist',dist_list[0])
        if dist_list[0]<0.3 and self.aflag == 0:
            self.aflag = 1
        if self.aflag == 1:
            self.control()

        self.xl.append(self.x)
        self.yl.append(self.y)
        if len(self.xl) > 1000 and dist(self.xl[0]-self.xl[-1],self.yl[0]-self.yl[-1])<0.5:
            d = {'x':self.xl,'y':self.yl}
            print(d)
            os.system('rosnode kill -a')



    def imu_sub(self,data):
        x = data.orientation.x
        y = data.orientation.y
        z = data.orientation.z
        w = data.orientation.w
        [row,pitch,yaw] = euler_from_quaternion([x,y,z,w])
        self.yaw = yaw



    def img_sub(self,data):
        self.img = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        _, dst = cv2.threshold(img_gray, 166, 255, cv2.THRESH_BINARY_INV)
        if self.aflag != 1:
            left = 960
            right = 960
            while dst[1000][left] == 255:
                left -= 10
                if left < 0:
                    left = 0
                    break
            while dst[1000][right] == 255:
                right += 10
                if right > 1919:
                    right = 1919
                    break
            mid = (right+left+1)/2
            if 950 < mid < 970:
                angular_z = 0
            else:
                angular_z = (mid - 960)/960 * (-3)
            print(angular_z)
            self.vel.angular.z = angular_z
            self.vel_pub.publish(self.vel)
            

        
        
        
    


    def control(self):
        global bflag,flag
        dist_list = list(dist(self.x - res['x'][i], self.y - res['y'][i]) for i in range(len(res['x'])))
        #print(dist_list)
        length = len(dist_list)
        #print('len',length)
        
        min = dist_list[0]
        for i in range(bflag,bflag+25):
            # if i in dlist:
            #     continue

            if min>dist_list[i]:
                min = dist_list[i]
                flag = i

        print('flag:',flag)
        print('trace:',res['x'][flag],res['y'][flag])
        bflag = flag
        if length - bflag < 25:
            flag = length -1
            self.aflag = 2
        flag += 15
        if flag > length:
            flag = length-1

        theta = math.atan2(res['y'][flag]-self.y , res['x'][flag]-self.x)
        self.vel.angular.z = self.pid.con(self.yaw, theta)

        print('speed:',self.vel.linear.x)        

        self.vel_pub.publish(self.vel)


if __name__=='__main__':
    rospy.init_node('trace_node')
    trace = Trace()

    while not rospy.is_shutdown():
        rospy.spin()
