"""
This script is used to collect data for testing
It is mainly used in a script which uses googlemap api client if you don't want to apply it
"""


"""
DIRECTIONS_TEST_DATA is collected by the following method:
# origin = "台北101"
# destination = "台北市立動物園"
# data = googlemaps.Client(key=API_KEY).directions(origin, destination)

The data shows the details of the route from origin to destination
It is used to determine polylines, points of route in each step, in order to calculte risk index
"""

DIRECTIONS = [{
    'bounds': {
        'northeast': {'lat': 25.0359038, 'lng': 121.5843379},
        'southwest': {'lat': 24.9952619, 'lng': 121.5635382}},
    'copyrights': 'Map data ©2024 Google',
    'legs': [{
        'distance': {'text': '8.4 km', 'value': 8395},
        'duration': {'text': '17 mins', 'value': 993},
        'end_address': 'No. 30號, Section 2, Xinguang Rd, Wenshan District, Taipei City, Taiwan 116',
        'end_location': {'lat': 24.9989525, 'lng': 121.5807017},
        'start_address': 'Taipei 101, No. 7, Section 5, Xinyi Rd, Xinyi District, Taipei City, Taiwan 110',
        'start_location': {'lat': 25.0333612, 'lng': 121.5637614},
        'steps': [{'distance': {'text': '25 m', 'value': 25},
                'duration': {'text': '1 min', 'value': 8},
                'end_location': {'lat': 25.0332567, 'lng': 121.5635382},
                'html_instructions': 'Head <b>southwest</b> toward <b>市府路</b>',
                'polyline': {'points': 'oixwCo|}dVRj@'},
                'start_location': {'lat': 25.0333612, 'lng': 121.5637614},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.3 km', 'value': 294},
                'duration': {'text': '2 mins', 'value': 96},
                'end_location': {'lat': 25.0359038, 'lng': 121.5635845},
                'html_instructions': 'Turn <b>right</b> onto <b>市府路</b>',
                'maneuver': 'turn-right',
                'polyline': {'points': '{hxwCc{}dVW?EAU?G?I?mAAiAAq@?i@A_@?uD?'},
                'start_location': {'lat': 25.0332567, 'lng': 121.5635382},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.2 km', 'value': 187},
                'duration': {'text': '1 min', 'value': 56},
                'end_location': {'lat': 25.0358687, 'lng': 121.565437},
                'html_instructions': 'Turn <b>right</b> onto <b>松壽路</b>',
                'maneuver': 'turn-right',
                'polyline': {'points': 'kyxwCk{}dV@qA@oA?eA?u@?}@@W'},
                'start_location': {'lat': 25.0359038, 'lng': 121.5635845},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.3 km', 'value': 319},
                'duration': {'text': '2 mins', 'value': 92},
                'end_location': {'lat': 25.0330042, 'lng': 121.5653914},
                'html_instructions': 'Turn <b>right</b> onto <b>松智路</b>',
                'maneuver': 'turn-right',
                'polyline': {'points': 'eyxwC_g~dV^?dA@lA?R@LAf@@L?\\?n@@X?L@rC@J?@?X?'},
                'start_location': {'lat': 25.0358687, 'lng': 121.565437},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.4 km', 'value': 421},
                'duration': {'text': '2 mins', 'value': 91},
                'end_location': {'lat': 25.0327428, 'lng': 121.5694146},
                'html_instructions': 'Turn <b>left</b> onto <b>信義路五段</b>',
                'maneuver': 'turn-left',
                'polyline': {'points': 'ggxwCuf~dVX??c@@kA@O?S?_A?k@FsE?e@@g@BS@[@e@BaAAu@@s@'},
                'start_location': {'lat': 25.0330042, 'lng': 121.5653914},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.4 km', 'value': 364},
                'duration': {'text': '1 min', 'value': 36},
                'end_location': {'lat': 25.0312594, 'lng': 121.5716292},
                'html_instructions': 'Slight <b>left</b> onto the <b>Xinyi Expwy.</b>/<wbr/><b>Muzha</b> ramp',
                'maneuver': 'ramp-left',
                'polyline': {'points': 'sexwCy__eVAAAAAC?C?C?Q@s@BmA?I@cB?Y@Y@Q@M@K@GBGBGBGDGFG@ABCDEDCFABABAB?BAFAH@NAh@@`@?h@Bf@AVC'},
                'start_location': {'lat': 25.0327428, 'lng': 121.5694146},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '2.8 km', 'value': 2834},
                'duration': {'text': '3 mins', 'value': 199},
                'end_location': {'lat': 25.0078893, 'lng': 121.5812147},
                'html_instructions': 'Continue onto <b>信義快速道路</b>',
                'polyline': {'points': 'k|wwCum_eVb@?H?V?JAPCPCRETERGZI`@Sd@SXMl@]NIl@]^Sh@[RK^S\\S^SLIn@]fAm@hBcAhAm@xBmAjBeALIdBaAdBmA~B}AZUJEJEHGHE^Wp@[ZQPINGFELEPEVIRIXK`@QZQ\\Sf@WnAm@`B}@fDkBdB_AVM^SzAw@BA~CqA@A`@O|@[BA|Ag@p@Sl@QlBg@h@Mf@K~@Qb@I`@IrB[fBU`BQBAbAIDA\\Ab@CZCF?@?XAFAfAEb@?b@Ab@Ab@A|EID?`@B`@@p@B`CFvBL'},
                'start_location': {'lat': 25.0312594, 'lng': 121.5716292},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.5 km', 'value': 458},
                'duration': {'text': '1 min', 'value': 24},
                'end_location': {'lat': 25.0039153, 'lng': 121.5801856},
                'html_instructions': 'Keep <b>left</b> to stay on <b>信義快速道路</b>',
                'maneuver': 'keep-left',
                'polyline': {'points': 'ijswCqiaeV\\CTB\\Bx@DfAF^Bf@Db@D^BXDPBr@L|@PXDND@?NDRD`@JLDRJx@\\B@HBD@D@D@DBf@V'},
                'start_location': {'lat': 25.0078893, 'lng': 121.5812147},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.5 km', 'value': 470},
                'duration': {'text': '1 min', 'value': 31},
                'end_location': {'lat': 25.0009028, 'lng': 121.5769592},
                'html_instructions': 'Keep <b>left</b>',
                'maneuver': 'keep-left',
                'polyline': {'points': 'oqrwCecaeV\\RNHn@b@NLXRh@f@LJXZDDRTZ^`@j@^j@V\\@BdA|Ab@p@Zb@PVJLPRHHRNZR'},
                'start_location': {'lat': 25.0039153, 'lng': 121.5801856},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '79 m', 'value': 79},
                'duration': {'text': '1 min', 'value': 12},
                'end_location': {'lat': 25.0002151, 'lng': 121.5768096},
                'html_instructions': 'Continue onto <b>萬芳交流道</b>',
                'polyline': {'points': 's~qwC_o`eVDBD@DBJBr@PR@LAH?HA'},
                'start_location': {'lat': 25.0009028, 'lng': 121.5769592},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.8 km', 'value': 798},
                'duration': {'text': '2 mins', 'value': 98},
                'end_location': {'lat': 25.002947, 'lng': 121.5839685},
                'html_instructions': 'Turn <b>left</b> onto <b>木柵路五段</b>/<wbr/><b>106縣道</b>',
                'maneuver': 'turn-left',
                'polyline': {'points': 'kzqwCan`eVREEQQiAGWIg@GYCICIKc@Yy@M[Yu@o@eBm@}A_@_A?AMYQa@Yo@Qa@Oc@ISWq@Oa@Ma@GW]mAEKCKCGEGWoAI[COAGCKIc@COM{@Ii@G]'},
                'start_location': {'lat': 25.0002151, 'lng': 121.5768096},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.3 km', 'value': 329},
                'duration': {'text': '1 min', 'value': 35},
                'end_location': {'lat': 25.0005712, 'lng': 121.5831392},
                'html_instructions': 'Turn <b>right</b> onto <b>新光路二段</b>/<wbr/><b>萬福橋</b><div style="font-size:0.9em">Continue to follow 新光路二段</div>',
                'maneuver': 'turn-right',
                'polyline': {'points': 'mkrwCyzaeVTGn@Q`@KZKDAXIJCJCFAFA@?F?H?H?F?F@J@D@D@B?LDPFFBDBD@BBFFHHJLJNBFBF?F@D@D@DBDLRTb@R^BHBB@B@?@@B?@?D?'},
                'start_location': {'lat': 25.002947, 'lng': 121.5839685},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.6 km', 'value': 612},
                'duration': {'text': '1 min', 'value': 70},
                'end_location': {'lat': 24.9975879, 'lng': 121.5780605},
                'html_instructions': 'At the roundabout, take the <b>1st</b> exit and stay on <b>新光路二段</b>',
                'maneuver': 'roundabout-right',
                'polyline': {'points': 'q|qwCsuaeV?@@@@B?@@@@?@@@@?F?D@D@FBFJRFP@@\\n@v@zAJRdBnDr@rA`AnBt@vAj@jAhCbF'},
                'start_location': {'lat': 25.0005712, 'lng': 121.5831392},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.4 km', 'value': 441},
                'duration': {'text': '1 min', 'value': 42},
                'end_location': {'lat': 24.9953815, 'lng': 121.5744247},
                'html_instructions': 'Keep <b>right</b> to stay on <b>新光路二段</b>',
                'maneuver': 'keep-right',
                'polyline': {'points': '}iqwC{u`eVHPDFpCpFFLXn@DFR^?@lA~BxBfERZ'},
                'start_location': {'lat': 24.9975879, 'lng': 121.5780605},
                'travel_mode': 'DRIVING'},
                {'distance': {'text': '0.8 km', 'value': 764},
                'duration': {'text': '2 mins', 'value': 103},
                'end_location': {'lat': 24.9989525, 'lng': 121.5807017},
                'html_instructions': 'Make a <b>U-turn</b><div style="font-size:0.9em">Destination will be on the right</div>',
                'maneuver': 'uturn-left',
                'polyline': {'points': 'c|pwCc_`eVVKkBaEgBoDMSIQ}@eBwBgEeAqB]s@u@yAIMEKQ_@c@{@EGAES_@Uc@i@eACG'},
                'start_location': {'lat': 24.9953815, 'lng': 121.5744247},
                'travel_mode': 'DRIVING'}],
        'traffic_speed_entry': [],
        'via_waypoint': []}],
    'overview_polyline': {'points': 'oixwCo|}dVRj@W?[AiDCqHAB}G@uAdB@vC@dHDr@?@oB@oCFyFD{@BaA@wB?u@CE@mADuEFeAL_@RUVMREdB@pA@z@C~@EnAW|@]~@a@jCyA`HyDxKeGrBkAdFkD|@i@h@]lAm@v@]vAe@bCoA~LwGvC{A`G_C`EoAvCu@fB]xDo@pGs@fCMvCIjHMvFPvBL\\Cr@FhEVnBRzCj@fAV~Ap@ZHzAx@~@p@bAz@l@l@n@t@`AvAbCpDjA|A~@p@jAZt@AREEQYaBYuAe@}Ag@qA}BeGkAmCaAkCy@sCGS]wAS_Ae@yCG]TGpA]fA[\\Gb@?^Fj@PVPd@n@FZfAtBH@D@BDDDBTXt@bB`DvMtWtK`TRZVKkBaEgBoDWe@uDmHcDmGaAoByAwC'},
    'summary': '信義快速道路 and 新光路二段',
    'warnings': [],
    'waypoint_order': []}]


"""
GEOCODE_TEST_DATA is collected by the following method:
# address = "台北101"
# data = googlemaps.Client(key=API_KEY).geocode(address)

The data is used to translate an address into coordinates
"""
GEOCODE = [{
    'address_components': [
        {'long_name': 'Taipei 101', 'short_name': 'Taipei 101', 'types': ['premise']},
        {'long_name': '7', 'short_name': '7', 'types': ['street_number']},
        {'long_name': 'Section 5, Xinyi Road', 'short_name': 'Section 5, Xinyi Rd', 'types': ['route']},
        {'long_name': '西村里', 'short_name': '西村里', 'types': ['administrative_area_level_3', 'political']},
        {'long_name': 'Xinyi District', 'short_name': 'Xinyi District', 'types': ['administrative_area_level_2', 'political']},
        {'long_name': 'Taipei City', 'short_name': 'Taipei City', 'types': ['administrative_area_level_1', 'political']},
        {'long_name': 'Taiwan', 'short_name': 'TW', 'types': ['country', 'political']},
        {'long_name': '110', 'short_name': '110', 'types': ['postal_code']}],
    'formatted_address': 'Taipei 101, No. 7, Section 5, Xinyi Rd, Xinyi District, Taipei City, Taiwan 110',
    'geometry': {'bounds': {'northeast': {'lat': 25.034646, 'lng': 121.5652829},
                            'southwest': {'lat': 25.0332035, 'lng': 121.5638757}},
                'location': {'lat': 25.033976, 'lng': 121.5645389},
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 25.0351900802915, 'lng': 121.5658639802915},
                            'southwest': {'lat': 25.0324921197085, 'lng': 121.5631660197085}}},
    'place_id': 'ChIJH56c2rarQjQRphD9gvC8BhI',
    'types': ['premise']}]

GEOCODE_ZH = [{
    'address_components': [
        {'long_name': '大安森林公園', 'short_name': '大安森林公園', 'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']}, 
        {'long_name': '1號', 'short_name': '1號', 'types': ['street_number']}, 
        {'long_name': '新生南路二段', 'short_name': '新生南路二段', 'types': ['route']}, 
        {'long_name': '龍門里', 'short_name': '龍門里', 'types': ['administrative_area_level_3', 'political']}, 
        {'long_name': '大安區', 'short_name': '大安區', 'types': ['administrative_area_level_2', 'political']}, 
        {'long_name': '台北市', 'short_name': '台北市', 'types': ['administrative_area_level_1', 'political']}, 
        {'long_name': '台灣', 'short_name': 'TW', 'types': ['country', 'political']}, 
        {'long_name': '106', 'short_name': '106', 'types': ['postal_code']}], 
    'formatted_address': '106台灣台北市大安區新生南路二段1號大安森林公園', 
    'geometry': {'location': {'lat': 25.0296587, 'lng': 121.5362867}, 
                 'location_type': 'ROOFTOP', 
                 'viewport': {'northeast': {'lat': 25.0334161, 'lng': 121.5375213}, 
                              'southwest': {'lat': 25.0288186, 'lng': 121.5345102}}}, 
    'partial_match': True, 
    'place_id': 'ChIJnzZlOoCpQjQRH-WG9egh-2E', 
    'plus_code': {'compound_code': '2GHP+VG 台灣台北市大安區龍門里', 'global_code': '7QQ32GHP+VG'}, 
    'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']}]

GEOCODE_ZH_1 = [{
    'address_components': [
        {'long_name': '386', 'short_name': '386', 'types': ['street_number']}, 
        {'long_name': '建國路', 'short_name': '建國路', 'types': ['route']}, 
        {'long_name': '瑞興里', 'short_name': '瑞興里', 'types': ['administrative_area_level_3', 'political']}, 
        {'long_name': '八德區', 'short_name': '八德區', 'types': ['administrative_area_level_2', 'political']}, 
        {'long_name': '桃園市', 'short_name': '桃園市', 'types': ['administrative_area_level_1', 'political']}, 
        {'long_name': '台灣', 'short_name': 'TW', 'types': ['country', 'political']}, 
        {'long_name': '334', 'short_name': '334', 'types': ['postal_code']}], 
    'formatted_address': '334台灣桃園市八德區建國路386號', 
    'geometry': {'location': {'lat': 24.9401104, 'lng': 121.2882407}, 
                 'location_type': 'ROOFTOP', 
                 'viewport': {'northeast': {'lat': 24.9414507802915, 'lng': 121.2895322302915}, 
                              'southwest': {'lat': 24.9387528197085, 'lng': 121.2868342697085}}}, 
    'place_id': 'ChIJ96H7-OoYaDQR5ez5vbPTTnc', 
    'plus_code': {'compound_code': 'W7RQ+27 台灣桃園市八德區瑞興里', 'global_code': '7QP3W7RQ+27'}, 
    'types': ['street_address']}]

GEOCODE_ZH_2 = [{
    'address_components': [
        {'long_name': '55', 'short_name': '55', 'types': ['street_number']}, 
        {'long_name': '文化一路', 'short_name': '文化一路', 'types': ['route']},
        {'long_name': '樂善里', 'short_name': '樂善里', 'types': ['administrative_area_level_3', 'political']}, 
        {'long_name': '龜山區', 'short_name': '龜山區', 'types': ['administrative_area_level_2', 'political']}, 
        {'long_name': '桃園市', 'short_name': '桃園市', 'types': ['administrative_area_level_1', 'political']}, 
        {'long_name': '台灣', 'short_name': 'TW', 'types': ['country', 'political']}, 
        {'long_name': '333', 'short_name': '333', 'types': ['postal_code']}], 
    'formatted_address': '333台灣桃園市龜山區文化一路55號', 
    'geometry': {'location': {'lat': 25.0564006, 'lng': 121.3751299}, 
                 'location_type': 'ROOFTOP', 
                 'viewport': {'northeast': {'lat': 25.05765158029151, 'lng': 121.3764402802915}, 
                              'southwest': {'lat': 25.0549536197085, 'lng': 121.3737423197085}}}, 
    'place_id': 'ChIJibXZuD2nQjQRnOTgxi2az-w', 
    'plus_code': {'compound_code': '394G+H3 台灣桃園市龜山區樂善里', 'global_code': '7QQ3394G+H3'}, 
    'types': ['street_address']}]

GEOCODE_ZH_2 = [{
    'address_components': [
        {'long_name': '27', 'short_name': '27', 'types': ['street_number']}, 
        {'long_name': '浯江街', 'short_name': '浯江街', 'types': ['route']}, 
        {'long_name': '893', 'short_name': '893', 'types': ['postal_code']}], 
    'formatted_address': '893浯江街27', 
    'geometry': {'bounds': {'northeast': {'lat': 24.4328786, 'lng': 118.3179771}, 
                            'southwest': {'lat': 24.4326281, 'lng': 118.3177942}}, 
                 'location': {'lat': 24.43276, 'lng': 118.3178872}, 
                 'location_type': 'ROOFTOP', 
                 'viewport': {'northeast': {'lat': 24.4340838302915, 'lng': 118.3191920302915}, 
                              'southwest': {'lat': 24.4313858697085, 'lng': 118.3164940697085}}}, 
    'place_id': 'ChIJjYeq42uiFDQREdi7jUBZgRQ', 
    'types': ['premise']}]
