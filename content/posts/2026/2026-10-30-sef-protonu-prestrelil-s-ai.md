---
title: Šéf Protonu přestřelil s AI ve firmě, která stojí na důvěře…
slug: sef-protonu-prestrelil-s-ai
author: Patrick Zandl
categories:
  - AI
post_excerpt: Reportáž 404 Media popisuje, jak vedení Protonu zavádí AI jako náboženství, odbývá bezpečnostní námitky a spojuje používání AI se strachem o místo.
summary_points:
  - Andy Yen označil návrh na penetrační testy před nasazením za „myšlení loserů“
  - AI podle CTO napsala v říjnu 90 % kódu a firma měří podíl AI na počítačích zaměstnanců
  - Přepohovory o používání AI mohou vést ke změnám rolí i ukončení zaměstnání
  - Ověřený bezpečnostní incident zatím nikdo nedoložil
  - Proton se po vydání omluvil, popřel měřicí software i přepohovory a slíbil zveřejnit pravidla pro AI a postup kontroly kódu
thumbnail: https://www.marigold.cz/assets/andy-yen-proton.webp
audio_url: ''
hide: false
---

_Aktualizace 31. 10. 2026: Proton po vydání reportáže zveřejnil na X [prohlášení s omluvou](https://x.com/protonprivacy/status/2116302824577405320). Doplnil jsem ho do textu níže._

Proton stojí na jediném aktivu: důvěře. Lidé mu svěřují e-maily, hesla a soubory, protože věří, že tam bezpečnost má přednost. [Reportáž 404 Media](https://www.404media.co/manifestos-fear-and-loser-thinking-inside-protons-ai-reckoning/) ukazuje, jak snadno se ta důvěra dá ohrozit, když vedení začne AI zavádět jako náboženství.

Koncem srpna navrhl zaměstnanec v bezpečnostním kanálu na Slacku, aby se nový kód před nasazením pár dní penetračně testoval. Šéf Andy Yen odepsal: „To je bullshit a myšlení loserů. Samozřejmě jde být rychlý i bezpečný.“ A vyzval tým, ať přestane „s láskou ručně vyrábět kód“ a víc používá AI. Jiný inženýr v téže debatě poznamenal, že bezpečnost má ve firmě teď nízkou prioritu. Další zaměstnanec vůči 404 Media zdůraznil, že se inženýři o bezpečný kód dál snaží.

Co dalšího reportáž popisuje (8 současných a 1 bývalý zaměstnanec, interní Slack, nahrávky porad):

- Yen zřídil e-mail, kam mají lidé hlásit vše, co brzdí nasazení AI, aby to vedení mohlo „nemilosrdně rozdrtit“.
- Na počítačích zaměstnanců běží software, který měří, kolik kódu napsala AI. (Proton to po vydání popřel, viz níže.)
- Podle CTO Barta Butlera napsala AI v říjnu 90 % kódu, z velké části přes Claude.
- Butlerův „AI manifest“ vzkazuje programátorům: „Vaše stará práce je pryč.“ Cílem je, aby většinu kódu kontrolovala AI místo lidí.
- Yen: letos firma naposledy nabírá programátory, od příštího roku jen lidi, kteří budou stavět věci s AI.
- AI firma interně schválila i pro zpracování finančních dat a pro odpovědi zákazníkům na Redditu a LinkedInu.
- Podle interního dokumentu Proton kvůli „nedostatečné rychlosti“ není na cestě splnit letošní cíl opakovaných tržeb a sám sebe označuje za podvýkonnou firmu.

K tomu kultura strachu. Zaměstnanci popisují, že si netroufnou ozvat. Když senior zaměstnanec veřejně kritizoval chystané přepohovory o používání AI, Yen mu před celým kanálem napsal, že pokud ho obviňuje z finančního motivu a nevěří mu, tohle pro něj možná není to pravé místo. Přepohovory měly proběhnout 4.-11. listopadu a podle uniklého e-mailu mohou vést ke „změnám rolí, odpovědností a pokračování zaměstnání“. (I to Proton po vydání popřel.)

Proton na Redditu popřel, že by propouštěl s AI jako výmluvou, prý mu chybějí lidi a nabírá. Mluvčí firmy ale vůči 404 Media nic z reportáže nerozporoval, jen připustil, že vedení bylo při vysvětlování „příliš přímé nebo příliš pomalé“.

## Proton se brání a omlouvá

Po vydání reportáže firma na X zveřejnila [prohlášení](https://x.com/protonprivacy/status/2116302824577405320), které jde mnohem dál:

- Software, který by na počítačích zaměstnanců měřil podíl kódu od AI, podle Protonu neexistuje. Fáma prý vznikla z nepochopení, jak funguje MDM (software pro správu firemních zařízení).
- Používání AI podle firmy nikdy nepůjde na úkor bezpečnosti. Za poslední rok prý naopak přibyly další vrstvy bezpečnostní kontroly, protože útočníci s pomocí AI prohledávají open source kód Protonu a hledají v něm zranitelnosti.
- Proton zaměstnance kvůli používání AI znovu nebude vyslýchat a nikdo kvůli takovým pohovorům nepřijde o práci.
- Firma zveřejní, jak u ní probíhá kontrola kódu a bezpečnostní revize, a své zásady pro AI: kde ji smí používat, kde ne a proč. Jako open source uvolní i několik interních nástrojů, včetně pokročilejších verzí asistenta Lumo, které dosud nebyly mimo firmu k dispozici.
- Na závěr: „Víme, že jsme nedostáli vysokému standardu, který od nás právem očekáváte. Za to se můžeme jen omluvit, je nám to líto.“

Prohlášení je ale potřeba číst pozorně. Výslovně popírá dvě věci: měřicí software a přepohovory. U přepohovorů proti němu stojí uniklý e-mail s konkrétním termínem a zmínkou o „pokračování zaměstnání“. Formulace v přítomném čase tak může znamenat i to, že firma plán po reportáži zrušila, ne že nikdy neexistoval. U měřicího softwaru je nedorozumění věrohodnější, MDM toho o zařízení sbírá hodně a zaměstnanci si jeho účel mohli vyložit po svém. Z vnějšku ani jedno ověřit nejde. Yenovy výroky na Slacku, manifest CTO, 90 % kódu od AI ani konec náboru programátorů prohlášení nerozporuje.

Slib zveřejnit, jak firma kontroluje kód a kde AI používá, je přesně to, co by firma stavějící na důvěře měla udělat. Hodnotit ho půjde, až dokumenty skutečně vyjdou.

## Co si z toho vzít

Ověřený bezpečnostní incident zatím nikdo nedoložil a nevíme ani, jak dnes vypadá skutečná kontrola kódu před vydáním. To má ukázat slíbený dokument Protonu. Proton je přesto učebnicový příklad, jak AI ve firmě zavádět nemáte:

- měřit podíl kódu od AI jako cíl, protože lidé začnou honit číslo místo kvality,
- nechat AI kontrolovat kód, který napsala AI, a lidi z kontroly vytlačit,
- bezpečnostní námitky odbýt jako zdržování,
- spojit používání AI se strachem o místo, takže lidé přestanou hlásit problémy.

AI umí vývoj výrazně zrychlit, to dnes zažívá většina týmů. Jenže u firmy, jejíž produkt je důvěra, se rychlost platí právě důvěrou. A tu si zákazníci odnesou mnohem rychleji, než ji AI stihne vygenerovat zpátky.

_Zdroj: 404 Media, [Manifestos, Fear, and 'Loser Thinking': Inside Proton's AI Reckoning](https://www.404media.co/manifestos-fear-and-loser-thinking-inside-protons-ai-reckoning/) (29. 10. 2026)_
