---
slug: "hrw"
url: "/mobilnisite/slovnik/hrw/"
type: "slovnik"
title: "HRW – Highest Received PDCP SN on WLAN"
date: 2025-01-01
abbr: "HRW"
fullName: "Highest Received PDCP SN on WLAN"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hrw/"
summary: "HRW je proměnná čísla sekvence PDCP používaná v agregaci LTE-WLAN (LWA) pro sledování nejvyššího čísla sekvence PDCP úspěšně přijatého přes WLAN spojení. Zajišťuje doručování ve správném pořadí a dete"
---

HRW je nejvyšší číslo sekvence PDCP úspěšně přijaté přes WLAN spojení v agregaci LTE-WLAN (LWA), používané pro zajištění doručování ve správném pořadí a detekci duplicit.

## Popis

Nejvyšší přijaté číslo sekvence PDCP na WLAN (HRW) je specifická proměnná udržovaná v rámci entity Protokolu konvergence paketových dat (PDCP) v uživatelském zařízení (UE), když je UE nakonfigurováno pro agregaci LTE-WLAN ([LWA](/mobilnisite/slovnik/lwa/)). LWA je funkce zavedená ve 3GPP Release 13, která umožňuje současné využití rádiových prostředků LTE a WLAN pro jeden datový bearer za účelem zvýšení propustnosti pro uživatele a efektivity sítě. Vrstva PDCP je bodem agregace, kde jsou data z jádra sítě rozdělena pro přenos přes rozhraní LTE-Uu (přes [eNB](/mobilnisite/slovnik/enb/)) a/nebo přes WLAN spojení (přes WT - WLAN Termination).

V downlinku může eNB (nebo WT, v závislosti na architektuře LWA) směrovat PDCP protokolové datové jednotky (PDU) k UE přes LTE cestu nebo přes WLAN cestu. UE přijímá tyto PDU na dvou nezávislých rádiových spojích. Entita PDCP v UE je zodpovědná za opětovné sestavení datového proudu ve správném pořadí před jeho doručením do vyšších vrstev (RLC). Pro provedení tohoto přeřazení a vyhnutí se zpracování duplicitních paketů udržuje entita PDCP několik stavových proměnných, včetně HRW.

Konkrétně proměnná HRW uchovává nejvyšší číslo sekvence (SN) PDCP ze všech PDCP PDU, které byly úspěšně přijaty a zpracovány z WLAN spojení. Tato proměnná je porovnávána s SN příchozích PDU z LTE spojení. Když je PDU přijato přes LTE, jeho SN je zkontrolováno vůči HRW. Pokud je SN LTE PDU menší nebo rovno HRW, znamená to, že PDU s tímto SN (nebo vyšším) již bylo přijato přes WLAN a LTE PDU může být považováno za duplicitní a zahozeno, v závislosti na konkrétním algoritmu přeřazení a detekce duplicit. Tím se zabrání tomu, aby vyšší vrstvy přijaly stejný datový paket dvakrát.

Udržování HRW je nedílnou součástí funkce přeřazení PDCP v LWA. Bez ní by UE nebylo schopno správně seřadit pakety přicházející ze dvou heterogenních spojení s potenciálně různou latencí a charakteristikami ztrát. Proměnná je aktualizována vždy, když je nové PDCP PDU doručeno z nižších vrstev asociovaných s WLAN bearerem (tj. z WLAN adaptéru do entity PDCP). Její hodnota monotónně roste, jak jsou přijímána vyšší SN. Tento mechanismus zajišťuje spolehlivost a bezproblémovost agregovaného spojení, čímž je duální konektivita transparentní pro aplikační vrstvu.

## K čemu slouží

HRW bylo vytvořeno k řešení zásadní výzvy agregace dat přes dvě rozdílné rádiové přístupové technologie: LTE a WLAN. Před [LWA](/mobilnisite/slovnik/lwa/) fungovaly LTE a WLAN nezávisle, což často vedlo k neefektivnímu využití dostupných rádiových prostředků. UE mohlo být připojeno k oběma, ale nemohlo kombinovat jejich kapacity pro jeden datový tok. LWA bylo zavedeno, aby využilo všudypřítomnost a vysokou kapacitu WLAN k odlehčení a zvýšení výkonu LTE.

Základním technickým problémem v agregaci je zachování integrity dat – konkrétně zajištění doručování ve správném pořadí a eliminace duplicit, když pakety pro jeden logický kanál mohou využívat dvě různé fyzické cesty s nezávislými profily ztrát a zpoždění. Vrstva PDCP, jakožto společný koncový bod před rozdělením dat v downlinku (nebo po jejich sloučení v uplinku), je přirozeným místem pro tuto koordinaci. HRW jako součást stavového stroje PDCP poskytuje nezbytnou paměť toho, co bylo přijato na WLAN větvi, což umožňuje entitě PDCP činit inteligentní rozhodnutí o paketech přicházejících na LTE větvi.

Tento mechanismus řeší omezení jednodušších agregačních nebo odlehčovacích technik, které mohou fungovat na IP vrstvě (např. MP-TCP), nejsou rádiově-aware a mohou být méně efektivní. Integrací řízení na vrstvě PDCP zajistilo 3GPP těsné propojení s řízením rádiového spoje, zpracováním QoS a bezpečnostními procedurami systému LTE, čímž poskytlo řešení agregace na úrovni operátora. HRW je klíčovým prvkem, který umožňuje síti dynamicky a bezproblémově rozdělovat data mezi LTE a WLAN na základě reálných rádiových podmínek bez kompromisů v kvalitě služby.

## Klíčové vlastnosti

- Sleduje nejvyšší číslo sekvence PDCP úspěšně přijaté přes WLAN spojení v LWA.
- Umožňuje doručování PDCP PDU do vyšších vrstev (RLC) ve správném pořadí, když data přicházejí ze dvou spojení.
- Umožňuje detekci duplicit pro PDU přijatá přes LTE spojení poté, co bylo stejné nebo vyšší SN přijato přes WLAN.
- Udržována jako stavová proměnná v rámci entity PDCP v UE pro každý bearer nakonfigurovaný pro LWA.
- Nezbytná pro funkci přeřazení PDCP v scénářích agregace heterogenních sítí.
- Monotónně roste, jak jsou z nižších vrstev WLAN doručována PDU s vyššími čísly sekvence.

## Definující specifikace

- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [HRW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrw/)
