---
slug: "up"
url: "/mobilnisite/slovnik/up/"
type: "slovnik"
title: "UP – IP User Plane Integrity Protection"
date: 2026-01-01
abbr: "UP"
fullName: "IP User Plane Integrity Protection"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/up/"
summary: "UP je bezpečnostní mechanismus, který zajišťuje integritu paketů uživatelských dat v sítích 3GPP. Chrání proti neoprávněné modifikaci, vložení nebo smazání dat během přenosu mezi UE a sítí. To je klíč"
---

UP (User Plane Integrity Protection) je bezpečnostní mechanismus, který zajišťuje integritu paketů uživatelských dat v sítích 3GPP tím, že je chrání proti neoprávněné modifikaci během přenosu.

## Popis

IP User Plane Integrity Protection (UP) je kryptografická bezpečnostní funkce navržená k zajištění integrity uživatelského datového provozu. Funguje tak, že generuje a ověřuje kontrolní součty integrity, známé jako Message Authentication Codes ([MAC](/mobilnisite/slovnik/mac/)), pro IP pakety procházející uživatelskou rovinou. Proces zahrnuje bezpečnostní algoritmus a tajný integritní klíč sdílený mezi uživatelským zařízením (UE) a síťovým uzlem, který ochranu ukončuje, typicky gNB v 5G nebo [eNB](/mobilnisite/slovnik/enb/) v 4G. Pro každý odchozí paket odesílatel vypočítá MAC nad datovou částí paketu a určitými poli hlavičky a tento MAC k paketu připojí. Příjemce nezávisle vypočítá očekávaný MAC pomocí stejného algoritmu a klíče; pokud se vypočítaný MAC shoduje s přijatým, je integrita paketu ověřena. Pokud ne, je paket zahozen, čímž se zabrání zpracování poškozených nebo pozměněných dat.

Architektura pro UP je integrována ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) jak v LTE, tak v NR rádiových přístupových sítích. Entita PDCP je zodpovědná za aplikaci šifrování a, pokud je nakonfigurováno, i integrity pro uživatelskou rovinu. Rozhodnutí o aktivaci UP řídí síť prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) na základě politiky, profilu účastníka a citlivosti datové služby. Použitý integritní klíč je odvozen jako součást procedury 3GPP Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), což zajišťuje jeho jedinečnost pro danou relaci a bezpečné navázání.

Úlohou UP je poskytovat ochranu integrity na koncové spojení pro datový spoj mezi UE a rádiovou přístupovou sítí, čímž chrání proti útokům přes vzdušné rozhraní, jako je vkládání, opakování nebo manipulace paketů ze strany útočníka. Obvykle neposkytuje ochranu integrity pro celou koncovou cestu k aplikačnímu serveru, protože to je zodpovědnost protokolů vyšších vrstev, jako je [TLS](/mobilnisite/slovnik/tls/) nebo [IPsec](/mobilnisite/slovnik/ipsec/). Avšak uvnitř hranice důvěry 3GPP představuje UP základní obrannou vrstvu, která zvyšuje celkovou bezpečnostní úroveň pro služby jako finanční transakce, průmyslové řízení nebo kritické komunikace, kde je autenticita dat prvořadá.

## K čemu slouží

UP bylo zavedeno, aby řešilo rostoucí potřebu robustní bezpečnosti v mobilních datových službách nad rámec tradiční ochrany důvěrnosti. Rané standardy 3GPP se primárně zaměřovaly na šifrování uživatelských dat pro zajištění soukromí, ale nevyžadovaly ochranu integrity pro uživatelskou rovinu, což ji činilo zranitelnou vůči útokům na manipulaci s daty. Jak mobilní sítě začaly přenášet citlivý provoz, jako je mobilní bankovnictví, přístup k podnikovým [VPN](/mobilnisite/slovnik/vpn/) nebo řídicí příkazy pro IoT, riziko neodhaleného pozměňování dat se stalo významným problémem. Ochrana integrity zajišťuje, že přijatá data jsou přesně ta, která byla odeslána, což je kritický požadavek pro důvěru v digitální služby.

Motivace pro specifikaci UP vycházela z analýz hrozeb, které identifikovaly, že útočník s přístupem k rádiovému rozhraní může neodhaleně měnit pakety uživatelských dat, což by mohlo vést k podvodům, narušení služeb nebo bezpečnostním problémům. Například v nezabezpečeném scénáři by útočník mohl upravit částky transakcí ve finančních datech nebo odeslat falešné příkazy k IoT zařízení. UP to řeší tím, že poskytuje mechanismus pro detekci jakékoli modifikace, čímž zajišťuje autenticitu dat a nepopiratelnost v rámci segmentu rádiového přístupu. Jeho vytvoření bylo součástí širšího úsilí 3GPP o posílení bezpečnostní architektury napříč releasy, v souladu s regulatorními a průmyslovými požadavky na bezpečnější telekomunikační infrastrukturu.

Zpočátku volitelná, adopce a význam UP rostly s každou generací, zejména v 5G, kde je klíčovou funkcí pro umožnění služeb rozšířeného mobilního širokopásmového přístupu (eMBB), ultra-spolehlivé komunikace s nízkou latencí (URLLC) a masivního IoT. Řeší omezení předchozích přístupů, které se spoléhaly pouze na bezpečnost na aplikační vrstvě nebo obranu na síťovém perimetru, což nemusí chránit zranitelné rádiové spojení. Integrací integrity na vrstvě PDCP poskytuje UP standardizovaný, efektivní a vynutitelný bezpečnostní základ pro veškerý provoz v uživatelské rovině.

## Klíčové vlastnosti

- Ochrana integrity pro IP pakety uživatelské roviny na vrstvě PDCP
- Pro detekci manipulace využívá Message Authentication Codes (MAC)
- Odvození klíče založené na 3GPP AKA pro bezpečné relací klíče
- Aktivace řízená sítí prostřednictvím signalizace RRC na základě politiky
- Ochrana proti útokům vkládání, opakování a modifikace paketů
- Standardizované bezpečnostní algoritmy (např. 128-bit SNOW 3G, AES, ZUC)

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.714** (Rel-14) — Study on CP-UP separation in EPC
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TS 28.531** (Rel-20) — Management and Orchestration
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [UP na 3GPP Explorer](https://3gpp-explorer.com/glossary/up/)
