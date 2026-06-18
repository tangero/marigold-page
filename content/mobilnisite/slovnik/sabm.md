---
slug: "sabm"
url: "/mobilnisite/slovnik/sabm/"
type: "slovnik"
title: "SABM – Set Asynchronous Balanced Mode frame"
date: 2025-01-01
abbr: "SABM"
fullName: "Set Asynchronous Balanced Mode frame"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sabm/"
summary: "Rámec vrstvy 2 v GSM a UMTS používaný k navázání logického spojení v asynchronním vyváženém režimu mezi mobilní stanicí a sítí. Iniciuje zřízení spojové vrstvy pro signalizační komunikaci, což je zákl"
---

SABM je rámec vrstvy 2 v GSM a UMTS používaný k navázání logického spojení v asynchronním vyváženém režimu mezi mobilní stanicí a sítí, čímž iniciuje zřízení datového spoje pro signalizaci.

## Popis

Rámec Set Asynchronous Balanced Mode (SABM) je základní řídicí rámec vrstvy 2 (spojové vrstvy) používaný v rádiových rozhraních GSM a UMTS, konkrétně v protokolu LAPDm odvozeném od [LAPD](/mobilnisite/slovnik/lapd/) z [ISDN](/mobilnisite/slovnik/isdn/). Jeho primární funkcí je navázání logického spojení mezi dvěma rovnocennými entitami – typicky mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BSS](/mobilnisite/slovnik/bss/)) v GSM, nebo mezi UE a [RNC](/mobilnisite/slovnik/rnc/) v UMTS – v asynchronním vyváženém režimu ([ABM](/mobilnisite/slovnik/abm/)). ABM je režim provozu, kde jsou obě stanice považovány za rovnocenné partnery a každá z nich může iniciovat přenos, příkaz nebo odpověď bez předchozího souhlasu druhé. Rámec SABM je příkaz, který spouští navázání tohoto vyváženého, peer-to-peer logického spoje.

V protokolové architektuře je spojová vrstva nad fyzickým rádiovým kanálem zodpovědná za poskytování spolehlivého, sekvenovaného spojení pro přenos signalizačních zpráv. Rámec SABM je klíčovou součástí procedury zřizování spoje. Vysílá ho iniciující entita (často síťová strana pro mobilně ukončenou transakci nebo mobil pro mobilně iniciovanou) na vyhrazeném signalizačním kanálu, jako je Standalone Dedicated Control Channel ([SDCCH](/mobilnisite/slovnik/sdcch/)) nebo hlavní [DCCH](/mobilnisite/slovnik/dcch/) v GSM/UMTS. Rámec obsahuje předdefinovaný identifikátor řídicího pole pro SABM a zahrnuje informační pole, které nese první signalizační zprávu vrstvy 3 (např. CM Service Request nebo Paging Response), jež má být přenesena po navázání spoje. Toto přenášení zvyšuje efektivitu.

Operace je řízena jednoduchým handshake. Odesílatel vysílá příkazový rámec SABM. Po jeho správném přijetí musí příjemce potvrdit navázání logického spoje odesláním rámce Unnumbered Acknowledgment (UA) zpět. Tato výměna resetuje sekvenční čísla (V(S) a V(R)) na obou koncích na nulu, čímž synchronizuje spoj pro následný přenos rámců. Pokud je rámec SABM přijat s chybami, je ignorován. Odesílatel používá časovač (timer T200) a při vypršení časového limitu bez přijetí UA rámec SABM znovu vysílá. Po přijetí UA je logický spoj považován za navázaný a zpráva vrstvy 3 obsažená v rámci SABM je předána vyšší vrstvě ke zpracování. Všechny následující I-rámce (informační rámce) přenášející signalizační zprávy jsou pak přenášeny přes tento navázaný spoj. Handshake SABM/UA je tedy kritickým úvodním krokem pro prakticky všechny signalizační dialogy, včetně zřizování hovoru, přenosu SMS a aktualizace polohy.

## K čemu slouží

Rámec SABM existuje, aby poskytl standardizovanou, spolehlivou metodu pro navázání peer-to-peer logického spojení na spojové vrstvě v digitálních mobilních komunikačních systémech. Před digitální érou měly analogové systémy méně formalizované řízení spoje. Přijetí protokolového zásobníku založeného na ISDN pro GSM si vyžádalo robustní proceduru spojové vrstvy. Účelem SABM je inicializovat spoj ve známém stavu (ABM) se synchronizovanými sekvenčními čísly, což zajišťuje, že následné signalizační zprávy jsou doručovány spolehlivě a ve správném pořadí. Řeší problém, jak spolehlivě zahájit signalizační konverzaci přes nespolehlivý rádiový kanál.

Historická motivace vychází z návrhu GSM, který pro svou signalizaci využil osvědčené protokoly ISDN. Protokol LAPD používaný na pevných rozhraních Abis a A byl pro rádiové rozhraní upraven jako LAPDm. Příkaz SABM byl převzat z této linie. Reaguje na potřebu jasného, jednoznačného začátku signalizační transakce. Bez takového mechanismu by neexistoval způsob, jak zajistit, aby oba konce spoje souhlasily s výchozím bodem pro číslování rámců a stav spoje, což by vedlo ke ztrátě nebo poškození dat. Procedura SABM s její povinnou odpovědí UA vytváří tuto shodu. Její vznik byl hnán požadavkem na spolehlivý, na opravách chyb založený signalizační spoj jako základ pro všechny pokročilé mobilní služby, což z ní dělá základní kámen circuit-switched a rané packet-switched signalizace GSM a UMTS.

## Klíčové vlastnosti

- Řídicí příkaz vrstvy 2 používaný k navázání logického spoje v asynchronním vyváženém režimu (ABM)
- Iniciuje peer-to-peer spoj, kde kterákoli stanice může vysílat bez dotazování
- Pro efektivitu nese první signalizační zprávu vrstvy 3 ve svém informačním poli
- Pro úspěšné navázání vyžaduje rámec Unnumbered Acknowledgment (UA)
- Resetuje proměnné sekvenčních čísel pro odesílání a příjem (V(S), V(R)) na nulu na obou koncích spoje
- Pro spolehlivost přes rádiové rozhraní používá opakovaný přenos založený na časovači (timer T200)

## Související pojmy

- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [SABM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sabm/)
