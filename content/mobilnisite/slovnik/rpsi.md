---
slug: "rpsi"
url: "/mobilnisite/slovnik/rpsi/"
type: "slovnik"
title: "RPSI – Reference Picture Selection Indication"
date: 2025-01-01
abbr: "RPSI"
fullName: "Reference Picture Selection Indication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rpsi/"
summary: "Mechanismus v multimediální telefonii 3GPP (MTSI) pro zlepšení kvality videohovoru tím, že signalizuje, který dříve přenesený snímek videa má být použit jako referenční pro dekódování při výskytu ztrá"
---

RPSI je mechanismus v multimediální telefonii 3GPP, který signalizuje, který dříve přenesený snímek videa má být použit jako referenční pro dekódování po ztrátě paketu, čímž zlepšuje kvalitu videohovoru a odolnost proti chybám.

## Popis

Reference Picture Selection Indication (RPSI) je funkce definovaná v rámci specifikace 3GPP Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)), konkrétně podrobně popsaná v TS 26.922. Funguje na aplikační vrstvě jako součást řídicího protokolu videokodeku. Hlavní funkcí RPSI je poskytnout zpětnovazební mechanismus od příjemce videa k odesílateli videa, který odesílateli instruuje, aby budoucí snímky videa kódoval pomocí konkrétního, staršího referenčního snímku, který příjemce úspěšně dekódoval a uložil ve své vyrovnávací paměti. Tento mechanismus se aktivuje, když příjemce zjistí, že aktuální nebo nedávný snímek videa (nebo na něm závislé snímky) byl během přenosu ztracen nebo poškozen. Signalizací odesílateli, aby přešel na známý správný referenční snímek, může příjemce přerušit řetězec šíření chyb, který je typický pro prediktivní kódování videa (jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/)), kde každý snímek často odkazuje na ten bezprostředně předcházející. Zpráva RPSI obsahuje identifikátor konkrétního referenčního snímku, což umožňuje přesné obnovení. Z architektonického hlediska je součástí řídicí signalizace typu end-to-end mezi klienty MTSI, nezávisle na mechanismech opravy chyb podléhající přenosové sítě. Její role je klíčová pro udržení přijatelné kvality videa v konverzačních službách, kde je prvořadá nízká latence a opětovné přenosy často nejsou proveditelné.

## K čemu slouží

RPSI bylo zavedeno, aby řešilo výzvu udržení kvality videa v paketově přepínaných službách reálné komunikace, jako jsou videohovory Voice over LTE (VoLTE). Tradiční videokodeky jsou vysoce účinné, ale zranitelné vůči ztrátě paketů; jediný ztracený paket může poškodit snímek a v důsledku prediktivního kódování se toto poškození přenese na všechny následující snímky, které na něj odkazují, což způsobí viditelné artefakty nebo zamrznutí obrazu až do přijetí dalšího nezávisle kódovaného snímku (I-snímku). V konverzačních službách s nízkou latencí je čekání na periodický I-snímek nepřijatelné. RPSI poskytuje okamžitý mechanismus obnovy na aplikační vrstvě. Řeší problém tím, že umožňuje příjemci proaktivně usměrňovat výběr referenčního snímku v kodéru, což umožňuje rychlé zotavení z chyb bez režie šířky pásma pro časté I-snímky nebo latence spojené s opětovnými přenosy na transportní vrstvě. Jeho vytvoření bylo motivováno potřebou učinit videotelefonii založenou na IMS robustní v IP sítích, které jsou ze své podstaty best-effort a náchylné k kolísání zpoždění a ztrátám, zejména v raných nasazeních LTE a v náročných rádiových podmínkách.

## Klíčové vlastnosti

- Zpětnovazební mechanismus na aplikační vrstvě pro řízení chyb videa
- Signalizuje konkrétní identifikátor referenčního snímku od příjemce k odesílateli
- Přerušuje časové řetězení šíření chyb v prediktivním kódování videa
- Funguje v rámci architektury 3GPP MTSI a IMS
- Snižuje závislost na obnově pomocí vnitrosnímkového kódování pro zotavení z chyb
- Zlepšuje uživatelský zážitek z reálných videohovorů přes paketové sítě

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [RPSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpsi/)
