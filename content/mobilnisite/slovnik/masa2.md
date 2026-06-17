---
slug: "masa2"
url: "/mobilnisite/slovnik/masa2/"
type: "slovnik"
title: "MASA2 – MASA with 2 TC (stereo-MASA)"
date: 2025-01-01
abbr: "MASA2"
fullName: "MASA with 2 TC (stereo-MASA)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/masa2/"
summary: "Profil MASA, v němž základní audio obsahuje dva transportní kanály (typicky tvořící stereo pár). Metadata poskytují dodatečné prostorové informace, které vylepšují nebo přesouvají prvky mimo základní"
---

MASA2 je profil MASA pro audio, v němž základní audio používá dva transportní kanály pro stereo, obohacené metadaty, která poskytují dodatečné prostorové informace pro vytvoření působivějšího zvuku než základní stereo.

## Popis

MASA2, známý jako stereo-MASA, je profil v rámci standardu [MASA](/mobilnisite/slovnik/masa/), který používá dva audio transportní kanály (TC) jako základní audio datovou část. Tyto kanály typicky tvoří standardní stereo signál (levý a pravý). Přidružená metadata MASA tento stereo záznam nenahrazují, ale rozšiřují. Metadata mohou popsat scénu tak, že renderer dokáže pochopit původně zamýšlené pozice zdrojů zvuku, které se mohou lišit od jednoduchého panoramování implikovaného stereo průběhem. Například zvuk panoramovaný do středu ve stereo mixu může být pomocí metadat označen jako pocházející zezadu od posluchače. Renderer pak tato metadata použije ke zpracování dvoukanálového signálu, aplikuje korekce a vylepšení, aby znovu vytvořil přesnější trojrozměrné zvukové pole vhodné pro poslechové prostředí. Tento proces může zahrnovat upmix, potlačení přeslechu a personalizované zpracování [HRTF](/mobilnisite/slovnik/hrtf/). Architektura efektivně staví na známém stereo přenosu a přidává vrstvu prostorové inteligence, což z ní činí praktickou cestu upgradu pro stávající stereo hudbu a vysílací služby.

## K čemu slouží

MASA2 byl vytvořen, aby překlenul propast mezi všudypřítomným stereo obsahem a audio příští generace pro působivý poslech. Miliardy stávajících audio aktiv jsou ve stereo formátu a infrastruktura pro přímé vysílání/přenos je optimalizována pro dvoukanálové audio. Účelem MASA2 je obohatit tato aktiva o prostorové schopnosti bez nutnosti úplného přeznačení do složitého formátu založeného na objektech. Řeší omezení sterea, které uzavírá zvuk do jednorozměrného levopravého panoráma, tím, že umožňuje tvůrcům obsahu vložit zamýšlený prostorový záměr prostřednictvím metadat. To umožňuje zpětnou kompatibilitu (dva kanály se na zařízeních bez podpory [MASA](/mobilnisite/slovnik/masa/) přehrávají jako běžné stereo) a zároveň nabízí prémiový, působivý zážitek na přijímačích s podporou MASA. Je motivován zejména hudebním streamováním, živým vysíláním sportu a filmovým obsahem, kde je žádoucí bohatý, obklopující zvuk.

## Klíčové vlastnosti

- Základní audio se skládá ze dvou transportních kanálů (stereo základ)
- Metadata poskytují vylepšující a přesouvací data nad rámec stereo obrazu
- Zachovává zpětnou kompatibilitu se staršími systémy pro přehrávání sterea
- Umožňuje upmix a 3D render ze standardního stereo zdroje
- Ideální pro vylepšení hudby, filmů a vysílaného obsahu
- Poskytuje vyvážený kompromis mezi kvalitou zvuku, efektivitou datového toku a působivostí poslechu

## Související pojmy

- [MASA – Metadata-Assisted Spatial Audio](/mobilnisite/slovnik/masa/)
- [MASA1 – MASA with 1 TC (mono-MASA)](/mobilnisite/slovnik/masa1/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [MASA2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/masa2/)
