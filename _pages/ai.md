---
layout: page
title: AI čili Umělá Inteligence
permalink: /ai/
---

Zde najdete články zaměřené na umělou inteligenci a její využití v různých oblastech. Moji knihu [Mýty a naděje digitálního světa](https://www.kosmas.cz/knihy/517526/myty-a-nadeje-digitalniho-sveta/) můžete využít jako skvělého průvodce moderními technologiemi, pokud si chcete počíst vše vcelku. 


<h2>💎 Osvědčené postupy a návody na práci s AI</h2>
🎓 [AI pro rodiče školáků](https://www.pii.cz/clanky/ai-pro-rodice-skolaku/) - návody a postupy pro vzdělávání s dětmi \
📕 [Využití AI pro psaní beletrie, knih](/item/ai-psani-povidek/) \
👾 [Programování s pomocí AI](/item/jak-programovat-s-ai/) \
🗞️ [Jak pomocí umělé inteligence nastudovat téma a napsat lepší článek do novin](/item/jak-psat-clanky-s-pomoci-umele-inteligence-ai/) \
🤖 [Zápis z porady či jednání pomocí umělé inteligence](/item/zapisy_z_porad_pomoci_ai/) \
🎧 [Jak vytvořit audio podcast z vašich textů automaticky pomocí AI](/item/podcasty-z-textu-automaticky/) \
🔎 [Hluboký výzkum tématu s vygenerovanou zprávou pomocí Google Gemini Deep Research](/item/Google-Gemini-Deep-Research/)



<h2>🧭 Základy fungování AI</h2>

{% assign emoji_chars = "⌚️⌨️📱📲💻⌨️🖥️🖨️🖱️🖲️🕹️🗜️💽💾💿📀📼📷📸📹🎥📽️" | split: '' %}
{% assign sorted_posts = site.ai | where_exp: "post", "post.order" | sort: "order" %}

<ul>
{% for post in sorted_posts %}
  {% assign random_index = forloop.index | plus: post.title.size | modulo: emoji_chars.size %}
  {% assign random_emoji = emoji_chars[random_index] %}
  <li>{{ random_emoji }} <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>


<h2>💡 Rady, tipy a triky</h2>
{% assign unsorted_posts = site.ai | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
{% for post in unsorted_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

<h2>✍️ Příručky správného promptování</h2>
V poslední době vyšlo několik dobrých materiálů k tomu, jak sestavit dobrý prompt pro AI:
- Google vydal pro své [Gemini Prompting Guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf) - 68 stran pro jeho modely
- Anthropic vydal [Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- Ten má i verzi [Interaktivního tutoriálu na Githubu](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial/Anthropic%201P)
- nebo [na Google Sheets](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?gid=150872633#gid=150872633)
- A ještě [Best reasoning practices](https://platform.openai.com/docs/guides/reasoning-best-practices) od OpenAI - 
- A od OpenAI [GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)

Jen faktická poznámka: tohle jsou příručky hlavně pro promptování přes API, kde musíte řešit spoustu věcí od začátku a prompty bývají o řád složitější. Web/aplikace spoustu kontextu řeší za vás, 

<h2>Články a aktuality z oblasti Umělé inteligence</h2>

{% assign ai_posts = site.posts | where: "categories", "AI" %}
{% assign ui_posts = site.posts | where: "categories", "Umělá inteligence" %}
{% assign combined_posts = ai_posts | concat: ui_posts | uniq | sort: "date" | reverse %}


{% for post in combined_posts %}
<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  
<div class="post-content clearfix">
{% if post.thumbnail %}
{% assign thumbnail_url = post.thumbnail | replace: 'http://', 'https://' %}
<div class="thumbnail">
<a href="{{ site.baseurl }}{{ post.url }}">
 <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ thumbnail_url }}" alt="{{ post.title }}">
</a>
</div>
{% endif %}
</div>

<div class="excerpt">
{{ post.excerpt | strip_html | truncatewords: 60 }} - {{ post.date | date: "%d. %m. %Y" }}
</div>
{% endfor %}

## O této rubrice

Tato rubrika se zaměřuje na nejnovější trendy a vývoj v oblasti umělé inteligence. Diskutujeme zde o různých aspektech AI, od strojového učení až po etické otázky spojené s využíváním AI v každodenním životě.
