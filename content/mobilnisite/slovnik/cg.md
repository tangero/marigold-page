---
slug: "cg"
url: "/mobilnisite/slovnik/cg/"
type: "slovnik"
title: "CG – Charging Gateway"
date: 2025-01-01
abbr: "CG"
fullName: "Charging Gateway"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cg/"
summary: "Charging Gateway (CG) je síťová funkce, která shromažďuje, zpracovává a přeposílá účtovací data ze síťových prvků, jako je P-GW nebo SMF, do fakturačního systému. Funguje jako prostředník a zajišťuje"
---

CG je síťová funkce, která shromažďuje, zpracovává a přeposílá účtovací data ze síťových prvků do fakturačního systému, přičemž funguje jako prostředník pro spolehlivý přenos záznamů o využití.

## Popis

Charging Gateway (CG) je klíčová komponenta v rámci účtovací architektury 3GPP, konkrétně definovaná jako součást Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). Její primární role spočívá v tom, že funguje jako sběrný a přeposílací bod pro Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) session. Síťové prvky generující účtovací informace, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) ve 3G, Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v 4G nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G, jsou známé jako Charging Trigger Functions ([CTF](/mobilnisite/slovnik/ctf/)). Tyto CTF odesílají účtovací události na CG pomocí referenčního bodu Ga, který je založen na základním protokolu Diameter s aplikací 3GPP Charging Data (Charging Data, 32.299).

Architektonicky se CG nachází mezi CTF v síti a centrální fakturační doménou neboli Billing System ([BS](/mobilnisite/slovnik/bs/)). Přijímá CDR z více CTF a provádí jejich počáteční zpracování, dočasné uložení a konsolidaci. Klíčovou technickou funkcí je korelace částečných CDR, které patří ke stejné servisní session, ale mohly být vygenerovány různými síťovými uzly nebo v různých časech. CG zajišťuje integritu a správné pořadí těchto záznamů před jejich hromadným přeposláním do Billing Domain přes rozhraní Bx. Rozhraní Bx typicky používá protokol pro přenos souborů, jako je FTP nebo SFTP, a přenáší soubory formátované podle 3GPP TS 32.297 (Charging Data Record (CDR) file format and transfer).

Interně se CG skládá z několika logických funkcí. Zahrnuje Diameter stack pro komunikaci přes rozhraní Ga, CDR processing engine pro validaci a korelaci, spolehlivý subsystém úložiště pro uchování CDR před přenosem (často s redundancí) a modul pro generování souborů pro vytvoření finálních přenosových souborů. Také řeší chybové scénáře, jako je retransmise ztracených CDR nebo oznámení o selhání CTF. Její provoz se řídí účtovacími charakteristikami a profily, které určují, jak mají být záznamy zpracovány pro různé účastníky nebo služby.

V širší 5G Service-Based Architecture (SBA), přestože je tradiční CG stále definována jako samostatný síťový prvek, mohou být podobné funkce integrovány v rámci Charging Function (CHF) jako součást Converged Charging System (CCS). CG však zůstává klíčová v nasazeních, kde je vyžadováno jasné oddělení mezi real-time síťovými funkcemi a offline, hromadně orientovanými fakturačními systémy. Poskytuje buffer, který absorbuje špičky v generování účtovacích dat, a zajišťuje, že přechodné problémy ve fakturační doméně neovlivní schopnost jádra sítě generovat účtovací události, čímž zachovává jak výkon sítě, tak přesnost fakturace.

## K čemu slouží

Charging Gateway byla vytvořena k řešení základní obchodní potřeby spolehlivého a přesného účtování služeb účastníkům v paketově přepínaných mobilních sítích. Jak se služby vyvíjely od jednoduchých hlasových hovorů k zahrnutí GPRS, IMS a komplexních datových služeb, objem a složitost účtovacích dat explodovaly. Síťové prvky jako GGSN nebyly navrženy pro přímé, spolehlivé připojení k potenciálně vzdáleným a heterogenním fakturačním systémům. Přímé odesílání CDR z každého síťového uzlu představovalo významná rizika: mohlo přetížit fakturační systém, způsobit ztrátu dat při síťové kongesci a vyžadovalo, aby každý uzel implementoval složitou logiku přenosu souborů a ošetření chyb, což zvyšovalo jeho náklady a složitost.

Historicky, před standardizací CG, operátoři čelili výzvám při konsolidaci účtovacích dat z četných síťových prvků. To vedlo k nespolehlivému přenosu dat, nepřesnostem v účtování a únikům příjmů. CG, zavedená ve 3GPP Release 8 jako součást vyspělého offline účtovacího rámce, to vyřešila tím, že fungovala jako vyhrazená mediční vrstva. Odděluje fakturační systém od sítě, umožňuje CTF používat jednoduchý real-time protokol Diameter (Ga) pro zasílání záznamů, zatímco CG přebírá odpovědnost za spolehlivý, hromadný přenos do fakturační domény pomocí robustních mechanismů založených na souborech. Toto oddělení zájmů zlepšuje škálovatelnost a provozní efektivitu.

CG navíc umožňuje kritické funkce, jako je korelace CDR a předzpracování, které jsou nezbytné pro služby zahrnující více síťových komponent (např. videohovor využívající jak přístupové, tak IMS zdroje). Provedením těchto funkcí centrálně snižuje procesní zátěž jednotlivých CTF a zajišťuje konzistentní, jednotný pohled na session účastníka pro účely fakturace. Jejím vytvořením byla motivována potřeba standardizovaného, operátorské úrovně řešení pro zajištění ochrany příjmů, jak se mobilní sítě staly primární platformou pro digitální služby.

## Klíčové vlastnosti

- Sbírání CDR přes rozhraní Ga pomocí protokolu Diameter
- Spolehlivé ukládání a přeposílání účtovacích záznamů do fakturačního systému
- Korelace a konsolidace CDR z více síťových zdrojů
- Přenos založený na souborech do fakturační domény pomocí rozhraní Bx (např. FTP/SFTP)
- Mechanismy pro ošetření chyb a retransmise při neúspěšném přenosu CDR
- Buffering a vyrovnávání zátěže pro ochranu fakturačních systémů před provozními špičkami

## Definující specifikace

- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.473** (Rel-19) — W1 Application Protocol (W1AP) Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [CG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cg/)
