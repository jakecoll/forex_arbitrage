import get_rates
import math

class Arbitrage:

	def __init__(self):
		#self.rate_fetch = get_rates.GetRates()
		#self.rates = self.rate_fetch.get_forex_rates()
		self.rates = {u'USD': {u'IDR': 13314.0, u'BGN': 1.819, u'ILS': 3.6313, u'GBP': 0.80723, u'DKK': 6.9146, u'CAD': 1.3355, u'JPY': 112.71, u'HUF': 287.05, u'RON': 4.2415, u'MYR': 4.4265, u'SEK': 8.8428, u'SGD': 1.3979, u'HKD': 7.7657, u'AUD': 1.2948, u'CHF': 0.99702, u'KRW': 1115.7, u'CNY': 6.9074, u'TRY': 3.6335, u'HRK': 6.8876, u'NZD': 1.4203, u'THB': 34.725, u'EUR': 0.93006, u'NOK': 8.4894, u'RUB': 57.53, u'INR': 65.365, u'MXN': 19.114, u'CZK': 25.131, u'BRL': 3.1079, u'PLN': 3.9825, u'PHP': 50.061, u'ZAR': 12.676}, 
						u'IDR': {u'USD': 7.511e-05, u'BGN': 0.00013663, u'ILS': 0.00027275, u'GBP': 6.0631e-05, u'DKK': 0.00051936, u'CAD': 0.00010031, u'JPY': 0.0084659, u'HUF': 0.021561, u'RON': 0.00031858, u'MYR': 0.00033248, u'SEK': 0.00066418, u'SGD': 0.00010499, u'HKD': 0.00058328, u'AUD': 9.7255e-05, u'CHF': 7.4886e-05, u'KRW': 0.0838, u'CNY': 0.00051881, u'TRY': 0.00027291, u'HRK': 0.00051732, u'NZD': 0.00010668, u'THB': 0.0026082, u'EUR': 6.9857e-05, u'NOK': 0.00063764, u'RUB': 0.0043211, u'INR': 0.0049095, u'MXN': 0.0014356, u'CZK': 0.0018876, u'BRL': 0.00023343, u'PLN': 0.00029913, u'PHP': 0.0037601, u'ZAR': 0.00095208}, 
						u'BGN': {u'USD': 0.54975, u'IDR': 7319.3, u'ILS': 1.9963, u'GBP': 0.44377, u'DKK': 3.8013, u'CAD': 0.73418, u'JPY': 61.964, u'HUF': 157.81, u'RON': 2.3318, u'MYR': 2.4335, u'SEK': 4.8613, u'SGD': 0.76848, u'HKD': 4.2692, u'AUD': 0.71183, u'CHF': 0.54811, u'KRW': 613.36, u'CNY': 3.7973, u'TRY': 1.9975, u'HRK': 3.7864, u'NZD': 0.78081, u'THB': 19.09, u'EUR': 0.5113, u'NOK': 4.667, u'RUB': 31.627, u'INR': 35.934, u'MXN': 10.508, u'CZK': 13.816, u'BRL': 1.7086, u'PLN': 2.1894, u'PHP': 27.521, u'ZAR': 6.9685}, 
						u'ILS': {u'USD': 0.27538, u'IDR': 3666.4, u'BGN': 0.50092, u'GBP': 0.2223, u'DKK': 1.9042, u'CAD': 0.36776, u'JPY': 31.039, u'HUF': 79.049, u'RON': 1.168, u'MYR': 1.219, u'SEK': 2.4352, u'SGD': 0.38495, u'HKD': 2.1385, u'AUD': 0.35657, u'CHF': 0.27456, u'KRW': 307.24, u'CNY': 1.9022, u'TRY': 1.0006, u'HRK': 1.8967, u'NZD': 0.39112, u'THB': 9.5625, u'EUR': 0.25612, u'NOK': 2.3378, u'RUB': 15.843, u'INR': 18.0, u'MXN': 5.2635, u'CZK': 6.9207, u'BRL': 0.85585, u'PLN': 1.0967, u'PHP': 13.786, u'ZAR': 3.4907}, u'GBP': {u'USD': 1.2388, u'IDR': 16493.0, u'BGN': 2.2534, u'ILS': 4.4985, u'DKK': 8.5659, u'CAD': 1.6544, u'JPY': 139.63, u'HUF': 355.6, u'RON': 5.2545, u'MYR': 5.4836, u'SEK': 10.955, u'SGD': 1.7317, u'HKD': 9.6202, u'AUD': 1.604, u'CHF': 1.2351, u'KRW': 1382.1, u'CNY': 8.5569, u'TRY': 4.5012, u'HRK': 8.5324, u'NZD': 1.7595, u'THB': 43.017, u'EUR': 1.1522, u'NOK': 10.517, u'RUB': 71.268, u'INR': 80.974, u'MXN': 23.678, u'CZK': 31.133, u'BRL': 3.8501, u'PLN': 4.9336, u'PHP': 62.017, u'ZAR': 15.703}, u'DKK': {u'USD': 0.14462, u'IDR': 1925.5, u'BGN': 0.26307, u'ILS': 0.52517, u'GBP': 0.11674, u'CAD': 0.19314, u'JPY': 16.301, u'HUF': 41.514, u'RON': 0.61342, u'MYR': 0.64017, u'SEK': 1.2789, u'SGD': 0.20216, u'HKD': 1.1231, u'AUD': 0.18726, u'CHF': 0.14419, u'KRW': 161.35, u'CNY': 0.99895, u'TRY': 0.52548, u'HRK': 0.99609, u'NZD': 0.2054, u'THB': 5.0219, u'EUR': 0.13451, u'NOK': 1.2277, u'RUB': 8.32, u'INR': 9.4531, u'MXN': 2.7642, u'CZK': 3.6345, u'BRL': 0.44947, u'PLN': 0.57596, u'PHP': 7.2399, u'ZAR': 1.8332}, u'CAD': {u'USD': 0.7488, u'IDR': 9969.4, u'BGN': 1.3621, u'ILS': 2.7191, u'GBP': 0.60445, u'DKK': 5.1777, u'JPY': 84.4, u'HUF': 214.95, u'RON': 3.1761, u'MYR': 3.3146, u'SEK': 6.6215, u'SGD': 1.0467, u'HKD': 5.815, u'AUD': 0.96957, u'CHF': 0.74657, u'KRW': 835.43, u'CNY': 5.1722, u'TRY': 2.7207, u'HRK': 5.1574, u'NZD': 1.0635, u'THB': 26.002, u'EUR': 0.69643, u'NOK': 6.3568, u'RUB': 43.078, u'INR': 48.945, u'MXN': 14.312, u'CZK': 18.818, u'BRL': 2.3272, u'PLN': 2.9821, u'PHP': 37.486, u'ZAR': 9.4916}, u'MXN': {u'USD': 0.052319, u'IDR': 696.56, u'BGN': 0.095168, u'ILS': 0.18999, u'GBP': 0.042233, u'DKK': 0.36176, u'CAD': 0.06987, u'HUF': 15.018, u'RON': 0.22191, u'MYR': 0.23159, u'SEK': 0.46264, u'SGD': 0.073135, u'HKD': 0.40629, u'AUD': 0.067744, u'CHF': 0.052163, u'KRW': 58.372, u'CNY': 0.36138, u'TRY': 0.1901, u'HRK': 0.36035, u'NZD': 0.074308, u'THB': 1.8167, u'EUR': 0.048659, u'NOK': 0.44415, u'RUB': 3.0099, u'INR': 3.4198, u'JPY': 5.897, u'CZK': 1.3148, u'BRL': 0.1626, u'PLN': 0.20836, u'PHP': 2.6191, u'ZAR': 0.66318}, u'HUF': {u'USD': 0.0034837, u'IDR': 46.381, u'BGN': 0.0063368, u'ILS': 0.01265, u'GBP': 0.0028121, u'DKK': 0.024088, u'CAD': 0.0046523, u'JPY': 0.39266, u'RON': 0.014776, u'MYR': 0.015421, u'SEK': 0.030805, u'SGD': 0.0048698, u'HKD': 0.027053, u'AUD': 0.0045108, u'CHF': 0.0034733, u'KRW': 3.8867, u'CNY': 0.024063, u'TRY': 0.012658, u'HRK': 0.023994, u'NZD': 0.0049478, u'THB': 0.12097, u'EUR': 0.00324, u'NOK': 0.029574, u'RUB': 0.20041, u'INR': 0.22771, u'MXN': 0.066586, u'CZK': 0.087549, u'BRL': 0.010827, u'PLN': 0.013874, u'PHP': 0.1744, u'ZAR': 0.044158}, u'RON': {u'USD': 0.23576, u'IDR': 3138.9, u'BGN': 0.42886, u'ILS': 0.85613, u'GBP': 0.19031, u'DKK': 1.6302, u'CAD': 0.31486, u'JPY': 26.574, u'HUF': 67.677, u'MYR': 1.0436, u'SEK': 2.0848, u'SGD': 0.32957, u'HKD': 1.8309, u'AUD': 0.30527, u'CHF': 0.23506, u'KRW': 263.04, u'CNY': 1.6285, u'TRY': 0.85664, u'HRK': 1.6238, u'NZD': 0.33485, u'THB': 8.1868, u'EUR': 0.21927, u'NOK': 2.0015, u'RUB': 13.563, u'INR': 15.411, u'MXN': 4.5063, u'CZK': 5.925, u'BRL': 0.73273, u'PLN': 0.93893, u'PHP': 11.803, u'ZAR': 2.9885}, u'MYR': {u'USD': 0.22591, u'IDR': 3007.7, u'BGN': 0.41093, u'ILS': 0.82036, u'GBP': 0.18236, u'DKK': 1.5621, u'CAD': 0.3017, u'JPY': 25.463, u'HUF': 64.849, u'RON': 0.95821, u'SEK': 1.9977, u'SGD': 0.3158, u'HKD': 1.7544, u'AUD': 0.29252, u'CHF': 0.22524, u'KRW': 252.05, u'CNY': 1.5604, u'TRY': 0.82084, u'HRK': 1.556, u'NZD': 0.32086, u'THB': 7.8447, u'EUR': 0.21011, u'NOK': 1.9178, u'RUB': 12.997, u'INR': 14.767, u'MXN': 4.318, u'CZK': 5.6774, u'BRL': 0.70211, u'PLN': 0.89969, u'PHP': 11.309, u'ZAR': 2.8636}, u'SEK': {u'USD': 0.11309, u'IDR': 1505.6, u'BGN': 0.2057, u'ILS': 0.41065, u'GBP': 0.091286, u'DKK': 0.78195, u'CAD': 0.15102, u'JPY': 12.746, u'HUF': 32.462, u'RON': 0.47966, u'MYR': 0.50058, u'SGD': 0.15808, u'HKD': 0.87819, u'AUD': 0.14643, u'CHF': 0.11275, u'KRW': 126.17, u'CNY': 0.78113, u'TRY': 0.41089, u'HRK': 0.77889, u'NZD': 0.16062, u'THB': 3.9269, u'EUR': 0.10518, u'NOK': 0.96003, u'RUB': 6.5058, u'INR': 7.3918, u'MXN': 2.1615, u'CZK': 2.842, u'BRL': 0.35146, u'PLN': 0.45037, u'PHP': 5.6612, u'ZAR': 1.4335}, u'SGD': {u'USD': 0.71537, u'IDR': 9524.3, u'BGN': 1.3013, u'ILS': 2.5977, u'GBP': 0.57747, u'DKK': 4.9465, u'CAD': 0.95536, u'JPY': 80.632, u'HUF': 205.35, u'RON': 3.0343, u'MYR': 3.1666, u'SEK': 6.3259, u'HKD': 5.5554, u'AUD': 0.92628, u'CHF': 0.71324, u'KRW': 798.14, u'CNY': 4.9413, u'TRY': 2.5993, u'HRK': 4.9271, u'NZD': 1.016, u'THB': 24.841, u'EUR': 0.66534, u'NOK': 6.0731, u'RUB': 41.155, u'INR': 46.76, u'MXN': 13.673, u'CZK': 17.978, u'BRL': 2.2233, u'PLN': 2.849, u'PHP': 35.812, u'ZAR': 9.0679}, u'HKD': {u'USD': 0.12877, u'IDR': 1714.4, u'BGN': 0.23424, u'ILS': 0.46761, u'GBP': 0.10395, u'DKK': 0.8904, u'CAD': 0.17197, u'JPY': 14.514, u'HUF': 36.964, u'RON': 0.54619, u'MYR': 0.57001, u'SEK': 1.1387, u'SGD': 0.18001, u'AUD': 0.16674, u'CHF': 0.12839, u'KRW': 143.67, u'CNY': 0.88947, u'TRY': 0.46789, u'HRK': 0.88692, u'NZD': 0.18289, u'THB': 4.4715, u'EUR': 0.11976, u'NOK': 1.0932, u'RUB': 7.4082, u'INR': 8.4171, u'MXN': 2.4613, u'CZK': 3.2362, u'BRL': 0.40021, u'PLN': 0.51283, u'PHP': 6.4465, u'ZAR': 1.6323}, u'AUD': {u'USD': 0.7723, u'IDR': 10282.0, u'BGN': 1.4048, u'ILS': 2.8045, u'GBP': 0.62342, u'DKK': 5.3402, u'CAD': 1.0314, u'JPY': 87.049, u'HUF': 221.69, u'RON': 3.2758, u'MYR': 3.4186, u'SEK': 6.8293, u'SGD': 1.0796, u'HKD': 5.9975, u'CHF': 0.77, u'KRW': 861.66, u'CNY': 5.3346, u'TRY': 2.8061, u'HRK': 5.3193, u'NZD': 1.0969, u'THB': 26.818, u'EUR': 0.71829, u'NOK': 6.5564, u'RUB': 44.43, u'INR': 50.481, u'MXN': 14.762, u'CZK': 19.409, u'BRL': 2.4002, u'PLN': 3.0757, u'PHP': 38.663, u'ZAR': 9.7895}, u'CHF': {u'USD': 1.003, u'IDR': 13354.0, u'BGN': 1.8244, u'ILS': 3.6422, u'GBP': 0.80964, u'DKK': 6.9353, u'CAD': 1.3395, u'JPY': 113.05, u'HUF': 287.91, u'RON': 4.2542, u'MYR': 4.4397, u'SEK': 8.8692, u'SGD': 1.4021, u'HKD': 7.7889, u'AUD': 1.2987, u'KRW': 1119.0, u'CNY': 6.928, u'TRY': 3.6443, u'HRK': 6.9081, u'NZD': 1.4245, u'THB': 34.828, u'EUR': 0.93284, u'NOK': 8.5147, u'RUB': 57.701, u'INR': 65.56, u'MXN': 19.171, u'CZK': 25.206, u'BRL': 3.1172, u'PLN': 3.9944, u'PHP': 50.211, u'ZAR': 12.714}, u'KRW': {u'USD': 0.0008963, u'IDR': 11.933, u'BGN': 0.0016304, u'ILS': 0.0032548, u'GBP': 0.00072352, u'DKK': 0.0061976, u'CAD': 0.001197, u'JPY': 0.10103, u'HUF': 0.25729, u'RON': 0.0038017, u'MYR': 0.0039675, u'SEK': 0.0079258, u'SGD': 0.0012529, u'HKD': 0.0069604, u'AUD': 0.0011606, u'CHF': 0.00089363, u'CNY': 0.0061911, u'TRY': 0.0032567, u'HRK': 0.0061733, u'NZD': 0.001273, u'THB': 0.031124, u'EUR': 0.00083361, u'NOK': 0.007609, u'RUB': 0.051564, u'INR': 0.058586, u'MXN': 0.017132, u'CZK': 0.022525, u'BRL': 0.0027856, u'PLN': 0.0035695, u'PHP': 0.04487, u'ZAR': 0.011361}, u'CNY': {u'USD': 0.14477, u'IDR': 1927.5, u'BGN': 0.26334, u'ILS': 0.52572, u'GBP': 0.11686, u'DKK': 1.0011, u'CAD': 0.19334, u'JPY': 16.318, u'HUF': 41.558, u'RON': 0.61406, u'MYR': 0.64084, u'SEK': 1.2802, u'SGD': 0.20238, u'HKD': 1.1243, u'AUD': 0.18746, u'CHF': 0.14434, u'KRW': 161.52, u'TRY': 0.52603, u'HRK': 0.99713, u'NZD': 0.20562, u'THB': 5.0272, u'EUR': 0.13465, u'NOK': 1.229, u'RUB': 8.3288, u'INR': 9.463, u'MXN': 2.7671, u'CZK': 3.6383, u'BRL': 0.44994, u'PLN': 0.57656, u'PHP': 7.2475, u'ZAR': 1.8351}, u'TRY': {u'USD': 0.27522, u'IDR': 3664.2, u'BGN': 0.50063, u'ILS': 0.99941, u'GBP': 0.22216, u'DKK': 1.903, u'CAD': 0.36755, u'JPY': 31.021, u'HUF': 79.003, u'RON': 1.1674, u'MYR': 1.2183, u'SEK': 2.4337, u'SGD': 0.38472, u'HKD': 2.1373, u'AUD': 0.35636, u'CHF': 0.2744, u'KRW': 307.06, u'CNY': 1.901, u'HRK': 1.8956, u'NZD': 0.39089, u'THB': 9.5569, u'EUR': 0.25597, u'NOK': 2.3364, u'RUB': 15.833, u'INR': 17.99, u'MXN': 5.2604, u'CZK': 6.9166, u'BRL': 0.85535, u'PLN': 1.0961, u'PHP': 13.778, u'ZAR': 3.4886}, u'HRK': {u'USD': 0.14519, u'IDR': 1933.0, u'BGN': 0.2641, u'ILS': 0.52723, u'GBP': 0.1172, u'DKK': 1.0039, u'CAD': 0.1939, u'JPY': 16.365, u'HUF': 41.677, u'RON': 0.61583, u'MYR': 0.64268, u'SEK': 1.2839, u'SGD': 0.20296, u'HKD': 1.1275, u'AUD': 0.188, u'CHF': 0.14476, u'KRW': 161.99, u'CNY': 1.0029, u'TRY': 0.52754, u'NZD': 0.20621, u'THB': 5.0417, u'EUR': 0.13503, u'NOK': 1.2326, u'RUB': 8.3527, u'INR': 9.4902, u'MXN': 2.7751, u'CZK': 3.6488, u'BRL': 0.45123, u'PLN': 0.57822, u'PHP': 7.2684, u'ZAR': 1.8404}, u'NZD': {u'USD': 0.70408, u'IDR': 9374.0, u'BGN': 1.2807, u'ILS': 2.5567, u'GBP': 0.56835, u'DKK': 4.8684, u'CAD': 0.94028, u'JPY': 79.36, u'HUF': 202.11, u'RON': 2.9864, u'MYR': 3.1166, u'SEK': 6.226, u'SGD': 0.98422, u'HKD': 5.4677, u'AUD': 0.91166, u'CHF': 0.70198, u'KRW': 785.54, u'CNY': 4.8633, u'TRY': 2.5582, u'HRK': 4.8494, u'THB': 24.449, u'EUR': 0.65484, u'NOK': 5.9772, u'RUB': 40.506, u'INR': 46.022, u'MXN': 13.458, u'CZK': 17.694, u'BRL': 2.1882, u'PLN': 2.804, u'PHP': 35.247, u'ZAR': 8.9248}, u'THB': {u'USD': 0.028798, u'IDR': 383.41, u'BGN': 0.052384, u'ILS': 0.10457, u'GBP': 0.023246, u'DKK': 0.19913, u'CAD': 0.038459, u'JPY': 3.2459, u'HUF': 8.2666, u'RON': 0.12215, u'MYR': 0.12747, u'SEK': 0.25466, u'SGD': 0.040256, u'HKD': 0.22364, u'AUD': 0.037288, u'CHF': 0.028712, u'KRW': 32.13, u'CNY': 0.19892, u'TRY': 0.10464, u'HRK': 0.19835, u'NZD': 0.040902, u'EUR': 0.026784, u'NOK': 0.24448, u'RUB': 1.6567, u'INR': 1.8824, u'MXN': 0.55043, u'CZK': 0.72373, u'BRL': 0.089501, u'PLN': 0.11469, u'PHP': 1.4417, u'ZAR': 0.36504}, 'EUR': {u'USD': 1.0752, u'IDR': 14315.0, u'BGN': 1.9558, u'ILS': 3.9044, u'GBP': 0.86793, u'DKK': 7.4346, u'CAD': 1.4359, u'JPY': 121.19, u'HUF': 308.64, u'RON': 4.5605, u'MYR': 4.7594, u'SEK': 9.5078, u'SGD': 1.503, u'HKD': 8.3497, u'AUD': 1.3922, u'CHF': 1.072, u'KRW': 1199.6, u'CNY': 7.4268, u'TRY': 3.9067, u'HRK': 7.4055, u'NZD': 1.5271, u'THB': 37.336, u'NOK': 9.1278, u'RUB': 61.856, u'INR': 70.28, u'MXN': 20.551, u'CZK': 27.021, u'BRL': 3.3416, u'PLN': 4.282, u'PHP': 53.826, u'ZAR': 13.629}, u'NOK': {u'USD': 0.11779, u'IDR': 1568.3, u'BGN': 0.21427, u'ILS': 0.42775, u'GBP': 0.095086, u'DKK': 0.8145, u'CAD': 0.15731, u'JPY': 13.277, u'HUF': 33.813, u'RON': 0.49963, u'MYR': 0.52142, u'SEK': 1.0416, u'SGD': 0.16466, u'HKD': 0.91475, u'AUD': 0.15252, u'CHF': 0.11744, u'KRW': 131.42, u'CNY': 0.81365, u'TRY': 0.428, u'HRK': 0.81131, u'NZD': 0.1673, u'THB': 4.0904, u'EUR': 0.10956, u'RUB': 6.7767, u'INR': 7.6996, u'MXN': 2.2515, u'CZK': 2.9603, u'BRL': 0.36609, u'PLN': 0.46912, u'PHP': 5.8969, u'ZAR': 1.4931}, u'RUB': {u'USD': 0.017382, u'IDR': 231.42, u'BGN': 0.031619, u'ILS': 0.063121, u'GBP': 0.014031, u'DKK': 0.12019, u'CAD': 0.023214, u'JPY': 1.9592, u'HUF': 4.9897, u'RON': 0.073728, u'MYR': 0.076943, u'SEK': 0.15371, u'SGD': 0.024298, u'HKD': 0.13499, u'AUD': 0.022507, u'CHF': 0.017331, u'KRW': 19.393, u'CNY': 0.12007, u'TRY': 0.063158, u'HRK': 0.11972, u'NZD': 0.024688, u'THB': 0.6036, u'EUR': 0.016167, u'NOK': 0.14757, u'INR': 1.1362, u'MXN': 0.33224, u'CZK': 0.43684, u'BRL': 0.054022, u'PLN': 0.069225, u'PHP': 0.87018, u'ZAR': 0.22033}, u'INR': {u'USD': 0.015299, u'IDR': 203.69, u'BGN': 0.027829, u'ILS': 0.055555, u'GBP': 0.01235, u'DKK': 0.10579, u'CAD': 0.020431, u'JPY': 1.7244, u'HUF': 4.3916, u'RON': 0.06489, u'MYR': 0.067721, u'SEK': 0.13528, u'SGD': 0.021386, u'HKD': 0.11881, u'AUD': 0.019809, u'CHF': 0.015253, u'KRW': 17.069, u'CNY': 0.10567, u'TRY': 0.055588, u'HRK': 0.10537, u'NZD': 0.021729, u'THB': 0.53125, u'EUR': 0.014229, u'NOK': 0.12988, u'RUB': 0.88014, u'MXN': 0.29242, u'CZK': 0.38448, u'BRL': 0.047547, u'PLN': 0.060928, u'PHP': 0.76588, u'ZAR': 0.19392}, u'JPY': {u'USD': 0.008872, u'IDR': 118.12, u'BGN': 0.016138, u'ILS': 0.032217, u'GBP': 0.0071617, u'DKK': 0.061347, u'CAD': 0.011848, u'HUF': 2.5467, u'RON': 0.037631, u'MYR': 0.039272, u'SEK': 0.078454, u'SGD': 0.012402, u'HKD': 0.068898, u'AUD': 0.011488, u'CHF': 0.0088456, u'KRW': 9.8985, u'CNY': 0.061282, u'TRY': 0.032236, u'HRK': 0.061107, u'NZD': 0.012601, u'THB': 0.30808, u'EUR': 0.0082515, u'NOK': 0.075318, u'RUB': 0.51041, u'INR': 0.57992, u'MXN': 0.16958, u'CZK': 0.22296, u'BRL': 0.027573, u'PLN': 0.035333, u'PHP': 0.44415, u'ZAR': 0.11246}, u'CZK': {u'USD': 0.039791, u'IDR': 529.77, u'BGN': 0.072381, u'ILS': 0.1445, u'GBP': 0.032121, u'DKK': 0.27514, u'CAD': 0.05314, u'JPY': 4.485, u'HUF': 11.422, u'RON': 0.16878, u'MYR': 0.17614, u'SEK': 0.35187, u'SGD': 0.055623, u'HKD': 0.30901, u'AUD': 0.051523, u'CHF': 0.039673, u'KRW': 44.395, u'CNY': 0.27485, u'TRY': 0.14458, u'HRK': 0.27406, u'NZD': 0.056515, u'THB': 1.3817, u'EUR': 0.037008, u'NOK': 0.3378, u'RUB': 2.2892, u'INR': 2.6009, u'MXN': 0.76056, u'BRL': 0.12367, u'PLN': 0.15847, u'PHP': 1.992, u'ZAR': 0.50439}, u'BRL': {u'USD': 0.32176, u'IDR': 4283.9, u'BGN': 0.58529, u'ILS': 1.1684, u'GBP': 0.25973, u'DKK': 2.2249, u'CAD': 0.4297, u'JPY': 36.267, u'HUF': 92.363, u'RON': 1.3648, u'MYR': 1.4243, u'SEK': 2.8453, u'SGD': 0.44978, u'HKD': 2.4987, u'AUD': 0.41663, u'CHF': 0.3208, u'KRW': 358.99, u'CNY': 2.2225, u'TRY': 1.1691, u'HRK': 2.2162, u'NZD': 0.457, u'THB': 11.173, u'EUR': 0.29926, u'NOK': 2.7316, u'RUB': 18.511, u'INR': 21.032, u'MXN': 6.15, u'CZK': 8.0862, u'PLN': 1.2814, u'PHP': 16.108, u'ZAR': 4.0786}, u'PLN': {u'USD': 0.2511, u'IDR': 3343.1, u'BGN': 0.45675, u'ILS': 0.91182, u'GBP': 0.20269, u'DKK': 1.7362, u'CAD': 0.33533, u'JPY': 28.302, u'HUF': 72.078, u'RON': 1.065, u'MYR': 1.1115, u'SEK': 2.2204, u'SGD': 0.351, u'HKD': 1.95, u'AUD': 0.32513, u'CHF': 0.25035, u'KRW': 280.15, u'CNY': 1.7344, u'TRY': 0.91235, u'HRK': 1.7294, u'NZD': 0.35663, u'THB': 8.7193, u'EUR': 0.23354, u'NOK': 2.1317, u'RUB': 14.446, u'INR': 16.413, u'MXN': 4.7994, u'CZK': 6.3104, u'BRL': 0.78038, u'PHP': 12.57, u'ZAR': 3.1829}, u'PHP': {u'USD': 0.019975, u'IDR': 265.95, u'BGN': 0.036336, u'ILS': 0.072537, u'GBP': 0.016125, u'DKK': 0.13812, u'CAD': 0.026677, u'JPY': 2.2515, u'HUF': 5.734, u'RON': 0.084727, u'MYR': 0.088422, u'SEK': 0.17664, u'SGD': 0.027923, u'HKD': 0.15512, u'AUD': 0.025865, u'CHF': 0.019916, u'KRW': 22.287, u'CNY': 0.13798, u'TRY': 0.07258, u'HRK': 0.13758, u'NZD': 0.028371, u'THB': 0.69364, u'EUR': 0.018578, u'NOK': 0.16958, u'RUB': 1.1492, u'INR': 1.3057, u'MXN': 0.3818, u'CZK': 0.50201, u'BRL': 0.062082, u'PLN': 0.079553, u'ZAR': 0.2532}, u'ZAR': {u'USD': 0.078891, u'IDR': 1050.3, u'BGN': 0.1435, u'ILS': 0.28648, u'GBP': 0.063683, u'DKK': 0.5455, u'CAD': 0.10536, u'JPY': 8.8921, u'HUF': 22.646, u'RON': 0.33462, u'MYR': 0.34921, u'SEK': 0.69762, u'SGD': 0.11028, u'HKD': 0.61264, u'AUD': 0.10215, u'CHF': 0.078656, u'KRW': 88.018, u'CNY': 0.54493, u'TRY': 0.28665, u'HRK': 0.54336, u'NZD': 0.11205, u'THB': 2.7395, u'EUR': 0.073373, u'NOK': 0.66973, u'RUB': 4.5386, u'INR': 5.1567, u'MXN': 1.5079, u'CZK': 1.9826, u'BRL': 0.24518, u'PLN': 0.31418, u'PHP': 3.9494}}
		self.log_rates = self.rates
		self.d = {}
		self.p = {}
		self.paths = []


	def arbitrage(self):

		for base_currency in self.log_rates.keys():
			for exchange_ctr in self.log_rates[base_currency].keys():
				self.log_rates[base_currency][exchange_ctr] = -math.log(float(self.log_rates[base_currency][exchange_ctr]))

		"""
		for key in self.log_rates.keys():
			path = self.bellman_ford(key)
			if path not in self.paths:
				self.paths.append(path)

		"""

		return self.bellman_ford('USD')
		
	def bellman_ford(self, src):

		self.initialize(src)

		
		for i in range(len(self.log_rates.keys())-1):
			for base_currency in self.log_rates.keys():
				for exchange_ctr in self.log_rates[base_currency].keys():

					
					self.relax(base_currency,exchange_ctr)

		for base_currency in self.log_rates.keys(): 
			for exchange_ctr in self.log_rates[base_currency].keys():
				if self.d[exchange_ctr] < self.d[base_currency] + self.log_rates[base_currency][exchange_ctr]:
					print base_currency
					print exchange_ctr
					return self.get_neg_wt_cycle(exchange_ctr)

		print "No Arbitrage Cycle"
		return []

	def initialize(self, src):
		self.p = {}
		self.d = {}
	
		for denom in self.log_rates.keys():
			self.d[denom] = float('inf')
			self.p[denom] = None

		self.d[src] = 0

	def relax(self, u, v):
		if self.d[v] > self.d[u] + self.log_rates[u][v]:
			self.d[v] = self.d[u] + self.log_rates[u][v]
			self.p[v] = u

	def get_neg_wt_cycle(self, v):

		cycle = [self.p[v]]
		i=self.p[v]

		#while i not in cycle or v not in cycle:
		while True:
			print(cycle)
			if self.p.get(i) == None:
				print("Error: Broken Predecessor Chain")
				return []
			else: 
				i = self.p[i]
				if i not in cycle:
					cycle.append(i)
				else: 
					cycle.append(i)
					cycle = cycle[cycle.index(i):-1]
					return cycle


if __name__ == "__main__":

	arbitrage = Arbitrage()
	print(arbitrage.arbitrage())