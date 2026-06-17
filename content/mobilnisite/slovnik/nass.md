---
slug: "nass"
url: "/mobilnisite/slovnik/nass/"
type: "slovnik"
title: "NASS – Network Attachment Subsystem"
date: 2025-01-01
abbr: "NASS"
fullName: "Network Attachment Subsystem"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nass/"
summary: "Network Attachment Subsystem je funkční blok v rámci IP Multimedia Subsystem (IMS), který poskytuje služby registrace na síťové úrovni a správy IP adres. Umožňuje aplikacím v IMS získávat informace o"
---

NASS (Network Attachment Subsystem) je podsystém pro připojení k síti v rámci IP Multimedia Subsystem, který zajišťuje registraci na síťové úrovni a správu IP adres, což umožňuje aplikacím v IMS získávat informace o stavu připojení uživatele a jeho IP konfiguraci.

## Popis

Network Attachment Subsystem (NASS) je soubor funkcí definovaných Evropským institutem pro telekomunikační standardy ([ETSI](/mobilnisite/slovnik/etsi/)) a přijatých v architektuře IP Multimedia Subsystem (IMS) konsorcia 3GPP pro pevný širokopásmový přístup (např. xDSL, optické vlákno). Je specifikován v kontextu sítí nové generace ([NGN](/mobilnisite/slovnik/ngn/)) a poskytuje standardizovaný způsob, jakým se uživatelské zařízení (UE), často označované v pevných sítích jako zařízení v prostoru zákazníka ([CPE](/mobilnisite/slovnik/cpe/)), připojí k IP síti a získá potřebnou konfiguraci pro přístup ke službám, zejména k službám založeným na IMS, jako je Voice over LTE (VoLTE) nebo pevná VoIP. NASS funguje na transportní vrstvě, pod služební vrstvou, kde sídlí IMS, a poskytuje kritické informace o připojení směrem vzhůru.

Hlavní funkcí NASS je řídit počáteční proceduru přístupu k síti. Když se CPE/směrovač zapne, komunikuje s NASS za účelem provedení autentizace (např. pomocí PPP, [DHCP](/mobilnisite/slovnik/dhcp/) nebo 802.1X), autorizace a přidělení IP adresy. Mezi klíčové logické funkce v rámci NASS patří Network Access Configuration Function (NACF), která přiřazuje parametry IP konfigurace UE; Access Management Function ([AMF](/mobilnisite/slovnik/amf/)), která spravuje přístupovou relaci; a Connectivity Session Location and Repository Function ([CLF](/mobilnisite/slovnik/clf/)), což je centrální databáze. CLF ukládá vazbu mezi fyzickým identifikátorem uživatelské linky (např. port DSLAMu), přiřazenou IP adresou a uživatelským profilem. Tato vazba je klíčová pro poskytnutí lokalizačních informací pro tísňové služby.

NASS komunikuje s jádrem IMS přes referenční body `e2` a `e4`. Nejdůležitější interakce probíhá mezi CLF v rámci NASS a funkcí Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) nebo Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)) v jádru IMS. Když je spuštěna aplikace v IMS, například tísňové volání, může P-CSCF nebo E-CSCF dotazovat CLF (přes rozhraní `e2`), aby na základě zdrojové IP adresy SIP signalizace získala informace o umístění účastníka v přístupové síti. To umožňuje síti IMS určit správné místo příjmu tísňových volání (PSAP), kam má tísňové volání směrovat, a to i v případě, že je uživatel nomádský (používá pevnou linku z různých fyzických zásuvek).

Dále NASS umožňuje scénáře přenosu přístupu a kontinuity služeb. Například v kontextu Voice Call Continuity (VCC) nebo Single Radio Voice Call Continuity (SRVCC) zahrnujícího předání mezi pevným a mobilním přístupem může NASS poskytnout informace o charakteristikách pevné přístupové větve aplikačnímu serveru IMS, který předání spravuje. Stručně řečeno, NASS funguje jako 'tmel' mezi fyzickou/transportní vrstvou pevné širokopásmové sítě a služebně-aware vrstvou IMS. Abstrahuje detaily přístupové sítě a poskytuje standardizované rozhraní pro služební vrstvy, aby získaly nezbytný kontext připojení, což je zásadní pro regulované služby jako tísňová volání a pokročilé funkce kontinuity služeb.

## K čemu slouží

Network Attachment Subsystem byl vytvořen k řešení konkrétního problému při konvergenci poskytování služeb v pevných a mobilních sítích, zejména pro služby založené na IMS. V tradiční telefonii (PSTN) fyzický identifikátor linky (telefonní číslo/linka) přímo a neměnně určoval geografickou polohu, což bylo pro směrování tísňových volání jednoduché. S příchodem IP-based pevného širokopásmového přístupu (jako VoIP přes DSL) tento vztah přestal platit. Uživatel mohl získat IP adresu prostřednictvím DHCP ze sítě poskytovatele, ale tato IP adresa nebyla staticky vázána na fyzickou polohu, zvláště pokud uživatel přemístil svůj směrovač (nomadismus). To představovalo velkou výzvu pro tísňové služby, které vyžadují přesné lokalizační informace.

NASS byl vyvinut v rámci standardů NGN ETSI TISPAN, aby znovu zavedl toto povědomí o poloze a připojení do paketových sítí. Jeho vytvoření bylo motivováno potřebou, aby operátoři pevných sítí mohli nabízet VoIP na úrovni operátora a další služby IMS se stejnou spolehlivostí a regulovanou shodou (zejména pro tísňová volání - E112) jako v PSTN. Před NASS architektury IMS primárně předpokládaly mobilní nebo spravovaný přístup, kde se poloha odvozovala z mobilní sítě (např. ID buňky). Pro pevný přístup byl potřebný standardizovaný podsystém, který by prováděl připojení, autentizaci a – což je klíčové – udržoval dynamickou vazbu mezi IP adresou, identitou uživatele a polohou fyzického přístupového bodu.

Poskytnutím standardizované sady funkcí a rozhraní (jako `e2`) umožňuje NASS služební vrstvě IMS zůstat z velké části nezávislou na podkladové technologii pevného přístupu (xDSL, FTTH, kabel). Řeší omezení spočívající v přímé interakci služební logiky s přístupově specifickými protokoly, jako je DHCP nebo PPP. Místo toho se funkce IMS dotazují NASS CLF přes jednotné rozhraní, aby získaly potřebné informace o poloze a charakteristikách přístupu. Toto oddělení zájmů umožňuje operátorům pevných sítí nasadit IMS pro multimediální služby při splnění regulatorních požadavků na lokalizaci tísňového volajícího a usnadňuje vývoj jednotných služeb, které bezproblémově fungují napříč pevnými a mobilními přístupovými sítěmi.

## Klíčové vlastnosti

- Spravuje přidělování IP adres a konfiguraci pro pevný přístup UE/CPE
- Udržuje dynamickou vazební databázi (v CLF) spojující IP adresu, identifikátor linky a uživatelský profil
- Poskytuje lokalizační informace IMS pro směrování tísňových volání (dotaz E-CSCF)
- Podporuje autentizaci a autorizaci uživatele na úrovni síťového připojení
- Umožňuje služby citlivé na přístup a scénáře přenosu přístupu v IMS
- Definuje standardizované referenční body (e2, e4) mezi transportní a IMS vrstvou

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [NASS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nass/)
