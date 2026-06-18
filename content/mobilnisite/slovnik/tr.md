---
slug: "tr"
url: "/mobilnisite/slovnik/tr/"
type: "slovnik"
title: "TR – UE delay in receiving direction"
date: 2026-01-01
abbr: "TR"
fullName: "UE delay in receiving direction"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tr/"
summary: "Klíčový parametr kvality služeb (QoS), který měří časové zpoždění, jemuž jsou vystaveny datové pakety putující od sítě k uživatelskému zařízení (UE). Je zásadní pro hodnocení a zajištění výkonu služeb"
---

TR je zpoždění směrem k uživatelskému zařízení (UE delay in receiving direction), parametr kvality služeb (QoS), který měří časové zpoždění datových paketů na cestě od sítě k uživatelskému zařízení.

## Popis

TR, formálně definované jako 'zpoždění směrem k uživatelskému zařízení (UE delay in receiving direction)', je základní metrika výkonnosti kvality služeb (QoS) standardizovaná v řadě technických specifikací 3GPP. Kvantifikuje zpoždění přenosu paketů konkrétně ve směru downlink – od aplikačního serveru v síti (nebo referenčního bodu uvnitř core sítě) k uživatelskému zařízení (UE). Toto zpoždění je měření end-to-end, zahrnující veškeré zpracování, fronty, přenos a šíření latencí, které paket získá při průchodu core sítí, rádiovou přístupovou sítí (RAN) a vzdušným rozhraním, než je úspěšně doručen do aplikační vrstvy UE. Měření je typicky definováno pro konkrétní QoS Flow nebo bearer, což odráží výkonnost konkrétního datového proudu služby.

Metodika měření TR je pečlivě definována pro zajištění konzistence. Zahrnuje časové označení paketů na definovaném měřicím bodě, často na vstupu do core sítě (např. na User Plane Function – [UPF](/mobilnisite/slovnik/upf/)) nebo na koncovém bodě služby. Odpovídající časové razítko nebo potvrzení je zaznamenáno, když paket úspěšně přijme a zpracuje cílová aplikace na UE. Rozdíl mezi těmito časovými razítky dává hodnotu TR. V praxi se často měří statisticky, s reportováním hodnot jako 95. nebo 99. percentil zpoždění, aby se charakterizovala latence v nejhorším případě, kterou zažívá většina paketů – to je pro záruky služeb relevantnější než průměrné zpoždění. Tato měření mohou sbírat UE nebo síťové elementy a reportovat je systémům řízení, jako je Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) nebo systémy Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), pro sledování výkonnosti a její zajištění.

TR hraje ústřední roli v architektuře QoS 3GPP. Je přímo spojeno s hodnotami QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) a 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)), které definují standardizované chování při přeposílání paketů. Například hodnota 5QI pro služby Ultra-Reliable Low-Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)) bude mít přísný přidružený požadavek na TR (např. maximum několika milisekund). Síť tyto požadavky využívá pro rozhodování o řízení zdrojů. Plánovač RAN, který zná QoS profil bearu, může upřednostnit pakety patřící tokům s těsnými omezeními TR, přidělit jim okamžité rádiové zdroje, použít kratší přenosové časové intervaly ([TTI](/mobilnisite/slovnik/tti/)) nebo využít robustnější modulační a kódovací schémata ke snížení retransmisí. TR tedy není jen měření, ale cíl na úrovni služby, který řídí přidělování rádiových a síťových zdrojů v reálném čase, aby byla zajištěna uživatelská zkušenost pro aplikace kritické na zpoždění.

## K čemu slouží

Koncept a přesná definice zpoždění směrem k uživatelskému zařízení (UE delay in receiving direction, TR) byly nedílnou součástí standardů 3GPP již od prvních release, aby řešily základní výzvu řízení a zajištění kvality služeb v paketově orientovaných sítích. Když se mobilní sítě vyvíjely od přepojování okruhů pro hlas (kde bylo zpoždění inherentně řízeno) k plně IP sítím přenášejícím různé služby, standardizovaný způsob kvantifikace a specifikace zpoždění se stal nezbytným. Různé aplikace mají velmi rozdílnou toleranci k latenci; interaktivní hlas a video vyžadují nízké zpoždění, zatímco e-mail nebo stahování souborů jsou méně citlivé. Bez standardizované metriky jako TR by bylo nemožné definovat jasné smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), navrhovat efektivní QoS mechanismy nebo objektivně porovnávat výkon sítě.

Její průběžný vývoj v každém release 3GPP podtrhuje její klíčový význam. Každá nová generace technologie (3G, 4G, 5G) a nová kategorie služeb (např. MBB, MTC, URLLC) přinesla přísnější a rozmanitější požadavky na zpoždění. TR poskytuje společný měřicí standard. Pro 4G LTE byla klíčová pro definici QoS pro Voice over LTE (VoLTE). Pro 5G je naprosto zásadní pro umožnění služeb kritických pro misi, jako je automatizace továren, vzdálená chirurgie a řízení autonomních vozidel, kde zpoždění na úrovni milisekund je nepřijatelné. Účelem TR je tedy převést abstraktní požadavky služeb ('nízká latence') na konkrétní, měřitelné technické parametry, které mohou být zakomponovány do síťové architektury, použity pro ověření výkonnosti a vynucovány mechanismy řízení QoS, čímž je zajištěno, že síť může dostát svým slibům pro stávající i budoucí aplikace citlivé na latenci.

## Klíčové vlastnosti

- Měří end-to-end zpoždění paketů ve směru od sítě k UE (downlink)
- Jádrový parametr spojený s identifikátory třídy QoS (QCI/5QI) pro diferenciaci služeb
- Podporuje statistické reportování (např. 95. percentil) pro charakterizaci výkonnosti
- Řídí rozhodování o plánování zdrojů v RAN v reálném čase pro toky kritické na latenci
- Nezbytný pro ověřování smluv o úrovni služeb (SLA) a zajištění výkonnosti sítě
- Základní metrika pro umožnění služeb Ultra-Reliable Low-Latency Communication (URLLC)

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [TR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tr/)
