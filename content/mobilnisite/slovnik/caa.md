---
slug: "caa"
url: "/mobilnisite/slovnik/caa/"
type: "slovnik"
title: "CAA – Capacity Allocation Acknowledgement"
date: 2025-01-01
abbr: "CAA"
fullName: "Capacity Allocation Acknowledgement"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/caa/"
summary: "Capacity Allocation Acknowledgement (CAA) je protokolová zpráva používaná v sítích 3GPP k potvrzení úspěšného přidělení rádiových prostředků. Jedná se o klíčovou součást protokolů Radio Resource Contr"
---

CAA je protokolová zpráva v sítích 3GPP, která potvrzuje úspěšné přidělení rádiových prostředků a slouží jako klíčová součást protokolů RRC a RLC pro spolehlivý přenos a efektivní využití spektra.

## Popis

Capacity Allocation Acknowledgement (CAA) je řídicí protokolová zpráva nedílně patřící k vrstvám Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a Radio Link Control (RLC) v architekturách 3GPP Universal Mobile Telecommunications System (UMTS) a Long-Term Evolution (LTE). Funguje jako potvrzovací signál odesílaný z uživatelského zařízení (UE) k řadiči rádiové sítě (RNC) v UMTS nebo k eNodeB v LTE, kterým se potvrzuje úspěšný příjem a zpracování zprávy Capacity Allocation ([CA](/mobilnisite/slovnik/ca/)). Samotná zpráva CA uživatelskému zařízení přikazuje konkrétní přidělené rádiové prostředky (jako jsou kódy, časové sloty nebo frekvenční pásma) pro uplinkový nebo downlinkový přenos dat.

Mechanismus CAA je základní součástí procesu dynamického přidělování prostředků. Když se síť rozhodne přiřadit nebo upravit prostředky pro UE – často v důsledku faktorů, jako jsou měnící se podmínky kanálu, požadavky na kvalitu služeb (QoS) nebo události předávání spojení – odešle zprávu CA prostřednictvím vrstvy RRC. Po jejím přijetí entita RRC v UE přidělení zpracuje, odpovídajícím způsobem nakonfiguruje svou fyzickou vrstvu a vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a poté vygeneruje zprávu CAA. Toto potvrzení je přeneseno zpět k síťovému prvku (RNC/eNodeB), aby se potvrdilo, že UE nyní pracuje s novou konfigurací prostředků. Tento handshake zajišťuje synchronizaci obou stran a předchází tak ztrátě dat nebo chybám přenosu, ke kterým by mohlo dojít, pokud by se UE pokusilo používat nepotvrzené prostředky.

Z pohledu zásobníku protokolů jsou zprávy CAA typicky přenášeny v signalizačních rádiových přenosech RRC. Jsou zapouzdřeny a zabezpečeny nižšími vrstvami, včetně Packet Data Convergence Protocol (PDCP) pro ochranu integrity a šifrování a RLC pro spolehlivou segmentaci a doručení. Zařazení CAA zvyšuje robustnost správy rádiových prostředků. Bez takového potvrzení by síť fungovala za předpokladu, že přidělení prostředků je vždy úspěšné, což je na náchylných k chybám rádiových kanálech nespolehlivé. CAA poskytuje kladné potvrzení, což síti umožňuje pokračovat v plánování přenosu dat nebo, pokud potvrzení není přijato v rámci časovače, zahájit obnovovací procedury, jako je opětovné vyslání přidělení nebo spuštění šetření selhání rádiového spoje.

V širším síťovém kontextu CAA přispívá k efektivnímu využití rádiových prostředků a zajištění QoS. Potvrzováním přidělení pomáhá udržovat přesné stavové informace jak v UE, tak v síti, což je klíčové pro řízení přístupu, vyvažování zátěže a koordinaci rušení. Jedná se o režijně nenáročný, ale zásadní prvek protokolu, který podporuje dynamickou a sdílenou povahu buněčného rádiového přístupu, kde jsou prostředky vzácné a musí být rychle přidělovány a získávány zpět mezi mnoha uživateli, aby se maximalizovala kapacita a výkon.

## K čemu slouží

Protokol Capacity Allocation Acknowledgement (CAA) byl zaveden, aby řešil základní výzvu spolehlivého řízení rádiových prostředků v paketově přepínaných buněčných sítích, počínaje 3G UMTS ve verzi Release 99. Předchozí systémy, jako 2G GSM, primárně používaly spojově přepínaná spojení s vyhrazenými, staticky přidělenými časovými sloty, kde bylo přidělování prostředků relativně jednoduché a potvrzení byla méně kritická. S příchodem 3G a jeho podpory vysokorychlostních paketových datových služeb se však rádiové prostředky začaly dynamicky sdílet a přidělovat na základě přerušovaných vzorců provozu. To přineslo významné riziko: pokud byl příkaz k přidělení prostředků odeslaný k UE ztracen nebo poškozen přes rozhraní vzduchu, UE nemuselo přenášet nebo přijímat data správně, což vedlo ke zhoršení služby, plýtvání šířkou pásma a nekonzistencím síťového stavu.

Primárním účelem CAA je poskytnout spolehlivý handshake mechanismus pro přidělování prostředků. Řeší problém nepotvrzených přidělení tím, že zajišťuje, aby síť obdržela kladné potvrzení od UE, než předpokládá, že je přiřazení prostředků aktivní. To je obzvláště důležité v prostředích s proměnlivými rádiovými podmínkami, mobilitou a rušením. Bez CAA by síť mohla plánovat přenos dat pro UE na prostředcích, které UE nepoužívá, což by způsobovalo kolize, ztráty paketů a neefektivní využití vzácného spektra. CAA navíc umožňuje agresivnější a dynamičtější plánovací algoritmy, protože síť může s jistotou přealokovávat prostředky s vědomím, že UE změnu potvrdí, čímž podporuje pokročilé funkce, jako je rychlé plánování, adaptace spoje a správa prostředků s ohledem na QoS, které jsou charakteristické pro systémy 3GPP od UMTS přes LTE až po 5G NR.

## Klíčové vlastnosti

- Poskytuje spolehlivé potvrzení příkazů k přidělení rádiových prostředků
- Zajišťuje synchronizaci stavů prostředků mezi UE a sítí
- Umožňuje robustní dynamické plánování a adaptaci spoje
- Podporuje obnovovací procedury při neúspěšných pokusech o přidělení
- Integruje se s protokoly RRC a RLC pro zabezpečené doručení
- Napomáhá efektivnímu využití spektra a správě QoS

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)

---

📖 **Anglický originál a plná specifikace:** [CAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/caa/)
