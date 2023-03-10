# (DL)시각장애인을 위한 안내 서비스

<br/>

## 프로젝트 기간
- 2022.07~

<br/>

## 프로젝트 소개 
사회적 약자를 위한 ***"Social Impact 프로젝트"*** 를 만들어 보고자 하는 취지에서 프로젝트를 시작했다.<br/>
Object detection, OCR, 음성 모델등을 통해 시각장애인들의 눈이되어 보행상황을 도와주고자 서비스를 제작했다.
<br/>

![image](https://user-images.githubusercontent.com/97331900/216985328-daa7d289-3474-4baa-abd8-b2bcaab2654e.png)

## 프로젝트 과정
#### 1. Object Detection
input으로 길거리 이미지 정보가 전달되면 자동차, 자전거 등 총 29가지의 장애물에 대해 Object Detection을 통해 객체를 탐지한다. 모델은 ***DETR***모델을 사용해 데이터를 도보 상황에 맞는 데이터로 전처리 후 학습을 통해 활용했다.
 <br/> 
#### 2. OCR
정보전달이 중요한 안내판, 바리케이드, 정류장, 교통 표지판 등의 라벨에 대해서는 글자를 탐지해주기 위해 OCR을 활용하여 Text정보를 처리했다. 모델은 Naver Clova AI team의 ***TRBA***를 활용했다.
<br/>
#### 3. Streamlit
이렇게 만들어 낸 서비스를 ***streamlit***이라는 플랫폼을 활용하여 송출하였다. 소리로 송출할 때는 Google의 ***gTTS***를 가져와 활용하였다.
