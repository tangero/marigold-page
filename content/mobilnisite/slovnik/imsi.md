---
slug: "imsi"
url: "/mobilnisite/slovnik/imsi/"
type: "slovnik"
title: "IMSI – International Mobile Subscriber Identity"
date: 2026-01-01
abbr: "IMSI"
fullName: "International Mobile Subscriber Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/imsi/"
summary: "IMSI je globálně unikátní trvalý identifikátor přiřazený účastníkovi v mobilní síti, uložený na SIM/USIM kartě. Síť jej používá k identifikaci a autentizaci účastníka, získání jeho profilu z HSS a vyt"
---

IMSI je globálně unikátní trvalý identifikátor přiřazený mobilnímu účastníkovi, uložený na SIM/USIM kartě a používaný sítí pro identifikaci, autentizaci a získání profilu účastníka.

## Popis

International Mobile Subscriber Identity (IMSI) je klíčový identifikátor v systémech GSM, UMTS, LTE a 5G. Jedná se o 15místný (nebo kratší) číselný kód trvale asociovaný s účastníkem a uložený v SIM (Subscriber Identity Module) nebo USIM (Universal SIM). Strukturálně se IMSI skládá ze tří částí: Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/), 3 číslice), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/), 2 nebo 3 číslice) a Mobile Subscriber Identification Number ([MSIN](/mobilnisite/slovnik/msin/), 9-10 číslic). MCC a MNC společně identifikují domovskou PLMN (Public Land Mobile Network) účastníka, zatímco MSIN jednoznačně identifikuje účastníka v rámci této sítě.

V síťových operacích se IMSI používá během počátečního připojovacího procesu (initial attach), kdy se mobilní zařízení připojuje k síti. Zařízení odešle IMSI obsluhujícímu síťovému prvku (např. [MME](/mobilnisite/slovnik/mme/) v LTE, [AMF](/mobilnisite/slovnik/amf/) v 5G), který jej následně použije k dotazování na domovskou síťovou [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) nebo ekvivalentní databázi (jako [AUC](/mobilnisite/slovnik/auc/)) pro autentizační vektory a data profilu účastníka. Autentizační proces zahrnuje generování výzvy sítí pomocí tajného klíče (Ki) asociovaného s IMSI. Z důvodu ochrany soukromí se IMSI nepřenáší otevřeně často; místo toho se po počáteční autentizaci používá dočasný identifikátor jako TMSI (Temporary Mobile Subscriber Identity) nebo [GUTI](/mobilnisite/slovnik/guti/) (Globally Unique Temporary Identity), aby se zabránilo vystavení IMSI na rádiovém rozhraní.

Role IMSI přesahuje pouhou identifikaci. Je primárním klíčem pro data účastníka v síťových databázích, spojuje se s detaily předplatného, servisními profily, parametry QoS a bezpečnostními přihlašovacími údaji. V rámci správy mobility pomáhá při aktualizacích lokalizační oblasti a přechodech mezi buňkami. V rámci správy relací se používá ke korelaci záznamů o účtování (CDR) se správným účtem účastníka. Jeho standardizovaný formát umožňuje mezinárodní roaming, neboť navštívená síť může pomocí MCC/MNC identifikovat domovskou síť účastníka a navázat příslušné roamingové dohody a směrování.

## K čemu slouží

IMSI byl vytvořen, aby poskytoval standardizovaný, globálně unikátní a trvalý identifikátor pro mobilní účastníky, řešící problémy identifikace účastníků a roamingu v raných analogových celulárních systémech. Před GSM byly identifikátory často specifické pro konkrétní síť, což bránilo interoperabilitě a mezinárodnímu roamingu. IMSI, zavedený s GSM, umožnil jakékoli síti na světě jednoznačně identifikovat účastníka a kontaktovat jeho domovskou síť pro autentizaci a získání servisního profilu, což umožnilo plynulou globální mobilitu.

Jeho návrh řeší několik klíčových požadavků: unikátnost (zajištěna strukturou MCC/MNC/MSIN), trvalost (vázána na předplatné, nikoli na zařízení) a bezpečnost (bezpečně uložena na SIM). Oddělení identifikátoru domovské sítě (MCC/MNC) od identifikátoru účastníka (MSIN) zjednodušuje směrování signalizačních zpráv pro roamingové účastníky. IMSI je zásadní pro bezpečnostní architekturu celulárních sítí, protože je spojen s tajným autentizačním klíčem účastníka (Ki). Bez robustní, standardizované trvalé identity jako je IMSI by funkce jako zákonné odposlechy, mezinárodní roamingové účtování a správa účastníků byly na globální úrovni extrémně složité nebo nemožné.

## Klíčové vlastnosti

- Globálně unikátní 15místná struktura (MCC+MNC+MSIN)
- Trvale uloženo na SIM/USIM kartě
- Používá se jako primární klíč pro data účastníka v HSS/AuC
- Umožňuje mezinárodní roaming prostřednictvím identifikace MCC/MNC
- Základ pro generování autentizačních vektorů (RAND, SRES, CK, IK)
- Mapováno na dočasné identifikátory (TMSI, GUTI) pro ochranu soukromí na rádiovém rozhraní

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.815** (Rel-5) — IMS Charging Implications
- … a dalších 62 specifikací

---

📖 **Anglický originál a plná specifikace:** [IMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/imsi/)
