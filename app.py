import pandas as pd
import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Field Shift — Satellite Agriculture Intelligence",
    page_icon="🛰️",
    layout="wide",
)

# --- VERIFIED DATASET (36 DISTRICTS OF PUNJAB, NASA POWER & SMAP L4)[cite: 1] ---
DATA = {
    "Attock": {
        "id": "PK-PB-01",
        "soil": {"clay": 32.4, "sand": 45.1, "silt": 22.5, "oc": 0.39, "ph": 7.93},
        "weather": {
            "max_temp": 28.2,
            "min_temp": 14.5,
            "mean_temp": 21.4,
            "rain": 815.2,
            "solar": 18.07,
            "wetness": 0.366,
        },
        "crops": {
            "wheat": {"yield": 4.67},
            "rice": {"yield": 2.49},
            "maize": {"yield": 6.69},
            "mung_bean": {"yield": 1.0},
            "chickpea": {"yield": 1.17},
        },
        "lat": 33.7667,
        "lng": 72.3667,
    },
    "Bahawalnagar": {
        "id": "PK-PB-02",
        "soil": {"clay": 18.2, "sand": 61.5, "silt": 20.3, "oc": 0.24, "ph": 8.43},
        "weather": {
            "max_temp": 31.2,
            "min_temp": 17.6,
            "mean_temp": 24.4,
            "rain": 776.5,
            "solar": 17.89,
            "wetness": 0.361,
        },
        "crops": {
            "wheat": {"yield": 4.33},
            "rice": {"yield": 2.81},
            "maize": {"yield": 4.16},
            "mung_bean": {"yield": 1.3},
            "chickpea": {"yield": 0.87},
        },
        "lat": 29.9983,
        "lng": 73.2525,
    },
    "Bahawalpur": {
        "id": "PK-PB-03",
        "soil": {"clay": 14.7, "sand": 67.6, "silt": 17.7, "oc": 0.21, "ph": 8.6},
        "weather": {
            "max_temp": 31.6,
            "min_temp": 18.1,
            "mean_temp": 24.9,
            "rain": 513.4,
            "solar": 17.98,
            "wetness": 0.344,
        },
        "crops": {
            "wheat": {"yield": 3.83},
            "rice": {"yield": 3.88},
            "maize": {"yield": 5.89},
            "mung_bean": {"yield": 0.99},
            "chickpea": {"yield": 1.34},
        },
        "lat": 29.3956,
        "lng": 71.6722,
    },
    "Bhakkar": {
        "id": "PK-PB-04",
        "soil": {"clay": 16.4, "sand": 64.3, "silt": 19.4, "oc": 0.22, "ph": 8.43},
        "weather": {
            "max_temp": 29.9,
            "min_temp": 16.4,
            "mean_temp": 23.1,
            "rain": 842.0,
            "solar": 18.07,
            "wetness": 0.358,
        },
        "crops": {
            "wheat": {"yield": 3.59},
            "rice": {"yield": 2.81},
            "maize": {"yield": 5.99},
            "mung_bean": {"yield": 1.67},
            "chickpea": {"yield": 1.13},
        },
        "lat": 31.6253,
        "lng": 71.0653,
    },
    "Chakwal": {
        "id": "PK-PB-05",
        "soil": {"clay": 27.7, "sand": 47.6, "silt": 24.7, "oc": 0.37, "ph": 7.8},
        "weather": {
            "max_temp": 28.6,
            "min_temp": 15.2,
            "mean_temp": 21.9,
            "rain": 540.5,
            "solar": 17.97,
            "wetness": 0.357,
        },
        "crops": {
            "wheat": {"yield": 3.43},
            "rice": {"yield": 4.03},
            "maize": {"yield": 4.96},
            "mung_bean": {"yield": 1.4},
            "chickpea": {"yield": 1.04},
        },
        "lat": 32.9328,
        "lng": 72.8558,
    },
    "Chiniot": {
        "id": "PK-PB-06",
        "soil": {"clay": 26.2, "sand": 42.1, "silt": 31.7, "oc": 0.43, "ph": 8.13},
        "weather": {
            "max_temp": 29.7,
            "min_temp": 16.2,
            "mean_temp": 22.9,
            "rain": 546.7,
            "solar": 18.0,
            "wetness": 0.356,
        },
        "crops": {
            "wheat": {"yield": 2.66},
            "rice": {"yield": 4.02},
            "maize": {"yield": 7.33},
            "mung_bean": {"yield": 1.06},
            "chickpea": {"yield": 1.18},
        },
        "lat": 31.72,
        "lng": 72.98,
    },
    "Dera Ghazi Khan": {
        "id": "PK-PB-07",
        "soil": {"clay": 22.0, "sand": 52.5, "silt": 25.6, "oc": 0.29, "ph": 8.27},
        "weather": {
            "max_temp": 31.0,
            "min_temp": 17.6,
            "mean_temp": 24.3,
            "rain": 577.5,
            "solar": 18.01,
            "wetness": 0.346,
        },
        "crops": {
            "wheat": {"yield": 4.89},
            "rice": {"yield": 2.15},
            "maize": {"yield": 6.74},
            "mung_bean": {"yield": 1.45},
            "chickpea": {"yield": 0.91},
        },
        "lat": 30.0561,
        "lng": 70.6348,
    },
    "Faisalabad": {
        "id": "PK-PB-08",
        "soil": {"clay": 29.5, "sand": 34.9, "silt": 35.6, "oc": 0.55, "ph": 7.97},
        "weather": {
            "max_temp": 29.9,
            "min_temp": 16.6,
            "mean_temp": 23.3,
            "rain": 602.7,
            "solar": 17.97,
            "wetness": 0.365,
        },
        "crops": {
            "wheat": {"yield": 3.43},
            "rice": {"yield": 3.59},
            "maize": {"yield": 4.25},
            "mung_bean": {"yield": 1.4},
            "chickpea": {"yield": 0.94},
        },
        "lat": 31.4187,
        "lng": 73.0791,
    },
    "Gujranwala": {
        "id": "PK-PB-09",
        "soil": {"clay": 33.7, "sand": 30.1, "silt": 36.3, "oc": 0.67, "ph": 7.9},
        "weather": {
            "max_temp": 29.4,
            "min_temp": 15.8,
            "mean_temp": 22.6,
            "rain": 576.8,
            "solar": 17.9,
            "wetness": 0.353,
        },
        "crops": {
            "wheat": {"yield": 4.1},
            "rice": {"yield": 3.34},
            "maize": {"yield": 5.94},
            "mung_bean": {"yield": 1.16},
            "chickpea": {"yield": 1.33},
        },
        "lat": 32.1617,
        "lng": 74.1883,
    },
    "Gujrat": {
        "id": "PK-PB-10",
        "soil": {"clay": 31.1, "sand": 36.3, "silt": 32.6, "oc": 0.6, "ph": 7.7},
        "weather": {
            "max_temp": 28.9,
            "min_temp": 15.5,
            "mean_temp": 22.2,
            "rain": 654.4,
            "solar": 18.06,
            "wetness": 0.354,
        },
        "crops": {
            "wheat": {"yield": 4.95},
            "rice": {"yield": 3.85},
            "maize": {"yield": 7.13},
            "mung_bean": {"yield": 1.21},
            "chickpea": {"yield": 0.96},
        },
        "lat": 32.5742,
        "lng": 74.0754,
    },
    "Hafizabad": {
        "id": "PK-PB-11",
        "soil": {"clay": 32.4, "sand": 32.2, "silt": 35.4, "oc": 0.58, "ph": 7.97},
        "weather": {
            "max_temp": 29.7,
            "min_temp": 16.3,
            "mean_temp": 22.9,
            "rain": 548.1,
            "solar": 17.95,
            "wetness": 0.352,
        },
        "crops": {
            "wheat": {"yield": 3.96},
            "rice": {"yield": 4.16},
            "maize": {"yield": 4.92},
            "mung_bean": {"yield": 1.49},
            "chickpea": {"yield": 1.18},
        },
        "lat": 32.0711,
        "lng": 73.6878,
    },
    "Jhang": {
        "id": "PK-PB-12",
        "soil": {"clay": 23.6, "sand": 48.4, "silt": 28.0, "oc": 0.39, "ph": 8.2},
        "weather": {
            "max_temp": 30.1,
            "min_temp": 16.5,
            "mean_temp": 23.3,
            "rain": 641.4,
            "solar": 18.06,
            "wetness": 0.35,
        },
        "crops": {
            "wheat": {"yield": 3.63},
            "rice": {"yield": 4.04},
            "maize": {"yield": 7.62},
            "mung_bean": {"yield": 0.99},
            "chickpea": {"yield": 1.4},
        },
        "lat": 31.2681,
        "lng": 72.3181,
    },
    "Jhelum": {
        "id": "PK-PB-13",
        "soil": {"clay": 27.0, "sand": 50.4, "silt": 22.6, "oc": 0.42, "ph": 7.67},
        "weather": {
            "max_temp": 28.7,
            "min_temp": 15.4,
            "mean_temp": 22.0,
            "rain": 597.3,
            "solar": 17.86,
            "wetness": 0.356,
        },
        "crops": {
            "wheat": {"yield": 4.54},
            "rice": {"yield": 3.34},
            "maize": {"yield": 5.8},
            "mung_bean": {"yield": 1.16},
            "chickpea": {"yield": 1.09},
        },
        "lat": 32.9425,
        "lng": 73.7256,
    },
    "Kasur": {
        "id": "PK-PB-14",
        "soil": {"clay": 29.5, "sand": 38.5, "silt": 32.0, "oc": 0.51, "ph": 8.13},
        "weather": {
            "max_temp": 30.5,
            "min_temp": 16.9,
            "mean_temp": 23.6,
            "rain": 567.4,
            "solar": 17.98,
            "wetness": 0.359,
        },
        "crops": {
            "wheat": {"yield": 4.16},
            "rice": {"yield": 2.22},
            "maize": {"yield": 5.49},
            "mung_bean": {"yield": 0.92},
            "chickpea": {"yield": 1.13},
        },
        "lat": 31.1167,
        "lng": 74.45,
    },
    "Khanewal": {
        "id": "PK-PB-15",
        "soil": {"clay": 27.9, "sand": 40.3, "silt": 31.8, "oc": 0.46, "ph": 8.23},
        "weather": {
            "max_temp": 31.0,
            "min_temp": 17.4,
            "mean_temp": 24.2,
            "rain": 573.0,
            "solar": 17.82,
            "wetness": 0.345,
        },
        "crops": {
            "wheat": {"yield": 4.68},
            "rice": {"yield": 4.17},
            "maize": {"yield": 5.84},
            "mung_bean": {"yield": 0.83},
            "chickpea": {"yield": 1.16},
        },
        "lat": 30.3017,
        "lng": 71.9322,
    },
    "Khushab": {
        "id": "PK-PB-16",
        "soil": {"clay": 21.9, "sand": 53.5, "silt": 24.7, "oc": 0.31, "ph": 8.3},
        "weather": {
            "max_temp": 29.3,
            "min_temp": 15.8,
            "mean_temp": 22.5,
            "rain": 550.1,
            "solar": 17.91,
            "wetness": 0.343,
        },
        "crops": {
            "wheat": {"yield": 3.54},
            "rice": {"yield": 2.06},
            "maize": {"yield": 3.91},
            "mung_bean": {"yield": 1.12},
            "chickpea": {"yield": 0.72},
        },
        "lat": 32.2967,
        "lng": 72.3528,
    },
    "Lahore": {
        "id": "PK-PB-17",
        "soil": {"clay": 29.9, "sand": 33.8, "silt": 36.2, "oc": 0.58, "ph": 8.0},
        "weather": {
            "max_temp": 29.8,
            "min_temp": 16.3,
            "mean_temp": 23.1,
            "rain": 401.7,
            "solar": 17.99,
            "wetness": 0.345,
        },
        "crops": {
            "wheat": {"yield": 3.17},
            "rice": {"yield": 2.7},
            "maize": {"yield": 5.89},
            "mung_bean": {"yield": 1.04},
            "chickpea": {"yield": 0.82},
        },
        "lat": 31.5204,
        "lng": 74.3587,
    },
    "Layyah": {
        "id": "PK-PB-18",
        "soil": {"clay": 17.0, "sand": 65.1, "silt": 17.9, "oc": 0.26, "ph": 8.43},
        "weather": {
            "max_temp": 30.5,
            "min_temp": 17.0,
            "mean_temp": 23.7,
            "rain": 539.8,
            "solar": 18.02,
            "wetness": 0.353,
        },
        "crops": {
            "wheat": {"yield": 3.41},
            "rice": {"yield": 3.8},
            "maize": {"yield": 6.94},
            "mung_bean": {"yield": 0.99},
            "chickpea": {"yield": 1.45},
        },
        "lat": 30.9614,
        "lng": 70.9394,
    },
    "Lodhran": {
        "id": "PK-PB-19",
        "soil": {"clay": 21.3, "sand": 52.7, "silt": 26.0, "oc": 0.31, "ph": 8.33},
        "weather": {
            "max_temp": 31.5,
            "min_temp": 18.1,
            "mean_temp": 24.8,
            "rain": 510.6,
            "solar": 18.02,
            "wetness": 0.348,
        },
        "crops": {
            "wheat": {"yield": 3.84},
            "rice": {"yield": 2.64},
            "maize": {"yield": 7.54},
            "mung_bean": {"yield": 0.92},
            "chickpea": {"yield": 0.86},
        },
        "lat": 29.5408,
        "lng": 71.6336,
    },
    "Mandi Bahauddin": {
        "id": "PK-PB-20",
        "soil": {"clay": 32.3, "sand": 31.1, "silt": 36.7, "oc": 0.63, "ph": 7.8},
        "weather": {
            "max_temp": 29.0,
            "min_temp": 15.5,
            "mean_temp": 22.3,
            "rain": 663.1,
            "solar": 18.02,
            "wetness": 0.363,
        },
        "crops": {
            "wheat": {"yield": 4.24},
            "rice": {"yield": 2.1},
            "maize": {"yield": 6.56},
            "mung_bean": {"yield": 0.99},
            "chickpea": {"yield": 1.01},
        },
        "lat": 32.587,
        "lng": 73.4912,
    },
    "Mianwali": {
        "id": "PK-PB-21",
        "soil": {"clay": 19.9, "sand": 58.0, "silt": 22.1, "oc": 0.29, "ph": 8.3},
        "weather": {
            "max_temp": 29.0,
            "min_temp": 15.6,
            "mean_temp": 22.3,
            "rain": 214.1,
            "solar": 18.07,
            "wetness": 0.332,
        },
        "crops": {
            "wheat": {"yield": 2.91},
            "rice": {"yield": 2.39},
            "maize": {"yield": 6.31},
            "mung_bean": {"yield": 0.97},
            "chickpea": {"yield": 1.2},
        },
        "lat": 32.5853,
        "lng": 71.5436,
    },
    "Multan": {
        "id": "PK-PB-22",
        "soil": {"clay": 27.7, "sand": 42.1, "silt": 30.3, "oc": 0.41, "ph": 8.27},
        "weather": {
            "max_temp": 31.2,
            "min_temp": 17.5,
            "mean_temp": 24.3,
            "rain": 395.7,
            "solar": 18.07,
            "wetness": 0.348,
        },
        "crops": {
            "wheat": {"yield": 3.67},
            "rice": {"yield": 2.84},
            "maize": {"yield": 6.55},
            "mung_bean": {"yield": 1.57},
            "chickpea": {"yield": 0.82},
        },
        "lat": 30.1984,
        "lng": 71.4687,
    },
    "Muzaffargarh": {
        "id": "PK-PB-23",
        "soil": {"clay": 20.1, "sand": 55.7, "silt": 24.2, "oc": 0.3, "ph": 8.33},
        "weather": {
            "max_temp": 31.1,
            "min_temp": 17.6,
            "mean_temp": 24.3,
            "rain": 642.8,
            "solar": 18.01,
            "wetness": 0.359,
        },
        "crops": {
            "wheat": {"yield": 3.77},
            "rice": {"yield": 3.33},
            "maize": {"yield": 7.24},
            "mung_bean": {"yield": 0.8},
            "chickpea": {"yield": 0.93},
        },
        "lat": 30.0703,
        "lng": 71.1933,
    },
    "Nankana Sahib": {
        "id": "PK-PB-24",
        "soil": {"clay": 31.7, "sand": 32.4, "silt": 35.9, "oc": 0.57, "ph": 7.97},
        "weather": {
            "max_temp": 30.0,
            "min_temp": 16.4,
            "mean_temp": 23.2,
            "rain": 542.9,
            "solar": 18.06,
            "wetness": 0.354,
        },
        "crops": {
            "wheat": {"yield": 4.3},
            "rice": {"yield": 4.05},
            "maize": {"yield": 7.43},
            "mung_bean": {"yield": 0.99},
            "chickpea": {"yield": 0.79},
        },
        "lat": 31.45,
        "lng": 73.7,
    },
    "Narowal": {
        "id": "PK-PB-25",
        "soil": {"clay": 35.1, "sand": 28.2, "silt": 36.7, "oc": 0.68, "ph": 7.7},
        "weather": {
            "max_temp": 29.4,
            "min_temp": 15.9,
            "mean_temp": 22.6,
            "rain": 690.0,
            "solar": 17.87,
            "wetness": 0.354,
        },
        "crops": {
            "wheat": {"yield": 5.0},
            "rice": {"yield": 2.84},
            "maize": {"yield": 5.97},
            "mung_bean": {"yield": 1.44},
            "chickpea": {"yield": 0.81},
        },
        "lat": 32.1,
        "lng": 74.87,
    },
    "Okara": {
        "id": "PK-PB-26",
        "soil": {"clay": 31.9, "sand": 31.8, "silt": 36.3, "oc": 0.58, "ph": 8.13},
        "weather": {
            "max_temp": 30.5,
            "min_temp": 17.0,
            "mean_temp": 23.8,
            "rain": 725.3,
            "solar": 18.04,
            "wetness": 0.35,
        },
        "crops": {
            "wheat": {"yield": 2.61},
            "rice": {"yield": 2.74},
            "maize": {"yield": 5.78},
            "mung_bean": {"yield": 1.26},
            "chickpea": {"yield": 0.74},
        },
        "lat": 30.8081,
        "lng": 73.4458,
    },
    "Pakpattan": {
        "id": "PK-PB-27",
        "soil": {"clay": 28.4, "sand": 40.3, "silt": 31.3, "oc": 0.5, "ph": 8.23},
        "weather": {
            "max_temp": 30.9,
            "min_temp": 17.4,
            "mean_temp": 24.2,
            "rain": 435.3,
            "solar": 18.1,
            "wetness": 0.336,
        },
        "crops": {
            "wheat": {"yield": 3.59},
            "rice": {"yield": 2.79},
            "maize": {"yield": 5.68},
            "mung_bean": {"yield": 1.19},
            "chickpea": {"yield": 0.97},
        },
        "lat": 30.341,
        "lng": 73.3866,
    },
    "Rahim Yar Khan": {
        "id": "PK-PB-28",
        "soil": {"clay": 15.9, "sand": 65.6, "silt": 18.4, "oc": 0.23, "ph": 8.6},
        "weather": {
            "max_temp": 32.5,
            "min_temp": 18.9,
            "mean_temp": 25.6,
            "rain": 699.7,
            "solar": 17.94,
            "wetness": 0.355,
        },
        "crops": {
            "wheat": {"yield": 3.54},
            "rice": {"yield": 2.03},
            "maize": {"yield": 4.44},
            "mung_bean": {"yield": 0.9},
            "chickpea": {"yield": 1.06},
        },
        "lat": 28.4212,
        "lng": 70.2989,
    },
    "Rajanpur": {
        "id": "PK-PB-29",
        "soil": {"clay": 18.4, "sand": 58.0, "silt": 23.6, "oc": 0.27, "ph": 8.47},
        "weather": {
            "max_temp": 32.0,
            "min_temp": 18.6,
            "mean_temp": 25.3,
            "rain": 527.2,
            "solar": 18.05,
            "wetness": 0.35,
        },
        "crops": {
            "wheat": {"yield": 3.09},
            "rice": {"yield": 2.64},
            "maize": {"yield": 7.92},
            "mung_bean": {"yield": 1.02},
            "chickpea": {"yield": 0.95},
        },
        "lat": 29.1035,
        "lng": 70.325,
    },
    "Rawalpindi": {
        "id": "PK-PB-30",
        "soil": {"clay": 29.0, "sand": 43.8, "silt": 27.2, "oc": 0.53, "ph": 7.6},
        "weather": {
            "max_temp": 28.4,
            "min_temp": 15.0,
            "mean_temp": 21.7,
            "rain": 374.7,
            "solar": 17.93,
            "wetness": 0.347,
        },
        "crops": {
            "wheat": {"yield": 3.61},
            "rice": {"yield": 2.27},
            "maize": {"yield": 7.45},
            "mung_bean": {"yield": 1.34},
            "chickpea": {"yield": 0.83},
        },
        "lat": 33.5973,
        "lng": 73.0479,
    },
    "Sahiwal": {
        "id": "PK-PB-31",
        "soil": {"clay": 32.4, "sand": 31.1, "silt": 36.5, "oc": 0.59, "ph": 8.0},
        "weather": {
            "max_temp": 30.4,
            "min_temp": 17.2,
            "mean_temp": 23.8,
            "rain": 623.1,
            "solar": 17.93,
            "wetness": 0.351,
        },
        "crops": {
            "wheat": {"yield": 4.2},
            "rice": {"yield": 2.38},
            "maize": {"yield": 6.62},
            "mung_bean": {"yield": 1.25},
            "chickpea": {"yield": 1.28},
        },
        "lat": 30.6667,
        "lng": 73.1,
    },
    "Sargodha": {
        "id": "PK-PB-32",
        "soil": {"clay": 30.4, "sand": 36.2, "silt": 33.4, "oc": 0.55, "ph": 8.0},
        "weather": {
            "max_temp": 29.5,
            "min_temp": 16.0,
            "mean_temp": 22.8,
            "rain": 455.9,
            "solar": 17.95,
            "wetness": 0.349,
        },
        "crops": {
            "wheat": {"yield": 2.95},
            "rice": {"yield": 3.22},
            "maize": {"yield": 6.89},
            "mung_bean": {"yield": 0.96},
            "chickpea": {"yield": 1.04},
        },
        "lat": 32.0836,
        "lng": 72.6711,
    },
    "Sheikhupura": {
        "id": "PK-PB-33",
        "soil": {"clay": 35.7, "sand": 26.4, "silt": 37.9, "oc": 0.65, "ph": 7.93},
        "weather": {
            "max_temp": 29.8,
            "min_temp": 16.3,
            "mean_temp": 23.0,
            "rain": 619.4,
            "solar": 17.9,
            "wetness": 0.352,
        },
        "crops": {
            "wheat": {"yield": 3.92},
            "rice": {"yield": 2.87},
            "maize": {"yield": 6.08},
            "mung_bean": {"yield": 1.33},
            "chickpea": {"yield": 1.15},
        },
        "lat": 31.7131,
        "lng": 73.9783,
    },
    "Sialkot": {
        "id": "PK-PB-34",
        "soil": {"clay": 35.0, "sand": 25.4, "silt": 39.6, "oc": 0.69, "ph": 7.63},
        "weather": {
            "max_temp": 29.1,
            "min_temp": 15.6,
            "mean_temp": 22.3,
            "rain": 641.3,
            "solar": 18.03,
            "wetness": 0.361,
        },
        "crops": {
            "wheat": {"yield": 3.71},
            "rice": {"yield": 2.03},
            "maize": {"yield": 4.75},
            "mung_bean": {"yield": 1.47},
            "chickpea": {"yield": 1.28},
        },
        "lat": 32.4945,
        "lng": 74.5229,
    },
    "Toba Tek Singh": {
        "id": "PK-PB-35",
        "soil": {"clay": 29.0, "sand": 37.6, "silt": 33.4, "oc": 0.52, "ph": 8.07},
        "weather": {
            "max_temp": 30.3,
            "min_temp": 16.9,
            "mean_temp": 23.6,
            "rain": 423.2,
            "solar": 17.94,
            "wetness": 0.354,
        },
        "crops": {
            "wheat": {"yield": 2.95},
            "rice": {"yield": 3.56},
            "maize": {"yield": 5.94},
            "mung_bean": {"yield": 1.34},
            "chickpea": {"yield": 1.17},
        },
        "lat": 30.9744,
        "lng": 72.4828,
    },
    "Vehari": {
        "id": "PK-PB-36",
        "soil": {"clay": 27.0, "sand": 44.4, "silt": 28.6, "oc": 0.39, "ph": 8.27},
        "weather": {
            "max_temp": 31.0,
            "min_temp": 17.6,
            "mean_temp": 24.3,
            "rain": 683.2,
            "solar": 18.01,
            "wetness": 0.364,
        },
        "crops": {
            "wheat": {"yield": 4.31},
            "rice": {"yield": 3.46},
            "maize": {"yield": 7.09},
            "mung_bean": {"yield": 0.8},
            "chickpea": {"yield": 0.85},
        },
        "lat": 30.0419,
        "lng": 72.3489,
    },
}

ROTATIONS = [
    {
        "id": "rice_wheat",
        "name": "Rice–Wheat",
        "crops": ["Rice", "Wheat"],
        "water": 1490,
        "soilHealth": 42,
        "stability": 68,
        "nitrogenFixation": 0,
        "desc": "Traditional system; high grain yield, demands ~1,490 mm water.",
    },
    {
        "id": "maize_wheat",
        "name": "Maize–Wheat",
        "crops": ["Maize", "Wheat"],
        "water": 870,
        "soilHealth": 58,
        "stability": 82,
        "nitrogenFixation": 0,
        "desc": "Saves 620 mm water vs Rice–Wheat.",
    },
    {
        "id": "rice_chickpea",
        "name": "Rice–Chickpea",
        "crops": ["Rice", "Chickpea"],
        "water": 1250,
        "soilHealth": 78,
        "stability": 75,
        "nitrogenFixation": 45,
        "desc": "Drought-hardy winter chickpea (+45 kg N).",
    },
    {
        "id": "maize_chickpea",
        "name": "Maize–Chickpea",
        "crops": ["Maize", "Chickpea"],
        "water": 630,
        "soilHealth": 88,
        "stability": 86,
        "nitrogenFixation": 50,
        "desc": "Lowest water demand (~630 mm) +50 kg N/ha.",
    },
    {
        "id": "rice_wheat_mung",
        "name": "Rice–Wheat–Mung",
        "crops": ["Rice", "Wheat", "Mung Bean"],
        "water": 1690,
        "soilHealth": 91,
        "stability": 84,
        "nitrogenFixation": 65,
        "desc": "Adds 75-day summer Mung (+65 kg N/ha).",
    },
    {
        "id": "chickpea_maize_mung",
        "name": "Chickpea–Maize–Mung",
        "crops": ["Chickpea", "Maize", "Mung Bean"],
        "water": 830,
        "soilHealth": 96,
        "stability": 89,
        "nitrogenFixation": 95,
        "desc": "Dual legumes restore carbon (+95 kg N/ha).",
    },
    {
        "id": "cotton_wheat",
        "name": "Cotton–Wheat",
        "crops": ["Cotton", "Wheat"],
        "water": 1140,
        "soilHealth": 54,
        "stability": 72,
        "nitrogenFixation": 0,
        "desc": "Warm southern Punjab cash-crop (~1,140 mm).",
    },
]

# --- STREAMLIT SIDEBAR: FARMER PROFILE & DECISION INPUTS[cite: 1] ---
st.sidebar.header("📍 Farmer Profile & Decision Inputs")

selected_district = st.sidebar.selectbox(
    "1. Select District (Punjab):", sorted(list(DATA.keys()))
)
district_data = DATA[selected_district]

current_rot_options = {r["name"]: r["id"] for r in ROTATIONS}
selected_current_rot_name = st.sidebar.selectbox(
    "2. Your Current Crop Rotation:", list(current_rot_options.keys())
)
current_rot_id = current_rot_options[selected_current_rot_name]

area_ha = st.sidebar.slider(
    "3. Cultivated Farm Area (hectares):", 0.5, 100.0, 5.0, 0.5
)
area_acres = area_ha * 2.471
st.sidebar.markdown(f"**Equivalent Acres:** `{area_acres:.1f} ac`")

water_source = st.sidebar.selectbox(
    "4. Water Supply Source:",
    [
        ("canal", "Canal Water"),
        ("tubewell", "Tube-Well"),
        ("saline", "Saline / Brackish"),
        ("rainfed", "Rain-fed (Barani)"),
    ],
    format_func=lambda x: x[1],
)[0]

priority = st.sidebar.selectbox(
    "5. Primary Farming Goal:",
    [
        ("water", "Save Water"),
        ("soil", "Improve Soil"),
        ("yield", "Higher Yield"),
        ("stable", "Lower Risk"),
    ],
    format_func=lambda x: x[1],
)[0]

scenario = st.sidebar.selectbox(
    "6. Weather Condition:",
    [
        ("normal", "Normal (2024–25)"),
        ("heat", "Heat Stress"),
        ("drought", "Low Rainfall"),
        ("flash", "Heavy Rain"),
    ],
    format_func=lambda x: x[1],
)[0]

# --- MAIN APP TITLE & TABS ---
st.title("Field Shift // Satellite Agriculture Intelligence")
st.markdown(
    "*NASA POWER · NASA SMAP L4 · Punjab Crop Statistics (2024–25)*[cite: 1]"
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🗺️ District & Telemetry",
        "🔄 Crop Rotations (7)",
        "🌾 Yields & Profit Calculator",
        "🧪 Soil & NASA Labs",
        "📂 36-District Dataset",
    ]
)

# --- TAB 1: DISTRICT & TELEMETRY ---
with tab1:
  st.subheader(
    f"Geospatial & Satellite Telemetry for {selected_district} ({district_data['id']})"
  )

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Annual Rainfall", f"{district_data['weather']['rain']} mm")
  col2.metric("SMAP Soil Wetness", f"{district_data['weather']['wetness']}")
  col3.metric("Mean Temperature", f"{district_data['weather']['mean_temp']}°C")
  col4.metric("Solar Radiation", f"{district_data['weather']['solar']} MJ/m²")

  st.markdown("---")
  st.markdown("### District Location & Coordinates")
  st.write(
      f"**Latitude:** `{district_data['lat']}° N` | **Longitude:**"
      f" `{district_data['lng']}° E`"
  )

  # Display mini map using Streamlit map
  map_df = pd.DataFrame(
      [
          {
              "lat": district_data["lat"],
              "lon": district_data["lng"],
              "district": selected_district,
          }
      ]
  )
  st.map(map_df, zoom=8)

# --- TAB 2: CROP ROTATIONS (7) ---
with tab2:
  st.subheader("🏆 Recommended Crop Rotation Analysis")

  # Scoring logic[cite: 1]
  crop_key_map = {
      "Rice": "rice",
      "Wheat": "wheat",
      "Maize": "maize",
      "Chickpea": "chickpea",
      "Mung Bean": "mung_bean",
  }

  scored_rotations = []
  for rot in ROTATIONS:
    yield_sum = 0
    for c in rot["crops"]:
      k = crop_key_map.get(c)
      yield_sum += district_data["crops"][k]["yield"] if k else 3.2

    yield_score = min(
        100, max(40, (yield_sum / len(rot["crops"])) / 4.8 * 100)
    )
    water_score = max(20, min(100, (1 - rot["water"] / 1800) * 100))
    soil_score = rot["soilHealth"]
    stability_score = rot["stability"]

    if water_source == "saline":
      if "Rice" in rot["crops"]:
        yield_score *= 0.70
      if "Chickpea" in rot["crops"]:
        yield_score *= 0.85
    if water_source == "rainfed":
      if "Rice" in rot["crops"]:
        yield_score *= 0.45
        water_score *= 0.50
      if "Chickpea" in rot["crops"] or "Mung Bean" in rot["crops"]:
        yield_score *= 1.15
        water_score *= 1.25
    if scenario == "heat":
      if "Wheat" in rot["crops"]:
        yield_score *= 0.86
      if "Maize" in rot["crops"]:
        yield_score *= 1.05
    if scenario == "drought":
      water_score *= 1.30
      if "Rice" in rot["crops"]:
        yield_score *= 0.65

    w_yield, w_water, w_soil, w_stable = 0.25, 0.25, 0.25, 0.25
    if priority == "water":
      w_water, w_yield, w_soil, w_stable = 0.45, 0.15, 0.20, 0.20
    elif priority == "soil":
      w_soil, w_water, w_yield, w_stable = 0.45, 0.20, 0.15, 0.20
    elif priority == "yield":
      w_yield, w_water, w_soil, w_stable = 0.45, 0.15, 0.20, 0.20
    elif priority == "stable":
      w_stable, w_yield, w_water, w_soil = 0.45, 0.20, 0.20, 0.15

    total_score = round(
        min(
            100,
            max(
                30,
                yield_score * w_yield
                + water_score * w_water
                + soil_score * w_soil
                + stability_score * w_stable,
            ),
        )
    )
    scored_rotations.append(
        {
            **rot,
            "totalScore": total_score,
            "soilScore": soil_score,
            "stabilityScore": round(stability_score),
        }
    )

  scored_rotations = sorted(
      scored_rotations, key=lambda x: x["totalScore"], reverse=True
  )
  top_rot = scored_rotations[0]

  st.success(
      f"**Top Recommendation:** {top_rot['name']} (Match Score:"
      f" **{top_rot['totalScore']}/100**)"
  )
  st.write(top_rot["desc"])

  col1, col2, col3 = st.columns(3)
  col1.metric("Water Requirement", f"{top_rot['water']} mm")
  col2.metric("Soil Health Index", f"{top_rot['soilScore']} / 100")
  col3.metric("Biological N-Fixation", f"+{top_rot['nitrogenFixation']} kg N/ha")

  st.markdown("---")
  st.markdown("### All 7 Crop Rotations Compared")
  rot_df = pd.DataFrame(scored_rotations)[
      ["name", "totalScore", "water", "soilScore", "nitrogenFixation", "desc"]
  ]
  rot_df.columns = [
      "Rotation System",
      "Match Score",
      "Water (mm)",
      "Soil Health",
      "N-Fix (kg/ha)",
      "Description",
  ]
  st.dataframe(rot_df, use_container_width=True)

# --- TAB 3: YIELDS & PROFIT CALCULATOR ---
with tab3:
  st.subheader("🌾 Verified District Crop Yields & PKR Profit Calculator")
  st.write(
      "Recorded district average yield (t/ha) and total harvest for your"
      f" **{area_ha} ha** farm[cite: 1]:"
  )

  yield_cols = st.columns(5)
  crops_list = [
      ("wheat", "Wheat"),
      ("rice", "Rice"),
      ("maize", "Maize"),
      ("mung_bean", "Mung Bean"),
      ("chickpea", "Chickpea"),
  ]
  for i, (k, label) in enumerate(crops_list):
    y = district_data["crops"][k]["yield"]
    tot = y * area_ha
    yield_cols[i].metric(label, f"{y:.2f} t/ha", f"Total: {tot:.2f} t")

  st.markdown("---")
  st.markdown("### Financial Profit Margin Calculator (PKR)")
  col_f1, col_f2 = st.columns(2)
  input_cost_per_ha = col_f1.number_input(
      "Total Input Cost (PKR per ha):", value=75000, step=5000
  )
  market_price_maund = col_f2.number_input(
      "Market Selling Price (PKR / 40kg maund):", value=3800, step=100
  )

  avg_yield = (
      district_data["crops"]["wheat"]["yield"]
      + district_data["crops"]["maize"]["yield"]
  ) / 2
  total_tonnes = avg_yield * area_ha
  total_maunds = total_tonnes * 24.69

  total_cost = input_cost_per_ha * area_ha
  gross_rev = total_maunds * market_price_maund
  net_profit = gross_rev - total_cost
  margin_pct = (net_profit / gross_rev * 100) if gross_rev > 0 else 0

  res_col1, res_col2, res_col3 = st.columns(3)
  res_col1.metric("Total Investment", f"PKR {total_cost:,.0f}")
  res_col2.metric("Estimated Gross Revenue", f"PKR {gross_rev:,.0f}")
  res_col3.metric(
      "Net Profit Margin",
      f"PKR {net_profit:,.0f}",
      f"{margin_pct:.1f}% Return",
  )

# --- TAB 4: SOIL & NASA LABS ---
with tab4:
  st.subheader(
      f"🧪 Soil Profile & NASA Satellite Measurements for {selected_district}"
  )

  col1, col2, col3 = st.columns(3)
  col1.metric("Clay Content", f"{district_data['soil']['clay']}%")
  col2.metric("Sand Content", f"{district_data['soil']['sand']}%")
  col3.metric("Silt Content", f"{district_data['soil']['silt']}%")

  col_s1, col_s2 = st.columns(2)
  col_s1.metric("Soil pH Level", f"{district_data['soil']['ph']} pH")
  col_s2.metric(
      "Soil Organic Carbon (OC %)", f"{district_data['soil']['oc']}%"
  )
  st.info(
      "Pulse crops (Chickpea, Mung bean) rebuild soil organic matter and"
      " natural nitrogen fixation[cite: 1]."
  )

# --- TAB 5: 36-DISTRICT DATASET ---
with tab5:
  st.subheader("📂 Complete 36-District Punjab & NASA Satellite Dataset[cite: 1]")

  dataset_rows = []
  for d_name, d_val in DATA.items():
    dataset_rows.append(
        {
            "District ID": d_val["id"],
            "District": d_name,
            "Rain (mm)": d_val["weather"]["rain"],
            "Mean Temp (°C)": d_val["weather"]["mean_temp"],
            "SMAP Wetness": d_val["weather"]["wetness"],
            "Clay %": d_val["soil"]["clay"],
            "OC %": d_val["soil"]["oc"],
            "pH": d_val["soil"]["ph"],
            "Wheat (t/ha)": d_val["crops"]["wheat"]["yield"],
            "Rice (t/ha)": d_val["crops"]["rice"]["yield"],
            "Maize (t/ha)": d_val["crops"]["maize"]["yield"],
        }
    )

  df_all = pd.DataFrame(dataset_rows)
  st.dataframe(df_all, use_container_width=True)

  # CSV Download button
  csv_data = df_all.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="📥 Download Full Dataset as CSV",
      data=csv_data,
      file_name="Field_Shift_Punjab_36_Districts.csv",
      mime="text/csv",
  )