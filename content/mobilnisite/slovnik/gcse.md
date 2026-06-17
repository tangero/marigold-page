---
slug: "gcse"
url: "/mobilnisite/slovnik/gcse/"
type: "slovnik"
title: "GCSE – AS Group Communication Service Enabler Application Server"
date: 2025-01-01
abbr: "GCSE"
fullName: "AS Group Communication Service Enabler Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gcse/"
summary: "Aplikační server (AS), který umožňuje skupinové komunikační služby, jako je Mission Critical Push-to-Talk (MCPTT) přes LTE/5G. Spravuje skupinová volání, členství a řízení práva k vysílání a poskytuje"
---

GCSE je aplikační server, který umožňuje skupinové komunikační služby, jako je Mission Critical Push-to-Talk přes LTE/5G, tím, že spravuje skupinová volání, členství a řízení práva k vysílání pro veřejnou bezpečnost a komerční využití.

## Popis

Aplikační server pro skupinové komunikační služby (GCSE [AS](/mobilnisite/slovnik/as/)) je prvek jádra sítě definovaný v rámci architektury IP Multimedia Subsystem (IMS) pro zprostředkování efektivních skupinově orientovaných komunikačních služeb. Funguje jako specializovaný aplikační server, který řídí relace média typu jeden-k-více nebo mnoho-k-mnoho, primárně pro služby kritické pro misi ([MCS](/mobilnisite/slovnik/mcs/)). GCSE AS komunikuje s klíčovými prvky IMS, jako je Serving-Call Session Control Function (S-CSCF), prostřednictvím rozhraní [ISC](/mobilnisite/slovnik/isc/) a využívá rozhraní Ut pro konfiguraci služeb. Jeho architektura je navržena k optimalizaci využití síťových zdrojů pro skupinový provoz, což je klíčový požadavek pro sítě veřejné bezpečnosti, kde mnoho uživatelů potřebuje současně přijímat stejný mediální proud.

Operačně GCSE AS spravuje celý životní cyklus relace skupinové komunikace. To zahrnuje zřízení relace, kdy autorizuje účastníky na základě politik členství ve skupině, a správu relace, kdy zajišťuje distribuci média (hlas, video, data) všem autorizovaným členům. Kritickou funkcí je řízení práva k vysílání (floor control), které rozhoduje o žádostech uživatelů o slovo (získání 'práva k vysílání') v poloduplexní komunikaci typu Push-to-Talk a zajišťuje uspořádaný průběh konverzace. Server také udržuje dynamické informace o členství ve skupině, často komunikuje se serverem pro správu skupin, a může aktivovat specifické síťové funkce, jako je eMBMS (evolved Multimedia Broadcast Multicast Service), pro efektivní rozhlasové doručování přes rozhraní radiové sítě.

V rámci širšího síťového ekosystému hraje GCSE AS klíčovou roli při umožňování služeb kritických pro misi založených na 3GPP. Spolupracuje s dalšími funkcemi MCS, jako je server Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Pro optimalizaci zdrojů může komunikovat s Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) za účelem aktivace přenosů eMBMS, čímž zajišťuje, že vysoce prioritní skupinový provoz nezahlcuje síť použitím unicastového doručování pro každého uživatele zvlášť. Jeho návrh upřednostňuje nízkou latenci, vysokou dostupnost a přísnou kontrolu přístupu, což z něj činí základní komponentu pro profesionální a pro mise kritické skupinové komunikace v sítích LTE a 5G.

## K čemu slouží

GCSE byl vytvořen, aby řešil kritickou potřebu efektivních, spolehlivých a okamžitých skupinových komunikačních služeb přes sítě 3GPP, konkrétně pro uživatele z oblasti veřejné bezpečnosti a profesionály. Před jeho standardizací spoléhaly týmy první pomoci a průmyslové týmy na starší systémy pozemní mobilní radiokomunikace ([LMR](/mobilnisite/slovnik/lmr/)), které byly často izolované, úzkopásmové a postrádaly integraci s moderními širokopásmovými datovými službami. Přechod na LTE sliboval vyšší přenosovou kapacitu a bohatší služby, ale postrádal nativní mechanismy pro komunikaci jeden-k-více s nízkou latencí a řízenou mluvčím, která je zásadní pro koordinovanou skupinovou činnost.

Primární problém, který GCSE řeší, je neefektivní využití síťových zdrojů pro skupinová volání. Bez něj by bylo skupinové volání zřízeno jako více současných unicastových relací, což by duplikovalo stejný mediální proud pro každého příjemce a plýtvalo drahocennou kapacitou radiové sítě a jádra sítě. GCSE zavádí architektonický prvek pro správu těchto relací jako jediné logické entity, což umožňuje optimalizační techniky, jako je multicastové/rozhlasové doručování přes eMBMS. Jeho vytvoření v rámci 3GPP Release 12 byl základním krokem v širší iniciativě 'Mission Critical over LTE', jejímž cílem bylo nahradit nebo doplnit tradiční systémy LMR standardizovanými, interoperabilními a funkčně bohatými službami na komerčních mobilních sítích, čímž se umožnilo lepší povědomí o situaci a vyšší provozní efektivita.

## Klíčové vlastnosti

- Řídí zřízení a ukončení relace skupinového volání v rámci IMS
- Implementuje řízení práva k vysílání pro poloduplexní komunikaci typu Push-to-Talk
- Spravuje dynamické členství ve skupině a autorizaci účastníků
- Spolupracuje s eMBMS pro efektivní rozhlasové/multicastové doručování média
- Poskytuje rozhraní pro konfiguraci služby (Ut) a řízení IMS (ISC)
- Podporuje požadavky služeb kritických pro misi na prioritu, přednostní přerušení a kvalitu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 29.468** (Rel-19) — MB2 Reference Point Protocol Definition
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [GCSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/gcse/)
