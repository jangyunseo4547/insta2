## posts modeling
- 이미지필드 사용 위해서는 pillow 설치 필요 ! 
```python
- image = models.ImageField(upload_to = 'image') 
# image 폴더 생성 후 그 안에 이미지 저장됨 / pillow 설치    
```

## admin에 model 등록 
- 목적 : 관리자 인터페이스에서 데이터 관리를 쉽게 하기 위해

## .gitignore에 image 폴더 추가
```python
# image 폴더를 git으로 관리하지 않음.
image/
```

## 새로운 라이브러리 생성 시 requirements.txt 추가
`pip freeze > requirements.txt`

## media 설정
```python
# 업로드한 사진을 저장한 위치 (실제 폴더 경로)
 MEDIA_ROOT = BASE_DIR / 'image'
 
 # 미디어 경로를 처리할 URL
 MEDIA_URL = '/image/'
 ```