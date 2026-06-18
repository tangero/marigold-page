---
slug: "stsa"
url: "/mobilnisite/slovnik/stsa/"
type: "slovnik"
title: "STSA – Stepwise Temporal Sub-layer Access"
date: 2025-01-01
abbr: "STSA"
fullName: "Stepwise Temporal Sub-layer Access"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/stsa/"
summary: "Stepwise Temporal Sub-layer Access (STSA) je technika streamování médií definovaná 3GPP pro Dynamic Adaptive Streaming over HTTP (DASH). Umožňuje streamovacímu klientovi postupně přistupovat k vyšším"
---

STSA je technika streamování médií od 3GPP pro DASH, která umožňuje klientovi postupně přistupovat k vyšším časovým subvrstvám videa pro plynulejší přechody kvality při kolísání sítě.

## Popis

Stepwise Temporal Sub-layer Access (STSA) je funkce specifikovaná ve standardech 3GPP [DASH](/mobilnisite/slovnik/dash/) (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)), zejména pro obsah kódovaný pomocí Scalable Video Coding ([SVC](/mobilnisite/slovnik/svc/)). SVC kóduje videoproud do více vrstev: základní vrstvy (poskytující nejnižší kvalitu) a jedné nebo více vylepšujících vrstev (které zlepšují prostorové rozlišení, kvalitu nebo časovou snímkovou frekvenci). STSA se konkrétně zabývá časovými vylepšujícími vrstvami, které zvyšují snímkovou frekvenci (např. z 15 fps na 30 fps).

V typickém scénáři SVC-DASH soubor Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) popisuje dostupné videoreprezentace (datové toky, rozlišení, snímkové frekvence) a jejich závislostní vztahy. Bez STSA by přepnutí na reprezentaci s vyšší časovou vrstvou (vyšší snímkovou frekvencí) mohlo vyžadovat, aby klient stáhl velký segment obsahující jak základní vrstvu, tak data nové časové vylepšující vrstvy, což může být neefektivní, pokud uživatel chce pouze mírné zlepšení snímkové frekvence. STSA to řeší strukturou mediálních segmentů tak, že data pro každou časovou subvrstvu (např. snímky, které zvyšují snímkovou frekvenci z 15 fps na 30 fps) jsou přístupná postupným, přírůstkovým způsobem.

Provozně MPD indikuje, že určité reprezentace podporují STSA. Když se klient DASH rozhodne adaptovat směrem nahoru na vyšší snímkovou frekvenci, může nejprve požadovat a stáhnout pouze přírůstkovou časovou vylepšující subvrstvu pro následující segment(y), nikoli plnou reprezentaci s vysokou snímkovou frekvencí. Tato data subvrstvy jsou pak kombinována s již staženými daty základní vrstvy k rekonstrukci videa s vyšší snímkovou frekvencí. Tím se snižuje počáteční „špička“ datového toku při přepnutí nahoru, což vede k plynulejšímu přechodu, menšímu riziku vyprázdnění vyrovnávací paměti a responsivnější adaptaci na zlepšující se síťové podmínky. Umožňuje jemnější granularitu v adaptaci kvality, konkrétně na časové ose.

## K čemu slouží

STSA byla vytvořena za účelem zvýšení efektivity a kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)) pro adaptivní videostreamování, zejména v mobilních prostředích, kde je šířka pásma proměnlivá a omezená. Tradiční adaptivní streamování (pomocí [AVC](/mobilnisite/slovnik/avc/)/H.264) vyžaduje přepínání mezi zcela odlišně zakódovanými datovými toky, což může být neefektivní a způsobovat znatelné skoky v kvalitě. Přijetí Scalable Video Coding ([SVC](/mobilnisite/slovnik/svc/)) slibovalo efektivnější přepínání, ale rané implementace stále měly hrubé adaptační kroky.

Konkrétním problémem, který STSA řeší, je neefektivní přechod na vyšší časová rozlišení (snímkové frekvence). Zvýšení snímkové frekvence výrazně zlepšuje vnímanou kvalitu, zejména u sportovního nebo akčního obsahu, ale vyžádání plného segmentu s vysokou snímkovou frekvencí okamžitě spotřebuje značnou šířku pásma. Při špatných nebo kolísavých síťových podmínkách by to mohlo způsobit vyčerpání a opětovné načítání vyrovnávací paměti. STSA umožňuje „měkčí“ cestu upgradu: klient může nejprve zvýšit snímkovou frekvenci přírůstkově stažením pouze dodatečných časových dat, což je menší stažení. Tím se snižuje režie adaptace a klient se stává obratnějším a konzervativnějším ve správě své vyrovnávací paměti, což vede ke stabilnějšímu přehrávání.

Zavedená v 3GPP Release 12 jako součást vyvíjejících se standardů [DASH](/mobilnisite/slovnik/dash/) a SVC, byla STSA motivována potřebou sofistikovanější adaptační logiky pro podporu vysokokvalitních mobilních videoslužeb, jako je LTE Broadcast (eMBMS) a později doručování médií v 5G. Umožňuje poskytovatelům obsahu kódovat jednou s využitím SVC a značek STSA, což klientům umožňuje činit chytřejší, postupná adaptační rozhodnutí, což v konečném důsledku šetří síťové zdroje a maximalizuje plynulost videa vnímanou uživatelem.

## Klíčové vlastnosti

- Umožňuje přírůstkové načítání časových vylepšujících vrstev v obsahu DASH kódovaném pomocí SVC
- Snižuje režii datového toku při přepnutí na reprezentaci s vyšší snímkovou frekvencí
- Usnadňuje plynulejší přechody kvality a responsivnější adaptaci na zlepšující se šířku pásma
- Vyžaduje specifickou signalizaci v souboru DASH Media Presentation Description (MPD)
- Zlepšuje správu vyrovnávací paměti klienta umožněním jemněji odstupňovaných adaptačních kroků
- Optimalizováno pro mobilní streamovací scénáře s kolísavými síťovými podmínkami

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [STSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/stsa/)
