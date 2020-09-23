# 덕성여대 멋사 2학기 DJANGO 댓글 구현

1. fork로 내 원격 저장소에 가져오기
2. fork해서 만들어진 repository의 url 복사 후 clone
```git
git clone https://github.com/(아이디)/comment.git

#로그인 사용자에게만 권한 주기(20.09.23)
로그인 사용자에게만 보이게 하고 싶으면
{% if request.user.is_authenticated %}
이 안에 내용 가두기
{% endif %}

if 썼으면 반드시 endif 달기