# virtual-companion

Virtual Companion for Conversation and Sentiment Analysis

## Frontend Setup

Enter in terminal

```
cd frontend
npm install
npm start
```

## Backend Setup

Download dataset for setiment analysis [here](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
Download dataset for translation (Eng to Kan) [here](https://ai4bharat.iitm.ac.in/samanantar)
Place datasets in `backend/data` folder

Create `app.db` in `backend/instance`

Enter in terminal

```
pip install -r requirements.txt
python app.py
```

## Overall Setup

Run frontend and backend simultaneously

## Dealing with CORS

Use `Allow CORS: Access-Control-Allow-Origin` extension and enable it
