# Video Frame Interpolation 성능 향상을 위한 기법 연구 (논문화 진행중)

## Video Frame Interpolation이란?

- 영상은 이미지를 빠르게 다음 장면으로 넘기면서 움직이는 것처럼 보이게 함
- 이 이미지가 1초에 몇개를 보여주냐에 따라 프레임 수가 결정
- 저 프레임의 영상에서 중간에 프레임을 보간하여 고프레임의 영상으로 만드는 것이 VFI(Video Frame Interpolation)임

## VFI(Video Frame Interpolation)의 모델 종류

 크게 두가지 갈래로 나뉘게 되는데 Flow 기반 추정방법과 Kernel 기반 추정방법이 있다.

- flow 기반 추정 방법
    - 기본적인 흐름은 영상 내에서 각 픽셀의 움직임을 뽑아내는 Optical Flow 추출 모델과 이를 활용하여 프레임 보간을 하는 VFI모델이 존재한다. ex) Softmax Splatting, dain
    - 모델 두개가 이어진 모형으로 End to End 구조가 아님
    - 최신 sota모델은 flow기반 모델임
- kernel 기반 추정 방법
    - kernel 기반 추정 방법은 이미지 자체를 CNN처럼 kernel을 학습하여 가운데 프레임을 생성하는 모델로 End to End 구조를 가진다. ex) FILM, AdaCoF, CDFI

## 성능 향상 기법 연구

- 영상의 객체에 집중하여 객체에 대한 정보 주입으로 객체에 대한 성능을 향상시키고자 했음
    - 해당 연구는 flow 기반 모델인 Softmax Splatting 모델을 기반으로 AIhub의 K-pop 안무영상 데이터를 전처리하여 학습시켰음.
    - 한계점 : 사용 가능한 데이터셋이 한정적이며, 우리가 학습시키고자 했던 데이터셋의 품질이 좋지 않았음. 따라서 일반화 성능이 좋지 않았음.
- 방향을 틀어 kernel based 모델인 FILM, AdaCoF, CDFI 모델들의 구조를 파악하고, 모델의 구조를 변경하여 성능을 올리고자 실험중
    - 해당 연구는 AdaCoF모델을 선정하여 이미지를 받아들이는 U-Net 구조에서 구조 변경을 통한 성능 향상을 기대하고 있음.
    - VFI모델들의 Base Dataset인 Vimeo Triplet 데이터셋과 이전에 전처리했던 K-pop 안무영상 데이터를 모두 확인해보며, 모델의 성능 향상, 경량화 등 다양한 실험을 진행중임
  
![image](https://user-images.githubusercontent.com/97331900/217249446-aa6e99ae-4be7-448a-b92c-e93b7664f562.png)
