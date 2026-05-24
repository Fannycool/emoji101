import os, json

OUT_DIR = '/Users/fanny/DevProjects/Tools/emoji101/meanings'

DATA = [
  {"e":"😂","slug":"face-with-tears-of-joy","name":"Face with Tears of Joy","aliases":"laughing crying emoji, lol emoji, tears of joy, funny emoji","meaning":"The <strong>Face with Tears of Joy</strong> (😂) is the most used emoji worldwide. It shows a face laughing so hard that tears stream down its cheeks. It expresses that something is extremely funny — the kind of laugh where you can't breathe. Unlike 😭 (loudly crying face), this emoji is about <strong>happy tears</strong>, not sadness.<br><br>In 2015, Oxford Dictionaries named 😂 the <strong>Word of the Year</strong> — the first time an emoji won. While Gen Z sometimes calls it \"cheugy\" (outdated), it remains the most universally understood emoji across all age groups. Use it when something is genuinely hilarious, not just mildly amusing.","usage":["\"That joke was so bad it's good 😂\"","\"When you trip in public and pretend you meant to do that 😂\"","\"Me watching my dog run into a glass door for the third time 😂\""],"related":["🤣","😹","💀","😭","😅"],"cat":"smileys"},
  {"e":"💀","slug":"skull-emoji","name":"Skull","aliases":"skull emoji, death emoji, dead, dying of laughter, Gen Z skull","meaning":"The <strong>Skull emoji</strong> (💀) has undergone one of the biggest meaning shifts in emoji history. Originally meaning death, danger, or poison, Gen Z repurposed it to mean <strong>\"I'm dead\" — from laughing so hard</strong>. It's essentially the new 😂 for younger users.<br><br>When someone says \"that's so funny I'm dead 💀\", they're using the skull as an intensifier for humor. It can also express figurative death: \"This assignment is killing me 💀\" or \"I stayed up until 4am 💀\". Unlike the literal skull-and-crossbones ☠️, the plain skull 💀 is used almost exclusively in the slang sense by younger generations. If you see a millennial or Gen X use it, they might still mean it literally — context is everything.","usage":["\"This TikTok had me crying 💀\"","\"My boss just asked if I could work Saturday 💀\"","\"When your mom finds your finsta 💀\"","\"The wifi went out during my final exam 💀\""],"related":["😂","🤣","😭","🪦","☠️"],"cat":"smileys"},
  {"e":"🥺","slug":"pleading-face","name":"Pleading Face","aliases":"pleading face, puppy eyes, begging emoji, cute emoji, please emoji","meaning":"The <strong>Pleading Face</strong> (🥺) is one of the most emotionally versatile emojis. With its big, glossy puppy-dog eyes and slight frown, it conveys <strong>begging, adoration, vulnerability, or being overwhelmed by cuteness</strong>. It makes the user appear small and endearing — perfect for asking for a favor or reacting to something adorable.<br><br>This emoji became hugely popular in 2019-2020 on stan Twitter (fan communities) as a reaction to favorite celebrities or cute animals. It can mean \"please please please\" when asking for something, or \"I can't handle how cute this is\" when reacting. Unlike 😢 (crying face), it's not about sadness — it's about being <strong>soft</strong>. In romantic contexts, it can be flirty: \"Come over 🥺\". It's one of the most-searched emoji meanings on Google because its usage is so nuanced.","usage":["\"Can we please get pizza tonight 🥺\"","\"Look at this puppy I'm in love 🥺\"","\"Text me back please 🥺\"","\"This video of the cat hugging its owner 🥺\""],"related":["😢","😭","🥰","😊","🙏"],"cat":"smileys"},
  {"e":"🫠","slug":"melting-face","name":"Melting Face","aliases":"melting face, melting emoji, embarrassed emoji, overwhelmed, dissolving","meaning":"The <strong>Melting Face</strong> (🫠) was introduced in 2022 and quickly became a favorite. It shows a face dissolving downward, like a popsicle in summer. It expresses <strong>embarrassment, being overwhelmed, extreme heat, or feeling like you're dissolving into a puddle</strong>.<br><br>Use it when you're so embarrassed you want to sink into the floor: \"I waved at someone who wasn't waving at me 🫠\". Or when you're completely overwhelmed: \"Looking at my inbox like 🫠\". It's also the perfect emoji for a brutally hot day: \"It's 105 degrees and my AC broke 🫠\". Because it's relatively new, its meanings are still evolving — early adopters of new emojis often shape their cultural meaning.","usage":["\"When you realize you've been pronouncing a word wrong your entire life 🫠\"","\"Me after that 3-hour Zoom meeting 🫠\"","\"Summer in Arizona be like 🫠\"","\"Seeing the price of eggs in 2026 🫠\""],"related":["😅","😰","🥵","😮‍💨","🫥"],"cat":"smileys"},
  {"e":"🫡","slug":"saluting-face","name":"Saluting Face","aliases":"saluting face, salute emoji, respect, yes sir, reporting for duty","meaning":"The <strong>Saluting Face</strong> (🫡) shows a face with one hand raised in a military-style salute. Introduced in 2022, it quickly spread as a way to say <strong>\"understood,\" \"I'm on it,\" or \"respect.\"</strong> It conveys a sense of duty, loyalty, and readiness — like saying \"yes sir\" or \"reporting for duty.\"<br><br>It's widely used on social media when someone is about to do something with determination: \"Time to study for this exam 🫡\". It also expresses respect or gratitude: \"Thank you for your service 🫡\". In gaming communities, it's used as a respectful sign-off before a mission. Because the emoji is gender-neutral and the expression is earnest (not ironic), it works in a wide range of contexts — from professional Slack channels to meme pages.","usage":["\"Starting my new job today 🫡\"","\"Respect to all the teachers out there 🫡\"","\"3am and still debugging — reporting for duty 🫡\"","\"You handled that so well, salute 🫡\""],"related":["👍","🙏","🤝","👏","💪"],"cat":"smileys"},
  {"e":"😭","slug":"loudly-crying-face","name":"Loudly Crying Face","aliases":"loudly crying, crying emoji, sobbing, overwhelmed with emotion, ugly cry","meaning":"The <strong>Loudly Crying Face</strong> (😭) shows a face with an open mouth and streams of tears flooding from closed eyes. It expresses <strong>overwhelming emotion — sadness, joy, laughter, or being deeply moved</strong>. This is not a quiet tear (😢) but full-on sobbing, the kind where your face is wet and you can't speak.<br><br>Despite technically being a sad emoji, 😭 is frequently used for <strong>happy crying</strong> — when something is so beautiful, heartwarming, or funny that it brings you to tears. \"This wedding video 😭\" means it's incredibly touching, not tragic. It's also used hyperbolically for minor frustrations: \"They were out of oat milk 😭\". The key distinction from 😂 is that 😭 implies a stronger, more overwhelming emotional response — you're not just laughing, you're <strong>moved</strong>.","usage":["\"This movie ending has me sobbing 😭\"","\"My best friend surprised me for my birthday 😭\"","\"When your code finally works after 4 hours 😭\"","\"They canceled my favorite show 😭\""],"related":["😂","😢","🥲","🥺","💔"],"cat":"smileys"},
]

def gen_page(d):
  title = f'{d["e"]} {d["name"]} Emoji — Meaning, Copy & Paste'
  desc = d["meaning"][:160].replace('<strong>','').replace('</strong>','').replace('<br>',' ') + '...'

  related_html = ''.join([f'<a href="{r.lower().replace(" ","-")}-emoji.html" class="rel-chip">{r}</a>' for r in d["related"]])
  usage_html = ''.join([f'<li>{u}</li>' for u in d["usage"]])

  html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MJ9EFVJYNZ"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-MJ9EFVJYNZ');</script>
<style>
:root{{--primary:#FF6B35;--primary-light:#FFF0E8;--bg:#F8F9FA;--card:#fff;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.7}}
.container{{max-width:680px;margin:0 auto;padding:20px 16px}}
.header{{text-align:center;padding:40px 0 24px}}
.header .big-emoji{{font-size:96px;line-height:1.2;margin-bottom:12px}}
.header h1{{font-size:24px;font-weight:700;margin-bottom:6px}}
.header .aliases{{font-size:14px;color:var(--text-secondary)}}
.nav-back{{display:inline-block;margin-bottom:20px;font-size:14px;color:var(--primary);text-decoration:none}}
.nav-back:hover{{text-decoration:underline}}
.copy-bar{{background:var(--card);border:1.5px solid var(--border);border-radius:var(--radius);padding:16px 20px;display:flex;align-items:center;gap:12px;margin-bottom:20px;flex-wrap:wrap}}
.copy-bar .emoji-display{{font-size:40px;flex-shrink:0}}
.copy-bar .copy-info{{flex:1;min-width:140px}}
.copy-bar .copy-name{{font-weight:600;font-size:15px}}
.copy-bar .copy-hint{{font-size:13px;color:var(--text-secondary)}}
.copy-bar .copy-btn{{padding:10px 20px;background:var(--primary);color:#fff;border:none;border-radius:20px;font-size:14px;font-weight:600;cursor:pointer;font-family:var(--font);white-space:nowrap;transition:all .15s}}
.copy-bar .copy-btn:hover{{opacity:.9;transform:scale(1.03)}}
.copy-bar .copy-btn.copied{{background:#059669}}
.card{{background:var(--card);border-radius:var(--radius);padding:24px;margin-bottom:16px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid var(--border)}}
.card h2{{font-size:20px;margin-bottom:14px}}
.card p{{font-size:15px;line-height:1.8;color:var(--text-secondary);margin-bottom:12px}}
.card h3{{font-size:16px;margin:16px 0 10px}}
.card ul{{padding-left:20px;margin-bottom:12px}}
.card li{{font-size:15px;color:var(--text-secondary);margin-bottom:8px;line-height:1.6}}
.related-bar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}}
.related-bar .rel-label{{font-size:13px;color:var(--text-muted)}}
.rel-chip{{display:inline-block;padding:6px 14px;background:var(--primary-light);color:var(--primary);border-radius:16px;text-decoration:none;font-size:14px;font-weight:500;transition:all .15s}}
.rel-chip:hover{{background:var(--primary);color:#fff}}
.prev-next{{display:flex;gap:12px;justify-content:space-between;margin-bottom:20px}}
.prev-next a{{font-size:14px;color:var(--primary);text-decoration:none}}
.footer{{text-align:center;padding:32px 16px;color:#94A3B8;font-size:13px}}
.footer a{{color:var(--primary);text-decoration:none}}
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#1E293B;color:#fff;padding:10px 24px;border-radius:20px;font-size:14px;font-weight:500;box-shadow:0 10px 25px rgba(0,0,0,.2);z-index:999;opacity:0;transition:opacity .2s;pointer-events:none}}
.toast.show{{opacity:1}}
@media(max-width:480px){{.container{{padding:12px 8px}}.header .big-emoji{{font-size:72px}}.copy-bar{{flex-direction:column;text-align:center}}}}
</style>
</head>
<body>
<div class="container">
<a href="/" class="nav-back">← Back to Emoji101</a>
<div class="header">
  <div class="big-emoji">{d["e"]}</div>
  <h1>{d["name"]} Emoji {d["e"]}</h1>
  <p class="aliases">Also known as: {d["aliases"]}</p>
</div>

<div class="copy-bar" id="copyBar">
  <div class="emoji-display">{d["e"]}</div>
  <div class="copy-info">
    <div class="copy-name">{d["name"]}</div>
    <div class="copy-hint">Click to copy this emoji</div>
  </div>
  <button class="copy-btn" id="copyBtn" onclick="copyEmoji('{d["e"]}')">Copy Emoji</button>
</div>

<div class="related-bar">
  <span class="rel-label">Related:</span>
  {related_html}
</div>

<div class="card">
  <h2>What Does {d["e"]} Mean?</h2>
  <p>{d["meaning"]}</p>
</div>

<div class="card">
  <h2>How to Use the {d["name"]} Emoji {d["e"]}</h2>
  <h3>Example Sentences</h3>
  <ul>{usage_html}</ul>
</div>

<div class="card">
  <h2>When to Use {d["e"]} vs Similar Emojis</h2>
  <p>Not sure if {d["e"]} is the right choice? The {d["name"]} emoji is best for expressing the specific emotions described above. If you need a different nuance, try one of the related emojis listed above. Each emoji carries its own emotional weight and cultural context — choosing the right one can completely change how your message lands.</p>
</div>

<div class="card">
  <h2>Copy & Paste {d["e"]}</h2>
  <p>Click the copy button above to copy the {d["name"]} emoji ({d["e"]}) to your clipboard. Then paste it anywhere — iMessage, WhatsApp, Instagram, TikTok, Twitter, Facebook, email, or any app that supports emojis. On desktop, you can also <strong>right-click the emoji and select \"Copy Emoji\"</strong> or use <strong>Ctrl+C (Cmd+C on Mac)</strong> after selecting it.</p>
</div>

<div class="prev-next">
  <a href="/">← Back to All Emojis</a>
  <a href="/meanings/">Browse All Meanings →</a>
</div>
</div>

<footer class="footer">
  <p><a href="/">emoji101.com</a> — Fast emoji search & meanings</p>
</footer>
<div class="toast" id="toast">Copied!</div>
<script>
function copyEmoji(e){{
  navigator.clipboard.writeText(e).then(()=>{{
    var t=document.getElementById('toast');var b=document.getElementById('copyBtn');
    t.classList.add('show');b.textContent='Copied!';b.classList.add('copied');
    setTimeout(()=>{{t.classList.remove('show');b.textContent='Copy Emoji';b.classList.remove('copied');}},1500);
  }});
}}
(function(){{
  var k='pv_meanings_{d["slug"]}',d={{total:0,unique:0,first:'',last:''}};
  try{{var s=localStorage.getItem(k);if(s)d=JSON.parse(s);}}catch(e){{}}
  d.total++;var t=new Date().toISOString().split('T')[0];
  if(d.last!==t){{d.unique++;d.last=t;}}
  if(!d.first)d.first=t;
  try{{localStorage.setItem(k,JSON.stringify(d));}}catch(e){{}}
}})();
</script>
</body>
</html>'''
  return html

# Generate all pages
os.makedirs(OUT_DIR, exist_ok=True)
for d in DATA:
  html = gen_page(d)
  path = os.path.join(OUT_DIR, f'{d["slug"]}.html')
  with open(path, 'w') as f:
    f.write(html)
  print(f'Created: {d["slug"]}.html')

# Create index page for meanings directory
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Emoji Meanings — Complete Emoji Dictionary | Emoji101</title>
<meta name="description" content="Browse all emoji meanings. Search by emoji or keyword. Find out what every emoji really means. Free emoji dictionary.">
<style>
:root{--primary:#FF6B35;--primary-light:#FFF0E8;--bg:#F8F9FA;--card:#fff;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.7}
.container{max-width:680px;margin:0 auto;padding:20px 16px}
.header{text-align:center;padding:40px 0 24px}
.header h1{font-size:28px;font-weight:800;margin-bottom:6px}
.header p{color:var(--text-secondary);font-size:15px}
.nav-back{display:inline-block;margin-bottom:20px;font-size:14px;color:var(--primary);text-decoration:none}
.emoji-list{display:flex;flex-direction:column;gap:8px}
.emoji-row{display:flex;align-items:center;gap:14px;padding:14px 18px;background:var(--card);border-radius:var(--radius);text-decoration:none;color:var(--text);border:1px solid var(--border);transition:all .15s}
.emoji-row:hover{border-color:var(--primary);transform:translateX(4px)}
.emoji-row .e{font-size:36px;flex-shrink:0}
.emoji-row .info{flex:1}
.emoji-row .info .n{font-weight:600;font-size:15px}
.emoji-row .info .a{font-size:13px;color:var(--text-secondary);margin-top:2px}
.emoji-row .arrow{color:var(--primary);font-size:18px}
.footer{text-align:center;padding:32px 16px;color:#94A3B8;font-size:13px}
.footer a{color:var(--primary);text-decoration:none}
</style>
</head>
<body>
<div class="container">
<a href="/" class="nav-back">← Back to Emoji101</a>
<div class="header">
  <h1>Emoji Meanings Dictionary</h1>
  <p>Click any emoji to see its full meaning, usage examples, and related emojis.</p>
</div>
<div class="emoji-list">
'''
for d in DATA:
  index_html += f'''  <a href="{d['slug']}.html" class="emoji-row">
    <span class="e">{d['e']}</span>
    <span class="info"><span class="n">{d['name']}</span><br><span class="a">{d['aliases'][:60]}...</span></span>
    <span class="arrow">→</span>
  </a>\n'''

index_html += '''</div>
</div>
<footer class="footer"><p><a href="/">emoji101.com</a></p></footer>
</body>
</html>'''

with open(os.path.join(OUT_DIR, 'index.html'), 'w') as f:
  f.write(index_html)
print('Created: index.html (meanings directory)')

print(f'\nDone! Generated {len(DATA)} pages.')

MORE_DATA = [
  {"e":"😅","slug":"grinning-face-with-sweat","name":"Grinning Face with Sweat","aliases":"sweat smile, nervous laugh, awkward smile, relief, phew","meaning":"The <strong>Grinning Face with Sweat</strong> (😅) shows a smiling face with a single bead of sweat on its forehead. It's the universal emoji for <strong>\"phew, that was close\"</strong> — relief after narrowly avoiding disaster. It also expresses nervousness, awkwardness, or being embarrassed but trying to stay positive. You made it through, but barely.<br><br>Use it when you almost forgot a deadline but submitted at 11:59 😅. Or when someone brings up that thing you said three years ago in front of everyone 😅. The sweat drop is the key detail — it distinguishes this from a normal smile (😊) and adds that layer of \"I'm smiling but internally screaming.\"","usage":["\"When the professor says 'I lost your exam' ... just kidding 😅\"","\"Me after explaining the bug and realizing it was a typo 😅\"","\"Almost missed my flight but made it 😅\""],"related":["😅","😰","😬","🤣","🫠"],"cat":"smileys"},
  {"e":"😡","slug":"pouting-face","name":"Pouting Face","aliases":"angry face, pouting, mad, furious, red face anger","meaning":"The <strong>Pouting Face</strong> (😡) is the definitive anger emoji. Its red face, furrowed eyebrows, and downturned mouth communicate pure <strong>rage and fury</strong>. This is not mild annoyance (that's 😒) or frustration (that's 😤) — this is \"I am genuinely angry.\" The red color is intentional, mirroring how human faces actually flush with blood during anger.<br><br>Use it for serious anger: \"They laid off half the team with zero notice 😡\". It's also used for righteous anger about social issues: \"This policy is discrimination, plain and simple 😡\". Because the anger is so unambiguous, be careful using it in personal conflicts — it escalates rather than de-escalates. For milder irritation, consider 😤 or 😒 instead.","usage":["\"When someone takes credit for your work 😡\"","\"This company's customer service is a joke 😡\"","\"Me reading the comments section 😡\""],"related":["😤","🤬","😠","💢","👿"],"cat":"smileys"},
  {"e":"😏","slug":"smirking-face","name":"Smirking Face","aliases":"smirk, smug, flirty, sly, confident smirk","meaning":"The <strong>Smirking Face</strong> (😏) is the emoji equivalent of raising one eyebrow. With its half-smile and sidelong glance, it conveys <strong>smugness, flirtation, inside jokes, or knowing something others don't</strong>. It's the face you make when you're feeling clever, suggestive, or just a little too pleased with yourself.<br><br>In flirty contexts, 😏 is a classic: \"You looked good in that photo 😏\". In competitive contexts, it's pure smugness: \"Told you I'd win 😏\". The emoji walks a fine line between playful and arrogant — tone and relationship matter a lot here. With close friends, it's teasing. With strangers, it can read as creepy. Use with caution.","usage":["\"I know something you don't know 😏\"","\"That text from your ex? Called it 😏\"","\"You're not as subtle as you think 😏\""],"related":["😉","🙃","🤨","😼","💅"],"cat":"smileys"},
  {"e":"🥰","slug":"smiling-face-with-hearts","name":"Smiling Face with Hearts","aliases":"heart face, feeling loved, warm and fuzzy, adored, loving emoji","meaning":"The <strong>Smiling Face with Hearts</strong> (🥰) is the warmest, most affectionate smile in the emoji keyboard. Unlike ❤️ (which is about love in general) or 😍 (which is about attraction), 🥰 is about <strong>feeling loved and appreciated</strong>. The three floating hearts around the smiling face show someone who is basking in affection — not just giving love, but receiving it.<br><br>Use it when someone does something genuinely thoughtful: \"You brought me soup because I'm sick? 🥰\" Or when you're feeling especially grateful: \"This community is the best 🥰\". It's softer and more wholesome than 😍, making it perfect for close friends, family, and supportive communities — not just romantic partners.","usage":["\"When your partner remembers the little things 🥰\"","\"This comment section is so supportive 🥰\"","\"My dog waiting at the door when I come home 🥰\""],"related":["😍","❤️","🥺","💕","😊"],"cat":"smileys"},
  {"e":"🥲","slug":"smiling-face-with-tear","name":"Smiling Face with Tear","aliases":"smiling with tear, bittersweet, happy crying, touched, moved","meaning":"The <strong>Smiling Face with Tear</strong> (🥲) captures a very specific emotion: <strong>happiness through pain</strong>. It shows a gentle smile with a single tear rolling up the cheek — not sobbing (😭), not pleading (🥺), but a quiet, bittersweet joy. Think of it as \"I'm smiling, but I'm also emotional about it.\"<br><br>Use it for proud-but-sad moments: \"My kid's first day of school 🥲\". Or when you're grateful despite difficulty: \"It was a hard year but I made it 🥲\". Or when something is genuinely touching: \"This video of soldiers surprising their families 🥲\". The upward curve of the tear (it goes up, not down) is often interpreted as the tear being swept upward by the smile — emphasizing that the joy outweighs the sadness.","usage":["\"Seeing your baby take their first steps 🥲\"","\"When the series finale is perfect 🥲\"","\"Your last day at a job you loved 🥲\""],"related":["😭","😢","😊","🥺","😌"],"cat":"smileys"},
  {"e":"🙃","slug":"upside-down-face","name":"Upside-Down Face","aliases":"upside down, sarcasm, passive aggressive, silly, ironic","meaning":"The <strong>Upside-Down Face</strong> (🙃) is the unofficial emoji of <strong>passive aggression</strong>. By flipping a normal smile upside down, it communicates \"I'm smiling but everything is actually terrible\" or \"I'm being sarcastic.\" It's the emoji equivalent of saying \"I'm fine\" when you are absolutely not fine.<br><br>Use it to signal sarcasm: \"Thanks for the help 🙃\" (when no help was given). Or to acknowledge absurdity: \"The printer broke again 🙃\". Or to express exasperation with a smile: \"I love working weekends 🙃\". Because the upside-down face reads as deliberately silly rather than hostile, it's a socially acceptable way to express frustration without being directly confrontational. It's the \"laughing through the pain\" emoji.","usage":["\"When you're third in line and the first person has 27 coupons 🙃\"","\"Love it when my code works on the first try 🙃\"","\"Me explaining the same thing for the fourth time 🙃\""],"related":["😅","🫠","😬","😮‍💨","😐"],"cat":"smileys"},
  {"e":"🤌","slug":"pinched-fingers","name":"Pinched Fingers","aliases":"pinched fingers, Italian hand, what do you want, chef's kiss, ma che vuoi","meaning":"The <strong>Pinched Fingers</strong> (🤌) emoji — fingertips together pointing upward — is one of the most culturally specific and widely adopted hand gestures. In Italian culture, it means <strong>\"Ma che vuoi?\" (\"What do you want?\" or \"What are you talking about?\")</strong>. It can express disbelief, frustration, questioning, or emphasis.<br><br>Globally, it's also used as the <strong>\"chef's kiss\"</strong> gesture — the universal sign of perfection. When something is absolutely perfect, you kiss your fingertips and release: \"This pasta 🤌\". The emoji oscillates between these two meanings depending on context. In arguments, it's confrontational: \"What are you even saying right now 🤌\". In appreciation, it's pure approval: \"That sunset 🤌\". Its dual meaning makes it one of the most versatile hand gesture emojis.","usage":["\"This homemade pizza though 🤌\"","\"What do you expect me to do about it 🤌\"","\"The cinematography in that film — chef's kiss 🤌\""],"related":["👌","💅","🙄","👏","🤷"],"cat":"gestures"},
  {"e":"💅","slug":"nail-polish","name":"Nail Polish","aliases":"nail polish, sassy, unbothered, self-care, manicure, boss","meaning":"The <strong>Nail Polish</strong> (💅) emoji shows a hand painting its nails pink. It's become a symbol of <strong>being unbothered, sassy, or treating yourself</strong>. The gesture invokes the image of someone casually examining their freshly done nails while ignoring drama — the ultimate \"I don't care\" pose.<br><br>On social media, 💅 often accompanies a confident statement: \"They're still talking about me and I'm still not listening 💅\". It's about <strong>self-care as a power move</strong> — taking time for yourself while the world burns around you. In queer culture, it's a staple of sassy, confident expression. It can also be literal: \"Getting my nails done 💅\" — but the figurative use is far more common in digital communication.","usage":["\"Your opinion of me is none of my business 💅\"","\"Booked a spa day because I deserve it 💅\"","\"They thought I'd be bothered. I'm not 💅\""],"related":["😏","✨","👑","💁","🤌"],"cat":"gestures"},
  {"e":"🫶","slug":"heart-hands","name":"Heart Hands","aliases":"heart hands, love you, support, hearts, finger heart","meaning":"The <strong>Heart Hands</strong> (🫶) emoji shows two hands forming a heart shape. Introduced in 2022, it quickly became one of the most popular new emojis — especially among Gen Z. It's used to express <strong>love, gratitude, support, and solidarity</strong> in a way that feels more personal and human than a standard heart emoji.<br><br>The gesture originated from the Korean \"finger heart\" and was popularized globally by K-pop idols and their fans. Unlike ❤️ (abstract heart) or 🫀 (anatomical heart), 🫶 feels <strong>active</strong> — you're making the heart, you're sending it. Use it to show support: \"You've got this 🫶\". Or love: \"Best friends forever 🫶\". Or gratitude: \"Thank you all for the kind words 🫶\". It works in both romantic and platonic contexts.","usage":["\"Sending love to everyone who needs it today 🫶\"","\"So grateful for this community 🫶\"","\"Date night vibes 🫶\""],"related":["❤️","💕","🤟","🙌","💖"],"cat":"gestures"},
  {"e":"😮‍💨","slug":"face-exhaling","name":"Face Exhaling","aliases":"exhaling face, sigh of relief, phew, exhausted, relief","meaning":"The <strong>Face Exhaling</strong> (😮‍💨) shows a face blowing out a visible breath. It's the <strong>universal sigh emoji</strong> — expressing relief, exhaustion, or the release of tension. After a stressful situation resolves, after a long day, or after holding your breath (literally or figuratively): this is the exhale.<br><br>Use it after finishing something difficult: \"Finally submitted that report 😮‍💨\". Or after a close call: \"That was way too close 😮‍💨\". Or simply when you're tired: \"Longest week ever 😮‍💨\". Unlike 😅 (sweat smile), which is about nervous relief, 😮‍💨 feels more like a genuine release of pressure — less smiling, more breathing. It's also used as a reaction to disappointing news: \"They canceled the show 😮‍💨\".","usage":["\"When your flight is delayed for the third time 😮‍💨\"","\"That conversation was exhausting 😮‍💨\"","\"Finally home after a 12-hour shift 😮‍💨\""],"related":["😅","😰","🫠","😌","😤"],"cat":"smileys"},
  {"e":"😶‍🌫️","slug":"face-in-clouds","name":"Face in Clouds","aliases":"face in clouds, foggy brain, confused, spaced out, brain fog","meaning":"The <strong>Face in Clouds</strong> (😶‍🌫️) is one of the more abstract but relatable new emojis. It shows a face partially obscured by clouds or fog — representing <strong>confusion, brain fog, being spaced out, or not quite understanding what's going on</strong>. The face itself is expressionless (the mouthless 😶), emphasizing the blankness.<br><br>Use it when you're mentally checked out: \"Me in my 3pm meeting 😶‍🌫️\". Or when you genuinely don't understand something: \"Can someone explain this math to me 😶‍🌫️\". Or when you're dissociating: \"Looking at my bank account after the weekend 😶‍🌫️\". It's become particularly associated with the experience of \"brain fog\" — that feeling of not being able to think clearly — making it relatable across mental health, chronic illness, and just being really tired.","usage":["\"My brain after 4 hours of Zoom calls 😶‍🌫️\"","\"When someone explains something three times and you still don't get it 😶‍🌫️\"","\"Monday mornings be like 😶‍🌫️\""],"related":["😵‍💫","🫠","😮‍💨","😐","🫥"],"cat":"smileys"},
  {"e":"🗿","slug":"moai-statue","name":"Moai","aliases":"moai, Easter Island statue, stone face, deadpan,🗿meme","meaning":"The <strong>Moai</strong> (🗿) emoji depicts one of the famous stone statues from Easter Island. In emoji culture, it's been adopted as the ultimate <strong>deadpan reaction</strong>. The stone face with its chiseled, expressionless features perfectly communicates \"I have no reaction to this\" or \"that was so unfunny I've turned to stone.\"<br><br>🗿 gained meme status in 2022 as a reaction to terrible jokes. Use it when someone tells a joke so bad that you don't just not laugh — you become an ancient megalith: \"That was the worst pun I've ever heard 🗿\". It can also mean stoicism or being unmoved: \"They tried to get a reaction out of me 🗿\". Unlike 😐 (neutral face), which suggests mild disappointment, 🗿 implies a <strong>monumental level of unimpressed</strong>.","usage":["\"When your dad tells his favorite joke for the 50th time 🗿\"","\"That's crazy. Anyway. 🗿\"","\"Me after hearing the worst take on Twitter 🗿\""],"related":["😐","💀","🤖","🪨","🙄"],"cat":"smileys"},
  {"e":"🧋","slug":"bubble-tea","name":"Bubble Tea","aliases":"bubble tea, boba, milk tea, tapioca, boba tea","meaning":"The <strong>Bubble Tea</strong> (🧋) emoji depicts a cup of bubble tea (also called boba or boba tea) — the Taiwanese drink with tapioca pearls at the bottom. Introduced in 2021, it's become a symbol of <strong>treating yourself, hanging out with friends, and Asian cultural pride</strong>. Getting boba is often a social ritual: \"Boba run after class? 🧋\"<br><br>Beyond the literal drink, 🧋 can mean any self-care moment: \"Staying in with a good book and boba 🧋\". In Asian-American communities, it's a cultural identity marker — a small way of saying \"I see you\" to others who share the boba ritual. The emoji is also used in the broader context of AAPI representation, as bubble tea originated in Taiwan and spread globally through Asian diaspora communities.","usage":["\"Afternoon boba break anyone? 🧋\"","\"Self-care Sunday: book, bath, boba 🧋\"","\"First date idea: walk around and get boba 🧋\""],"related":["☕","🍵","🧁","🍜","✨"],"cat":"food"},
  {"e":"✨","slug":"sparkles","name":"Sparkles","aliases":"sparkles, magic, shiny, new, glitter, special, aesthetic","meaning":"The <strong>Sparkles</strong> (✨) emoji shows three golden stars radiating light. It's one of the most versatile and widely used decorative emojis. ✨ can mean <strong>something is new, special, magical, clean, or exciting</strong>. It's often used for emphasis around words to make them stand out: \"New post ✨\" or \"Fresh start ✨\".<br><br>In 2024-2026, ✨ has become the default <strong>\"aesthetic emphasis\" marker</strong> on social media, especially in Instagram bios, Twitter display names, and TikTok captions. It adds a touch of sparkle to any statement, making it feel more positive and intentional. It's also used in the context of manifestation and self-improvement: \"Manifesting good vibes only ✨\". Unlike the physical sparkle of a diamond 💎, ✨ is about intangible magic and positivity.","usage":["\"New chapter ✨\"","\"Just cleaned my entire apartment ✨\"","\"This outfit is giving ✨\""],"related":["💫","🌟","⭐","💖","🎀"],"cat":"symbols"},
  {"e":"🔥","slug":"fire","name":"Fire","aliases":"fire, lit, hot, trending, amazing, flame","meaning":"The <strong>Fire</strong> (🔥) emoji is one of the most versatile symbols in the emoji keyboard. In slang, 🔥 means amazing, trending, on fire, or lit. It is the go-to emoji for expressing that something is exceptional.<br><br>This song is straight fire 🔥 means the song is amazing. In social media, 🔥 is often used as a rating — the emoji equivalent of a five-star review. Unlike 👍 (thumbs up), 🔥 conveys intensity and excitement, not just approval. Something that is 🔥 is not just good — it is hot.","usage":["This album is absolute fire","Your presentation was 🔥 today","The comeback nobody expected"],"related":["💯","👍","⚡","🌟","💪"],"cat":"symbols"},
  {"e":"🤣","slug":"rolling-on-floor-laughing","name":"Rolling on the Floor Laughing","aliases":"ROFL, rolling on floor laughing, laughing hard, hilarious","meaning":"The <strong>Rolling on the Floor Laughing</strong> (🤣) emoji shows a face tilted sideways, laughing uncontrollably with tears. It is one step beyond 😂 — you are not just crying-laughing, you are <strong>literally rolling on the ground</strong>. The tilted angle makes it distinct: the laughter is so intense you have lost physical control.<br><br>Use 🤣 when 😂 does not feel strong enough. It is the emoji for when something is so funny you cannot type properly. Some Gen Z users prefer 💀 (skull) for extreme laughter — 🤣 can feel slightly millennial in certain contexts.","usage":["This stand-up special had me dying","When your friend retells the most embarrassing story","The autocorrect fail screenshot sent me"],"related":["😂","💀","😹","😭","😆"],"cat":"smileys"},

  {"e":"🙏","slug":"folded-hands","name":"Folded Hands","aliases":"folded hands, pray, please, thank you, high five, namaste","meaning":"The <strong>Folded Hands</strong> (🙏) emoji is one of the most debated emojis. Two hands pressed together. In Japan, it means please or thank you. In Western countries, it is widely used as prayer or hope. In some communities, it is interpreted as a high five.<br><br>Use it to express gratitude, hope, or a respectful greeting. Context usually makes the meaning clear. It is also commonly used in sports contexts as a high five celebration and in spiritual contexts as a sign of prayer or meditation.","usage":["Praying for good news","Thank you for all the support","Please let me pass this exam"],"related":["🤲","🧎","✨","🛐","🤝"],"cat":"gestures"},

  {"e":"👀","slug":"eyes","name":"Eyes","aliases":"eyes, looking, watching, side eye, staring","meaning":"The <strong>Eyes</strong> (👀) emoji shows a pair of wide-open eyes looking to the left. It is universally used to mean <strong>I see this, look at this, or this is interesting.</strong> It is the digital equivalent of leaning in and paying attention.<br><br>It is the go-to reaction when someone drops surprising information in a group chat. It is also the standard emoji for gossip, drama, or anything eyebrow-raising. On social media, brands use it to tease upcoming announcements. The eyes work because they are ambiguous — they could mean curiosity, attraction, suspicion, or just that something caught your attention.","usage":["Did you see the drama in the group chat","New job announcement coming next week","That is an interesting choice"],"related":["😳","🤔","🧐","😏","🫣"],"cat":"smileys"},

  {"e":"💯","slug":"hundred-points","name":"Hundred Points","aliases":"100, hundred points, perfect, keep it 100, a plus","meaning":"The <strong>Hundred Points</strong> (💯) emoji shows the number 100 underlined, as if written on a perfect test. It means <strong>completely agree, absolutely correct, or perfect.</strong> It is the strongest endorsement you can give in emoji form.<br><br>Originally from the phrase keep it 100 (keep it real, be authentic), 💯 has expanded to mean any form of full agreement or validation. In Black Twitter culture, it is a classic affirmation emoji. Unlike 👍 (okay) or 🔥 (impressive), 💯 means I could not agree more.","usage":["This take is correct","Keep it real always","Best pizza in the city no competition"],"related":["🔥","👍","✅","💪","🙌"],"cat":"symbols"},

  {"e":"❤️","slug":"red-heart","name":"Red Heart","aliases":"red heart, love, like, favorite, heart emoji, classic heart","meaning":"The <strong>Red Heart</strong> (❤️) is the most used emoji symbol in the world. It conveys <strong>love, affection, care, and deep emotional connection.</strong> It works in romantic, platonic, familial, and even casual contexts.<br><br>Unlike newer heart color variants, ❤️ remains the gold standard. It is the most serious heart — when someone switches from colored hearts to ❤️, it often signals deepening feelings. On Instagram and TikTok, it is the universal like reaction. The red heart has been an emoji since the earliest days of Unicode, making it one of the most trusted symbols in digital communication.","usage":["Thinking of you","This song has my whole heart","Goodnight love you"],"related":["💕","💗","💖","😍","🥰"],"cat":"symbols"},

  {"e":"🤡","slug":"clown-face","name":"Clown Face","aliases":"clown, ridiculous, foolish, embarrassing, clowning","meaning":"The <strong>Clown Face</strong> (🤡) emoji is one of the most brutal insults in the emoji keyboard. It is used to call someone <strong>ridiculous, foolish, or a joke.</strong> If someone replies to your take with 🤡, they are not laughing with you — they are laughing at you.<br><br>On Twitter and TikTok, 🤡 is the standard reaction to bad takes, hypocrisy, and embarrassing behavior. It is also used self-deprecatingly. Use it carefully — it can be playful among friends but genuinely insulting in public conversations.","usage":["This aged poorly","Me after that terrible life decision","The whole situation is a circus"],"related":["🙃","😬","🗿","💀","🎪"],"cat":"smileys"},

  {"e":"🥵","slug":"hot-face","name":"Hot Face","aliases":"hot face, overheated, sweating, attractive, spicy","meaning":"The <strong>Hot Face</strong> (🥵) emoji shows a red-faced, sweating emoji with its tongue hanging out — the universal sign of being <strong>extremely hot or overheated.</strong> But its meaning has expanded to also mean someone or something is <strong>attractive or hot.</strong><br><br>Literal: It is 100 degrees and no AC. Figurative: That person is incredibly attractive. In fitness communities, it is the post-workout emoji. It can also mean spicy food. The dual meaning makes it a versatile addition to any message.","usage":["Summer in Texas be like","That new profile picture","This curry is no joke"],"related":["🥶","😰","😅","🔥","🫠"],"cat":"smileys"},

  {"e":"🥶","slug":"cold-face","name":"Cold Face","aliases":"cold face, freezing, blue, icy, freezing cold, left on read","meaning":"The <strong>Cold Face</strong> (🥶) emoji shows a blue, shivering face with icicles hanging from its jaw. It represents <strong>extreme cold, being frozen, or metaphorically being ignored (the cold shoulder).</strong><br><br>Literal: Waiting for the bus in January. Figurative: He left me on read. In sports, 🥶 also means someone is ice cold in a positive way — calm under pressure, clutch. The icicles are the key visual that distinguish this from simply being unhappy.","usage":["Canadian winter mornings","She did not even say hi","That penalty kick under pressure was ice cold"],"related":["🥵","😰","🧊","❄️","😬"],"cat":"smileys"},

  {"e":"🫣","slug":"face-with-peeking-eye","name":"Face with Peeking Eye","aliases":"peeking, hiding, watching through fingers, cannot look, scared","meaning":"The <strong>Face with Peeking Eye</strong> (🫣) shows hands covering a face — except one eye is peeking through between the fingers. It captures the universal gesture of <strong>watching something through your fingers because you are scared, embarrassed, or cannot look away.</strong><br><br>Use it when watching a horror movie, experiencing secondhand embarrassment, or when you are curious about something you probably should not be looking at. Introduced in 2022, it quickly became a favorite for capturing a very specific and relatable human gesture.","usage":["Watching the scary movie like","Me reading the group chat drama","When the presentation is going really badly"],"related":["🙈","😳","😬","🤭","🫢"],"cat":"smileys"},

  {"e":"🫢","slug":"face-with-hand-over-mouth","name":"Face with Open Eyes and Hand Over Mouth","aliases":"gasp, shocked, surprised, hand over mouth, oops","meaning":"The <strong>Face with Hand Over Mouth</strong> (🫢) shows a face with wide eyes and a hand covering the mouth — the classic I cannot believe I just said that expression. It conveys <strong>shock, surprise, or the moment you realize you have made a mistake.</strong><br><br>Unlike 😱 (scream), which is about fear, 🫢 is about social surprise — saying something you should not have, hearing unexpected gossip, or witnessing an awkward moment. The combination of wide eyes plus covered mouth makes it feel more nuanced than simpler shock emojis.","usage":["When you accidentally hit reply all","Did he really just say that","The plot twist in episode 6 had me"],"related":["😱","😮","🤭","🫣","😳"],"cat":"smileys"}
,
  {"e":"🥳","slug":"partying-face","name":"Partying Face","aliases":"party, celebration, birthday, hat, horn, lets go","meaning":"The <strong>Partying Face</strong> (🥳) emoji shows a smiling face with a party hat and horn. It is the universal emoji for <strong>celebration, birthdays, and good times.</strong> Use it for congratulations, milestones achieved, or just a Friday night. It can also be ironic when something is underwhelming. The party hat makes it unmistakably festive.","usage":["Happy birthday","Weekend starts now","Got the promotion"],"related":["🎉","🎂","🎊","🥂","🎈"],"cat":"smileys"},

  {"e":"🎉","slug":"party-popper","name":"Party Popper","aliases":"party, celebration, confetti, congratulations, tada","meaning":"The <strong>Party Popper</strong> (🎉) emoji shows a party popper bursting with confetti. It represents <strong>celebration, congratulations, and exciting announcements.</strong> Use it for major life announcements, professional wins, or general good news. The confetti pattern makes it instantly recognizable as a celebration marker.","usage":["We did it","New job starts Monday","Happy New Year"],"related":["🥳","🎊","🥂","🎂","✨"],"cat":"smileys"},

  {"e":"💔","slug":"broken-heart","name":"Broken Heart","aliases":"broken heart, heartbreak, sad, lost love, emotional pain","meaning":"The <strong>Broken Heart</strong> (💔) emoji shows a red heart split in two. It represents <strong>heartbreak, emotional pain, loss, and grief.</strong> Unlike ❤️ which is about love and connection, 💔 is explicitly about love that has been damaged or lost. Use it for romantic heartbreak, general sadness, or empathy. The visual of the cracked heart makes the pain feel tangible.","usage":["Going through a rough breakup","This news is devastating","Saying goodbye to my childhood home"],"related":["❤️","😢","😭","💕","🥺"],"cat":"symbols"},

  {"e":"🤓","slug":"nerd-face","name":"Nerd Face","aliases":"nerd, geek, smart, studious, glasses, dork","meaning":"The <strong>Nerd Face</strong> (🤓) emoji shows a smiling face with thick black glasses. It represents <strong>intelligence, enthusiasm for niche interests, or being socially awkward in an endearing way.</strong> Once an insult, nerd has been reclaimed as a badge of honor. Use it to show genuine enthusiasm for academic topics or to be self-deprecating about being overly excited about something.","usage":["Actually according to my calculations","Me at trivia night","Just finished a 500 page book in one sitting"],"related":["🧐","🤔","📚","💻","🧠"],"cat":"smileys"},

  {"e":"🤧","slug":"sneezing-face","name":"Sneezing Face","aliases":"sneeze, sick, allergies, cold, tissue, bless you","meaning":"The <strong>Sneezing Face</strong> (🤧) emoji shows a face mid-sneeze with a tissue. It represents <strong>sickness, allergies, or the common cold.</strong> But it has also been adopted for ugly crying — the kind of crying that leaves you reaching for tissues. In anime and K-drama communities, it is the standard reaction to emotionally devastating scenes.","usage":["Pollen count is off the charts today","When the K-drama episode ends on a cliffhanger","Sick in bed all weekend"],"related":["😭","😢","😷","🤒","🥲"],"cat":"smileys"},

  {"e":"😤","slug":"face-with-steam-from-nose","name":"Face with Steam From Nose","aliases":"frustrated, angry, steam, triumph, determination, fed up","meaning":"The <strong>Face with Steam From Nose</strong> (😤) shows a scowling face with steam blowing from its nostrils — like an angry cartoon bull. It represents <strong>frustration, determination, or feeling fed up.</strong> The steam implies the anger is building up, about to boil over. Use it for minor but persistent annoyances or for showing competitive determination.","usage":["Fourth time restarting the computer today","When your team is losing with 2 minutes left","I will finish this project tonight no matter what"],"related":["😡","😠","💢","🤬","😮‍💨"],"cat":"smileys"},

  {"e":"🥹","slug":"face-holding-back-tears","name":"Face Holding Back Tears","aliases":"holding back tears, touched, moved, emotional, about to cry, grateful","meaning":"The <strong>Face Holding Back Tears</strong> (🥹) shows a face trying not to cry, with wide glossy eyes. It is the emoji for being <strong>profoundly moved, deeply grateful, or emotionally overwhelmed in a positive way.</strong> This is NOT a sad emoji — it is about being touched by kindness, a beautiful moment, or gratitude. Introduced in 2022, it quickly became a favorite for wholesome, heartfelt moments.","usage":["When your friend throws you a surprise party","This comment made my whole week","My parents reaction to the good news"],"related":["🥲","😭","😢","🥺","😊"],"cat":"smileys"},

  {"e":"😳","slug":"flushed-face","name":"Flushed Face","aliases":"flushed, embarrassed, blushing, shocked, wide eyes, caught off guard","meaning":"The <strong>Flushed Face</strong> (😳) shows a face with wide eyes and red cheeks — the universal I am embarrassed or I was not expecting that expression. It conveys <strong>surprise, embarrassment, or being caught off guard.</strong> The flushed cheeks are key — they show the physical reaction of blushing. In flirty contexts, it signals you are pleasantly flustered.","usage":["When your crush compliments you","Wait what did you just say","Me realizing the meeting was yesterday not today"],"related":["😊","😏","🫣","😅","😬"],"cat":"smileys"},

  {"e":"😬","slug":"grimacing-face","name":"Grimacing Face","aliases":"grimacing, awkward, cringe, yikes, nervous smile, teeth","meaning":"The <strong>Grimacing Face</strong> (😬) shows a face with clenched teeth in an awkward grimace. It is the <strong>yikes emoji</strong> — the face you make when something is awkward, uncomfortable, or you are in a tough spot but trying to smile through it. Use it for secondhand embarrassment or acknowledging an uncomfortable truth. The clenched teeth make the forced smile unmistakable.","usage":["When the professor says check your own work","That joke did not land at all","Me reading old Facebook posts from 2012"],"related":["😅","🫠","😰","🙃","😮‍💨"],"cat":"smileys"},

  {"e":"💖","slug":"sparkling-heart","name":"Sparkling Heart","aliases":"sparkling heart, excited love, grateful, touched, new love","meaning":"The <strong>Sparkling Heart</strong> (💖) shows a pink heart surrounded by sparkles. It is more excited and grateful than ❤️ — adding sparkle suggests the love is <strong>fresh, exciting, or deeply appreciated.</strong> Use it when someone does something unexpectedly thoughtful. It is less serious than ❤️ and more energetic than 💕. In fandom communities, it is the standard heart for love of a favorite character.","usage":["You are the sweetest person ever","This made my whole day sparkle","Look at this adorable puppy video"],"related":["❤️","💕","💗","✨","🥰"],"cat":"symbols"},

  {"e":"🎯","slug":"direct-hit","name":"Direct Hit","aliases":"bullseye, spot on, exactly right, target, nailed it, on point","meaning":"The <strong>Direct Hit</strong> (🎯) emoji shows a dart hitting the exact center of a target. It means <strong>exactly right, spot on, or you nailed it.</strong> Use it when agreeing strongly with an opinion, when someone accurately describes you, or for achieving goals. It is a stronger endorsement than 👍 — 🎯 means you could not have said it better.","usage":["This take is spot on","When the description is too accurate","Right on target for our monthly goal"],"related":["💯","👍","✅","🔥","👌"],"cat":"activities"},

  {"e":"🚩","slug":"triangular-flag","name":"Triangular Flag","aliases":"red flag, warning, alert, danger, red flag emoji","meaning":"The <strong>Triangular Flag</strong> (🚩) emoji shows a red flag on a pole. It has become the internet standard for signaling <strong>warning signs, dealbreakers, or toxic behavior</strong> — especially in dating and relationships. When someone describes concerning behavior and you reply with 🚩, you are saying that is a red flag. Beyond relationships, any warning sign can be flagged.","usage":["He still talks to his ex every day","The apartment listing says cozy which means tiny","Job interview asked if I work weekends for free"],"related":["⛳","⚠️","❗","❌","💀"],"cat":"symbols"},

  {"e":"🌈","slug":"rainbow","name":"Rainbow","aliases":"rainbow, pride, LGBTQ, hope, colorful, after the storm, weather","meaning":"The <strong>Rainbow</strong> (🌈) emoji shows a colorful rainbow arc. It carries multiple layers: <strong>LGBTQ+ pride, hope after hardship, weather, and general positivity.</strong> As a pride symbol, it represents the LGBTQ+ community. As a metaphor, it means hope — after every storm comes a rainbow. It is one of the most culturally significant emojis in the keyboard.","usage":["Happy Pride Month","Things will get better","The most beautiful sunset with a double rainbow"],"related":["🏳️‍🌈","☀️","🌦️","✨","💖"],"cat":"animals"},

  {"e":"🎂","slug":"birthday-cake","name":"Birthday Cake","aliases":"birthday cake, happy birthday, celebration, cake, birthday","meaning":"The <strong>Birthday Cake</strong> (🎂) emoji shows a decorated cake with lit candles. It is the universal symbol for <strong>birthdays and celebrations.</strong> Sending 🎂 is the quickest way to say happy birthday. Use it for literal birthdays, anniversaries, or milestones. Paired with 🥳 and 🎉, it forms the standard birthday message trio. The candles imply something worth celebrating.","usage":["Happy birthday hope you have the best day","Celebrating one year at my dream job","Homemade chocolate cake for the win"],"related":["🥳","🎉","🎁","🧁","🎈"],"cat":"food"},

  {"e":"💪","slug":"flexed-biceps","name":"Flexed Biceps","aliases":"flexed biceps, strong, muscle, power, strength, gym, workout","meaning":"The <strong>Flexed Biceps</strong> (💪) emoji shows a muscular arm flexing. It represents <strong>strength, power, hard work, and determination.</strong> Use it for workout motivation, encouraging someone, or acknowledging hard work. Beyond fitness, it is used for any show of resilience or power. It is one of the most versatile positive-affirmation emojis.","usage":["Gym session complete you got this","Nailed the presentation today","Working through challenges one day at a time"],"related":["👍","🔥","💯","🏋️","👏"],"cat":"gestures"},

  {"e":"🧊","slug":"ice","name":"Ice Cube","aliases":"ice, cold, cool, chill, frozen, ice cube","meaning":"The <strong>Ice Cube</strong> (🧊) emoji shows a translucent blue ice cube. At face value it is literal ice — for drinks or injuries. But it has also been adopted as a symbol for <strong>being cool, unbothered, or emotionally cold.</strong> In jewelry contexts, it can mean diamonds (ice). The versatility comes from its simplicity — temperature, attitude, or wealth depending on context.","usage":["Iced coffee season is here","She gave him the cold shoulder","Staying cool under all this pressure"],"related":["🥶","❄️","💎","🥵","✨"],"cat":"food"},

  {"e":"🎭","slug":"performing-arts","name":"Performing Arts","aliases":"theatre, drama, acting, performance, masks, comedy and tragedy","meaning":"The <strong>Performing Arts</strong> (🎭) emoji shows the classic comedy and tragedy masks. It represents <strong>theatre, drama, acting, and storytelling.</strong> But in everyday communication, it has a more pointed meaning: being dramatic or two-faced. The duality of the two masks speaks to performing different emotions for different audiences — authenticity versus acting.","usage":["Opening night was incredible","Stop being so dramatic about everything","Pretending to be nice when you are not"],"related":["🤡","🎪","🎬","😏","🙄"],"cat":"activities"},

  {"e":"🫂","slug":"people-hugging","name":"People Hugging","aliases":"hug, embrace, comfort, support, hugging, holding each other","meaning":"The <strong>People Hugging</strong> (🫂) emoji shows two figures embracing. Introduced in 2022, it filled a long-standing gap — a way to say <strong>I am giving you a hug or I am here for you.</strong> It represents comfort, support, and physical affection. Unlike 🤗 (hugging face), which shows one person offering a hug, 🫂 shows mutual embrace. The blue silhouettes make it gender-neutral.","usage":["Sending love to everyone going through it right now","Reunited with my family after so long","You are not alone in this"],"related":["🤗","❤️","🥺","💕","🙏"],"cat":"gestures"},

  {"e":"🧘","slug":"person-in-lotus-position","name":"Person in Lotus Position","aliases":"yoga, meditation, zen, calm, mindfulness, inner peace","meaning":"The <strong>Person in Lotus Position</strong> (🧘) emoji shows a person sitting cross-legged in meditation. It represents <strong>yoga, meditation, mindfulness, and inner peace.</strong> Use it literally about yoga or figuratively about staying centered in chaos. In wellness communities, it is a standard marker for self-care and mental health.","usage":["Starting the day with 20 minutes of meditation","Staying zen while the world burns around me","Not engaging with the drama today"],"related":["😌","🕉️","🧎","😮‍💨","✨"],"cat":"gestures"}

]

# Extend DATA and regenerate
DATA.extend(MORE_DATA)
print(f'Total emoji data: {len(DATA)}')

# Regenerate all
for d in DATA:
  html = gen_page(d)
  path = os.path.join(OUT_DIR, f'{d["slug"]}.html')
  with open(path, 'w') as f:
    f.write(html)
  print(f'Updated: {d["slug"]}.html')

# Update index
index_html = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Emoji Meanings — Complete Dictionary | Emoji101</title>\n<meta name="description" content="Complete emoji dictionary. Find meanings for every emoji. Skull, pleading face, melting face, fire, sparkles and more. Free emoji guide.">\n<script async src="https://www.googletagmanager.com/gtag/js?id=G-MJ9EFVJYNZ"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag(\'js\',new Date());gtag(\'config\',\'G-MJ9EFVJYNZ\');</script>\n<style>\n:root{--primary:#FF6B35;--primary-light:#FFF0E8;--bg:#F8F9FA;--card:#fff;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:12px;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}\n*{box-sizing:border-box;margin:0;padding:0}\nbody{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.7}\n.container{max-width:680px;margin:0 auto;padding:20px 16px}\n.header{text-align:center;padding:40px 0 24px}\n.header h1{font-size:28px;font-weight:800;margin-bottom:6px}\n.header p{color:var(--text-secondary);font-size:15px}\n.nav-back{display:inline-block;margin-bottom:20px;font-size:14px;color:var(--primary);text-decoration:none}\n.emoji-list{display:flex;flex-direction:column;gap:8px}\n.emoji-row{display:flex;align-items:center;gap:14px;padding:14px 18px;background:var(--card);border-radius:var(--radius);text-decoration:none;color:var(--text);border:1px solid var(--border);transition:all .15s}\n.emoji-row:hover{border-color:var(--primary);transform:translateX(4px)}\n.emoji-row .e{font-size:36px;flex-shrink:0}\n.emoji-row .info{flex:1}\n.emoji-row .info .n{font-weight:600;font-size:15px}\n.emoji-row .info .a{font-size:13px;color:var(--text-secondary);margin-top:2px}\n.emoji-row .arrow{color:var(--primary);font-size:18px}\n.footer{text-align:center;padding:32px 16px;color:#94A3B8;font-size:13px}\n.footer a{color:var(--primary);text-decoration:none}\n</style>\n</head>\n<body>\n<div class="container">\n<a href="/" class="nav-back">← Back to Emoji101</a>\n<div class="header">\n  <h1>Emoji Meanings Dictionary</h1>\n  <p>Click any emoji for its full meaning, usage examples, and related emojis.</p>\n</div>\n<div class="emoji-list">\n'
for d in DATA:
  index_html += f'  <a href="{d["slug"]}.html" class="emoji-row"><span class="e">{d["e"]}</span><span class="info"><span class="n">{d["name"]}</span><br><span class="a">{d["aliases"][:60]}...</span></span><span class="arrow">→</span></a>\n'
index_html += '</div>\n</div>\n<footer class="footer"><p><a href="/">emoji101.com</a></p></footer>\n</body>\n</html>'

with open(os.path.join(OUT_DIR, 'index.html'), 'w') as f:
  f.write(index_html)
print('Updated: index.html (meanings directory)')
print(f'Total pages generated: {len(DATA)}')
