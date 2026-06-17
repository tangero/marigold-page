---
slug: "hlr"
url: "/mobilnisite/slovnik/hlr/"
type: "slovnik"
title: "HLR – Home Location Register"
date: 2026-01-01
abbr: "HLR"
fullName: "Home Location Register"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hlr/"
summary: "Centrální databáze v 2G (GSM) a 3G (UMTS) sítích s přepojováním okruhů, která ukládá trvalá data účastníka a informace o jeho poloze. Je to klíčová komponenta pro správu mobility, autentizaci a směrov"
---

HLR je centrální databáze v 2G a 3G sítích s přepojováním okruhů, která ukládá trvalá data účastníka a informace o poloze pro správu mobility, autentizaci a směrování hovorů.

## Popis

Home Location Register (HLR) je základní, centralizovaná databáze v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) sítí GSM a UMTS. Je to primární úložiště všech trvalých informací o účastníkovi a jeho servisních profilů. Každý účastník v síti má v HLR přiřazený jedinečný záznam klíčovaný jeho mezinárodním identifikátorem mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)). Uložená data zahrnují IMSI, mezinárodní číslo účastníka mobilní stanice ([MSISDN](/mobilnisite/slovnik/msisdn/)), objednané služby (např. přesměrování hovoru, zákazy, doplňkové služby), autentizační informace (např. autentizační triplet: RAND, SRES, Kc) a aktuální polohu účastníka na úrovni Visitor Location Register (VLR) nebo SGSN (pro [GPRS](/mobilnisite/slovnik/gprs/)/UMTS). HLR není zapojen do přenosové cesty hlasového hovoru nebo SMS v reálném čase, ale je dotazován jinými síťovými elementy pro získání klíčových dat pro směrování a informací o předplatném.

Z architektonického hlediska HLR komunikuje s několika uzly jádra sítě prostřednictvím signalizace SS7 (Signaling System No. 7) v 2G/3G, často za použití protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)). Mezi klíčová rozhraní patří rozhraní HLR-VLR (rozhraní D), kde HLR aktualizuje VLR daty účastníka, když účastník vstoupí do jeho oblasti, a přijímá aktualizace polohy. HLR také komunikuje s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro směrování hovorů a s Authentication Center (AuC), které je často integrováno s HLR, pro získání autentizačních vektorů. Když dorazí mobilně-terminovaný hovor, Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje HLR pomocí MAP operace Send Routing Information (SRI). HLR následně dotazuje aktuální VLR pro dočasné směrovací číslo zvané Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)), které je pak vráceno GMSC, aby směroval hovor ke správnému MSC/VLR obsluhujícímu účastníka.

Při vývoji směrem k 4G LTE a 5G jsou funkce HLR (a AuC) převzaty Home Subscriber Server (HSS) v IP Multimedia Subsystem (IMS) a Packet Core. Pro legacy 2G/3G CS služby však HLR zůstává v provozu, často integrován s HSS v kombinovaném uzlu HLR/HSS. Jeho role je naprosto klíčová pro mobilitu: sleduje přibližnou polohu účastníka (adresu VLR/SGSN), jak se pohybuje, což síti umožňuje správně směrovat hovory a zprávy. Také slouží jako autoritativní zdroj pro určení, jaké služby je účastníkovi povoleno používat, a vynucuje kontrolu na základě předplatného.

## K čemu slouží

HLR byl vytvořen, aby vyřešil základní problém mobility účastníka a přenositelnosti služeb v raných digitálních celulárních sítích (GSM). Předchozí celulární systémy měly omezené nebo těžkopádné mechanismy pro zvládání roamingu. HLR jako centralizovaná, inteligentní databáze poskytl škálovatelné řešení. Odděluje trvalou identitu a profil účastníka od jeho dočasné fyzické polohy. To umožňuje účastníkovi pohybovat se kdekoli v rámci pokrytí sítě (a dokonce do sítí jiných operátorů prostřednictvím roamingových dohod), zatímco síť ho může vždy lokalizovat, aby mu poskytla služby.

Historický kontext představuje jasné oddělení domácí sítě (kde sídlí HLR) a navštívené sítě (kde sídlí VLR) v architektuře GSM. Tento model umožnil globální roaming. HLR řeší problémy: 1) **Směrování hovorů**: Určení aktuální obsluhující ústředny pro příchozí hovor bez vysílání dotazů po celé síti. 2) **Autentizace**: Poskytnutí přihlašovacích údajů navštívené síti pro bezpečné ověření identity účastníka. 3) **Konzistence služeb**: Zajištění, že personalizované služby účastníka (jako přesměrování hovoru) fungují konzistentně bez ohledu na polohu. Před existencí takového centralizovaného úložiště by bylo implementování těchto funkcí napříč velkou, distribuovanou sítí vysoce komplexní a neefektivní. HLR spolu s VLR vytvořil vzor pro správu mobility, který se později vyvinul do více IP-centrických modelů v 4G/5G.

## Klíčové vlastnosti

- Centralizované trvalé úložiště identity účastníka (IMSI), čísla (MSISDN) a servisního profilu
- Udržuje dynamické informace o poloze účastníka (aktuální adresa VLR/SGSN)
- Generuje a ukládá autentizační data (integrováno s nebo připojeno k AuC)
- Poskytuje klíčové informace pro směrování mobilně-terminovaných hovorů a SMS prostřednictvím získání MSRN
- Spravuje poskytování služeb a zákazy na základě předplatného
- Komunikuje se síťovými elementy (MSC, VLR, GMSC, SGSN) pomocí MAP přes signalizaci SS7

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- … a dalších 45 specifikací

---

📖 **Anglický originál a plná specifikace:** [HLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hlr/)
