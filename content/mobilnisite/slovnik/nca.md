---
slug: "nca"
url: "/mobilnisite/slovnik/nca/"
type: "slovnik"
title: "NCA – Network Status Continuous Report Answer"
date: 2025-01-01
abbr: "NCA"
fullName: "Network Status Continuous Report Answer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nca/"
summary: "NCA je příkaz aplikace Diameter používaný na rozhraní Rx podle 3GPP. Je to odpověď od funkce pro pravidla účtování a politiky (PCRF) směrem k funkci pro vynucování pravidel účtování a politiky (PCEF),"
---

NCA je příkaz Diameter typu odpověď na rozhraní Rx, ve kterém PCRF poskytuje PCEF nepřetržitý proud informací o stavu sítě, například události v uživatelské rovině, za účelem podpory dynamických rozhodnutí o politice.

## Popis

Network Status Continuous Report Answer (NCA) je příkaz Diameter definovaný v rámci aplikace referenčního bodu Rx podle 3GPP (specifikováno v 29.214 a odkazováno v 29.153). Je to klíčová součást architektury řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)). NCA je odesílán funkcí pro pravidla účtování a politiky ([PCRF](/mobilnisite/slovnik/pcrf/)) jako odpověď na příkaz Network Status Continuous Report Request ([NCR](/mobilnisite/slovnik/ncr/)) od funkce pro vynucování pravidel účtování a politiky ([PCEF](/mobilnisite/slovnik/pcef/)), která typicky sídlí v bráně paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/)) nebo v uzlu podpory [GPRS](/mobilnisite/slovnik/gprs/) (GGSN). Tato dvojice příkazů vytváří mechanismus, kterým může PCEF nepřetržitě hlásit PCRF konkrétní události v síti nebo uživatelské rovině a PCRF může tato hlášení potvrzovat a případně na ně reagovat.

Operačně proces začíná, když PCRF během zřízení nebo modifikace [IP-CAN](/mobilnisite/slovnik/ip-can/) (Internet Protocol Connectivity Access Network) relace rozhodne, že potřebuje být informována o určitých událostech. Pošle NCR PCEF se žádostí o hlášení těchto událostí. PCEF tuto žádost potvrdí pomocí NCA. Následně kdykoli dojde k odebírané události (např. změna typu přístupu k rádiové síti, změna obslužné brány nebo aktivace/deaktivace uživatelské roviny), PCEF odešle PCRF NCR, aby ji nahlásil. PCRF pak odpoví NCA, který může obsahovat nová rozhodnutí o politice nebo pravidla účtování spuštěná nahlášenou událostí. Tím vzniká nepřetržitý, událostmi řízený dialog pro dynamické vynucování politiky.

Příkaz NCA nese [AVP](/mobilnisite/slovnik/avp/) Diameter Result-Code, které označuje úspěch nebo selhání zpracování odpovídajícího NCR. Důležitější je, že může obsahovat AVP (dvojice atribut-hodnota), která poskytují aktualizovaná PCC pravidla, spouštěče událostí pro další hlášení nebo jiné informace související s politikou. To umožňuje PCRF reagovat v reálném čase na změny v síti nebo chování uživatele. Například po přijetí NCR hlásícího předání do přetížené buňky by PCRF mohla poslat NCA s novým pravidlem pro omezení šířky pásma uživatele. NCA tedy umožňuje systém uzavřené smyčky řízení, kde stav sítě přímo a okamžitě ovlivňuje služební politiku.

## K čemu slouží

Příkaz NCA existuje za účelem usnadnění politiky řízené událostmi v reálném čase v sítích 3GPP. Řeší problém statického vynucování politiky tím, že umožňuje PCRF dynamicky přizpůsobovat politiky na základě aktuálních síťových podmínek a událostí v uživatelské rovině. Před takovými mechanismy byla pravidla politiky v rámci relace z velké části statická a nemohla reagovat na změny, jako jsou události mobility nebo přetížení sítě, což vedlo k suboptimálnímu využití zdrojů a uživatelskému komfortu.

Jeho vytvoření bylo motivováno potřebou inteligentnějšího PCC pro podporu složitých služeb, jako je Voice over LTE (VoLTE), kde kontinuita a kvalita relace závisí na okamžité reakci na předání. Podporuje také sponzorované datové služby a služby kvality (QoS) na vyžádání. Dialog NCA/NCR řeší omezení jednorázového poskytování politiky vytvořením nepřetržitého kanálu pro hlášení, což umožňuje síti získat povědomí o kontextu a být responsivní.

Historicky zavedený ve vydání 13 jako součást vylepšení PCC, příkaz NCA formalizoval a standardizoval proces nepřetržitého hlášení stavu přes rozhraní Rx. To byl významný vývoj od jednodušších modelů řízení kreditu a autorizace, který umožnil pokročilé případy užití v LTE a později v systémech 5G. Poskytuje základní signalizaci pro modifikace služeb spouštěné sítí, které jsou nezbytné pro síťové segmenty, edge computing a další schopnosti jádra sítě 5G, které vyžadují agilní reakci politiky na síťové události.

## Klíčové vlastnosti

- Příkaz Diameter typu odpověď v aplikaci Rx (3GPP)
- Odesílán PCRF jako odpověď na Network Status Continuous Report Request (NCR) od PCEF
- Potvrzuje přijetí hlášení o událostech v síti/uživatelské rovině
- Může přenášet nová nebo upravená PCC pravidla spuštěná nahlášenou událostí
- Obsahuje AVP Result-Code pro označení výsledku zpracování
- Umožňuje dynamické, událostmi řízené řízení politiky a účtování

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [NCR – Network Status Continuous Report Request](/mobilnisite/slovnik/ncr/)

## Definující specifikace

- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF

---

📖 **Anglický originál a plná specifikace:** [NCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nca/)
