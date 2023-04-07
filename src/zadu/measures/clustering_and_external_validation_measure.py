from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score, normalized_mutual_info_score, v_measure_score


def clustering_and_external_validation_measure(emb, label, clustering="kmeans", clustering_args=None, measure="arand"):
	"""
	Evaluate DR embedding using clustering and external validation measure
	INPUT:
		ndarray: emb: embedded data
		str: clustering: clustering algorithm to use (Optional)
			Currently supports "K-Means", "DBSCAN"
		dict: clustering_args: arguments for clustering algorithm (Optional)
		str: measure: external validation measure to compute (Optional)
			Currently supports "arand", "ami", "nmi", "vmeasure"
	OUTPUT:
		dict: clustering and external validation measure value
	"""

	if clustering == "kmeans":
		clustering_result = KMeans(**clustering_args).fit(emb)
	elif clustering == "dbscan":
		clustering_result = DBSCAN(**clustering_args).fit(emb)
	else:
		raise ValueError("Invalid clustering algorithm")

	if measure == "arand":
		score = adjusted_rand_score(label, clustering_result.labels_)
	elif measure == "ami":
		score = adjusted_mutual_info_score(label, clustering_result.labels_)
	elif measure == "nmi":
		score = normalized_mutual_info_score(label, clustering_result.labels_)
	elif measure == "vmeasure":
		score = v_measure_score(label, clustering_result.labels_)
	
	return {
		f"{clustering}_{measure}": score
	}
