## posts modeling
- 이미지필드 사용 위해서는 pillow 설치 필요 ! 
```python
- image = models.ImageField(upload_to = 'image') 
# image 폴더 생성 후 그 안에 이미지 저장됨 / pillow 설치    
```

## admin에 model 등록 
- 목적 : 관리자 인터페이스에서 데이터 관리를 쉽게 하기 위해