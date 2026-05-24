# emoji101.com — 项目计划

## 定位
Emoji 含义词典 + 极速复制工具。SEO/GEO 主力，Shorts/TikTok 辅助。

## 网站结构

```
emoji101.com/
├── index.html                    ← 首页：搜索 + 复制工具 + 分类浏览
├── meanings/                     ← 含义页面目录（每个emoji一个页面）
│   ├── skull-emoji.html          ← 💀 含义页
│   ├── pleading-face-emoji.html  ← 🥺 含义页
│   ├── melting-face-emoji.html   ← 🫠 含义页
│   └── ... （先做50个，后续扩充）
├── gen-z-emoji-guide.html        ← Gen Z Emoji 指南专题页
├── new-emojis-2026.html          ← 新 Emoji 资讯页（季节性爆款）
├── emoji-meanings-list.html      ← 全量含义列表页（SEO 枢纽）
└── emoji-combos.html             ← Emoji 组合页
```

## 页面设计规范

### 首页（index.html）
- 搜索栏（联想推荐，但MVP先做即时筛选）
- 分类标签（笑脸、手势、动物、食物、符号、旗帜...）
- Emoji 网格（点击复制）
- 最近使用栏
- "Emoji of the Day" 板块
- "Trending Emojis" 板块
- SEO 文字区域（300-500字描述）
- 指向含义页的内部链接
- AdSense 广告位（审核通过后上线）

### 含义页模板（每页一个emoji）
- 大号 emoji 展示（80px+）
- 官方名称 + 所有别名
- 含义解释（200-300字）
- 使用例句（3-5个场景）
- "Copy This Emoji" 按钮
- 平台显示差异对比（Apple / Google / Samsung / Microsoft）
- 相关 emoji 推荐（3-5个）
- 上一篇/下一篇导航
- SEO 结构化数据（FAQ schema）
- AdSense 广告位
- 评论区框架（可后续接 Disqus）

### 专题页模板
- Gen Z Emoji Guide： "你老了就不懂的emoji" 列表式
- New Emojis 2026： 每年新emoji预览 + 含义
- Emoji Meanings List： 字母排序全表 + 搜索

## 技术方案
- 纯 HTML/CSS/JS，无框架
- GitHub Pages 托管 + emoji101.com 域名
- 每个含义页独立 HTML（利于 SEO），但用脚本批量生成
- 页面加载 < 0.3 秒
- 移动端优先

## 关键词矩阵

### 头部词（首页目标）
- "emoji copy and paste"
- "emoji search"
- "emoji finder"

### 身体词（含义页目标，每个页面一个emoji）
- "[emoji name] meaning"（如 "skull emoji meaning"）
- "what does [emoji] mean"
- "[emoji] copy and paste"

### 长尾词（专题页目标）
- "gen z emoji meanings 2026"
- "new emojis 2026"
- "flirty emojis"
- "emoji combos for instagram"
- "most misunderstood emojis"

## 变现路径
1. AdSense（主要，含义页停留时间长 RPM 高）
2. Amazon 联盟（emoji 周边、键盘、贴纸）
3. 付费 Emoji 素材包（高级表情包）

## 推广计划

### Shorts/TikTok 内容
- "3 emojis you're using wrong"
- "This emoji means something totally different now 💀"
- "Emoji combos that will level up your IG captions"
- "What your most used emoji says about you"

### SEO 节奏
- 周1-2：首页 + 前20含义页
- 周3-4：扩展到50含义页 + 专题页
- 周5-8：扩展到100含义页 + 第一批外链
- 月2-6：每个含义页监测排名，优化表现好的

## 成功指标
- 月3：GSC 显示有搜索点击
- 月6：月访问 2,000+，AdSense $20+/月
- 月12：月访问 10,000+，AdSense $100+/月
- 月18：月访问 50,000+，总收入 $200-500/月

## 第一批 50 个热门 Emoji（含义页优先做）

### Tier 1：搜索量最大（前20个）
😂 😭 ❤️ 🔥 👍 😍 🥺 💀 ✨ 😅 🤔 🙏 🫠 🫡 😊 💕 🎉 💯 🥰 😡

### Tier 2：Gen Z 常用（15个）
🧍 🧠 👁️👄👁️ 🗿 🧢 🐸 ☕ 🤡 🛒 🤓 🧋 🫶 😮‍💨 🥲 🫥

### Tier 3：容易误解（15个）
🙃 😏 🫤 😶‍🌫️ 😈 🧐 🙇 🧎 💅 🤌 🧌 🪷 🫘 🫧 🍆

## 目录结构（本地）
```
/Users/fanny/DevProjects/Tools/emoji101/
├── PROJECT_PLAN.md          ← 本文件
├── index.html               ← 首页
├── meanings/                ← 含义页
│   ├── skull-emoji.html
│   ├── pleading-face-emoji.html
│   └── ...
├── gen-z-emoji-guide.html
├── new-emojis-2026.html
├── emoji-meanings-list.html
└── emoji-combos.html
```
