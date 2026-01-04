import numpy

parameter = {'Aff': 0, 'Ahf': 1, 'BSLmax': 2, 'BSRmax': 3, 'CaMKo': 4, 'F': 5, 'GKb_tmp': 6, 'GNa': 7, 'Gncx_tmp': 8, 'GpCa': 9, 'Gto_tmp': 10, 'H': 11, 'Khp': 12, 'Kki': 13, 'Kko': 14, 'KmBSL': 15, 'KmBSR': 16, 'KmCaAct': 17, 'KmCaM': 18, 'KmCaMK': 19, 'Kmgatp': 20, 'Kmn': 21, 'Knai0': 22, 'Knao0': 23, 'Knap': 24, 'Kxkur': 25, 'L': 26, 'MgADP': 27, 'MgATP': 28, 'PCab': 29, 'PKNa': 30, 'PNab': 31, 'Pnak_tmp': 32, 'R': 33, 'T': 34, 'aCaMK': 35, 'amp': 36, 'bCaMK': 37, 'bt': 38, 'cao': 39, 'celltype': 40, 'cmdnmax_tmp': 41, 'csqnmax': 42, 'delta': 43, 'delta_epi_tmp': 44, 'duration': 45, 'eP': 46, 'k1m': 47, 'k1p': 48, 'k2m': 49, 'k2n': 50, 'k2p': 51, 'k3m': 52, 'k3p': 53, 'k4m': 54, 'k4p': 55, 'kasymm': 56, 'kcaoff': 57, 'kcaon': 58, 'kmcmdn': 59, 'kmcsqn': 60, 'kmtrpn': 61, 'kna1': 62, 'kna2': 63, 'kna3': 64, 'ko': 65, 'nao': 66, 'qca': 67, 'qna': 68, 'rad': 69, 'scale_HF_CaMKa': 70, 'scale_HF_GK1': 71, 'scale_HF_GNaL': 72, 'scale_HF_Gncx': 73, 'scale_HF_Gto': 74, 'scale_HF_Jleak': 75, 'scale_HF_Jrel_inf': 76, 'scale_HF_Jup': 77, 'scale_HF_Pnak': 78, 'scale_HF_cat50_ref': 79, 'scale_HF_thL': 80, 'scale_ICaL': 81, 'scale_IK1': 82, 'scale_IKr': 83, 'scale_IKs': 84, 'scale_INaL': 85, 'scale_drug_ICaL': 86, 'scale_drug_ICab': 87, 'scale_drug_IK1': 88, 'scale_drug_IKb': 89, 'scale_drug_IKr': 90, 'scale_drug_IKs': 91, 'scale_drug_INa': 92, 'scale_drug_INaL': 93, 'scale_drug_INab': 94, 'scale_drug_IpCa': 95, 'scale_drug_Isack': 96, 'scale_drug_Isacns': 97, 'scale_drug_Ito': 98, 'scale_sex_GCaL_EFP_female': 99, 'scale_sex_GCaL_EFP_male': 100, 'scale_sex_GCaL_female': 101, 'scale_sex_GCaL_male': 102, 'scale_sex_GJup_female': 103, 'scale_sex_GJup_male': 104, 'scale_sex_GK1_female': 105, 'scale_sex_GK1_male': 106, 'scale_sex_GKb_female': 107, 'scale_sex_GKb_male': 108, 'scale_sex_GKr_EFP_female': 109, 'scale_sex_GKr_EFP_male': 110, 'scale_sex_GKr_female': 111, 'scale_sex_GKr_male': 112, 'scale_sex_GKs_EFP_female': 113, 'scale_sex_GKs_EFP_male': 114, 'scale_sex_GKs_female': 115, 'scale_sex_GKs_male': 116, 'scale_sex_GNCX_female': 117, 'scale_sex_GNCX_male': 118, 'scale_sex_GNaL_female': 119, 'scale_sex_GNaL_male': 120, 'scale_sex_GNa_female': 121, 'scale_sex_GNa_male': 122, 'scale_sex_GpCa_female': 123, 'scale_sex_GpCa_male': 124, 'scale_sex_Gtos_female': 125, 'scale_sex_Gtos_male': 126, 'scale_sex_PNaK_female': 127, 'scale_sex_PNaK_male': 128, 'scale_sex_calm_female': 129, 'scale_sex_calm_male': 130, 'sex': 131, 'thL': 132, 'tjca': 133, 'trpnmax': 134, 'wca': 135, 'wna': 136, 'wnaca': 137, 'zca': 138, 'zk': 139}


def parameter_index(name: str) -> int:
    """Return the index of the parameter with the given name

    Arguments
    ---------
    name : str
        The name of the parameter

    Returns
    -------
    int
        The index of the parameter

    Raises
    ------
    KeyError
        If the name is not a valid parameter
    """

    return parameter[name]


state = {'hL': 0, 'a': 1, 'ap': 2, 'd': 3, 'ff': 4, 'fs': 5, 'hf': 6, 'hs': 7, 'm': 8, 'xrf': 9, 'xrs': 10, 'xs1': 11, 'CaMKt': 12, 'xk1': 13, 'hLp': 14, 'fcaf': 15, 'fcas': 16, 'jca': 17, 'j': 18, 'fcafp': 19, 'ffp': 20, 'hsp': 21, 'jp': 22, 'mL': 23, 'xs2': 24, 'nca': 25, 'iF': 26, 'iS': 27, 'iFp': 28, 'iSp': 29, 'cajsr': 30, 'cansr': 31, 'ki': 32, 'kss': 33, 'Jrelnp': 34, 'Jrelp': 35, 'cass': 36, 'nass': 37, 'cai': 38, 'nai': 39, 'v': 40}


def state_index(name: str) -> int:
    """Return the index of the state with the given name

    Arguments
    ---------
    name : str
        The name of the state

    Returns
    -------
    int
        The index of the state

    Raises
    ------
    KeyError
        If the name is not a valid state
    """

    return state[name]


monitor = {'zna': 0, 'Afcaf': 1, 'AiF': 2, 'Axrf': 3, 'ass': 4, 'assp': 5, 'dss': 6, 'dti_develop': 7, 'dti_recover': 8, 'fss': 9, 'hLss': 10, 'hLssp': 11, 'hss': 12, 'hssp': 13, 'iss': 14, 'mLss': 15, 'mss': 16, 'rkr': 17, 'ta': 18, 'td': 19, 'tfcaf': 20, 'tfcas': 21, 'tff': 22, 'tfs': 23, 'thf': 24, 'ths': 25, 'tj': 26, 'tm': 27, 'txk1': 28, 'txrf': 29, 'txrs': 30, 'txs1': 31, 'txs2': 32, 'xkb': 33, 'xrss': 34, 'xs1ss': 35, 'Afs': 36, 'Ageo': 37, 'vcell': 38, 'Ahs': 39, 'Jupnp_tmp': 40, 'Jupp_tmp': 41, 'KsCa': 42, 'Bcajsr': 43, 'Jdiff': 44, 'Bcass': 45, 'CaMKb': 46, 'vffrt': 47, 'vfrt': 48, 'rk1': 49, 'xk1ss': 50, 'EK': 51, 'EKs': 52, 'ENa': 53, 'GK1_tmp': 54, 'GKb': 55, 'GKr_tmp': 56, 'GKs_tmp': 57, 'GNaL_tmp': 58, 'Gncx_12': 59, 'Gto': 60, 'km2n': 61, 'Istim': 62, 'JdiffK': 63, 'JdiffNa': 64, 'Jleak': 65, 'Jtr': 66, 'Knai': 67, 'Knao': 68, 'P': 69, 'PCa_tmp': 70, 'Pnak_12': 71, 'a2': 72, 'a4': 73, 'a_rel': 74, 'btp': 75, 'tau_rel_tmp': 76, 'allo_i': 77, 'allo_ss': 78, 'b1': 79, 'delta_epi': 80, 'h10': 81, 'h10_i': 82, 'h4': 83, 'h4_i': 84, 'hca': 85, 'hna': 86, 'k2': 87, 'k2_i': 88, 'k5': 89, 'k5_i': 90, 'scale_sex_GCaL_EFP': 91, 'scale_sex_GJup': 92, 'scale_sex_GK1': 93, 'scale_sex_GKb': 94, 'scale_sex_GKr_EFP': 95, 'scale_sex_GKs_EFP': 96, 'scale_sex_GNCX': 97, 'scale_sex_GNa': 98, 'scale_sex_GNaL': 99, 'scale_sex_GpCa': 100, 'scale_sex_Gtos': 101, 'scale_sex_PNaK': 102, 'scale_sex_calm': 103, 'thLp': 104, 'Afcas': 105, 'AiS': 106, 'Axrs': 107, 'fcass': 108, 'dhL_dt': 109, 'jss': 110, 'da_dt': 111, 'dap_dt': 112, 'dd_dt': 113, 'tfcafp': 114, 'tffp': 115, 'dff_dt': 116, 'dfs_dt': 117, 'dhf_dt': 118, 'thsp': 119, 'dhs_dt': 120, 'tjp': 121, 'tmL': 122, 'dm_dt': 123, 'dxrf_dt': 124, 'dxrs_dt': 125, 'xs2ss': 126, 'dxs1_dt': 127, 'f': 128, 'fp': 129, 'Acap': 130, 'vjsr': 131, 'vmyo': 132, 'vnsr': 133, 'vss': 134, 'h': 135, 'hp': 136, 'Jupnp': 137, 'Jupp': 138, 'CaMKa': 139, 'dCaMKt_dt': 140, 'ICab': 141, 'INab': 142, 'PhiCaK': 143, 'PhiCaL': 144, 'PhiCaNa': 145, 'dxk1_dt': 146, 'GK1_12': 147, 'GKr_12': 148, 'GKs': 149, 'GNaL': 150, 'anca': 151, 'a1': 152, 'b4': 153, 'a3': 154, 'b2': 155, 'b3': 156, 'PCa_12': 157, 'Pnak': 158, 'a_relp': 159, 'tau_relp_tmp': 160, 'tau_rel': 161, 'tiF': 162, 'tiS': 163, 'h11': 164, 'h12': 165, 'h11_i': 166, 'h12_i': 167, 'h5': 168, 'h6': 169, 'h5_i': 170, 'h6_i': 171, 'h1': 172, 'h1_i': 173, 'h7': 174, 'h7_i': 175, 'scale_sex_GCaL': 176, 'IKb': 177, 'scale_sex_GKr': 178, 'scale_sex_GKs': 179, 'Gncx': 180, 'IpCa': 181, 'cmdnmax': 182, 'dhLp_dt': 183, 'fca': 184, 'fcap': 185, 'i': 186, 'ip': 187, 'xr': 188, 'dfcaf_dt': 189, 'dfcas_dt': 190, 'djca_dt': 191, 'dj_dt': 192, 'dfcafp_dt': 193, 'dffp_dt': 194, 'dhsp_dt': 195, 'djp_dt': 196, 'dmL_dt': 197, 'dxs2_dt': 198, 'fICaLp': 199, 'fINaLp': 200, 'fINap': 201, 'fItop': 202, 'fJrelp': 203, 'fJupp': 204, 'GK1': 205, 'GKr': 206, 'dnca_dt': 207, 'x2': 208, 'x1': 209, 'x3': 210, 'x4': 211, 'PCa': 212, 'tau_relp': 213, 'tiFp': 214, 'diF_dt': 215, 'tiSp': 216, 'diS_dt': 217, 'k1': 218, 'k1_i': 219, 'k6': 220, 'k6_i': 221, 'h2': 222, 'h3': 223, 'h2_i': 224, 'h3_i': 225, 'h8': 226, 'h9': 227, 'h8_i': 228, 'h9_i': 229, 'IKs': 230, 'Bcai': 231, 'INaL': 232, 'INa': 233, 'Ito': 234, 'Jrel': 235, 'Jup': 236, 'IK1': 237, 'IKr': 238, 'E1': 239, 'E2': 240, 'E3': 241, 'E4': 242, 'PCaK': 243, 'PCaNa': 244, 'PCap': 245, 'diFp_dt': 246, 'diSp_dt': 247, 'k4pp': 248, 'k7': 249, 'k4p_ss': 250, 'k4pp_i': 251, 'k7_i': 252, 'k4p_i': 253, 'k3pp': 254, 'k8': 255, 'k3p_ss': 256, 'k3pp_i': 257, 'k8_i': 258, 'k3p_i': 259, 'dcajsr_dt': 260, 'dcansr_dt': 261, 'JnakNa': 262, 'JnakK': 263, 'ICaL': 264, 'PCaKp': 265, 'PCaNap': 266, 'k4': 267, 'k4_i': 268, 'k3': 269, 'k3_i': 270, 'INaK': 271, 'Jrel_inf_tmp': 272, 'Jrel_infp_tmp': 273, 'ICaK': 274, 'ICaNa': 275, 'x2_ss': 276, 'x2_i': 277, 'x1_ss': 278, 'x3_ss': 279, 'x4_ss': 280, 'x1_i': 281, 'x3_i': 282, 'x4_i': 283, 'dki_dt': 284, 'Jrel_inf': 285, 'Jrel_infp': 286, 'dkss_dt': 287, 'E1_ss': 288, 'E2_ss': 289, 'E3_ss': 290, 'E4_ss': 291, 'E1_i': 292, 'E2_i': 293, 'E3_i': 294, 'E4_i': 295, 'dJrelnp_dt': 296, 'dJrelp_dt': 297, 'JncxCa_ss': 298, 'JncxNa_ss': 299, 'JncxCa_i': 300, 'JncxNa_i': 301, 'INaCa_ss': 302, 'INaCa_i': 303, 'dcass_dt': 304, 'dnass_dt': 305, 'dcai_dt': 306, 'dnai_dt': 307, 'dv_dt': 308}


def monitor_index(name: str) -> int:
    """Return the index of the monitor with the given name

    Arguments
    ---------
    name : str
        The name of the monitor

    Returns
    -------
    int
        The index of the monitor

    Raises
    ------
    KeyError
        If the name is not a valid monitor
    """

    return monitor[name]



def init_parameter_values(**values):
    """Initialize parameter values
    """
    #Aff=0.6, Ahf=0.99, BSLmax=1.124, BSRmax=0.047, CaMKo=0.05
    #F=96485.0, GKb_tmp=0.003, GNa=31, Gncx_tmp=0.0008
    #GpCa=0.0005, Gto_tmp=0.02, H=1e-07, Khp=1.698e-07, Kki=0.5
    #Kko=0.3582, KmBSL=0.0087, KmBSR=0.00087, KmCaAct=0.00015
    #KmCaM=0.0015, KmCaMK=0.15, Kmgatp=1.698e-07, Kmn=0.002
    #Knai0=9.073, Knao0=27.78, Knap=224.0, Kxkur=292.0, L=0.01
    #MgADP=0.05, MgATP=9.8, PCab=2.5e-08, PKNa=0.01833
    #PNab=3.75e-10, Pnak_tmp=30, R=8314.0, T=310.0, aCaMK=0.05
    #amp=-80.0, bCaMK=0.00068, bt=4.75, cao=1.8, celltype=0
    #cmdnmax_tmp=0.05, csqnmax=10.0, delta=-0.155
    #delta_epi_tmp=1.0, duration=0.5, eP=4.2, k1m=182.4, k1p=949.5
    #k2m=39.4, k2n=1000.0, k2p=687.2, k3m=79300.0, k3p=1899.0
    #k4m=40.0, k4p=639.0, kasymm=12.5, kcaoff=5000.0
    #kcaon=1500000.0, kmcmdn=0.00238, kmcsqn=0.8, kmtrpn=0.0005
    #kna1=15.0, kna2=5.0, kna3=88.12, ko=5.4, nao=140.0, qca=0.167
    #qna=0.5224, rad=0.0011, scale_HF_CaMKa=1.0, scale_HF_GK1=1.0
    #scale_HF_GNaL=1.0, scale_HF_Gncx=1.0, scale_HF_Gto=1.0
    #scale_HF_Jleak=1.0, scale_HF_Jrel_inf=1.0, scale_HF_Jup=1.0
    #scale_HF_Pnak=1.0, scale_HF_cat50_ref=1.0, scale_HF_thL=1.0
    #scale_ICaL=1.018, scale_IK1=1.414, scale_IKr=1.119
    #scale_IKs=1.648, scale_INaL=2.274, scale_drug_ICaL=1.0
    #scale_drug_ICab=1.0, scale_drug_IK1=1.0, scale_drug_IKb=1.0
    #scale_drug_IKr=1.0, scale_drug_IKs=1.0, scale_drug_INa=1.0
    #scale_drug_INaL=1.0, scale_drug_INab=1.0, scale_drug_IpCa=1.0
    #scale_drug_Isack=1.0, scale_drug_Isacns=1.0
    #scale_drug_Ito=1.0, scale_sex_GCaL_EFP_female=1.0
    #scale_sex_GCaL_EFP_male=0.82, scale_sex_GCaL_female=1.5798
    #scale_sex_GCaL_male=0.8462, scale_sex_GJup_female=0.9383
    #scale_sex_GJup_male=0.9594, scale_sex_GK1_female=0.5367
    #scale_sex_GK1_male=1.0628, scale_sex_GKb_female=1.7695
    #scale_sex_GKb_male=0.7998, scale_sex_GKr_EFP_female=0.98
    #scale_sex_GKr_EFP_male=1.0, scale_sex_GKr_female=0.9298
    #scale_sex_GKr_male=0.8638, scale_sex_GKs_EFP_female=1.19
    #scale_sex_GKs_EFP_male=1.4, scale_sex_GKs_female=0.791
    #scale_sex_GKs_male=1.0578, scale_sex_GNCX_female=0.8128
    #scale_sex_GNCX_male=1.0253, scale_sex_GNaL_female=1.1395
    #scale_sex_GNaL_male=1.4378, scale_sex_GNa_female=1.1395
    #scale_sex_GNa_male=1.4378, scale_sex_GpCa_female=1.0027
    #scale_sex_GpCa_male=0.9706, scale_sex_Gtos_female=0.8499
    #scale_sex_Gtos_male=1.3478, scale_sex_PNaK_female=0.2958
    #scale_sex_PNaK_male=0.3018, scale_sex_calm_female=1.4384
    #scale_sex_calm_male=1.0496, sex=0, thL=200.0, tjca=75.0
    #trpnmax=0.07, wca=60000.0, wna=60000.0, wnaca=5000.0, zca=2.0
    #zk=1.0

    parameters = numpy.array([0.6, 0.99, 1.124, 0.047, 0.05, 96485.0, 0.003, 31, 0.0008, 0.0005, 0.02, 1e-07, 1.698e-07, 0.5, 0.3582, 0.0087, 0.00087, 0.00015, 0.0015, 0.15, 1.698e-07, 0.002, 9.073, 27.78, 224.0, 292.0, 0.01, 0.05, 9.8, 2.5e-08, 0.01833, 3.75e-10, 30, 8314.0, 310.0, 0.05, -80.0, 0.00068, 4.75, 1.8, 0, 0.05, 10.0, -0.155, 1.0, 0.5, 4.2, 182.4, 949.5, 39.4, 1000.0, 687.2, 79300.0, 1899.0, 40.0, 639.0, 12.5, 5000.0, 1500000.0, 0.00238, 0.8, 0.0005, 15.0, 5.0, 88.12, 5.4, 140.0, 0.167, 0.5224, 0.0011, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.018, 1.414, 1.119, 1.648, 2.274, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.82, 1.5798, 0.8462, 0.9383, 0.9594, 0.5367, 1.0628, 1.7695, 0.7998, 0.98, 1.0, 0.9298, 0.8638, 1.19, 1.4, 0.791, 1.0578, 0.8128, 1.0253, 1.1395, 1.4378, 1.1395, 1.4378, 1.0027, 0.9706, 0.8499, 1.3478, 0.2958, 0.3018, 1.4384, 1.0496, 0, 200.0, 75.0, 0.07, 60000.0, 60000.0, 5000.0, 2.0, 1.0], dtype=numpy.float64)

    for key, value in values.items():
        parameters[parameter_index(key)] = value

    return parameters


def init_state_values(**values):
    """Initialize state values
    """
    #hL=1, a=0, ap=0, d=0, ff=1, fs=1, hf=1, hs=1, m=0, xrf=0
    #xrs=0, xs1=0, CaMKt=0, xk1=1, hLp=1, fcaf=1, fcas=1, jca=1
    #j=1, fcafp=1, ffp=1, hsp=1, jp=1, mL=0, xs2=0, nca=0, iF=1
    #iS=1, iFp=1, iSp=1, cajsr=1.2, cansr=1.2, ki=145, kss=145
    #Jrelnp=0, Jrelp=0, cass=0.0001, nass=7, cai=0.0001, nai=7
    #v=-87

    states = numpy.array([1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1.2, 1.2, 145, 145, 0, 0, 0.0001, 7, 0.0001, 7, -87], dtype=numpy.float64)

    for key, value in values.items():
        states[state_index(key)] = value

    return states


def rhs(t, states, parameters):

    # Assign states
    hL = states[0]
    a = states[1]
    ap = states[2]
    d = states[3]
    ff = states[4]
    fs = states[5]
    hf = states[6]
    hs = states[7]
    m = states[8]
    xrf = states[9]
    xrs = states[10]
    xs1 = states[11]
    CaMKt = states[12]
    xk1 = states[13]
    hLp = states[14]
    fcaf = states[15]
    fcas = states[16]
    jca = states[17]
    j = states[18]
    fcafp = states[19]
    ffp = states[20]
    hsp = states[21]
    jp = states[22]
    mL = states[23]
    xs2 = states[24]
    nca = states[25]
    iF = states[26]
    iS = states[27]
    iFp = states[28]
    iSp = states[29]
    cajsr = states[30]
    cansr = states[31]
    ki = states[32]
    kss = states[33]
    Jrelnp = states[34]
    Jrelp = states[35]
    cass = states[36]
    nass = states[37]
    cai = states[38]
    nai = states[39]
    v = states[40]

    # Assign parameters
    Aff = parameters[0]
    Ahf = parameters[1]
    BSLmax = parameters[2]
    BSRmax = parameters[3]
    CaMKo = parameters[4]
    F = parameters[5]
    GKb_tmp = parameters[6]
    GNa = parameters[7]
    Gncx_tmp = parameters[8]
    GpCa = parameters[9]
    Gto_tmp = parameters[10]
    H = parameters[11]
    Khp = parameters[12]
    Kki = parameters[13]
    Kko = parameters[14]
    KmBSL = parameters[15]
    KmBSR = parameters[16]
    KmCaAct = parameters[17]
    KmCaM = parameters[18]
    KmCaMK = parameters[19]
    Kmgatp = parameters[20]
    Kmn = parameters[21]
    Knai0 = parameters[22]
    Knao0 = parameters[23]
    Knap = parameters[24]
    Kxkur = parameters[25]
    L = parameters[26]
    MgADP = parameters[27]
    MgATP = parameters[28]
    PCab = parameters[29]
    PKNa = parameters[30]
    PNab = parameters[31]
    Pnak_tmp = parameters[32]
    R = parameters[33]
    T = parameters[34]
    aCaMK = parameters[35]
    amp = parameters[36]
    bCaMK = parameters[37]
    bt = parameters[38]
    cao = parameters[39]
    celltype = parameters[40]
    cmdnmax_tmp = parameters[41]
    csqnmax = parameters[42]
    delta = parameters[43]
    delta_epi_tmp = parameters[44]
    duration = parameters[45]
    eP = parameters[46]
    k1m = parameters[47]
    k1p = parameters[48]
    k2m = parameters[49]
    k2n = parameters[50]
    k2p = parameters[51]
    k3m = parameters[52]
    k3p = parameters[53]
    k4m = parameters[54]
    k4p = parameters[55]
    kasymm = parameters[56]
    kcaoff = parameters[57]
    kcaon = parameters[58]
    kmcmdn = parameters[59]
    kmcsqn = parameters[60]
    kmtrpn = parameters[61]
    kna1 = parameters[62]
    kna2 = parameters[63]
    kna3 = parameters[64]
    ko = parameters[65]
    nao = parameters[66]
    qca = parameters[67]
    qna = parameters[68]
    rad = parameters[69]
    scale_HF_CaMKa = parameters[70]
    scale_HF_GK1 = parameters[71]
    scale_HF_GNaL = parameters[72]
    scale_HF_Gncx = parameters[73]
    scale_HF_Gto = parameters[74]
    scale_HF_Jleak = parameters[75]
    scale_HF_Jrel_inf = parameters[76]
    scale_HF_Jup = parameters[77]
    scale_HF_Pnak = parameters[78]
    scale_HF_cat50_ref = parameters[79]
    scale_HF_thL = parameters[80]
    scale_ICaL = parameters[81]
    scale_IK1 = parameters[82]
    scale_IKr = parameters[83]
    scale_IKs = parameters[84]
    scale_INaL = parameters[85]
    scale_drug_ICaL = parameters[86]
    scale_drug_ICab = parameters[87]
    scale_drug_IK1 = parameters[88]
    scale_drug_IKb = parameters[89]
    scale_drug_IKr = parameters[90]
    scale_drug_IKs = parameters[91]
    scale_drug_INa = parameters[92]
    scale_drug_INaL = parameters[93]
    scale_drug_INab = parameters[94]
    scale_drug_IpCa = parameters[95]
    scale_drug_Isack = parameters[96]
    scale_drug_Isacns = parameters[97]
    scale_drug_Ito = parameters[98]
    scale_sex_GCaL_EFP_female = parameters[99]
    scale_sex_GCaL_EFP_male = parameters[100]
    scale_sex_GCaL_female = parameters[101]
    scale_sex_GCaL_male = parameters[102]
    scale_sex_GJup_female = parameters[103]
    scale_sex_GJup_male = parameters[104]
    scale_sex_GK1_female = parameters[105]
    scale_sex_GK1_male = parameters[106]
    scale_sex_GKb_female = parameters[107]
    scale_sex_GKb_male = parameters[108]
    scale_sex_GKr_EFP_female = parameters[109]
    scale_sex_GKr_EFP_male = parameters[110]
    scale_sex_GKr_female = parameters[111]
    scale_sex_GKr_male = parameters[112]
    scale_sex_GKs_EFP_female = parameters[113]
    scale_sex_GKs_EFP_male = parameters[114]
    scale_sex_GKs_female = parameters[115]
    scale_sex_GKs_male = parameters[116]
    scale_sex_GNCX_female = parameters[117]
    scale_sex_GNCX_male = parameters[118]
    scale_sex_GNaL_female = parameters[119]
    scale_sex_GNaL_male = parameters[120]
    scale_sex_GNa_female = parameters[121]
    scale_sex_GNa_male = parameters[122]
    scale_sex_GpCa_female = parameters[123]
    scale_sex_GpCa_male = parameters[124]
    scale_sex_Gtos_female = parameters[125]
    scale_sex_Gtos_male = parameters[126]
    scale_sex_PNaK_female = parameters[127]
    scale_sex_PNaK_male = parameters[128]
    scale_sex_calm_female = parameters[129]
    scale_sex_calm_male = parameters[130]
    sex = parameters[131]
    thL = parameters[132]
    tjca = parameters[133]
    trpnmax = parameters[134]
    wca = parameters[135]
    wna = parameters[136]
    wnaca = parameters[137]
    zca = parameters[138]
    zk = parameters[139]

    # Assign expressions

    values = numpy.zeros_like(states, dtype=numpy.float64)
    zna = 1.0
    Afcaf = 0.3 + 0.6/(numpy.exp((v - 10.0)/10.0) + 1.0)
    AiF = 1.0/(numpy.exp((v - 213.6)/151.2) + 1.0)
    Axrf = 1.0/(numpy.exp((v + 54.81)/38.21) + 1.0)
    ass = 1.0/(numpy.exp((-(v - 14.34))/14.82) + 1.0)
    assp = 1.0/(numpy.exp((-(v - 24.34))/14.82) + 1.0)
    dss = 1.0/(numpy.exp((-(v + 3.94))/4.23) + 1.0)
    dti_develop = 1.354 + 0.0001/(numpy.exp((-(v - 12.23))/0.2154) + numpy.exp((v - 167.4)/15.89))
    dti_recover = 1.0 - 0.5/(numpy.exp((v + 70.0)/20.0) + 1.0)
    fss = 1.0/(numpy.exp((v + 19.58)/3.696) + 1.0)
    hLss = 1.0/(numpy.exp((v + 87.61)/7.488) + 1.0)
    hLssp = 1.0/(numpy.exp((v + 93.81)/7.488) + 1.0)
    hss = 1.0/(numpy.exp((v + 78.5)/6.22) + 1)
    hssp = 1.0/(numpy.exp(((v + 78.5) + 6.2)/6.22) + 1)
    iss = 1.0/(numpy.exp((v + 43.94)/5.711) + 1.0)
    mLss = 1.0/(numpy.exp((-(v + 42.85))/5.264) + 1.0)
    mss = 1.0/(numpy.exp((-((v + 39.57) + 9.4))/7.5) + 1.0)
    rkr = (1.0*(1.0/(numpy.exp((v + 55.0)/75.0) + 1.0)))/(numpy.exp((v - 10.0)/30.0) + 1.0)
    ta = 1.0515/(1.0/((1.2089*(numpy.exp((-(v - 18.4099))/29.3814) + 1.0))) + 3.5/(numpy.exp((v + 100.0)/29.3814) + 1.0))
    td = 0.6 + 1.0/(numpy.exp((-0.05)*(v + 6.0)) + numpy.exp(0.09*(v + 14.0)))
    tfcaf = 7.0 + 1.0/(0.04*numpy.exp((-(v - 4.0))/7.0) + 0.04*numpy.exp((v - 4.0)/7.0))
    tfcas = 100.0 + 1.0/(0.00012*numpy.exp((-v)/3.0) + 0.00012*numpy.exp(v/7.0))
    tff = 7.0 + 1.0/(0.0045*numpy.exp((-(v + 20.0))/10.0) + 0.0045*numpy.exp((v + 20.0)/10.0))
    tfs = 1000.0 + 1.0/(3.5e-05*numpy.exp((-(v + 5.0))/4.0) + 3.5e-05*numpy.exp((v + 5.0)/6.0))
    thf = 1.0/(6.149*numpy.exp((v + 0.5096)/20.27) + 1.432e-05*numpy.exp((-(v + 1.196))/6.285))
    ths = 1.0/(0.009794*numpy.exp((-(v + 17.95))/28.05) + 0.3343*numpy.exp((v + 5.73)/56.66))
    tj = 2.038 + 1.0/(0.3052*numpy.exp((v + 0.9941)/38.45) + 0.02136*numpy.exp((-(v + 100.6))/8.281))
    tm = 1.0/(6.765*numpy.exp((v + 11.64)/34.77) + 8.552*numpy.exp((-(v + 77.42))/5.955))
    txk1 = 122.2/(numpy.exp((-(v + 127.2))/20.36) + numpy.exp((v + 236.8)/69.33))
    txrf = 12.98 + 1.0/(4.123e-05*numpy.exp((-(v - 47.78))/20.38) + 0.3652*numpy.exp((v - 31.66)/3.869))
    txrs = 1.865 + 1.0/(1.128e-05*numpy.exp((-(v - 29.74))/25.94) + 0.06629*numpy.exp((v - 34.7)/7.355))
    txs1 = 817.3 + 1.0/(0.0002326*numpy.exp((v + 48.28)/17.8) + 0.001292*numpy.exp((-(v + 210.0))/230.0))
    txs2 = 1.0/(0.01*numpy.exp((v - 50.0)/20.0) + 0.0193*numpy.exp((-(v + 66.54))/31.0))
    xkb = 1.0/(numpy.exp((-(v - 14.48))/18.34) + 1.0)
    xrss = 1.0/(numpy.exp((-(v + 8.337))/6.789) + 1.0)
    xs1ss = 1.0/(numpy.exp((-(v + 11.6))/8.932) + 1.0)
    Afs = 1.0 - Aff
    Ageo = L*((2*3.14)*rad) + rad*((2*3.14)*rad)
    vcell = L*(rad*((3.14*1000)*rad))
    Ahs = 1.0 - Ahf
    Jupnp_tmp = (0.004375*cai)/(cai + 0.00092)
    Jupp_tmp = ((0.004375*2.75)*cai)/((cai + 0.00092) - 0.00017)
    KsCa = 1.0 + 0.6/((3.8e-05/cai)**1.4 + 1.0)
    Bcajsr = 1.0/((csqnmax*kmcsqn)/(cajsr + kmcsqn)**2.0 + 1.0)
    Jdiff = (-cai + cass)/0.2
    Bcass = 1.0/((BSLmax*KmBSL)/(KmBSL + cass)**2.0 + ((BSRmax*KmBSR)/(KmBSR + cass)**2.0 + 1.0))
    CaMKb = (CaMKo*(1.0 - CaMKt))/(KmCaM/cass + 1.0)
    vffrt = (F*(F*v))/((R*T))
    vfrt = (F*v)/((R*T))
    rk1 = 1.0/(numpy.exp((-2.6*ko + (v + 105.8))/9.493) + 1.0)
    xk1ss = 1.0/(numpy.exp((-((2.5538*ko + v) + 144.59))/(1.5692*ko + 3.8115)) + 1.0)
    EK = ((R*T)/F)*numpy.log(ko/ki)
    EKs = ((R*T)/F)*numpy.log((PKNa*nao + ko)/(PKNa*nai + ki))
    ENa = ((R*T)/F)*numpy.log(nao/nai)
    GK1_tmp = scale_HF_GK1*((0.1908*scale_IK1)*scale_drug_IK1)
    GKb = numpy.where((celltype == 1), 0.6*GKb_tmp, GKb_tmp)
    GKr_tmp = (0.046*scale_IKr)*scale_drug_IKr
    GKs_tmp = (0.0034*scale_IKs)*scale_drug_IKs
    GNaL_tmp = scale_HF_GNaL*((0.0075*scale_INaL)*scale_drug_INaL)
    Gncx_12 = numpy.where((celltype == 1), 1.1*Gncx_tmp, 1.4*Gncx_tmp)
    Gto = numpy.where((celltype == 0), Gto_tmp, 4.0*Gto_tmp)
    km2n = 1.0*jca
    Istim = numpy.where((duration >= t), amp, 0)
    JdiffK = (-ki + kss)/2.0
    JdiffNa = (-nai + nass)/2.0
    Jleak = ((0.0039375*cansr)*scale_HF_Jleak)/15.0
    Jtr = (-cajsr + cansr)/100.0
    Knai = Knai0*numpy.exp((F*(delta*v))/(((3.0*R)*T)))
    Knao = Knao0*numpy.exp((F*(v*(1.0 - delta)))/(((3.0*R)*T)))
    P = eP/(((H/Khp + 1.0) + nai/Knap) + ki/Kxkur)
    PCa_tmp = (0.0001*scale_ICaL)*scale_drug_ICaL
    Pnak_12 = numpy.where((celltype == 1), 0.9*Pnak_tmp, 0.7*Pnak_tmp)
    a2 = k2p
    a4 = ((MgATP*k4p)/Kmgatp)/(1.0 + MgATP/Kmgatp)
    a_rel = 0.5*bt
    btp = 1.25*bt
    tau_rel_tmp = bt/(1.0 + 0.0123/cajsr)
    allo_i = 1.0/((KmCaAct/cai)**2.0 + 1.0)
    allo_ss = 1.0/((KmCaAct/cass)**2.0 + 1.0)
    b1 = MgADP*k1m
    delta_epi = numpy.where((celltype == 1), delta_epi_tmp - 0.95/(numpy.exp((v + 70.0)/5.0) + 1.0), delta_epi_tmp)
    h10 = (nao/kna1)*(1 + nao/kna2) + (kasymm + 1.0)
    h10_i = (nao/kna1)*(1.0 + nao/kna2) + (kasymm + 1.0)
    h4 = (nass/kna1)*(1 + nass/kna2) + 1.0
    h4_i = (nai/kna1)*(1 + nai/kna2) + 1.0
    hca = numpy.exp((F*(qca*v))/((R*T)))
    hna = numpy.exp((F*(qna*v))/((R*T)))
    k2 = kcaoff
    k2_i = kcaoff
    k5 = kcaoff
    k5_i = kcaoff
    scale_sex_GCaL_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GCaL_EFP_male, scale_sex_GCaL_EFP_female))
    scale_sex_GJup = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GJup_male, scale_sex_GJup_female))
    scale_sex_GK1 = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GK1_male, scale_sex_GK1_female))
    scale_sex_GKb = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKb_male, scale_sex_GKb_female))
    scale_sex_GKr_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKr_EFP_male, scale_sex_GKr_EFP_female))
    scale_sex_GKs_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKs_EFP_male, scale_sex_GKs_EFP_female))
    scale_sex_GNCX = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNCX_male, scale_sex_GNCX_female))
    scale_sex_GNa = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNa_male, scale_sex_GNa_female))
    scale_sex_GNaL = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNaL_male, scale_sex_GNaL_female))
    scale_sex_GpCa = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GpCa_male, scale_sex_GpCa_female))
    scale_sex_Gtos = numpy.where((sex == 0), 1.0, scale_sex_Gtos_male)
    scale_sex_PNaK = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_PNaK_male, scale_sex_PNaK_female))
    scale_sex_calm = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_calm_male, scale_sex_calm_female))
    thLp = scale_HF_thL*(3.0*thL)
    Afcas = 1.0 - Afcaf
    AiS = 1.0 - AiF
    Axrs = 1.0 - Axrf
    fcass = fss
    dhL_dt = (-hL + hLss)/((scale_HF_thL*thL))
    values[0] = dhL_dt
    jss = hss
    da_dt = (-a + ass)/ta
    values[1] = da_dt
    dap_dt = (-ap + assp)/ta
    values[2] = dap_dt
    dd_dt = (-d + dss)/td
    values[3] = dd_dt
    tfcafp = 2.5*tfcaf
    tffp = 2.5*tff
    dff_dt = (-ff + fss)/tff
    values[4] = dff_dt
    dfs_dt = (-fs + fss)/tfs
    values[5] = dfs_dt
    dhf_dt = (-hf + hss)/thf
    values[6] = dhf_dt
    thsp = 3.0*ths
    dhs_dt = (-hs + hss)/ths
    values[7] = dhs_dt
    tjp = 1.46*tj
    tmL = tm
    dm_dt = (-m + mss)/tm
    values[8] = dm_dt
    dxrf_dt = (-xrf + xrss)/txrf
    values[9] = dxrf_dt
    dxrs_dt = (-xrs + xrss)/txrs
    values[10] = dxrs_dt
    xs2ss = xs1ss
    dxs1_dt = (-xs1 + xs1ss)/txs1
    values[11] = dxs1_dt
    f = Aff*ff + Afs*fs
    fp = Aff*ffp + Afs*fs
    Acap = 2*Ageo
    vjsr = 0.0048*vcell
    vmyo = 0.68*vcell
    vnsr = 0.0552*vcell
    vss = 0.02*vcell
    h = Ahf*hf + Ahs*hs
    hp = Ahf*hf + Ahs*hsp
    Jupnp = numpy.where((celltype == 1), 1.3*Jupnp_tmp, Jupnp_tmp)
    Jupp = numpy.where((celltype == 1), 1.3*Jupp_tmp, Jupp_tmp)
    CaMKa = scale_HF_CaMKa*(CaMKb + CaMKt)
    dCaMKt_dt = -CaMKt*bCaMK + (CaMKb*aCaMK)*(CaMKb + CaMKt)
    values[12] = dCaMKt_dt
    ICab = ((vffrt*(4.0*(PCab*scale_drug_ICab)))*(cai*numpy.exp(2.0*vfrt) - 0.341*cao))/(numpy.exp(2.0*vfrt) - 1.0)
    INab = ((vffrt*(PNab*scale_drug_INab))*(nai*numpy.exp(vfrt) - nao))/(numpy.exp(vfrt) - 1.0)
    PhiCaK = ((1.0*vffrt)*(-0.75*ko + (0.75*kss)*numpy.exp(1.0*vfrt)))/(numpy.exp(1.0*vfrt) - 1.0)
    PhiCaL = ((4.0*vffrt)*(-0.341*cao + cass*numpy.exp(2.0*vfrt)))/(numpy.exp(2.0*vfrt) - 1.0)
    PhiCaNa = ((1.0*vffrt)*(-0.75*nao + (0.75*nass)*numpy.exp(1.0*vfrt)))/(numpy.exp(1.0*vfrt) - 1.0)
    dxk1_dt = (-xk1 + xk1ss)/txk1
    values[13] = dxk1_dt
    GK1_12 = numpy.where((celltype == 1), 1.2*GK1_tmp, 1.3*GK1_tmp)
    GKr_12 = numpy.where((celltype == 1), 1.3*GKr_tmp, 0.8*GKr_tmp)
    GKs = numpy.where((celltype == 1), 1.4*GKs_tmp, GKs_tmp)
    GNaL = numpy.where((celltype == 1), 0.6*GNaL_tmp, GNaL_tmp)
    anca = 1.0/(k2n/km2n + (Kmn/cass + 1.0)**4.0)
    a1 = (k1p*(nai/Knai)**3.0)/(((1.0 + ki/Kki)**2.0 + (1.0 + nai/Knai)**3.0) - 1.0)
    b4 = (k4m*(ki/Kki)**2.0)/(((1.0 + ki/Kki)**2.0 + (1.0 + nai/Knai)**3.0) - 1.0)
    a3 = (k3p*(ko/Kko)**2.0)/(((1.0 + ko/Kko)**2.0 + (1.0 + nao/Knao)**3.0) - 1.0)
    b2 = (k2m*(nao/Knao)**3.0)/(((1.0 + ko/Kko)**2.0 + (1.0 + nao/Knao)**3.0) - 1.0)
    b3 = (H*(P*k3m))/(1.0 + MgATP/Kmgatp)
    PCa_12 = numpy.where((celltype == 1), 1.2*PCa_tmp, 2.5*PCa_tmp)
    Pnak = numpy.where((celltype == 0), Pnak_tmp, Pnak_12)
    a_relp = 0.5*btp
    tau_relp_tmp = btp/(1.0 + 0.0123/cajsr)
    tau_rel = numpy.where((tau_rel_tmp < 0.001), 0.001, tau_rel_tmp)
    tiF = delta_epi*(1/(0.3933*numpy.exp((-(v + 100.0))/100.0) + 0.08004*numpy.exp((v + 50.0)/16.59))) + 4.562
    tiS = delta_epi*(1/(0.001416*numpy.exp((-(v + 96.52))/59.05) + 1.78e-08*numpy.exp((v + 114.1)/8.079))) + 23.62
    h11 = (nao*nao)/((kna2*(h10*kna1)))
    h12 = 1.0/h10
    h11_i = (nao*nao)/((kna2*(h10_i*kna1)))
    h12_i = 1.0/h10_i
    h5 = (nass*nass)/((kna2*(h4*kna1)))
    h6 = 1.0/h4
    h5_i = (nai*nai)/((kna2*(h4_i*kna1)))
    h6_i = 1.0/h4_i
    h1 = (nass/kna3)*(hna + 1) + 1
    h1_i = (nai/kna3)*(hna + 1) + 1
    h7 = (nao/kna3)*(1.0 + 1.0/hna) + 1.0
    h7_i = (nao/kna3)*(1.0 + 1.0/hna) + 1.0
    scale_sex_GCaL = scale_sex_GCaL_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GCaL_male, scale_sex_GCaL_female))
    IKb = (xkb*(scale_drug_IKb*(GKb*scale_sex_GKb)))*(-EK + v)
    scale_sex_GKr = scale_sex_GKr_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKr_male, scale_sex_GKr_female))
    scale_sex_GKs = scale_sex_GKs_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKs_male, scale_sex_GKs_female))
    Gncx = scale_sex_GNCX*numpy.where((celltype == 0), Gncx_tmp, Gncx_12)
    IpCa = (cai*(scale_drug_IpCa*(GpCa*scale_sex_GpCa)))/(cai + 0.0005)
    cmdnmax = scale_sex_calm*numpy.where((celltype == 1), 1.3*cmdnmax_tmp, cmdnmax_tmp)
    dhLp_dt = (-hLp + hLssp)/thLp
    values[14] = dhLp_dt
    fca = Afcaf*fcaf + Afcas*fcas
    fcap = Afcaf*fcafp + Afcas*fcas
    i = AiF*iF + scale_sex_Gtos*(AiS*iS)
    ip = AiF*iFp + scale_sex_Gtos*(AiS*iSp)
    xr = Axrf*xrf + Axrs*xrs
    dfcaf_dt = (-fcaf + fcass)/tfcaf
    values[15] = dfcaf_dt
    dfcas_dt = (-fcas + fcass)/tfcas
    values[16] = dfcas_dt
    djca_dt = (fcass - jca)/tjca
    values[17] = djca_dt
    dj_dt = (-j + jss)/tj
    values[18] = dj_dt
    dfcafp_dt = (-fcafp + fcass)/tfcafp
    values[19] = dfcafp_dt
    dffp_dt = (-ffp + fss)/tffp
    values[20] = dffp_dt
    dhsp_dt = (-hsp + hssp)/thsp
    values[21] = dhsp_dt
    djp_dt = (-jp + jss)/tjp
    values[22] = djp_dt
    dmL_dt = (-mL + mLss)/tmL
    values[23] = dmL_dt
    dxs2_dt = (-xs2 + xs2ss)/txs2
    values[24] = dxs2_dt
    fICaLp = 1.0/(1.0 + KmCaMK/CaMKa)
    fINaLp = 1.0/(1.0 + KmCaMK/CaMKa)
    fINap = 1.0/(1.0 + KmCaMK/CaMKa)
    fItop = 1.0/(1.0 + KmCaMK/CaMKa)
    fJrelp = 1.0/(1.0 + KmCaMK/CaMKa)
    fJupp = 1.0/(1.0 + KmCaMK/CaMKa)
    GK1 = numpy.where((celltype == 0), GK1_tmp, GK1_12)
    GKr = numpy.where((celltype == 0), GKr_tmp, GKr_12)
    dnca_dt = anca*k2n - km2n*nca
    values[25] = dnca_dt
    x2 = b4*(a2*a3) + (b4*(a3*b1) + (a3*(a1*a2) + b4*(b1*b2)))
    x1 = a2*(a1*b3) + (b3*(a2*b4) + (a2*(a1*a4) + b3*(b2*b4)))
    x3 = b1*(a3*a4) + (a4*(b1*b2) + (a4*(a2*a3) + b1*(b2*b3)))
    x4 = a1*(b2*b3) + (a1*(a4*b2) + (a1*(a3*a4) + b2*(b3*b4)))
    PCa = numpy.where((celltype == 0), PCa_tmp, PCa_12)
    tau_relp = numpy.where((tau_relp_tmp < 0.001), 0.001, tau_relp_tmp)
    tiFp = tiF*(dti_develop*dti_recover)
    diF_dt = (-iF + iss)/tiF
    values[26] = diF_dt
    tiSp = tiS*(dti_develop*dti_recover)
    diS_dt = (-iS + iss)/tiS
    values[27] = diS_dt
    k1 = kcaon*(cao*h12)
    k1_i = kcaon*(cao*h12_i)
    k6 = kcaon*(cass*h6)
    k6_i = kcaon*(cai*h6_i)
    h2 = (hna*nass)/((h1*kna3))
    h3 = 1.0/h1
    h2_i = (hna*nai)/((h1_i*kna3))
    h3_i = 1.0/h1_i
    h8 = nao/((h7*(hna*kna3)))
    h9 = 1.0/h7
    h8_i = nao/((h7_i*(hna*kna3)))
    h9_i = 1.0/h7_i
    IKs = (xs2*(xs1*(KsCa*(GKs*scale_sex_GKs))))*(-EKs + v)
    Bcai = 1.0/((kmtrpn*trpnmax)/(cai + kmtrpn)**2.0 + ((cmdnmax*kmcmdn)/(cai + kmcmdn)**2.0 + 1.0))
    INaL = (mL*((GNaL*scale_sex_GNaL)*(-ENa + v)))*(fINaLp*hLp + hL*(1.0 - fINaLp))
    INa = (m**3.0*((scale_drug_INa*(GNa*scale_sex_GNa))*(-ENa + v)))*(j*(h*(1.0 - fINap)) + jp*(fINap*hp))
    Ito = ((scale_HF_Gto*(Gto*scale_drug_Ito))*(-EK + v))*(i*(a*(1.0 - fItop)) + ip*(ap*fItop))
    Jrel = Jrelnp*(1.0 - fJrelp) + Jrelp*fJrelp
    Jup = -Jleak + (Jupnp*(scale_sex_GJup*(1.0 - fJupp)) + scale_HF_Jup*(Jupp*fJupp))
    IK1 = (xk1*(rk1*(numpy.sqrt(ko)*(GK1*scale_sex_GK1))))*(-EK + v)
    IKr = (rkr*(xr*((0.4303314829119352*numpy.sqrt(ko))*(GKr*scale_sex_GKr))))*(-EK + v)
    E1 = x1/(x4 + (x3 + (x1 + x2)))
    E2 = x2/(x4 + (x3 + (x1 + x2)))
    E3 = x3/(x4 + (x3 + (x1 + x2)))
    E4 = x4/(x4 + (x3 + (x1 + x2)))
    PCaK = 0.0003574*PCa
    PCaNa = 0.00125*PCa
    PCap = 1.1*PCa
    diFp_dt = (-iFp + iss)/tiFp
    values[28] = diFp_dt
    diSp_dt = (-iSp + iss)/tiSp
    values[29] = diSp_dt
    k4pp = h2*wnaca
    k7 = wna*(h2*h5)
    k4p_ss = (h3*wca)/hca
    k4pp_i = h2_i*wnaca
    k7_i = wna*(h2_i*h5_i)
    k4p_i = (h3_i*wca)/hca
    k3pp = h8*wnaca
    k8 = wna*(h11*h8)
    k3p_ss = h9*wca
    k3pp_i = h8_i*wnaca
    k8_i = wna*(h11_i*h8_i)
    k3p_i = h9_i*wca
    dcajsr_dt = Bcajsr*(-Jrel + Jtr)
    values[30] = dcajsr_dt
    dcansr_dt = Jup - (Jtr*vjsr)/vnsr
    values[31] = dcansr_dt
    JnakNa = 3.0*(E1*a3 - E2*b3)
    JnakK = 2.0*(-E3*a1 + E4*b1)
    ICaL = (d*(PhiCaL*(PCap*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca)) + (d*(PhiCaL*(PCa*(scale_sex_GCaL*(1.0 - fICaLp)))))*(f*(1.0 - nca) + nca*(fca*jca))
    PCaKp = 0.0003574*PCap
    PCaNap = 0.00125*PCap
    k4 = k4p_ss + k4pp
    k4_i = k4p_i + k4pp_i
    k3 = k3p_ss + k3pp
    k3_i = k3p_i + k3pp_i
    INaK = (scale_HF_Pnak*(Pnak*scale_sex_PNaK))*(JnakK*zk + JnakNa*zna)
    Jrel_inf_tmp = ((-ICaL)*a_rel)/(((1.5*scale_HF_Jrel_inf)/cajsr)**8.0 + 1.0)
    Jrel_infp_tmp = ((-ICaL)*a_relp)/(((1.5*scale_HF_Jrel_inf)/cajsr)**8.0 + 1.0)
    ICaK = (d*(PhiCaK*(PCaK*(1.0 - fICaLp))))*(f*(1.0 - nca) + nca*(fca*jca)) + (d*(PhiCaK*(PCaKp*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca))
    ICaNa = (d*(PhiCaNa*(PCaNa*(1.0 - fICaLp))))*(f*(1.0 - nca) + nca*(fca*jca)) + (d*(PhiCaNa*(PCaNap*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca))
    x2_ss = (k1*k7)*(k4 + k5) + (k4*k6)*(k1 + k8)
    x2_i = (k1_i*k7_i)*(k4_i + k5_i) + (k4_i*k6_i)*(k1_i + k8_i)
    x1_ss = (k2*k4)*(k6 + k7) + (k5*k7)*(k2 + k3)
    x3_ss = (k1*k3)*(k6 + k7) + (k6*k8)*(k2 + k3)
    x4_ss = (k2*k8)*(k4 + k5) + (k3*k5)*(k1 + k8)
    x1_i = (k2_i*k4_i)*(k6_i + k7_i) + (k5_i*k7_i)*(k2_i + k3_i)
    x3_i = (k1_i*k3_i)*(k6_i + k7_i) + (k6_i*k8_i)*(k2_i + k3_i)
    x4_i = (k2_i*k8_i)*(k4_i + k5_i) + (k3_i*k5_i)*(k1_i + k8_i)
    dki_dt = (Acap*(-(-2.0*INaK + (Istim + (IKb + (IK1 + (IKs + (IKr + Ito))))))))/((F*vmyo)) + (JdiffK*vss)/vmyo
    values[32] = dki_dt
    Jrel_inf = numpy.where((celltype == 2), 1.7*Jrel_inf_tmp, Jrel_inf_tmp)
    Jrel_infp = numpy.where((celltype == 2), 1.7*Jrel_infp_tmp, Jrel_infp_tmp)
    dkss_dt = -JdiffK + (Acap*(-ICaK))/((F*vss))
    values[33] = dkss_dt
    E1_ss = x1_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    E2_ss = x2_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    E3_ss = x3_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    E4_ss = x4_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    E1_i = x1_i/(x4_i + (x3_i + (x1_i + x2_i)))
    E2_i = x2_i/(x4_i + (x3_i + (x1_i + x2_i)))
    E3_i = x3_i/(x4_i + (x3_i + (x1_i + x2_i)))
    E4_i = x4_i/(x4_i + (x3_i + (x1_i + x2_i)))
    dJrelnp_dt = (Jrel_inf - Jrelnp)/tau_rel
    values[34] = dJrelnp_dt
    dJrelp_dt = (Jrel_infp - Jrelp)/tau_relp
    values[35] = dJrelp_dt
    JncxCa_ss = -E1_ss*k1 + E2_ss*k2
    JncxNa_ss = -E2_ss*k3pp + (E3_ss*k4pp + 3.0*(-E1_ss*k8 + E4_ss*k7))
    JncxCa_i = -E1_i*k1_i + E2_i*k2_i
    JncxNa_i = -E2_i*k3pp_i + (E3_i*k4pp_i + 3.0*(-E1_i*k8_i + E4_i*k7_i))
    INaCa_ss = (allo_ss*((0.2*Gncx)*scale_HF_Gncx))*(JncxCa_ss*zca + JncxNa_ss*zna)
    INaCa_i = (allo_i*((0.8*Gncx)*scale_HF_Gncx))*(JncxCa_i*zca + JncxNa_i*zna)
    dcass_dt = Bcass*(-Jdiff + ((Acap*(-(ICaL - 2.0*INaCa_ss)))/(((2.0*F)*vss)) + (Jrel*vjsr)/vss))
    values[36] = dcass_dt
    dnass_dt = -JdiffNa + (Acap*(-(ICaNa + 3.0*INaCa_ss)))/((F*vss))
    values[37] = dnass_dt
    dcai_dt = Bcai*(((Acap*(-(-2.0*INaCa_i + (ICab + IpCa))))/(((2.0*F)*vmyo)) - (Jup*vnsr)/vmyo) + (Jdiff*vss)/vmyo)
    values[38] = dcai_dt
    dnai_dt = (Acap*(-(INab + (3.0*INaK + (3.0*INaCa_i + (INa + INaL))))))/((F*vmyo)) + (JdiffNa*vss)/vmyo
    values[39] = dnai_dt
    dv_dt = -(Istim + (ICab + (IpCa + (IKb + (INab + (INaK + (INaCa_ss + (INaCa_i + (IK1 + (IKs + (IKr + (ICaK + (ICaNa + (ICaL + (Ito + (INa + INaL))))))))))))))))
    values[40] = dv_dt

    return values


def monitor_values(t, states, parameters):

    # Assign states
    hL = states[0]
    a = states[1]
    ap = states[2]
    d = states[3]
    ff = states[4]
    fs = states[5]
    hf = states[6]
    hs = states[7]
    m = states[8]
    xrf = states[9]
    xrs = states[10]
    xs1 = states[11]
    CaMKt = states[12]
    xk1 = states[13]
    hLp = states[14]
    fcaf = states[15]
    fcas = states[16]
    jca = states[17]
    j = states[18]
    fcafp = states[19]
    ffp = states[20]
    hsp = states[21]
    jp = states[22]
    mL = states[23]
    xs2 = states[24]
    nca = states[25]
    iF = states[26]
    iS = states[27]
    iFp = states[28]
    iSp = states[29]
    cajsr = states[30]
    cansr = states[31]
    ki = states[32]
    kss = states[33]
    Jrelnp = states[34]
    Jrelp = states[35]
    cass = states[36]
    nass = states[37]
    cai = states[38]
    nai = states[39]
    v = states[40]

    # Assign parameters
    Aff = parameters[0]
    Ahf = parameters[1]
    BSLmax = parameters[2]
    BSRmax = parameters[3]
    CaMKo = parameters[4]
    F = parameters[5]
    GKb_tmp = parameters[6]
    GNa = parameters[7]
    Gncx_tmp = parameters[8]
    GpCa = parameters[9]
    Gto_tmp = parameters[10]
    H = parameters[11]
    Khp = parameters[12]
    Kki = parameters[13]
    Kko = parameters[14]
    KmBSL = parameters[15]
    KmBSR = parameters[16]
    KmCaAct = parameters[17]
    KmCaM = parameters[18]
    KmCaMK = parameters[19]
    Kmgatp = parameters[20]
    Kmn = parameters[21]
    Knai0 = parameters[22]
    Knao0 = parameters[23]
    Knap = parameters[24]
    Kxkur = parameters[25]
    L = parameters[26]
    MgADP = parameters[27]
    MgATP = parameters[28]
    PCab = parameters[29]
    PKNa = parameters[30]
    PNab = parameters[31]
    Pnak_tmp = parameters[32]
    R = parameters[33]
    T = parameters[34]
    aCaMK = parameters[35]
    amp = parameters[36]
    bCaMK = parameters[37]
    bt = parameters[38]
    cao = parameters[39]
    celltype = parameters[40]
    cmdnmax_tmp = parameters[41]
    csqnmax = parameters[42]
    delta = parameters[43]
    delta_epi_tmp = parameters[44]
    duration = parameters[45]
    eP = parameters[46]
    k1m = parameters[47]
    k1p = parameters[48]
    k2m = parameters[49]
    k2n = parameters[50]
    k2p = parameters[51]
    k3m = parameters[52]
    k3p = parameters[53]
    k4m = parameters[54]
    k4p = parameters[55]
    kasymm = parameters[56]
    kcaoff = parameters[57]
    kcaon = parameters[58]
    kmcmdn = parameters[59]
    kmcsqn = parameters[60]
    kmtrpn = parameters[61]
    kna1 = parameters[62]
    kna2 = parameters[63]
    kna3 = parameters[64]
    ko = parameters[65]
    nao = parameters[66]
    qca = parameters[67]
    qna = parameters[68]
    rad = parameters[69]
    scale_HF_CaMKa = parameters[70]
    scale_HF_GK1 = parameters[71]
    scale_HF_GNaL = parameters[72]
    scale_HF_Gncx = parameters[73]
    scale_HF_Gto = parameters[74]
    scale_HF_Jleak = parameters[75]
    scale_HF_Jrel_inf = parameters[76]
    scale_HF_Jup = parameters[77]
    scale_HF_Pnak = parameters[78]
    scale_HF_cat50_ref = parameters[79]
    scale_HF_thL = parameters[80]
    scale_ICaL = parameters[81]
    scale_IK1 = parameters[82]
    scale_IKr = parameters[83]
    scale_IKs = parameters[84]
    scale_INaL = parameters[85]
    scale_drug_ICaL = parameters[86]
    scale_drug_ICab = parameters[87]
    scale_drug_IK1 = parameters[88]
    scale_drug_IKb = parameters[89]
    scale_drug_IKr = parameters[90]
    scale_drug_IKs = parameters[91]
    scale_drug_INa = parameters[92]
    scale_drug_INaL = parameters[93]
    scale_drug_INab = parameters[94]
    scale_drug_IpCa = parameters[95]
    scale_drug_Isack = parameters[96]
    scale_drug_Isacns = parameters[97]
    scale_drug_Ito = parameters[98]
    scale_sex_GCaL_EFP_female = parameters[99]
    scale_sex_GCaL_EFP_male = parameters[100]
    scale_sex_GCaL_female = parameters[101]
    scale_sex_GCaL_male = parameters[102]
    scale_sex_GJup_female = parameters[103]
    scale_sex_GJup_male = parameters[104]
    scale_sex_GK1_female = parameters[105]
    scale_sex_GK1_male = parameters[106]
    scale_sex_GKb_female = parameters[107]
    scale_sex_GKb_male = parameters[108]
    scale_sex_GKr_EFP_female = parameters[109]
    scale_sex_GKr_EFP_male = parameters[110]
    scale_sex_GKr_female = parameters[111]
    scale_sex_GKr_male = parameters[112]
    scale_sex_GKs_EFP_female = parameters[113]
    scale_sex_GKs_EFP_male = parameters[114]
    scale_sex_GKs_female = parameters[115]
    scale_sex_GKs_male = parameters[116]
    scale_sex_GNCX_female = parameters[117]
    scale_sex_GNCX_male = parameters[118]
    scale_sex_GNaL_female = parameters[119]
    scale_sex_GNaL_male = parameters[120]
    scale_sex_GNa_female = parameters[121]
    scale_sex_GNa_male = parameters[122]
    scale_sex_GpCa_female = parameters[123]
    scale_sex_GpCa_male = parameters[124]
    scale_sex_Gtos_female = parameters[125]
    scale_sex_Gtos_male = parameters[126]
    scale_sex_PNaK_female = parameters[127]
    scale_sex_PNaK_male = parameters[128]
    scale_sex_calm_female = parameters[129]
    scale_sex_calm_male = parameters[130]
    sex = parameters[131]
    thL = parameters[132]
    tjca = parameters[133]
    trpnmax = parameters[134]
    wca = parameters[135]
    wna = parameters[136]
    wnaca = parameters[137]
    zca = parameters[138]
    zk = parameters[139]

    # Assign expressions
    shape = 309 if len(states.shape) == 1 else (309, states.shape[1])
    values = numpy.zeros(shape)
    zna = 1.0
    values[0] = zna
    Afcaf = 0.3 + 0.6/(numpy.exp((v - 10.0)/10.0) + 1.0)
    values[1] = Afcaf
    AiF = 1.0/(numpy.exp((v - 213.6)/151.2) + 1.0)
    values[2] = AiF
    Axrf = 1.0/(numpy.exp((v + 54.81)/38.21) + 1.0)
    values[3] = Axrf
    ass = 1.0/(numpy.exp((-(v - 14.34))/14.82) + 1.0)
    values[4] = ass
    assp = 1.0/(numpy.exp((-(v - 24.34))/14.82) + 1.0)
    values[5] = assp
    dss = 1.0/(numpy.exp((-(v + 3.94))/4.23) + 1.0)
    values[6] = dss
    dti_develop = 1.354 + 0.0001/(numpy.exp((-(v - 12.23))/0.2154) + numpy.exp((v - 167.4)/15.89))
    values[7] = dti_develop
    dti_recover = 1.0 - 0.5/(numpy.exp((v + 70.0)/20.0) + 1.0)
    values[8] = dti_recover
    fss = 1.0/(numpy.exp((v + 19.58)/3.696) + 1.0)
    values[9] = fss
    hLss = 1.0/(numpy.exp((v + 87.61)/7.488) + 1.0)
    values[10] = hLss
    hLssp = 1.0/(numpy.exp((v + 93.81)/7.488) + 1.0)
    values[11] = hLssp
    hss = 1.0/(numpy.exp((v + 78.5)/6.22) + 1)
    values[12] = hss
    hssp = 1.0/(numpy.exp(((v + 78.5) + 6.2)/6.22) + 1)
    values[13] = hssp
    iss = 1.0/(numpy.exp((v + 43.94)/5.711) + 1.0)
    values[14] = iss
    mLss = 1.0/(numpy.exp((-(v + 42.85))/5.264) + 1.0)
    values[15] = mLss
    mss = 1.0/(numpy.exp((-((v + 39.57) + 9.4))/7.5) + 1.0)
    values[16] = mss
    rkr = (1.0*(1.0/(numpy.exp((v + 55.0)/75.0) + 1.0)))/(numpy.exp((v - 10.0)/30.0) + 1.0)
    values[17] = rkr
    ta = 1.0515/(1.0/((1.2089*(numpy.exp((-(v - 18.4099))/29.3814) + 1.0))) + 3.5/(numpy.exp((v + 100.0)/29.3814) + 1.0))
    values[18] = ta
    td = 0.6 + 1.0/(numpy.exp((-0.05)*(v + 6.0)) + numpy.exp(0.09*(v + 14.0)))
    values[19] = td
    tfcaf = 7.0 + 1.0/(0.04*numpy.exp((-(v - 4.0))/7.0) + 0.04*numpy.exp((v - 4.0)/7.0))
    values[20] = tfcaf
    tfcas = 100.0 + 1.0/(0.00012*numpy.exp((-v)/3.0) + 0.00012*numpy.exp(v/7.0))
    values[21] = tfcas
    tff = 7.0 + 1.0/(0.0045*numpy.exp((-(v + 20.0))/10.0) + 0.0045*numpy.exp((v + 20.0)/10.0))
    values[22] = tff
    tfs = 1000.0 + 1.0/(3.5e-05*numpy.exp((-(v + 5.0))/4.0) + 3.5e-05*numpy.exp((v + 5.0)/6.0))
    values[23] = tfs
    thf = 1.0/(6.149*numpy.exp((v + 0.5096)/20.27) + 1.432e-05*numpy.exp((-(v + 1.196))/6.285))
    values[24] = thf
    ths = 1.0/(0.009794*numpy.exp((-(v + 17.95))/28.05) + 0.3343*numpy.exp((v + 5.73)/56.66))
    values[25] = ths
    tj = 2.038 + 1.0/(0.3052*numpy.exp((v + 0.9941)/38.45) + 0.02136*numpy.exp((-(v + 100.6))/8.281))
    values[26] = tj
    tm = 1.0/(6.765*numpy.exp((v + 11.64)/34.77) + 8.552*numpy.exp((-(v + 77.42))/5.955))
    values[27] = tm
    txk1 = 122.2/(numpy.exp((-(v + 127.2))/20.36) + numpy.exp((v + 236.8)/69.33))
    values[28] = txk1
    txrf = 12.98 + 1.0/(4.123e-05*numpy.exp((-(v - 47.78))/20.38) + 0.3652*numpy.exp((v - 31.66)/3.869))
    values[29] = txrf
    txrs = 1.865 + 1.0/(1.128e-05*numpy.exp((-(v - 29.74))/25.94) + 0.06629*numpy.exp((v - 34.7)/7.355))
    values[30] = txrs
    txs1 = 817.3 + 1.0/(0.0002326*numpy.exp((v + 48.28)/17.8) + 0.001292*numpy.exp((-(v + 210.0))/230.0))
    values[31] = txs1
    txs2 = 1.0/(0.01*numpy.exp((v - 50.0)/20.0) + 0.0193*numpy.exp((-(v + 66.54))/31.0))
    values[32] = txs2
    xkb = 1.0/(numpy.exp((-(v - 14.48))/18.34) + 1.0)
    values[33] = xkb
    xrss = 1.0/(numpy.exp((-(v + 8.337))/6.789) + 1.0)
    values[34] = xrss
    xs1ss = 1.0/(numpy.exp((-(v + 11.6))/8.932) + 1.0)
    values[35] = xs1ss
    Afs = 1.0 - Aff
    values[36] = Afs
    Ageo = L*((2*3.14)*rad) + rad*((2*3.14)*rad)
    values[37] = Ageo
    vcell = L*(rad*((3.14*1000)*rad))
    values[38] = vcell
    Ahs = 1.0 - Ahf
    values[39] = Ahs
    Jupnp_tmp = (0.004375*cai)/(cai + 0.00092)
    values[40] = Jupnp_tmp
    Jupp_tmp = ((0.004375*2.75)*cai)/((cai + 0.00092) - 0.00017)
    values[41] = Jupp_tmp
    KsCa = 1.0 + 0.6/((3.8e-05/cai)**1.4 + 1.0)
    values[42] = KsCa
    Bcajsr = 1.0/((csqnmax*kmcsqn)/(cajsr + kmcsqn)**2.0 + 1.0)
    values[43] = Bcajsr
    Jdiff = (-cai + cass)/0.2
    values[44] = Jdiff
    Bcass = 1.0/((BSLmax*KmBSL)/(KmBSL + cass)**2.0 + ((BSRmax*KmBSR)/(KmBSR + cass)**2.0 + 1.0))
    values[45] = Bcass
    CaMKb = (CaMKo*(1.0 - CaMKt))/(KmCaM/cass + 1.0)
    values[46] = CaMKb
    vffrt = (F*(F*v))/((R*T))
    values[47] = vffrt
    vfrt = (F*v)/((R*T))
    values[48] = vfrt
    rk1 = 1.0/(numpy.exp((-2.6*ko + (v + 105.8))/9.493) + 1.0)
    values[49] = rk1
    xk1ss = 1.0/(numpy.exp((-((2.5538*ko + v) + 144.59))/(1.5692*ko + 3.8115)) + 1.0)
    values[50] = xk1ss
    EK = ((R*T)/F)*numpy.log(ko/ki)
    values[51] = EK
    EKs = ((R*T)/F)*numpy.log((PKNa*nao + ko)/(PKNa*nai + ki))
    values[52] = EKs
    ENa = ((R*T)/F)*numpy.log(nao/nai)
    values[53] = ENa
    GK1_tmp = scale_HF_GK1*((0.1908*scale_IK1)*scale_drug_IK1)
    values[54] = GK1_tmp
    GKb = numpy.where((celltype == 1), 0.6*GKb_tmp, GKb_tmp)
    values[55] = GKb
    GKr_tmp = (0.046*scale_IKr)*scale_drug_IKr
    values[56] = GKr_tmp
    GKs_tmp = (0.0034*scale_IKs)*scale_drug_IKs
    values[57] = GKs_tmp
    GNaL_tmp = scale_HF_GNaL*((0.0075*scale_INaL)*scale_drug_INaL)
    values[58] = GNaL_tmp
    Gncx_12 = numpy.where((celltype == 1), 1.1*Gncx_tmp, 1.4*Gncx_tmp)
    values[59] = Gncx_12
    Gto = numpy.where((celltype == 0), Gto_tmp, 4.0*Gto_tmp)
    values[60] = Gto
    km2n = 1.0*jca
    values[61] = km2n
    Istim = numpy.where((duration >= t), amp, 0)
    values[62] = Istim
    JdiffK = (-ki + kss)/2.0
    values[63] = JdiffK
    JdiffNa = (-nai + nass)/2.0
    values[64] = JdiffNa
    Jleak = ((0.0039375*cansr)*scale_HF_Jleak)/15.0
    values[65] = Jleak
    Jtr = (-cajsr + cansr)/100.0
    values[66] = Jtr
    Knai = Knai0*numpy.exp((F*(delta*v))/(((3.0*R)*T)))
    values[67] = Knai
    Knao = Knao0*numpy.exp((F*(v*(1.0 - delta)))/(((3.0*R)*T)))
    values[68] = Knao
    P = eP/(((H/Khp + 1.0) + nai/Knap) + ki/Kxkur)
    values[69] = P
    PCa_tmp = (0.0001*scale_ICaL)*scale_drug_ICaL
    values[70] = PCa_tmp
    Pnak_12 = numpy.where((celltype == 1), 0.9*Pnak_tmp, 0.7*Pnak_tmp)
    values[71] = Pnak_12
    a2 = k2p
    values[72] = a2
    a4 = ((MgATP*k4p)/Kmgatp)/(1.0 + MgATP/Kmgatp)
    values[73] = a4
    a_rel = 0.5*bt
    values[74] = a_rel
    btp = 1.25*bt
    values[75] = btp
    tau_rel_tmp = bt/(1.0 + 0.0123/cajsr)
    values[76] = tau_rel_tmp
    allo_i = 1.0/((KmCaAct/cai)**2.0 + 1.0)
    values[77] = allo_i
    allo_ss = 1.0/((KmCaAct/cass)**2.0 + 1.0)
    values[78] = allo_ss
    b1 = MgADP*k1m
    values[79] = b1
    delta_epi = numpy.where((celltype == 1), delta_epi_tmp - 0.95/(numpy.exp((v + 70.0)/5.0) + 1.0), delta_epi_tmp)
    values[80] = delta_epi
    h10 = (nao/kna1)*(1 + nao/kna2) + (kasymm + 1.0)
    values[81] = h10
    h10_i = (nao/kna1)*(1.0 + nao/kna2) + (kasymm + 1.0)
    values[82] = h10_i
    h4 = (nass/kna1)*(1 + nass/kna2) + 1.0
    values[83] = h4
    h4_i = (nai/kna1)*(1 + nai/kna2) + 1.0
    values[84] = h4_i
    hca = numpy.exp((F*(qca*v))/((R*T)))
    values[85] = hca
    hna = numpy.exp((F*(qna*v))/((R*T)))
    values[86] = hna
    k2 = kcaoff
    values[87] = k2
    k2_i = kcaoff
    values[88] = k2_i
    k5 = kcaoff
    values[89] = k5
    k5_i = kcaoff
    values[90] = k5_i
    scale_sex_GCaL_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GCaL_EFP_male, scale_sex_GCaL_EFP_female))
    values[91] = scale_sex_GCaL_EFP
    scale_sex_GJup = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GJup_male, scale_sex_GJup_female))
    values[92] = scale_sex_GJup
    scale_sex_GK1 = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GK1_male, scale_sex_GK1_female))
    values[93] = scale_sex_GK1
    scale_sex_GKb = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKb_male, scale_sex_GKb_female))
    values[94] = scale_sex_GKb
    scale_sex_GKr_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKr_EFP_male, scale_sex_GKr_EFP_female))
    values[95] = scale_sex_GKr_EFP
    scale_sex_GKs_EFP = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKs_EFP_male, scale_sex_GKs_EFP_female))
    values[96] = scale_sex_GKs_EFP
    scale_sex_GNCX = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNCX_male, scale_sex_GNCX_female))
    values[97] = scale_sex_GNCX
    scale_sex_GNa = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNa_male, scale_sex_GNa_female))
    values[98] = scale_sex_GNa
    scale_sex_GNaL = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GNaL_male, scale_sex_GNaL_female))
    values[99] = scale_sex_GNaL
    scale_sex_GpCa = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GpCa_male, scale_sex_GpCa_female))
    values[100] = scale_sex_GpCa
    scale_sex_Gtos = numpy.where((sex == 0), 1.0, scale_sex_Gtos_male)
    values[101] = scale_sex_Gtos
    scale_sex_PNaK = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_PNaK_male, scale_sex_PNaK_female))
    values[102] = scale_sex_PNaK
    scale_sex_calm = numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_calm_male, scale_sex_calm_female))
    values[103] = scale_sex_calm
    thLp = scale_HF_thL*(3.0*thL)
    values[104] = thLp
    Afcas = 1.0 - Afcaf
    values[105] = Afcas
    AiS = 1.0 - AiF
    values[106] = AiS
    Axrs = 1.0 - Axrf
    values[107] = Axrs
    fcass = fss
    values[108] = fcass
    dhL_dt = (-hL + hLss)/((scale_HF_thL*thL))
    values[109] = dhL_dt
    jss = hss
    values[110] = jss
    da_dt = (-a + ass)/ta
    values[111] = da_dt
    dap_dt = (-ap + assp)/ta
    values[112] = dap_dt
    dd_dt = (-d + dss)/td
    values[113] = dd_dt
    tfcafp = 2.5*tfcaf
    values[114] = tfcafp
    tffp = 2.5*tff
    values[115] = tffp
    dff_dt = (-ff + fss)/tff
    values[116] = dff_dt
    dfs_dt = (-fs + fss)/tfs
    values[117] = dfs_dt
    dhf_dt = (-hf + hss)/thf
    values[118] = dhf_dt
    thsp = 3.0*ths
    values[119] = thsp
    dhs_dt = (-hs + hss)/ths
    values[120] = dhs_dt
    tjp = 1.46*tj
    values[121] = tjp
    tmL = tm
    values[122] = tmL
    dm_dt = (-m + mss)/tm
    values[123] = dm_dt
    dxrf_dt = (-xrf + xrss)/txrf
    values[124] = dxrf_dt
    dxrs_dt = (-xrs + xrss)/txrs
    values[125] = dxrs_dt
    xs2ss = xs1ss
    values[126] = xs2ss
    dxs1_dt = (-xs1 + xs1ss)/txs1
    values[127] = dxs1_dt
    f = Aff*ff + Afs*fs
    values[128] = f
    fp = Aff*ffp + Afs*fs
    values[129] = fp
    Acap = 2*Ageo
    values[130] = Acap
    vjsr = 0.0048*vcell
    values[131] = vjsr
    vmyo = 0.68*vcell
    values[132] = vmyo
    vnsr = 0.0552*vcell
    values[133] = vnsr
    vss = 0.02*vcell
    values[134] = vss
    h = Ahf*hf + Ahs*hs
    values[135] = h
    hp = Ahf*hf + Ahs*hsp
    values[136] = hp
    Jupnp = numpy.where((celltype == 1), 1.3*Jupnp_tmp, Jupnp_tmp)
    values[137] = Jupnp
    Jupp = numpy.where((celltype == 1), 1.3*Jupp_tmp, Jupp_tmp)
    values[138] = Jupp
    CaMKa = scale_HF_CaMKa*(CaMKb + CaMKt)
    values[139] = CaMKa
    dCaMKt_dt = -CaMKt*bCaMK + (CaMKb*aCaMK)*(CaMKb + CaMKt)
    values[140] = dCaMKt_dt
    ICab = ((vffrt*(4.0*(PCab*scale_drug_ICab)))*(cai*numpy.exp(2.0*vfrt) - 0.341*cao))/(numpy.exp(2.0*vfrt) - 1.0)
    values[141] = ICab
    INab = ((vffrt*(PNab*scale_drug_INab))*(nai*numpy.exp(vfrt) - nao))/(numpy.exp(vfrt) - 1.0)
    values[142] = INab
    PhiCaK = ((1.0*vffrt)*(-0.75*ko + (0.75*kss)*numpy.exp(1.0*vfrt)))/(numpy.exp(1.0*vfrt) - 1.0)
    values[143] = PhiCaK
    PhiCaL = ((4.0*vffrt)*(-0.341*cao + cass*numpy.exp(2.0*vfrt)))/(numpy.exp(2.0*vfrt) - 1.0)
    values[144] = PhiCaL
    PhiCaNa = ((1.0*vffrt)*(-0.75*nao + (0.75*nass)*numpy.exp(1.0*vfrt)))/(numpy.exp(1.0*vfrt) - 1.0)
    values[145] = PhiCaNa
    dxk1_dt = (-xk1 + xk1ss)/txk1
    values[146] = dxk1_dt
    GK1_12 = numpy.where((celltype == 1), 1.2*GK1_tmp, 1.3*GK1_tmp)
    values[147] = GK1_12
    GKr_12 = numpy.where((celltype == 1), 1.3*GKr_tmp, 0.8*GKr_tmp)
    values[148] = GKr_12
    GKs = numpy.where((celltype == 1), 1.4*GKs_tmp, GKs_tmp)
    values[149] = GKs
    GNaL = numpy.where((celltype == 1), 0.6*GNaL_tmp, GNaL_tmp)
    values[150] = GNaL
    anca = 1.0/(k2n/km2n + (Kmn/cass + 1.0)**4.0)
    values[151] = anca
    a1 = (k1p*(nai/Knai)**3.0)/(((1.0 + ki/Kki)**2.0 + (1.0 + nai/Knai)**3.0) - 1.0)
    values[152] = a1
    b4 = (k4m*(ki/Kki)**2.0)/(((1.0 + ki/Kki)**2.0 + (1.0 + nai/Knai)**3.0) - 1.0)
    values[153] = b4
    a3 = (k3p*(ko/Kko)**2.0)/(((1.0 + ko/Kko)**2.0 + (1.0 + nao/Knao)**3.0) - 1.0)
    values[154] = a3
    b2 = (k2m*(nao/Knao)**3.0)/(((1.0 + ko/Kko)**2.0 + (1.0 + nao/Knao)**3.0) - 1.0)
    values[155] = b2
    b3 = (H*(P*k3m))/(1.0 + MgATP/Kmgatp)
    values[156] = b3
    PCa_12 = numpy.where((celltype == 1), 1.2*PCa_tmp, 2.5*PCa_tmp)
    values[157] = PCa_12
    Pnak = numpy.where((celltype == 0), Pnak_tmp, Pnak_12)
    values[158] = Pnak
    a_relp = 0.5*btp
    values[159] = a_relp
    tau_relp_tmp = btp/(1.0 + 0.0123/cajsr)
    values[160] = tau_relp_tmp
    tau_rel = numpy.where((tau_rel_tmp < 0.001), 0.001, tau_rel_tmp)
    values[161] = tau_rel
    tiF = delta_epi*(1/(0.3933*numpy.exp((-(v + 100.0))/100.0) + 0.08004*numpy.exp((v + 50.0)/16.59))) + 4.562
    values[162] = tiF
    tiS = delta_epi*(1/(0.001416*numpy.exp((-(v + 96.52))/59.05) + 1.78e-08*numpy.exp((v + 114.1)/8.079))) + 23.62
    values[163] = tiS
    h11 = (nao*nao)/((kna2*(h10*kna1)))
    values[164] = h11
    h12 = 1.0/h10
    values[165] = h12
    h11_i = (nao*nao)/((kna2*(h10_i*kna1)))
    values[166] = h11_i
    h12_i = 1.0/h10_i
    values[167] = h12_i
    h5 = (nass*nass)/((kna2*(h4*kna1)))
    values[168] = h5
    h6 = 1.0/h4
    values[169] = h6
    h5_i = (nai*nai)/((kna2*(h4_i*kna1)))
    values[170] = h5_i
    h6_i = 1.0/h4_i
    values[171] = h6_i
    h1 = (nass/kna3)*(hna + 1) + 1
    values[172] = h1
    h1_i = (nai/kna3)*(hna + 1) + 1
    values[173] = h1_i
    h7 = (nao/kna3)*(1.0 + 1.0/hna) + 1.0
    values[174] = h7
    h7_i = (nao/kna3)*(1.0 + 1.0/hna) + 1.0
    values[175] = h7_i
    scale_sex_GCaL = scale_sex_GCaL_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GCaL_male, scale_sex_GCaL_female))
    values[176] = scale_sex_GCaL
    IKb = (xkb*(scale_drug_IKb*(GKb*scale_sex_GKb)))*(-EK + v)
    values[177] = IKb
    scale_sex_GKr = scale_sex_GKr_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKr_male, scale_sex_GKr_female))
    values[178] = scale_sex_GKr
    scale_sex_GKs = scale_sex_GKs_EFP*numpy.where((sex == 0), 1.0, numpy.where((sex == 1), scale_sex_GKs_male, scale_sex_GKs_female))
    values[179] = scale_sex_GKs
    Gncx = scale_sex_GNCX*numpy.where((celltype == 0), Gncx_tmp, Gncx_12)
    values[180] = Gncx
    IpCa = (cai*(scale_drug_IpCa*(GpCa*scale_sex_GpCa)))/(cai + 0.0005)
    values[181] = IpCa
    cmdnmax = scale_sex_calm*numpy.where((celltype == 1), 1.3*cmdnmax_tmp, cmdnmax_tmp)
    values[182] = cmdnmax
    dhLp_dt = (-hLp + hLssp)/thLp
    values[183] = dhLp_dt
    fca = Afcaf*fcaf + Afcas*fcas
    values[184] = fca
    fcap = Afcaf*fcafp + Afcas*fcas
    values[185] = fcap
    i = AiF*iF + scale_sex_Gtos*(AiS*iS)
    values[186] = i
    ip = AiF*iFp + scale_sex_Gtos*(AiS*iSp)
    values[187] = ip
    xr = Axrf*xrf + Axrs*xrs
    values[188] = xr
    dfcaf_dt = (-fcaf + fcass)/tfcaf
    values[189] = dfcaf_dt
    dfcas_dt = (-fcas + fcass)/tfcas
    values[190] = dfcas_dt
    djca_dt = (fcass - jca)/tjca
    values[191] = djca_dt
    dj_dt = (-j + jss)/tj
    values[192] = dj_dt
    dfcafp_dt = (-fcafp + fcass)/tfcafp
    values[193] = dfcafp_dt
    dffp_dt = (-ffp + fss)/tffp
    values[194] = dffp_dt
    dhsp_dt = (-hsp + hssp)/thsp
    values[195] = dhsp_dt
    djp_dt = (-jp + jss)/tjp
    values[196] = djp_dt
    dmL_dt = (-mL + mLss)/tmL
    values[197] = dmL_dt
    dxs2_dt = (-xs2 + xs2ss)/txs2
    values[198] = dxs2_dt
    fICaLp = 1.0/(1.0 + KmCaMK/CaMKa)
    values[199] = fICaLp
    fINaLp = 1.0/(1.0 + KmCaMK/CaMKa)
    values[200] = fINaLp
    fINap = 1.0/(1.0 + KmCaMK/CaMKa)
    values[201] = fINap
    fItop = 1.0/(1.0 + KmCaMK/CaMKa)
    values[202] = fItop
    fJrelp = 1.0/(1.0 + KmCaMK/CaMKa)
    values[203] = fJrelp
    fJupp = 1.0/(1.0 + KmCaMK/CaMKa)
    values[204] = fJupp
    GK1 = numpy.where((celltype == 0), GK1_tmp, GK1_12)
    values[205] = GK1
    GKr = numpy.where((celltype == 0), GKr_tmp, GKr_12)
    values[206] = GKr
    dnca_dt = anca*k2n - km2n*nca
    values[207] = dnca_dt
    x2 = b4*(a2*a3) + (b4*(a3*b1) + (a3*(a1*a2) + b4*(b1*b2)))
    values[208] = x2
    x1 = a2*(a1*b3) + (b3*(a2*b4) + (a2*(a1*a4) + b3*(b2*b4)))
    values[209] = x1
    x3 = b1*(a3*a4) + (a4*(b1*b2) + (a4*(a2*a3) + b1*(b2*b3)))
    values[210] = x3
    x4 = a1*(b2*b3) + (a1*(a4*b2) + (a1*(a3*a4) + b2*(b3*b4)))
    values[211] = x4
    PCa = numpy.where((celltype == 0), PCa_tmp, PCa_12)
    values[212] = PCa
    tau_relp = numpy.where((tau_relp_tmp < 0.001), 0.001, tau_relp_tmp)
    values[213] = tau_relp
    tiFp = tiF*(dti_develop*dti_recover)
    values[214] = tiFp
    diF_dt = (-iF + iss)/tiF
    values[215] = diF_dt
    tiSp = tiS*(dti_develop*dti_recover)
    values[216] = tiSp
    diS_dt = (-iS + iss)/tiS
    values[217] = diS_dt
    k1 = kcaon*(cao*h12)
    values[218] = k1
    k1_i = kcaon*(cao*h12_i)
    values[219] = k1_i
    k6 = kcaon*(cass*h6)
    values[220] = k6
    k6_i = kcaon*(cai*h6_i)
    values[221] = k6_i
    h2 = (hna*nass)/((h1*kna3))
    values[222] = h2
    h3 = 1.0/h1
    values[223] = h3
    h2_i = (hna*nai)/((h1_i*kna3))
    values[224] = h2_i
    h3_i = 1.0/h1_i
    values[225] = h3_i
    h8 = nao/((h7*(hna*kna3)))
    values[226] = h8
    h9 = 1.0/h7
    values[227] = h9
    h8_i = nao/((h7_i*(hna*kna3)))
    values[228] = h8_i
    h9_i = 1.0/h7_i
    values[229] = h9_i
    IKs = (xs2*(xs1*(KsCa*(GKs*scale_sex_GKs))))*(-EKs + v)
    values[230] = IKs
    Bcai = 1.0/((kmtrpn*trpnmax)/(cai + kmtrpn)**2.0 + ((cmdnmax*kmcmdn)/(cai + kmcmdn)**2.0 + 1.0))
    values[231] = Bcai
    INaL = (mL*((GNaL*scale_sex_GNaL)*(-ENa + v)))*(fINaLp*hLp + hL*(1.0 - fINaLp))
    values[232] = INaL
    INa = (m**3.0*((scale_drug_INa*(GNa*scale_sex_GNa))*(-ENa + v)))*(j*(h*(1.0 - fINap)) + jp*(fINap*hp))
    values[233] = INa
    Ito = ((scale_HF_Gto*(Gto*scale_drug_Ito))*(-EK + v))*(i*(a*(1.0 - fItop)) + ip*(ap*fItop))
    values[234] = Ito
    Jrel = Jrelnp*(1.0 - fJrelp) + Jrelp*fJrelp
    values[235] = Jrel
    Jup = -Jleak + (Jupnp*(scale_sex_GJup*(1.0 - fJupp)) + scale_HF_Jup*(Jupp*fJupp))
    values[236] = Jup
    IK1 = (xk1*(rk1*(numpy.sqrt(ko)*(GK1*scale_sex_GK1))))*(-EK + v)
    values[237] = IK1
    IKr = (rkr*(xr*((0.4303314829119352*numpy.sqrt(ko))*(GKr*scale_sex_GKr))))*(-EK + v)
    values[238] = IKr
    E1 = x1/(x4 + (x3 + (x1 + x2)))
    values[239] = E1
    E2 = x2/(x4 + (x3 + (x1 + x2)))
    values[240] = E2
    E3 = x3/(x4 + (x3 + (x1 + x2)))
    values[241] = E3
    E4 = x4/(x4 + (x3 + (x1 + x2)))
    values[242] = E4
    PCaK = 0.0003574*PCa
    values[243] = PCaK
    PCaNa = 0.00125*PCa
    values[244] = PCaNa
    PCap = 1.1*PCa
    values[245] = PCap
    diFp_dt = (-iFp + iss)/tiFp
    values[246] = diFp_dt
    diSp_dt = (-iSp + iss)/tiSp
    values[247] = diSp_dt
    k4pp = h2*wnaca
    values[248] = k4pp
    k7 = wna*(h2*h5)
    values[249] = k7
    k4p_ss = (h3*wca)/hca
    values[250] = k4p_ss
    k4pp_i = h2_i*wnaca
    values[251] = k4pp_i
    k7_i = wna*(h2_i*h5_i)
    values[252] = k7_i
    k4p_i = (h3_i*wca)/hca
    values[253] = k4p_i
    k3pp = h8*wnaca
    values[254] = k3pp
    k8 = wna*(h11*h8)
    values[255] = k8
    k3p_ss = h9*wca
    values[256] = k3p_ss
    k3pp_i = h8_i*wnaca
    values[257] = k3pp_i
    k8_i = wna*(h11_i*h8_i)
    values[258] = k8_i
    k3p_i = h9_i*wca
    values[259] = k3p_i
    dcajsr_dt = Bcajsr*(-Jrel + Jtr)
    values[260] = dcajsr_dt
    dcansr_dt = Jup - (Jtr*vjsr)/vnsr
    values[261] = dcansr_dt
    JnakNa = 3.0*(E1*a3 - E2*b3)
    values[262] = JnakNa
    JnakK = 2.0*(-E3*a1 + E4*b1)
    values[263] = JnakK
    ICaL = (d*(PhiCaL*(PCap*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca)) + (d*(PhiCaL*(PCa*(scale_sex_GCaL*(1.0 - fICaLp)))))*(f*(1.0 - nca) + nca*(fca*jca))
    values[264] = ICaL
    PCaKp = 0.0003574*PCap
    values[265] = PCaKp
    PCaNap = 0.00125*PCap
    values[266] = PCaNap
    k4 = k4p_ss + k4pp
    values[267] = k4
    k4_i = k4p_i + k4pp_i
    values[268] = k4_i
    k3 = k3p_ss + k3pp
    values[269] = k3
    k3_i = k3p_i + k3pp_i
    values[270] = k3_i
    INaK = (scale_HF_Pnak*(Pnak*scale_sex_PNaK))*(JnakK*zk + JnakNa*zna)
    values[271] = INaK
    Jrel_inf_tmp = ((-ICaL)*a_rel)/(((1.5*scale_HF_Jrel_inf)/cajsr)**8.0 + 1.0)
    values[272] = Jrel_inf_tmp
    Jrel_infp_tmp = ((-ICaL)*a_relp)/(((1.5*scale_HF_Jrel_inf)/cajsr)**8.0 + 1.0)
    values[273] = Jrel_infp_tmp
    ICaK = (d*(PhiCaK*(PCaK*(1.0 - fICaLp))))*(f*(1.0 - nca) + nca*(fca*jca)) + (d*(PhiCaK*(PCaKp*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca))
    values[274] = ICaK
    ICaNa = (d*(PhiCaNa*(PCaNa*(1.0 - fICaLp))))*(f*(1.0 - nca) + nca*(fca*jca)) + (d*(PhiCaNa*(PCaNap*fICaLp)))*(fp*(1.0 - nca) + nca*(fcap*jca))
    values[275] = ICaNa
    x2_ss = (k1*k7)*(k4 + k5) + (k4*k6)*(k1 + k8)
    values[276] = x2_ss
    x2_i = (k1_i*k7_i)*(k4_i + k5_i) + (k4_i*k6_i)*(k1_i + k8_i)
    values[277] = x2_i
    x1_ss = (k2*k4)*(k6 + k7) + (k5*k7)*(k2 + k3)
    values[278] = x1_ss
    x3_ss = (k1*k3)*(k6 + k7) + (k6*k8)*(k2 + k3)
    values[279] = x3_ss
    x4_ss = (k2*k8)*(k4 + k5) + (k3*k5)*(k1 + k8)
    values[280] = x4_ss
    x1_i = (k2_i*k4_i)*(k6_i + k7_i) + (k5_i*k7_i)*(k2_i + k3_i)
    values[281] = x1_i
    x3_i = (k1_i*k3_i)*(k6_i + k7_i) + (k6_i*k8_i)*(k2_i + k3_i)
    values[282] = x3_i
    x4_i = (k2_i*k8_i)*(k4_i + k5_i) + (k3_i*k5_i)*(k1_i + k8_i)
    values[283] = x4_i
    dki_dt = (Acap*(-(-2.0*INaK + (Istim + (IKb + (IK1 + (IKs + (IKr + Ito))))))))/((F*vmyo)) + (JdiffK*vss)/vmyo
    values[284] = dki_dt
    Jrel_inf = numpy.where((celltype == 2), 1.7*Jrel_inf_tmp, Jrel_inf_tmp)
    values[285] = Jrel_inf
    Jrel_infp = numpy.where((celltype == 2), 1.7*Jrel_infp_tmp, Jrel_infp_tmp)
    values[286] = Jrel_infp
    dkss_dt = -JdiffK + (Acap*(-ICaK))/((F*vss))
    values[287] = dkss_dt
    E1_ss = x1_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    values[288] = E1_ss
    E2_ss = x2_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    values[289] = E2_ss
    E3_ss = x3_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    values[290] = E3_ss
    E4_ss = x4_ss/(x4_ss + (x3_ss + (x1_ss + x2_ss)))
    values[291] = E4_ss
    E1_i = x1_i/(x4_i + (x3_i + (x1_i + x2_i)))
    values[292] = E1_i
    E2_i = x2_i/(x4_i + (x3_i + (x1_i + x2_i)))
    values[293] = E2_i
    E3_i = x3_i/(x4_i + (x3_i + (x1_i + x2_i)))
    values[294] = E3_i
    E4_i = x4_i/(x4_i + (x3_i + (x1_i + x2_i)))
    values[295] = E4_i
    dJrelnp_dt = (Jrel_inf - Jrelnp)/tau_rel
    values[296] = dJrelnp_dt
    dJrelp_dt = (Jrel_infp - Jrelp)/tau_relp
    values[297] = dJrelp_dt
    JncxCa_ss = -E1_ss*k1 + E2_ss*k2
    values[298] = JncxCa_ss
    JncxNa_ss = -E2_ss*k3pp + (E3_ss*k4pp + 3.0*(-E1_ss*k8 + E4_ss*k7))
    values[299] = JncxNa_ss
    JncxCa_i = -E1_i*k1_i + E2_i*k2_i
    values[300] = JncxCa_i
    JncxNa_i = -E2_i*k3pp_i + (E3_i*k4pp_i + 3.0*(-E1_i*k8_i + E4_i*k7_i))
    values[301] = JncxNa_i
    INaCa_ss = (allo_ss*((0.2*Gncx)*scale_HF_Gncx))*(JncxCa_ss*zca + JncxNa_ss*zna)
    values[302] = INaCa_ss
    INaCa_i = (allo_i*((0.8*Gncx)*scale_HF_Gncx))*(JncxCa_i*zca + JncxNa_i*zna)
    values[303] = INaCa_i
    dcass_dt = Bcass*(-Jdiff + ((Acap*(-(ICaL - 2.0*INaCa_ss)))/(((2.0*F)*vss)) + (Jrel*vjsr)/vss))
    values[304] = dcass_dt
    dnass_dt = -JdiffNa + (Acap*(-(ICaNa + 3.0*INaCa_ss)))/((F*vss))
    values[305] = dnass_dt
    dcai_dt = Bcai*(((Acap*(-(-2.0*INaCa_i + (ICab + IpCa))))/(((2.0*F)*vmyo)) - (Jup*vnsr)/vmyo) + (Jdiff*vss)/vmyo)
    values[306] = dcai_dt
    dnai_dt = (Acap*(-(INab + (3.0*INaK + (3.0*INaCa_i + (INa + INaL))))))/((F*vmyo)) + (JdiffNa*vss)/vmyo
    values[307] = dnai_dt
    dv_dt = -(Istim + (ICab + (IpCa + (IKb + (INab + (INaK + (INaCa_ss + (INaCa_i + (IK1 + (IKs + (IKr + (ICaK + (ICaNa + (ICaL + (Ito + (INa + INaL))))))))))))))))
    values[308] = dv_dt

    return values

