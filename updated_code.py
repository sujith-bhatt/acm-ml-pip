{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing csv into python as a dataset\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "dataset = pd.read_csv(r'C:\\Users\\rakki\\Downloads\\acm-ml-pip-master\\loan_mortgage_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#replacing false with 0 and true with 1\n",
    "dataset.co_applicant = dataset.co_applicant.replace({True: 1, False: 0})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        row_id  loan_type  property_type  loan_purpose  occupancy  \\\n",
      "0            0          3              1             1          1   \n",
      "1            1          1              1             3          1   \n",
      "2            2          2              1             3          1   \n",
      "3            3          1              1             1          1   \n",
      "4            4          1              1             1          1   \n",
      "...        ...        ...            ...           ...        ...   \n",
      "499995  499995          1              1             1          2   \n",
      "499996  499996          1              1             1          1   \n",
      "499997  499997          1              2             1          1   \n",
      "499998  499998          1              1             2          1   \n",
      "499999  499999          1              1             3          1   \n",
      "\n",
      "        loan_amount  preapproval  msa_md  state_code  county_code  ...  \\\n",
      "0                70            3      18          37          246  ...   \n",
      "1               178            3     369          52          299  ...   \n",
      "2               163            3      16          10          306  ...   \n",
      "3               155            1     305          47          180  ...   \n",
      "4               305            3      24          37           20  ...   \n",
      "...             ...          ...     ...         ...          ...  ...   \n",
      "499995          150            1      -1          -1           -1  ...   \n",
      "499996          140            3      74          47           98  ...   \n",
      "499997           22            3      -1          46          131  ...   \n",
      "499998           35            3     367           6          149  ...   \n",
      "499999           71            3     408          28          133  ...   \n",
      "\n",
      "        applicant_income   population  minority_population_pct  \\\n",
      "0                   24.0  6203.000000                 44.23000   \n",
      "1                   57.0  5774.000000                 15.90500   \n",
      "2                   67.0  6094.000000                 61.27000   \n",
      "3                  105.0  6667.000000                  6.24600   \n",
      "4                   71.0  6732.000000                100.00000   \n",
      "...                  ...          ...                      ...   \n",
      "499995              87.0  5416.833956                 31.61731   \n",
      "499996             216.0  3452.000000                  6.88700   \n",
      "499997              35.0  2925.000000                 36.04600   \n",
      "499998              41.0  3442.000000                 98.87900   \n",
      "499999              85.0  3856.000000                 12.09500   \n",
      "\n",
      "        ffiecmedian_family_income  tract_to_msa_md_income_pct  \\\n",
      "0                    60588.000000                   50.933000   \n",
      "1                    54821.000000                  100.000000   \n",
      "2                    67719.000000                  100.000000   \n",
      "3                    78439.000000                  100.000000   \n",
      "4                    63075.000000                   82.200000   \n",
      "...                           ...                         ...   \n",
      "499995               69235.603298                   91.832624   \n",
      "499996               86307.000000                  100.000000   \n",
      "499997               47826.000000                  100.000000   \n",
      "499998               60327.000000                   62.803000   \n",
      "499999               45033.000000                  100.000000   \n",
      "\n",
      "        number_of_owner-occupied_units  number_of_1_to_4_family_units  lender  \\\n",
      "0                           716.000000                    2642.000000    4536   \n",
      "1                          1622.000000                    2108.000000    2458   \n",
      "2                           760.000000                    1048.000000    5710   \n",
      "3                          2025.000000                    2299.000000    5888   \n",
      "4                          1464.000000                    1847.000000     289   \n",
      "...                                ...                            ...     ...   \n",
      "499995                     1427.718282                    1886.147065     969   \n",
      "499996                     1423.000000                    1944.000000    5359   \n",
      "499997                     1062.000000                    1762.000000    2318   \n",
      "499998                      618.000000                    1297.000000    5339   \n",
      "499999                     1525.000000                    2750.000000    5710   \n",
      "\n",
      "        co_applicant  accepted  \n",
      "0                  0         1  \n",
      "1                  0         0  \n",
      "2                  0         1  \n",
      "3                  1         1  \n",
      "4                  0         1  \n",
      "...              ...       ...  \n",
      "499995             1         0  \n",
      "499996             1         0  \n",
      "499997             0         0  \n",
      "499998             0         0  \n",
      "499999             1         0  \n",
      "\n",
      "[500000 rows x 23 columns]\n"
     ]
    }
   ],
   "source": [
    "#Filling empty values with mean\n",
    "dataset=dataset.fillna(dataset.mean())\n",
    "print(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.to_numpy of         row_id  loan_type  property_type  loan_purpose  occupancy  \\\n",
       "0            0          3              1             1          1   \n",
       "1            1          1              1             3          1   \n",
       "2            2          2              1             3          1   \n",
       "3            3          1              1             1          1   \n",
       "4            4          1              1             1          1   \n",
       "...        ...        ...            ...           ...        ...   \n",
       "499995  499995          1              1             1          2   \n",
       "499996  499996          1              1             1          1   \n",
       "499997  499997          1              2             1          1   \n",
       "499998  499998          1              1             2          1   \n",
       "499999  499999          1              1             3          1   \n",
       "\n",
       "        loan_amount  preapproval  msa_md  state_code  county_code  ...  \\\n",
       "0                70            3      18          37          246  ...   \n",
       "1               178            3     369          52          299  ...   \n",
       "2               163            3      16          10          306  ...   \n",
       "3               155            1     305          47          180  ...   \n",
       "4               305            3      24          37           20  ...   \n",
       "...             ...          ...     ...         ...          ...  ...   \n",
       "499995          150            1      -1          -1           -1  ...   \n",
       "499996          140            3      74          47           98  ...   \n",
       "499997           22            3      -1          46          131  ...   \n",
       "499998           35            3     367           6          149  ...   \n",
       "499999           71            3     408          28          133  ...   \n",
       "\n",
       "        applicant_income   population  minority_population_pct  \\\n",
       "0                   24.0  6203.000000                 44.23000   \n",
       "1                   57.0  5774.000000                 15.90500   \n",
       "2                   67.0  6094.000000                 61.27000   \n",
       "3                  105.0  6667.000000                  6.24600   \n",
       "4                   71.0  6732.000000                100.00000   \n",
       "...                  ...          ...                      ...   \n",
       "499995              87.0  5416.833956                 31.61731   \n",
       "499996             216.0  3452.000000                  6.88700   \n",
       "499997              35.0  2925.000000                 36.04600   \n",
       "499998              41.0  3442.000000                 98.87900   \n",
       "499999              85.0  3856.000000                 12.09500   \n",
       "\n",
       "        ffiecmedian_family_income  tract_to_msa_md_income_pct  \\\n",
       "0                    60588.000000                   50.933000   \n",
       "1                    54821.000000                  100.000000   \n",
       "2                    67719.000000                  100.000000   \n",
       "3                    78439.000000                  100.000000   \n",
       "4                    63075.000000                   82.200000   \n",
       "...                           ...                         ...   \n",
       "499995               69235.603298                   91.832624   \n",
       "499996               86307.000000                  100.000000   \n",
       "499997               47826.000000                  100.000000   \n",
       "499998               60327.000000                   62.803000   \n",
       "499999               45033.000000                  100.000000   \n",
       "\n",
       "        number_of_owner-occupied_units  number_of_1_to_4_family_units  lender  \\\n",
       "0                           716.000000                    2642.000000    4536   \n",
       "1                          1622.000000                    2108.000000    2458   \n",
       "2                           760.000000                    1048.000000    5710   \n",
       "3                          2025.000000                    2299.000000    5888   \n",
       "4                          1464.000000                    1847.000000     289   \n",
       "...                                ...                            ...     ...   \n",
       "499995                     1427.718282                    1886.147065     969   \n",
       "499996                     1423.000000                    1944.000000    5359   \n",
       "499997                     1062.000000                    1762.000000    2318   \n",
       "499998                      618.000000                    1297.000000    5339   \n",
       "499999                     1525.000000                    2750.000000    5710   \n",
       "\n",
       "        co_applicant  accepted  \n",
       "0                  0         1  \n",
       "1                  0         0  \n",
       "2                  0         1  \n",
       "3                  1         1  \n",
       "4                  0         1  \n",
       "...              ...       ...  \n",
       "499995             1         0  \n",
       "499996             1         0  \n",
       "499997             0         0  \n",
       "499998             0         0  \n",
       "499999             1         0  \n",
       "\n",
       "[500000 rows x 23 columns]>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Converting into numpy array\n",
    "dataset.to_numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.73204734,  2.36581379, -0.20591757, ...,  0.44381963,\n",
       "        -0.81658504,  0.9995441 ],\n",
       "       [-1.73204042, -0.53040833, -0.20591757, ..., -0.68656561,\n",
       "        -0.81658504, -1.0004561 ],\n",
       "       [-1.73203349,  0.91770273, -0.20591757, ...,  1.08244921,\n",
       "        -0.81658504,  0.9995441 ],\n",
       "       ...,\n",
       "       [ 1.73203349, -0.53040833,  4.11554237, ..., -0.76272246,\n",
       "        -0.81658504, -1.0004561 ],\n",
       "       [ 1.73204042, -0.53040833, -0.20591757, ...,  0.88063356,\n",
       "        -0.81658504, -1.0004561 ],\n",
       "       [ 1.73204734, -0.53040833, -0.20591757, ...,  1.08244921,\n",
       "         1.2246122 , -1.0004561 ]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Scaling or Normalizing the data\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "scaler = StandardScaler()\n",
    "scaler.fit_transform(dataset)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>loan_type</th>\n",
       "      <th>property_type</th>\n",
       "      <th>loan_purpose</th>\n",
       "      <th>occupancy</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>preapproval</th>\n",
       "      <th>msa_md</th>\n",
       "      <th>county_code</th>\n",
       "      <th>applicant_income</th>\n",
       "      <th>population</th>\n",
       "      <th>minority_population_pct</th>\n",
       "      <th>ffiecmedian_family_income</th>\n",
       "      <th>number_of_owner-occupied_units</th>\n",
       "      <th>number_of_1_to_4_family_units</th>\n",
       "      <th>lender</th>\n",
       "      <th>co_applicant</th>\n",
       "      <th>accepted</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>18</td>\n",
       "      <td>246</td>\n",
       "      <td>24.0</td>\n",
       "      <td>6203.000000</td>\n",
       "      <td>44.23000</td>\n",
       "      <td>60588.000000</td>\n",
       "      <td>716.000000</td>\n",
       "      <td>2642.000000</td>\n",
       "      <td>4536</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>178</td>\n",
       "      <td>3</td>\n",
       "      <td>369</td>\n",
       "      <td>299</td>\n",
       "      <td>57.0</td>\n",
       "      <td>5774.000000</td>\n",
       "      <td>15.90500</td>\n",
       "      <td>54821.000000</td>\n",
       "      <td>1622.000000</td>\n",
       "      <td>2108.000000</td>\n",
       "      <td>2458</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>163</td>\n",
       "      <td>3</td>\n",
       "      <td>16</td>\n",
       "      <td>306</td>\n",
       "      <td>67.0</td>\n",
       "      <td>6094.000000</td>\n",
       "      <td>61.27000</td>\n",
       "      <td>67719.000000</td>\n",
       "      <td>760.000000</td>\n",
       "      <td>1048.000000</td>\n",
       "      <td>5710</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>155</td>\n",
       "      <td>1</td>\n",
       "      <td>305</td>\n",
       "      <td>180</td>\n",
       "      <td>105.0</td>\n",
       "      <td>6667.000000</td>\n",
       "      <td>6.24600</td>\n",
       "      <td>78439.000000</td>\n",
       "      <td>2025.000000</td>\n",
       "      <td>2299.000000</td>\n",
       "      <td>5888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>305</td>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "      <td>71.0</td>\n",
       "      <td>6732.000000</td>\n",
       "      <td>100.00000</td>\n",
       "      <td>63075.000000</td>\n",
       "      <td>1464.000000</td>\n",
       "      <td>1847.000000</td>\n",
       "      <td>289</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>499995</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>150</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>-1</td>\n",
       "      <td>87.0</td>\n",
       "      <td>5416.833956</td>\n",
       "      <td>31.61731</td>\n",
       "      <td>69235.603298</td>\n",
       "      <td>1427.718282</td>\n",
       "      <td>1886.147065</td>\n",
       "      <td>969</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>499996</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>140</td>\n",
       "      <td>3</td>\n",
       "      <td>74</td>\n",
       "      <td>98</td>\n",
       "      <td>216.0</td>\n",
       "      <td>3452.000000</td>\n",
       "      <td>6.88700</td>\n",
       "      <td>86307.000000</td>\n",
       "      <td>1423.000000</td>\n",
       "      <td>1944.000000</td>\n",
       "      <td>5359</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>499997</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>22</td>\n",
       "      <td>3</td>\n",
       "      <td>-1</td>\n",
       "      <td>131</td>\n",
       "      <td>35.0</td>\n",
       "      <td>2925.000000</td>\n",
       "      <td>36.04600</td>\n",
       "      <td>47826.000000</td>\n",
       "      <td>1062.000000</td>\n",
       "      <td>1762.000000</td>\n",
       "      <td>2318</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>499998</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>35</td>\n",
       "      <td>3</td>\n",
       "      <td>367</td>\n",
       "      <td>149</td>\n",
       "      <td>41.0</td>\n",
       "      <td>3442.000000</td>\n",
       "      <td>98.87900</td>\n",
       "      <td>60327.000000</td>\n",
       "      <td>618.000000</td>\n",
       "      <td>1297.000000</td>\n",
       "      <td>5339</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>499999</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>71</td>\n",
       "      <td>3</td>\n",
       "      <td>408</td>\n",
       "      <td>133</td>\n",
       "      <td>85.0</td>\n",
       "      <td>3856.000000</td>\n",
       "      <td>12.09500</td>\n",
       "      <td>45033.000000</td>\n",
       "      <td>1525.000000</td>\n",
       "      <td>2750.000000</td>\n",
       "      <td>5710</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>500000 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        loan_type  property_type  loan_purpose  occupancy  loan_amount  \\\n",
       "0               3              1             1          1           70   \n",
       "1               1              1             3          1          178   \n",
       "2               2              1             3          1          163   \n",
       "3               1              1             1          1          155   \n",
       "4               1              1             1          1          305   \n",
       "...           ...            ...           ...        ...          ...   \n",
       "499995          1              1             1          2          150   \n",
       "499996          1              1             1          1          140   \n",
       "499997          1              2             1          1           22   \n",
       "499998          1              1             2          1           35   \n",
       "499999          1              1             3          1           71   \n",
       "\n",
       "        preapproval  msa_md  county_code  applicant_income   population  \\\n",
       "0                 3      18          246              24.0  6203.000000   \n",
       "1                 3     369          299              57.0  5774.000000   \n",
       "2                 3      16          306              67.0  6094.000000   \n",
       "3                 1     305          180             105.0  6667.000000   \n",
       "4                 3      24           20              71.0  6732.000000   \n",
       "...             ...     ...          ...               ...          ...   \n",
       "499995            1      -1           -1              87.0  5416.833956   \n",
       "499996            3      74           98             216.0  3452.000000   \n",
       "499997            3      -1          131              35.0  2925.000000   \n",
       "499998            3     367          149              41.0  3442.000000   \n",
       "499999            3     408          133              85.0  3856.000000   \n",
       "\n",
       "        minority_population_pct  ffiecmedian_family_income  \\\n",
       "0                      44.23000               60588.000000   \n",
       "1                      15.90500               54821.000000   \n",
       "2                      61.27000               67719.000000   \n",
       "3                       6.24600               78439.000000   \n",
       "4                     100.00000               63075.000000   \n",
       "...                         ...                        ...   \n",
       "499995                 31.61731               69235.603298   \n",
       "499996                  6.88700               86307.000000   \n",
       "499997                 36.04600               47826.000000   \n",
       "499998                 98.87900               60327.000000   \n",
       "499999                 12.09500               45033.000000   \n",
       "\n",
       "        number_of_owner-occupied_units  number_of_1_to_4_family_units  lender  \\\n",
       "0                           716.000000                    2642.000000    4536   \n",
       "1                          1622.000000                    2108.000000    2458   \n",
       "2                           760.000000                    1048.000000    5710   \n",
       "3                          2025.000000                    2299.000000    5888   \n",
       "4                          1464.000000                    1847.000000     289   \n",
       "...                                ...                            ...     ...   \n",
       "499995                     1427.718282                    1886.147065     969   \n",
       "499996                     1423.000000                    1944.000000    5359   \n",
       "499997                     1062.000000                    1762.000000    2318   \n",
       "499998                      618.000000                    1297.000000    5339   \n",
       "499999                     1525.000000                    2750.000000    5710   \n",
       "\n",
       "        co_applicant  accepted  \n",
       "0                  0         1  \n",
       "1                  0         0  \n",
       "2                  0         1  \n",
       "3                  1         1  \n",
       "4                  0         1  \n",
       "...              ...       ...  \n",
       "499995             1         0  \n",
       "499996             1         0  \n",
       "499997             0         0  \n",
       "499998             0         0  \n",
       "499999             1         0  \n",
       "\n",
       "[500000 rows x 17 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Dropping unnecessary columns\n",
    "dataset.drop(['applicant_sex','applicant_ethnicity','applicant_race','state_code','row_id','tract_to_msa_md_income_pct'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Slicing the dataset\n",
    "X = dataset.iloc[:, :-1].values\n",
    "y = dataset.iloc[:, -1].values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Splitting the dataset into a training:testing split of 90:10\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing random forest classifier and training it\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import roc_auc_score\n",
    "from xgboost import XGBRegressor\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "#svclassifier = SVC(kernel='linear')\n",
    "#svclassifier.fit(X_train, y_train)\n",
    "#my_model_2 = XGBRegressor(random_state=0,n_estimators=1000,learning_rate=0.05,objective=\"binary:logistic\") \n",
    "#my_model_2.fit(X_train, y_train)\n",
    "clf = RandomForestClassifier(n_estimators=100,n_jobs=4,max_depth=5, random_state=42)\n",
    "clf.fit(X_train,y_train)\n",
    "# instantiate the model (using the default parameters)\n",
    "#logreg = LogisticRegression(random_state=0)\n",
    "\n",
    "# fit the model with data\n",
    "#logreg.fit(X_train,y_train)\n",
    "\n",
    "#\n",
    "y_pred=clf.predict(X_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Checking accuracy\n",
    "from sklearn.metrics import classification_report, confusion_matrix, accuracy_score\n",
    "result = confusion_matrix(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Confusion Matrix:\n",
      "[[39942 22568]\n",
      " [19305 43185]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Confusion Matrix:\")\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "result1 = classification_report(y_test, y_pred)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report:\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.67      0.64      0.66     62510\n",
      "           1       0.66      0.69      0.67     62490\n",
      "\n",
      "    accuracy                           0.67    125000\n",
      "   macro avg       0.67      0.67      0.66    125000\n",
      "weighted avg       0.67      0.67      0.66    125000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"Classification Report:\",)\n",
    "print (result1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.665016\n"
     ]
    }
   ],
   "source": [
    "result2 = accuracy_score(y_test,y_pred)\n",
    "print(\"Accuracy:\",result2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
