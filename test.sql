INSERT 
INTO "t_user" ( 
    "uuid"
    , "sub"
    , "name"
    , "picture"
    , "last_login_at"
    , "gender"
    , "first_page_id"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    "b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , "Ua749ed3410a6a8eb5a99bf5c5e0ccc19"
    , "櫻井"
    , "https://profile.line-scdn.net/0hWEQpeaprCGp8CR4I4Nh2FQxZCwBfeFF4BWxPC08JXgkWOUg9AjpDC05cBAhHbk9pU2tCCEgLVV9wGn8MYl_0Xns5VVtAOkk-UmhEhA"
    , "2024/01/21 10:48:25.701"
    , 0
    , ""
    , CURRENT_DATE
    , CURRENT_DATE
);

INSERT 
INTO "t_saving_history" ( 
    "id"
    ,"uuid"
    , "amount"
    , "group_id"
    , "user_id"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    1
    , "b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , 10000
    , NULL
    , 1
    , CURRENT_DATE
    , CURRENT_DATE
);

INSERT 
INTO "t_saving_history" ( 
    "id"
    ,"uuid"
    , "amount"
    , "group_id"
    , "user_id"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    2
    , "b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , 2000
    , NULL
    , 1
    , CURRENT_DATE
    , CURRENT_DATE
);

INSERT 
INTO "t_wishlist" ( 
    "id"
    ,"uuid"
    , "title"
    , "category"
    , "price"
    , "image_url"
    , "group_id"
    , "user_id"
    , "purchased_at"
    , "memo"
    , "wish_rank"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    1
    , "b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , "ピアノ"
    , 1
    , 200000
    , "ele_piano.jpg"
    , NULL
    , 1
    , CURRENT_DATE
    , "ピアノ欲しい"
    , 1
    , CURRENT_DATE
    , CURRENT_DATE
);

INSERT 
INTO "t_wishlist" ( 
    "id"
    ,"uuid"
    , "title"
    , "category"
    , "price"
    , "image_url"
    , "group_id"
    , "user_id"
    , "purchased_at"
    , "memo"
    , "wish_rank"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    2
    , "b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , "ねこ"
    , 1
    , 320000
    , "cat.jpg"
    , NULL
    , 1
    , CURRENT_DATE
    , "ねこ欲しい"
    , 2
    , CURRENT_DATE
    , CURRENT_DATE
);

INSERT 
INTO "t_wishlist" ( 
    "id"
    ,"uuid"
    , "title"
    , "category"
    , "price"
    , "image_url"
    , "group_id"
    , "user_id"
    , "purchased_at"
    , "memo"
    , "wish_rank"
    , "created_at"
    , "updated_at"
) 
VALUES ( 
    3
    ,"b5375cc3-1cae-4bf6-a467-bde2593ece75"
    , "ヨーロッパ旅行"
    , 2
    , 500000
    , "europe.jpg"
    , NULL
    , 1
    , CURRENT_DATE
    , NULL
    , 3
    , CURRENT_DATE
    , CURRENT_DATE
);