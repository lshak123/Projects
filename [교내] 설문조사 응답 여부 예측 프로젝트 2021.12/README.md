# (ML)설문조사 응답 여부 예측 프로젝트

<br/>

## 프로젝트 기간
- 2021.11~12

<br/>

## 프로젝트 소개 
설문조사 데이터와 고객의 데이터를 통해 고객이 설문조사에 응답할지를 예측하는 프로젝트
 <br/>
 평가지표 : **ROC-AUC**
 
<br/>

## 프로젝트 과정
1. 다양한 feature를 생성하여 예측 성능 향상

<br/>

2. 이상치 처리와 scaler활용해 데이터를 처리해주었다
 
 <br/>

3. **shap** 을 통한 Feature Selection을 통해 모델에 적합한 feature 선정
 
 <br/>

4. 선형회귀 모델(LinearRegression, Lidge, Lasso, ElasticNet, ARD, BayesianRidge), 트리 계열 모델(DecisionTree, RandomForest, GradientBoosting, XGBoost, LGBM, Catboost), KNN, SVR, MLP 등 많은 회귀 모델을 실험

<br/>

5. 최종적으로 **RandomForest, LGBM** / Keras 라이브러리를 사용하여 구성한 **DNN**에서의  submission을 수집하여 **submission ensemble**을 통해 최종 성능을 도출함 
 
 <br/> 

+ 성격이 약간 다른 feature_set을 활용해 LGBM의 경우는 2가지의 submission을 얻음
 
 <br/> 
 
## 느낀점
- 많은양의 feature를 생성하는 것보다 양질의 feature 몇개가 성능이 더 좋을 수 있다는 것을 느낌
- 튜닝을 통해 더 좋은 성능을 기대할 수 있었으나 하지 못했던 것이 아쉬움으로 남음
- 해결하고자 하는 문제의 성격에 따라 데이터 선정을 해야된다는것을 느낌
  - Ex) 설문 참여 여부를 판단하는 문제에서 학습할때 전체 데이터를 모두 활용한 것 보다 최근 1~2개월치의 데이터로 학습했을 때 예측 성능이 크게 오른것을 확인함
