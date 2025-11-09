{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dfddfe35-cefa-4be9-9c11-afd27fbf05c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "65aa3f82-18e4-4385-9188-54ddb0e566b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 16:40:44.463 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"All-in-One Data Analysis App\", layout=\"wide\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b6d3342e-b466-4abf-8795-fdad66ec3455",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 16:41:49.040 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:41:49.388 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Lenovo\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-11-07 16:41:49.389 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"All-in-One Data Analysis + Prediction App\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "53253091-ac3c-4f26-8509-bf33f0dfcced",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 16:45:37.110 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:45:37.111 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:45:37.113 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:45:37.234 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:45:37.237 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "uploaded_file = st.file_uploader(\"Upload CSV or Excel file\", type=[\"csv\", \"xlsx\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0df6e4de-f500-4d9a-8f0d-97757f62ae7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "if uploaded_file is not None:\n",
    "    if uploaded_file.name.endswith('.csv'):\n",
    "        df = pd.read-csv(uploaded_file)\n",
    "    else:\n",
    "        df = pd.read_excel(uploaded_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b337036e-8bf4-469e-9dc8-335cf2f7ec7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 16:49:04.286 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:49:04.287 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.success(\"File uploaded successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7e0358f0-f85e-4fa6-9bf0-433de55577d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 16:50:24.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 16:50:24.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m st\u001b[38;5;241m.\u001b[39msubheader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mData Preview\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m st\u001b[38;5;241m.\u001b[39mdataframe(df\u001b[38;5;241m.\u001b[39mhead())\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "st.subheader(\"Data Preview\")\n",
    "st.dataframe(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e818ae4e-f860-41a8-850e-5b34a37c7d17",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m**Rows:** \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdf\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m | **Columns:** \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdf\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m1\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m### Column Names:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;28mlist\u001b[39m(df\u001b[38;5;241m.\u001b[39mcolumns))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "st.write(f\"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}\")\n",
    "st.write(\"### Column Names:\")\n",
    "st.write(list(df.columns))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2dd445cd-78e6-430e-a79e-2238a7fda533",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:02:02.056 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:02:02.058 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[13], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m st\u001b[38;5;241m.\u001b[39msubheader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mStatistical Summary\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(df\u001b[38;5;241m.\u001b[39mdescirbe(include\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mall\u001b[39m\u001b[38;5;124m'\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "st.subheader(\"Statistical Summary\")\n",
    "st.write(df.descirbe(include='all'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "53664f96-c6a7-47a5-9a28-d1243b556957",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:06:16.938 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:06:16.940 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:06:16.944 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:06:16.945 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[14], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m st\u001b[38;5;241m.\u001b[39msubheader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAdvanced Statistics\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m**Missing Values:**\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 3\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(df\u001b[38;5;241m.\u001b[39misNone()\u001b[38;5;241m.\u001b[39msum())\n\u001b[0;32m      4\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m**Data Types:**\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      5\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(df\u001b[38;5;241m.\u001b[39mdtypes)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "st.subheader(\"Advanced Statistics\")\n",
    "st.write(\"**Missing Values:**\")\n",
    "st.write(df.isNone().sum())\n",
    "st.write(\"**Data Types:**\")\n",
    "st.write(df.dtypes)\n",
    "st.write(\"**Correlation Matrix:**\")\n",
    "st.write(df.corr(numeric_only=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "35ddb30a-703f-431a-b991-2f1e6a08fbd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:08:35.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:08:35.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:08:35.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:08:35.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.subheader(\"Visualization\")\n",
    "st.write(\"Select X and Y columns to visualize:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "dca85a6f-4f80-4ab0-8e2c-c0ee01c67fb9",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[16], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m cols \u001b[38;5;241m=\u001b[39m df\u001b[38;5;241m.\u001b[39mcolumns\u001b[38;5;241m.\u001b[39mtolist()\n\u001b[0;32m      2\u001b[0m x_col \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mselectbox(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mX-axis\u001b[39m\u001b[38;5;124m\"\u001b[39m, options\u001b[38;5;241m=\u001b[39mcols)\n\u001b[0;32m      3\u001b[0m y_col \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mselection(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mY- axis\u001b[39m\u001b[38;5;124m\"\u001b[39m, options\u001b[38;5;241m=\u001b[39mcols)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "cols = df.columns.tolist()\n",
    "x_col = st.selectbox(\"X-axis\", options=cols)\n",
    "y_col = st.selection(\"Y- axis\", options=cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "320d8dc8-d2cd-4e42-9e18-2ed06da6d313",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:12:32.685 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:12:32.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:12:32.690 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:12:32.692 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:12:32.694 Session state does not function when running a script without `streamlit run`\n",
      "2025-11-07 17:12:32.699 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:12:32.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "graph_type = st.selectbox(\"Select Graph Type\", [\"Line\", \"Bar\", \"Scatter\", \"Histogram\", \"Boxplot\",\"Heatmap\", \"Pairplot\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "153321d6-d9d1-48f1-9b2a-65a644e88594",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:28:39.611 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:28:39.616 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:28:39.618 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:28:39.622 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:28:39.625 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button(\"Generate Graph\"):\n",
    "    plt.figure(figsize=(8,5))\n",
    "    if graph_type == \"Line\":\n",
    "        sns.lineplot(data=df, x=x_col, y=y_col)\n",
    "    elif graph_type == \"Bar\":\n",
    "        sns.barplot(data=df, x=x_col, y=y_col)\n",
    "    elif graph_type == \"Scatter\":\n",
    "        sns.scattterplot(data=df, x=x_col, y=y_col)\n",
    "    elif graph_type == \"Histogram\":\n",
    "        sns.hisplot(df[x_col], kde=True)\n",
    "    elif graph_type == \"Boxplot\":\n",
    "        sns.boxplot(data=df, x=x_col, y=y_col)\n",
    "    elif graph_type == \"Heatmap\":\n",
    "        st.write(sns.heatmap(df.corr(numeric_only=True), annot=True))\n",
    "    elif graph_type == \"Pairplot\":\n",
    "        st.pyplot(sns.pairplot(df))\n",
    "    st.pyplot(plt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "dbe825b6-527b-4da5-acf2-4f53ba464e36",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:29:18.600 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:29:18.602 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.subheader(\"Machine Learning Prediction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "bdb5fdf3-82c2-4046-b183-7afb1f88d3f2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[20], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m numeric_cols \u001b[38;5;241m=\u001b[39m df\u001b[38;5;241m.\u001b[39mselect_dtypes(include\u001b[38;5;241m=\u001b[39mnp\u001b[38;5;241m.\u001b[39mnumber)\u001b[38;5;241m.\u001b[39mcolumns\u001b[38;5;241m.\u001b[39mtolist()\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "numeric_cols = df.select_dtypes(include=np.number).columns.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "72c9cd19-c1de-4d56-adff-472f4660e765",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'numeric_cols' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[21], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(numeric_cols) \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m2\u001b[39m:\n\u001b[0;32m      2\u001b[0m     st\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot enough numeric columns for prediction.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m: \n",
      "\u001b[1;31mNameError\u001b[0m: name 'numeric_cols' is not defined"
     ]
    }
   ],
   "source": [
    "if len(numeric_cols) < 2:\n",
    "    st.warning(\"Not enough numeric columns for prediction.\")\n",
    "else: \n",
    "    target_col = st.selectbox(\"Select Target (what you want to predicr)\", options=numeric_cols)\n",
    "    feature_cols = st.multiselect(\"Select Features (independent variables)\", options=[c for c in numeric_cols if c !=  target_col])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "563b671f-bc07-44c7-98b1-780aab4d726e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:36:29.703 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:36:29.705 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:36:29.706 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:36:29.708 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:36:29.710 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button(\"Train & Predict\"):\n",
    "    x = df[feature_cols]\n",
    "    y = df[target_col]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bea36fd1-9762-4d6f-aa65-3bff7b88587e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'X' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[23], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m X_train, X_test, y_train, y_test \u001b[38;5;241m=\u001b[39m train_test_split(X, y, test_size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0.2\u001b[39m, random_state\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m42\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'X' is not defined"
     ]
    }
   ],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "22e3b1d1-8039-4f07-818c-a89ac7ec4e40",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'X_train' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[24], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m model \u001b[38;5;241m=\u001b[39m LinearRegression()\n\u001b[1;32m----> 2\u001b[0m model\u001b[38;5;241m.\u001b[39mfit(X_train, y_train)\n\u001b[0;32m      3\u001b[0m y_pred \u001b[38;5;241m=\u001b[39m model\u001b[38;5;241m.\u001b[39mpredict(X_test)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'X_train' is not defined"
     ]
    }
   ],
   "source": [
    "model = LinearRegression()\n",
    "model.fit(X_train, y_train)\n",
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c124128b-cf93-458a-854c-0a3f96dc681a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:47:54.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:47:54.527 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:47:54.533 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:47:54.535 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'y_test' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[25], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m st\u001b[38;5;241m.\u001b[39msuccess(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mModel Trained Successfully!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m### Model Evaluation:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 3\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mR² Score: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mr2_score(y_test\u001b[38;5;241m.\u001b[39my_pred)\u001b[38;5;132;01m:\u001b[39;00m\u001b[38;5;124m.3f\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      4\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMean Absolute Error: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mmean_absolute_error(y_test,\u001b[38;5;250m \u001b[39my_pred)\u001b[38;5;132;01m:\u001b[39;00m\u001b[38;5;124m.3f\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      5\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMean Squared Error: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mmean_squared_error(y_test,y_pred)\u001b[38;5;132;01m:\u001b[39;00m\u001b[38;5;124m3.f\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'y_test' is not defined"
     ]
    }
   ],
   "source": [
    "st.success(\"Model Trained Successfully!\")\n",
    "st.write(\"### Model Evaluation:\")\n",
    "st.write(f\"R² Score: {r2_score(y_test.y_pred):.3f}\")\n",
    "st.write(f\"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.3f}\")\n",
    "st.write(f\"Mean Squared Error: {mean_squared_error(y_test,y_pred):3.f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3f146040-69d8-4464-827f-7226c82dde54",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:51:22.506 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:51:22.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'feature_cols' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[26], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m### Try Prediction\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m input_data \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m col \u001b[38;5;129;01min\u001b[39;00m feature_cols:\n\u001b[0;32m      4\u001b[0m     val \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mnumber_input(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mcol\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28mfloat\u001b[39m(df[col]\u001b[38;5;241m.\u001b[39mmin()), \u001b[38;5;28mfloat\u001b[39m(df[col]\u001b[38;5;241m.\u001b[39mmax()))\n\u001b[0;32m      5\u001b[0m     input_data\u001b[38;5;241m.\u001b[39mappend(val)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'feature_cols' is not defined"
     ]
    }
   ],
   "source": [
    "st.write(\"### Try Prediction\")\n",
    "input_data = []\n",
    "for col in feature_cols:\n",
    "    val = st.number_input(f\"Enter {col}\", float(df[col].min()), float(df[col].max()))\n",
    "    input_data.append(val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a936f9a8-9c8e-47ce-9df1-5ce1f39e171f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-07 17:57:39.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.968 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.970 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.972 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.984 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-07 17:57:39.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button(\"Predict Value\"):\n",
    "    pred = model.predict([input_data])\n",
    "    st.success(f\"Predicted {target_col}: {preed[0]:.3f}\")\n",
    "else:\n",
    "    st.info(\"D:ecommerce_sales_data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d00c9237-80fd-4b14-aa3a-821c86fbf845",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
