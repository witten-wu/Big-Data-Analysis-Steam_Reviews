#### game_info.csv：

包含游戏本身信息，共 500 条

字段说明：
**appId:**	游戏 id
**name:**	游戏名
**is_free:**	游戏本体是否免费
**genres0:**	游戏类型1，少数为空
**genres1:**	游戏类型2，部分为空
**release_date:**	发行日期
**review_score:**	评价分数，范围 0-10
**review_score_desc:**	评价描述，与 review_score 相对应
**total_positive:**	好评总数
**total_negative:**	差评总数
**total_reviews:**	评论总数

---
#### game_reviews.csv:

包含游戏评论信息，每个游戏 200 条，约 100000 条

字段说明：
**appId:**	游戏 id
**link:**	评论者主页链接
**title:**	是否好评
**hour:**	总游玩时间
**date:**	评论创建时间
**comment:**	评论内容

