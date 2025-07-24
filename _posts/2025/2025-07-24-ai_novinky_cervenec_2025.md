---
author: Patrick Zandl
categories:
- AI
- OpenAI
- Anthropic
- Mistral
- Google
- Amazon
- xAI
- Runway
- Decart
layout: post
post_excerpt: Překotné uvádění novinek v oblasti AI a návazných oblastech, jako je robotika, pokračuje.  OpenAI sjednotil své nástroje do ChatGPT Agent, Mistral AI vydal první open-source model pro porozumění řeči a Decart ukázal slušný průlom v real-time video zpracování. Pojďme se podívat na novinky poslední doby. 
summary_points:
- OpenAI představil ChatGPT Agent spojující nástroje Operator a Deep Research do jednotného systému
- Mistral AI vydal Voxtral, první open-source model pro porozumění řeči s podporou 40 minut zvuku
- Runway ukázal Act-Two pro pokročilý motion capture celého těla z jediného videa
- Anthropic rozšířil Claude o adresář nástrojů pro jednoduché propojení s aplikacemi jako Notion a Canva
- Google rozšířil AI Mode o Deep Search a AI telefonování do obchodů
- Decart představil MirageLSD, první model pro real-time transformaci video streamů
title: "Novinky AI v červenci 2025 - ChatGPT Agent, Voxtral a real-time video modely mění herní pravidla"
---

Překotné uvádění novinek v oblasti AI a návazných oblastech, jako je robotika, pokračuje.  OpenAI sjednotil své nástroje do ChatGPT Agent, Mistral AI vydal první open-source model pro porozumění řeči a Decart ukázal slušný průlom v real-time video zpracování. Pojďme se podívat na novinky poslední doby. 

## OpenAI představil ChatGPT Agent jako jednotný agentní systém

OpenAI 17. července představil [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/), systém který spojuje možnosti nástroje Operator pro ovládání webových stránek, funkce Deep Research pro syntézu informací a konverzační schopnosti ChatGPT do jednotného agentního systému. ChatGPT Agent dokáže autonomně navigovat webové stránky, filtrovat výsledky, požádat uživatele o přihlášení k službám při potřebě, spouštět kód a vytvářet editovatelné prezentace a tabulky. [Referoval jsem zde](https://www.marigold.cz/item/openai-agent/).

Systém používá vlastní virtuální počítač a plynule přepíná mezi uvažováním a jednáním při zpracování složitých pracovních postupů od začátku do konce na základě uživatelských instrukcí. Uživatelé mohou například požádat o "analýzu kalendáře a briefing nadcházejících klientských schůzek na základě aktuálních zpráv" nebo "plánování a nákup ingrediencí pro japonskou snídani pro čtyři osoby".

ChatGPT Agent je dostupný pro uživatele plánů Pro, Plus a Team prostřednictvím výběru "agent mode" z rozbalovacího menu nástrojů. Pro uživatelé získají přístup do konce dne, zatímco uživatelé Plus a Team během několika následujících dní. Pro uživatelé mají přístup k 400 zprávám měsíčně, ostatní platící uživatelé k 40 zprávám měsíčně s možností dalšího využití prostřednictvím flexibilních kreditových opcí.

## Runway Act-Two přináší pokročilý motion capture bez speciálního vybavení

Runway představil [Act-Two](https://runwayml.com/), model nové generace pro motion capture, který dokáže přenést pohyby herce včetně jemných pohybů hlavy, obličeje a rukou z jediného referenčního videa na jakoukoliv digitální postavu. Act-Two eliminuje potřebu specializovaných kamer nebo oblečků a je dostupný všem podnikovým klientům.

Act-Two se vyznačuje schopností zachytit detailní pohyby obličeje, gesta a oční linie s přesností, přenos pocitu performace, nikoli pouze pohybů. Model podporuje komplexní sledování pohybů napříč více částmi těla - hlavu, výrazy obličeje, horní část těla, ruce a dokonce i prvky pozadí. Systém funguje napříč různými styly postav, prostředími a uměleckými směry bez kompromisů ve věrnosti performace.

Runway oficiálně zpřístupnil Act-Two také prostřednictvím Runway API, což umožňuje vývojářům integrovat tento pokročilý model motion capture do vlastních aplikací, webových stránek nebo platforem. To představuje významný krok vpřed v democratizaci pokročilých AI nástrojů pro animaci.

## xAI rozšířil Grok o AI společníky s kontroverzními funkcemi

xAI spustil novou funkci "Companions" v aplikaci [Grok](https://grok.x.ai), která obsahuje dvě AI postavy - Ani, anime postavu v gotickém oblečení, a Bad Rudi, červenou pandu s agresivním chováním. Grok Companions představují první pokus velkých AI firem o sexualizované AI společníky.

Postava Ani má pokročilý systém náklonnosti - čím více s ní uživatel interaguje flirtovním způsobem, tím více se odhaluje až do spodního prádla a zapojuje se do explicitnějšího obsahu. Bad Rudi může být přepnut do režimu "Bad Rudy", kde se stává homicidním maniakem podporujícím násilí včetně útoků na školy.

xAI věnuje této funkci značné zdroje - firma hledá full-stack "waifus" inženýra a Musk oznámil třetího společníka jménem "Valentine" inspirovaného postavami Edward Cullen z Twilight a Christian Grey z 50 odstínů šedi. Kritici upozorňují, že aplikace je dostupná uživatelům od 13 let, zatímco obsahuje sexualizovaný obsah.

## Anthropic představil adresář nástrojů pro Claude

Anthropic 14. července představil [nový adresář nástrojů](https://www.anthropic.com/news/connectors-directory), které se připojují k Claude jedním kliknutím. Claude Connectors Directory obsahuje nové konektory vytvořené partnery pro vzdálené služby jako Notion, Canva a Stripe i lokální desktopové aplikace jako Figma, Socket a Prisma.

Místo opakovaného vysvětlování detailů projektu, termínů a nástrojů může uživatel požádat Claude o "napsání poznámek k vydání pro náš nejnovější sprint z Linear", čímž Claude vytáhne skutečné tikety z Linear a vygeneruje profesionální poznámky k vydání připravené k publikaci. Systém transformuje Claude z užitečného asistenta na informovaného AI spolupracovníka s přístupem ke stejným nástrojům, datům a kontextu jako uživatel.

Adresář je dostupný všem uživatelům Claude na webu a desktopu na adrese [claude.ai/directory](https://claude.ai/directory). Konektory pro vzdálené aplikace a služby jsou dostupné pouze uživatelům placených plánů. Všechny integrace využívají open-source Model Context Protocol (MCP) od Anthropic, který zjednodušuje proces připojení AI modelů k externím aplikacím.

## Mistral AI vydal Voxtral jako první open-source model pro porozumění řeči

Mistral AI 15. července představil [Voxtral](https://mistral.ai/news/voxtral), své první open-source modely pro porozumění řeči dostupné ve dvou velikostech - 24B variantě pro aplikace v produkčním měřítku a 3B variantě pro lokální a edge nasazení. Voxtral je vydán pod licencí Apache 2.0 a je také dostupný prostřednictvím API. [Referoval jsem zde](https://www.marigold.cz/item/mistral-voxtral/).

Model nabízí špičkovou přesnost a nativní sémantické porozumění ve formátu otevřeného zdrojového kódu za méně než poloviční cenu srovnatelných API. S délkou kontextu 32k tokenů Voxtral zpracovává zvukové soubory až 30 minut pro transkripci nebo 40 minut pro porozumění.

Mistral tvrdí, že Voxtral může transkribovat až 30 minut zvuku a díky své jazykové páteři Mistral Small 3.1 rozumí až 40 minutám, což umožňuje uživatelům pokládat otázky o zvukovém obsahu, generovat souhrny nebo přeměnit hlasové příkazy na akce v reálném čase. API začíná na 0,001 dolaru za minutu a dosahuje přibližně 0,004 dolaru s údajně lepší mírou chybovosti slov než gpt-4o-mini-transcribe.

## Amazon uvedl Kiro jako agentní IDE pro vývoj

Amazon 14. července spustil v preview nový nástroj jménem [Kiro](https://kiro.dev/), agentní IDE které kombinuje agentní kódování se spec-driven vývojem. Kiro se zaměřuje na řešení problému nedokumentovaného AI-generovaného softwaru, který se stává obtížně udržovatelným. [Referoval jsem zde](https://www.marigold.cz/item/kiro-ide-amazon/).

Kiro pomáhá přejít od "vibe coding" k "viable code" prostřednictvím spec-driven vývoje - rozebírá vývojářské výzvy do strukturovaných komponent včetně požadavků, návrhových dokumentů a seznamů úkolů pro vedení implementace a testování. Nástroj obsahuje agent hooks - automatizace řízené událostmi, které spouštějí agenta k provedení úkolu na pozadí při ukládání, vytváření nebo mazání souborů.

Kiro je během preview období zdarma. Finálně firma plánuje tři cenové úrovně - bezplatnou verzi s 50 agentními interakcemi měsíčně, Pro úroveň za 19 dolarů na uživatele měsíčně s 1000 interakcemi a Pro+ úroveň za 39 dolarů na uživatele měsíčně s 3000 interakcemi.

## Google rozšířil AI Mode o Deep Search a telefonování obchodům

Google představil [pokročilé AI funkce v Search](https://blog.google/products/search/deep-search-business-calling-google-search/) včetně modelu Gemini 2.5 Pro a Deep Search pro předplatitele Google AI Pro a AI Ultra. Google AI Mode navíc získává agentní funkci pro AI-powered telefonování místním obchodům.

Deep Search je nejpokročilejší výzkumný nástroj Google Search, který pomáhá ušetřit hodiny provedením stovek vyhledávání, uvažováním napříč různými informacemi a vytvořením komprehensivní, plně citované zprávy během minut. Funkce je užitečná pro hloubkové výzkumy související s prací, koníčky nebo studiem i při důležitých životních rozhodnutích.

Nová funkce telefonování obchodům používá AI k volání místních podniků jménem uživatele za účelem získání informací o dostupnosti a cenách. Systém funguje na technologii Gemini modelů a Duplex - uživatel vyhledá například "pěstitelé domácích zvířat v mé blízkosti" a v výsledcích uvidí novou možnost "Nechat AI zkontrolovat ceny". Automatizovaný hlas informuje podniky, že volá AI systém a uživatel obdrží informace textovou zprávou.

## Decart představil MirageLSD jako první real-time live-stream model

Decart uvedl [MirageLSD](https://about.decart.ai/publications/mirage), první Live-Stream Diffusion (LSD) AI video model, který dokáže vkládat představivost do jakéhokoliv živého video streamu s odezvou pod 40 milisekund. MirageLSD představuje první systém dosahující nekonečné, real-time video generování s nulovou latencí.

Na rozdíl od jiných AI video modelů se zpožděním 10+ sekund a klipy dlouhé 5-10 sekund Mirage transformuje nekonečné video streamy v reálném čase. Model generuje každý snímek samostatně a používá techniky jako diffusion forcing a history augmentation pro vyvarování se kumulativních chyb a udržení stabilních výsledků napříč rozšířenými video sekvencemi.

Podle Decart může Mirage fungovat při 20 snímcích za sekundu při standardním webovém rozlišení se zpožděním zpracování přibližně 100 milisekund na snímek. Wired poznamenává, že změna živého obrazu v reálném čase vyžaduje značný výpočetní výkon - Decart optimalizoval nízkoúrovňový kód pro maximalizaci výkonu na Nvidia hardware.

MirageLSD je již dostupný jako platforma s mobilními aplikacemi na cestě a cílí na použití jako živé streamování, video hovory a hraní her. Uživatelé si mohou nástroj vyzkoušet na [demo webu Decart](https://mirage.decart.ai/).

## Proton představil Lumo jako soukromý AI asistent

Proton v červenci uvedl [Lumo](https://lumo.proton.me), AI asistenta zaměřeného na soukromí uživatelů. Na rozdíl od velkých AI firem Lumo neuchovává logy konverzací na serverech, používá zero-access šifrování pro uložená data a nevyužívá uživatelské konverzace pro trénink modelů. Služba je dostupná zdarma bez nutnosti registrace a běží na open-source jazykových modelech v evropských datacentrech.

Lumo nabízí funkce jako "ghost mode" pro kompletní anonymní konverzace, webové vyhledávání pro aktuální informace, nahrávání souborů s garancí jejich nezaznamenávání a integraci s Proton Drive. [Dokumentace a srovnání](https://proton.me/blog/lumo-ai) ukazuje, jak se Lumo liší od ostatních AI asistentů zejména v oblasti ochrany dat a transparentnosti. Z jakého modelu Lumo vychází, ale není jasné. Model na to cíleně neodpovídá. V tarifu Lumo Free máte 50 otázek za den (cca, záleží spíše na počtu tokenů, přesně to nebylo publikováno). Cena tarifu Lumo Plus bez omezení byla stanovena na 10 € měsíčně. 

Uvedení Lumo je součástí širší investice Proton přes 100 milionů eur do evropské technologické infrastruktury zvané EuroStack. Proton přesouvá většinu své fyzické infrastruktury ze Švýcarska do EU kvůli právní nejistotě kolem švýcarských návrhů na masové sledování, které byly v EU zakázány. Proton je známý svým důrazem na soukromí (používám jeho služby).

## Pokroky v robotice a hardwaru

### Figure představil pokročilou baterii F.03 s 78% úsporou nákladů

[Figure](https://www.figure.ai) oznámil novou 2,3 kWh baterii F.03, kterou navrhl a vyrábí vlastními silami. Klíčové vlastnosti zahrnují 5 hodin provozu, vylepšenou hustotu energie, 2 kW rychlé nabíjení s aktivním chlazením, vlastní BMS pro udržení zdraví baterie a 78% snížení nákladů oproti předchozí verzi F.02. Baterie představuje významný pokrok ve snaze učinit humanoidní roboty ekonomicky životaschopnými pro průmyslové nasazení. Společnost také [otevřela nové pozice](https://figure.ai/careers) ve své výrobní divizi BotQ.

### UBTECH Walker S2 jako první humanoid s autonomní výměnou baterie

Čínská společnost [UBTECH](https://www.ubtrobot.com) představila Walker S2, humanoidního robota nové generace pro průmyslové aplikace. Společnost tvrdí, že jde o prvního humanoida, který dokáže vyměnit svou baterii samostatně, což zajišťuje nepřetržitý provoz 24 hodin denně. Tato schopnost řeší jeden z klíčových problémů humanoidní robotiky - omezený čas provozu na baterii.

### Pollen Robotics open-source robotická ruka za 200 dolarů

Tým [Pollen Robotics](https://www.pollen-robotics.com) od Hugging Face open-source zpřístupnil plně 3D-tištěnou robotickou ruku s názvem "The Amazing Hand" za méně než 200 dolarů. Ruka vážící 400 gramů používá měkký TPU kryt a slibuje 8 stupňů volnosti s dvojicí hobby serv na prst. Open-source přístup značně snižuje náklady na pokročilé robotické komponenty a democratizuje přístup k robotickým technologiím.

### Agility Robotics ukázal odolnost robota Digit

[Agility Robotics](https://agilityrobotics.com) zveřejnil video svého robota Digit, které ukazuje, jak se dokáže zotavit z nepříjemných situací, například když mu někdo vytáhne koberec zpod nohou. Společnost cílí na průmyslové úkoly se svými roboty a spolupracuje s giganty jako Amazon na nasazení humanoidní robotiky ve skladech a výrobních zařízeních.

## Infrastruktura a financování AI

### Meta investuje stovky miliard do AI superklustrů

[Meta](https://ai.meta.com) oznámila plány na stavbu superklustrů v Louisiana a Ohio pro vývoj AI superinteligence. První 1GW zařízení bude uvedeno do provozu v roce 2026, zatímco druhé nazvané Hyperion se rozšíří z 2 na 5GW. Společnost míří na investice v řádu stovek miliard dolarů do této infrastruktury, což představuje jeden z největších závazků v historii pro AI výpočetní kapacity.

### Mira Murati získala 2 miliardy dolarů pro Thinking Machines Lab

Bývalá CTO OpenAI Mira Murati [oznámila](https://thinkingmachines.paperform.co) seed financování ve výši 2 miliard dolarů pro svou společnost Thinking Machines Lab. Murati uvedla, že společnost vyvíjí multimodální AI a uvede svůj první produkt "v příštích několika měsících" s významnou open-source komponentou. Financování vede a16z s účastí NVIDIA, Accel, ServiceNow, CISCO, AMD, Jane Street a dalších investorů.

### Hume AI představil EVI-3 pro pokročilou řečovou syntézu

[Hume AI](https://hume.ai) spustil EVI-3, nový speech-to-speech model, který nejen napodobuje hlas mluvčího, ale také jeho tón, styl mluvení, nuance, jazyk a osobnost. Model potřebuje pouze 15-20 sekund zvuku pro kompletní syntézu hlasových charakteristik, což představuje významný pokrok v personalizaci AI hlasových asistentů.

