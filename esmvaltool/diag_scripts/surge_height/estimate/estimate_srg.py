import numpy as np
import pandas as pd

#from .load import load_betas_intercept as llbi
from load import load_monmean_srgclim


def estimate_srg(X, dates, stat, betas, intercept):
    if not type(stat) == list:
        stat = [stat]
    #
    #global srg_est_full, srg_est
    srg_est = {}
    srg_est_full = {}
    for s in stat:
        srg_est[s] = np.zeros(len(dates)).tolist()
        for t in range(len(dates)):
            srg_est[s][t] = sum(X[s][t] * betas[s][:9250]) + float(
                intercept[s])
        # Add seasonal cycle back to surge
        monanom_srg = load_monmean_srgclim.load_monmean_srgclim(s)
        srg_est_full[s] = []
        for t in range(len(dates)):
            srg_est_t = srg_est[s][t] + monanom_srg[s][dates[t].month - 1]
            srg_est_full[s].append(srg_est_t)

    return srg_est_full