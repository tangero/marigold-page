---
slug: "hoa2"
url: "/mobilnisite/slovnik/hoa2/"
type: "slovnik"
title: "HOA2 – Higher-Order Ambisonics (2nd order)"
date: 2025-01-01
abbr: "HOA2"
fullName: "Higher-Order Ambisonics (2nd order)"
category: "Services"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/hoa2/"
summary: "HOA2 je specifická implementace Higher Order Ambisonics využívající sférické harmoniky druhého řádu, která nabízí vylepšenou přesnost prostorového zvuku oproti prvnímu řádu. Poskytuje lepší rovnováhu"
---

HOA2 je implementace vyššího řádu Ambisonics používající sférické harmoniky druhého řádu, která nabízí vylepšenou přesnost prostorového zvuku pro lepší rovnováhu mezi kvalitou a datovým tokem u immersivních služeb, jako je streamování VR přes sítě 5G.

## Popis

HOA2 označuje reprezentaci a zpracování prostorového zvukového pole pomocí Ambisonics druhého řádu. Jedná se o konkrétní úroveň v rámci škálovatelného rámce Higher Order Ambisonics ([HOA](/mobilnisite/slovnik/hoa/)). Matematicky signál Ambisonics druhého řádu rozkládá zvukové pole na sadu koeficientů sférických harmonik až do stupně l=2. Výsledkem je (2+1)² = 9 samostatných zvukových kanálů (často označovaných W, X, Y, Z, R, S, T, U, V). Každý kanál představuje specifický vzor sférické harmoniky a zachycuje podrobnější směrové informace než Ambisonics prvního řádu (který má 4 kanály), přičemž zvláště zlepšuje vnímání šířky zdroje zvuku, výšky a externalizace (pocit umístění zvuku vně hlavy).

Pracovní postup pro HOA2 zahrnuje kódování, přenos a dekódování. Při produkci je zvuk zachycen mikrofonním polem Ambisonics druhého řádu nebo je generován namapováním virtuálních zvukových objektů do B-formátu druhého řádu. Tento 9-kanálový signál je následně komprimován pomocí podporovaného kodeku, jako je MPEG-H 3D Audio, který dokáže účinně snížit jeho datový tok při zachování prostorových informací. V řetězci dodávky 3GPP je komprimovaný HOA2 bitový proud zabalen do mediálních segmentů, typicky v kontejneru [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) pro Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)).

Na klientském zařízení, jako je [VR](/mobilnisite/slovnik/vr/) headset, je přijatý HOA2 stream dekódován zvukovým kodekem a následně renderován pro přehrávání. Renderování zahrnuje aplikaci dekódovací matice na 9 kanálů, aby byly získány signály pro konkrétní výstupní konfiguraci, ať už jde o soustavu více reproduktorů nebo binaurální sluchátka. Pro přehrávání s head-trackingu se data o orientaci hlavy ze senzorů zařízení používají k dynamické rotaci celého zvukového pole před dekódováním, což zajišťuje, že zvuky zůstanou pevně umístěny ve virtuálním světě. Zvýšený počet kanálů v HOA2 oproti prvnímu řádu umožňuje přesnější rekonstrukci zvukového pole, což vede k ostřejší lokalizaci zvuků a přesvědčivějšímu pocitu ponoření, zejména u zvuků nad a pod posluchačem.

## K čemu slouží

HOA2 bylo specifikováno, aby poskytlo konkrétní, střední kvalitativní stupeň v žebříčku kvality [HOA](/mobilnisite/slovnik/hoa/), který řeší kompromis mezi věrností immersivního zvuku a praktickými omezeními šířky pásma, výpočetního výkonu a úložiště. Ambisonics prvního řádu (HOA1), ačkoli je dobrým výchozím bodem, má omezené prostorové rozlišení, které může způsobovat slyšitelné rozmazání zdrojů zvuku a slabé výškové informace. Ambisonics třetího nebo vyššího řádu poskytuje vynikající věrnost, ale za cenu výrazně vyššího počtu kanálů a datového toku, což může být pro mobilní streamování nepřijatelné. HOA2 bylo zavedeno, aby tuto mezeru zaplnilo, a nabízí podstatné zlepšení oproti HOA1 za cenu umírněného nárůstu složitosti.

Konkrétní motivací v rámci vydání 3GPP bylo umožnit poskytovatelům služeb nabízet stupňované immersivní zvukové zážitky. Například základní [VR](/mobilnisite/slovnik/vr/) stream může používat HOA1, zatímco prémiová služba může pro vylepšený realismus využívat HOA2. Standardizace HOA2 jako definovaného profilu zajišťuje interoperabilitu mezi kodéry, streamovacími servery a dekodéry, což umožňuje průmyslu konvergovat na konkrétní sadu parametrů pro tuto úroveň kvality. To je klíčové pro efektivní implementaci kodeků a certifikaci zařízení.

Z pohledu sítě pomáhá definice HOA2 při optimalizaci sítě s ohledem na média. Síťové funkce mohou být informovány o charakteristikách HOA2 streamů (např. o jejich citlivosti na ztrátu paketů u určitých kanálů), aby mohly uplatňovat vhodné zásady QoS (Quality of Service). Jeho standardizace v pozdějších vydáních 3GPP odráží zrání služeb immersivních médií a potřebu sofistikovanějších zvukových formátů pro plné využití vysoké propustnosti a nízké latence pokročilých sítí 5G.

## Klíčové vlastnosti

- Definován jako reprezentace sférickými harmonikami 2. řádu, sestávající z 9 zvukových kanálů.
- Poskytuje výrazně vylepšené prostorové rozlišení a lokalizaci zdroje zvuku oproti Ambisonics 1. řádu.
- Přináší lepší vnímání šířky zdroje zvuku, výšky a externalizace.
- Standardizován jako specifický profil v rámci specifikací immersivních médií 3GPP.
- Optimalizován pro kompresi pomocí kodeků jako MPEG-H 3D Audio pro efektivní streamování.
- Podporuje dynamické binaurální renderování s head-trackingu pro aplikace VR/AR headsetů.

## Související pojmy

- [HOA – Higher Order Ambisonics](/mobilnisite/slovnik/hoa/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [HOA2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hoa2/)
