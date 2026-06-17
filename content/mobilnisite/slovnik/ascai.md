---
slug: "ascai"
url: "/mobilnisite/slovnik/ascai/"
type: "slovnik"
title: "ASCAI – Application Satellite Coverage Availability Information"
date: 2026-01-01
abbr: "ASCAI"
fullName: "Application Satellite Coverage Availability Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ascai/"
summary: "ASCAI je služba 3GPP, která umožňuje pozemním sítím dotazovat se a přijímat informace o dostupnosti satelitního pokrytí v reálném čase pro konkrétní geografické oblasti. Umožňuje aplikacím činit intel"
---

ASCAI je služba 3GPP, která umožňuje pozemním sítím dotazovat se a přijímat informace o dostupnosti satelitního pokrytí v reálném čase pro konkrétní geografické oblasti.

## Popis

Application Satellite Coverage Availability Information (ASCAI) je standardizovaná služba definovaná v rámci specifikací 3GPP, konkrétně ve vydání Release 19 a vylepšená ve vydání Release 20. Funguje jako služba pro zpřístupnění informací, kdy si pozemní síť (typicky 5G Core Network nebo aplikační funkce) může vyžádat od satelitní sítě nebo vyhrazeného informačního úložiště aktuální a předpokládanou budoucí dostupnost satelitního pokrytí pro určenou geografickou oblast, časový interval a potenciálně pro konkrétní typy satelitních služeb (např. narrowband IoT, broadband). Architektura zahrnuje Poskytovatele služby ASCAI (ASCAI Service Provider), který hostuje informace o pokrytí, a Spotřebitele služby ASCAI (ASCAI Service Consumer), který tyto údaje žádá. Interakce je standardizována prostřednictvím [API](/mobilnisite/slovnik/api/), což zajišťuje interoperabilitu mezi různými operátory pozemních a nepozemních sítí (NTN).

Základní mechanismus spočívá v tom, že Spotřebitel služby sestaví dotaz obsahující parametry, jako je geografická oblast (definovaná polygonem nebo seznamem sledovacích oblastí – Tracking Areas), časové okno zájmu a volitelně požadované ukazatele kvality (např. minimální elevace, prahové hodnoty síly signálu). Tento dotaz je odeslán Poskytovateli služby ASCAI. Poskytatel žádost zpracuje proti své dynamické databázi efemerid satelitů, stop paprsků a provozních plánů. Následně vrátí odpověď udávající pro dotazovanou oblast a čas, zda je satelitní pokrytí dostupné, a často zahrnuje podrobnosti, jako jsou konkrétní satelit(y) poskytující pokrytí, dostupné typy služeb a předpokládaná doba trvání pokrytí.

Klíčové součásti rámce ASCAI zahrnují standardizované severové API (NBI) pro dotaz a odpověď, datové modely definující strukturu informací o pokrytí (např. mapy dostupnosti, jízdní řády) a podkladové zdroje dat, jako jsou systémy správy satelitních sítí. Služba hraje klíčovou roli v integrovaném ekosystému pozemních a nepozemních sítí (TN-NTN) tím, že poskytuje kritický vstup pro rozhodování na úrovni sítě a aplikací. Například funkce [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) nebo [SMF](/mobilnisite/slovnik/smf/) (Session Management Function) v 5G jádru by mohla použít data ASCAI k rozhodnutí, zda má být UE v konkrétní lokalitě předána satelitní přístupové síti, nebo zda lze PDU sezení navázat či udržovat prostřednictvím satelitních zdrojů.

Z provozní perspektivy umožňuje ASCAI proaktivní správu sítě. Aplikace nebo síťové funkce již nemusí slepě zkoušet satelitní připojení, což může být pro zařízení energeticky náročné a může selhat. Místo toho se mohou dotázat služby ASCAI a učinit informovaná, efektivní rozhodnutí. Tím se snižuje signalizační režie, zlepšuje se uživatelský zážitek prevencí pokusů o připojení v oblastech bez pokrytí a optimalizuje se využití zdrojů v hybridní síti. Informace jsou typicky poskytovány s určitou dobou platnosti a mohou zahrnovat předpovědi, což umožňuje plánování komunikačních plánů pro služby tolerantní k zpoždění nebo IoT zařízení.

## K čemu slouží

ASCAI bylo vytvořeno, aby řešilo základní výzvu efektivní integrace satelitních sítí s pozemními systémy 5G a dalšími generacemi. Historicky satelitní komunikace fungovala izolovaně a pozemní sítě měly malé nebo žádné povědomí o dostupnosti satelitních zdrojů v reálném čase. Tento nedostatek přehledu ztěžoval, ne-li znemožňoval, bezproblémovou kontinuitu služeb a dynamické směrování provozu mezi pozemními a nepozemními segmenty. Aplikace a síťové funkce se musely spoléhat na statické konfigurace nebo reaktivní mechanismy objevování, což vedlo k neefektivnímu využití satelitní kapacity, zvýšené spotřebě baterie zařízení kvůli neúspěšným pokusům o připojení a zhoršenému uživatelskému zážitku v oblastech spoléhajících na hybridní pokrytí.

Primární problém, který ASCAI řeší, je informační asymetrie mezi operátory pozemních sítí / poskytovateli aplikací a operátory satelitních sítí. Standardizací metody pro zpřístupnění dynamických informací o satelitním pokrytí umožňuje inteligentní, daty řízenou orchestraci v integrovaném prostředí TN-NTN. To bylo motivováno širší iniciativou 3GPP formálně začlenit Nezemské sítě (NTN) jako nativní součást systému 5G, počínaje vydáním Release 15 a významně rozšířenou v následujících vydáních. Cílem je poskytnout všudypřítomné, spolehlivé připojení a [ASCI](/mobilnisite/slovnik/asci/) je klíčovým prvkem pro dosažení efektivního řízení zdrojů a zajištění služeb v této složité, heterogenní síťové topologii.

Předchozí přístupy byly omezeny na proprietární rozhraní nebo postrádaly podrobnost a aktuálnost požadovanou pro dynamické služby 5G. ASCAI poskytuje standardizovaný, škálovatelný a dotazovací model, který tyto nedostatky řeší. Umožňuje pozemní síti zacházet se satelitním pokrytím jako s objevitelným a plánovatelným zdrojem, podobně jako spravuje buňky v rádiové přístupové síti. To je zásadní pro podporu případů užití, jako je globální sledování IoT zařízení, nouzová komunikace v oblastech katastrof, kde je pozemní infrastruktura poškozena, a poskytování přenosu pro pohybující se platformy (lodě, letadla), kde je znalost oken pokrytí kritická pro správu relací a mobility.

## Klíčové vlastnosti

- Standardizované API pro dotazování na aktuální a předpokládanou dostupnost satelitního pokrytí
- Podporuje dotazy založené na geografické oblasti (např. polygon, seznam sledovacích oblastí – Tracking Areas) s časovými intervaly
- Poskytuje podrobné informace včetně dostupnosti typu služby a konkrétních identifikátorů satelitů
- Umožňuje proaktivní rozhodování sítě a aplikací pro směrování provozu a správu relací
- Snižuje zbytečnou signalizaci a spotřebu energie zařízení prevencí pokusů o připojení v nepokrytých oblastech
- Usnadňuje efektivní orchestraci zdrojů v integrovaných pozemních a nepozemních sítích (TN-NTN)

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.558** (Rel-20) — Architecture for Edge Applications

---

📖 **Anglický originál a plná specifikace:** [ASCAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ascai/)
