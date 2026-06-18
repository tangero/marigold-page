---
slug: "brid"
url: "/mobilnisite/slovnik/brid/"
type: "slovnik"
title: "BRID – Broadcast Remote Identification"
date: 2026-01-01
abbr: "BRID"
fullName: "Broadcast Remote Identification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/brid/"
summary: "BRID je služba dle standardů 3GPP, která umožňuje bezpilotním systémům (UAS) vysílat identifikační a polohové údaje pro účely bezpečnosti a regulatorní compliance. Umožňuje oprávněným subjektům vzdále"
---

BRID je služba dle standardů 3GPP, která umožňuje bezpilotním systémům (UAS) vysílat identifikační a polohové údaje pro účely bezpečnosti, splnění regulatorních požadavků a dálkové identifikace oprávněnými subjekty.

## Popis

Broadcast Remote Identification (BRID) je standardizovaná služba v sítích 3GPP navržená pro poskytování identifikace a sledování bezpilotních systémů ([UAS](/mobilnisite/slovnik/uas/)), běžně známých jako drony, v reálném čase. Služba funguje tak, že UAS vysílá sadu identifikačních a polohových parametrů, které mohou být přijaty oprávněnými pozorovateli, síťovými entitami nebo jinými UAS v dosahu. Tento vysílací mechanismus se liší od síťové identifikace, protože pro příjem informací blízkými stranami se nespoléhá na aktivní připojení k mobilní síti, i když může síť využívat pro další služby UAS.

Z architektonického hlediska BRID využívá stávajících schopností uživatelského zařízení (UE) 3GPP, přičemž samotný UAS funguje jako UE. Mezi klíčové funkční komponenty patří UAS, který generuje a vysílá zprávu BRID, a pozorovatel, který ji přijímá a zpracovává. Aplikační vrstva UAS formátuje zprávu BRID obsahující povinné a volitelné prvky. Tato zpráva je následně předána protokolovým zásobníkem k vysílání. Konkrétní rádiová technologie použitá pro vysílání (např. LTE sidelink, NR sidelink nebo jiné metody přímé komunikace) je definována v příslušných specifikacích rádiového přístupového síťového rozhraní (RAN) (např. 36.331, 38.331). Vysílání obvykle probíhá na vyhrazených frekvencích nebo prostředcích, aby se zabránilo rušení jiné mobilní komunikace.

Samotná zpráva BRID je strukturovaná datová sada definovaná ve specifikacích jádra sítě (např. 24.577, 24.578). Mezi povinné informace patří identifikátor UAS (kterým může být sériové číslo nebo ID relace), poloha/výška UAS a časové razítko. Mezi volitelné informace může patřit poloha operátora UAS (dálkového pilota), rychlost UAS, stav nouze a informace o trase. Bezpečnost je prvořadá a je řešena ve specifikacích jako 33.256, které definují mechanismy pro zajištění pravosti a integrity vysílaných zpráv, aby se zabránilo podvržení.

Úloha BRID v síti spočívá v umožnění správy provozu UAS ([UTM](/mobilnisite/slovnik/utm/)) a dodržování regulatorních požadavků. Poskytuje základní vrstvu pro 'elektronické identifikační tabulky' dronů. Přestože funguje prostřednictvím vysílacího mechanismu, je integrována do širšího rámce UAS 3GPP definovaného ve specifikacích jako 23.256 a 23.754. Tento rámec zahrnuje síťovou identifikaci, komunikaci pro řízení a řízení letu ([C2](/mobilnisite/slovnik/c2/)) a autorizaci služeb UAS. BRID konkrétně řeší požadavek na identifikaci v přímé viditelnosti a bezprostřední blízkosti, který vyžadují letecké úřady po celém světě, a doplňuje tak síťové sledování, které se používá pro operace za hranicí přímé viditelnosti ([BVLOS](/mobilnisite/slovnik/bvlos/)) a správu flotily poskytovateli služeb.

## K čemu slouží

BRID byl vytvořen, aby vyřešil kritickou regulatorní a bezpečnostní mezeru v rychle se rozvíjející oblasti komerčních a rekreačních operací s drony. Letecké úřady, jako je FAA ve Spojených státech a EASA v Evropě, uložily povinnost, aby drony musely být za letu vzdáleně identifikovatelné, aby bylo zajištěno odpovědní zařízení, zvýšena bezpečnost a umožněna bezpečná integrace [UAS](/mobilnisite/slovnik/uas/) do národního vzdušného prostoru. Před standardizací v rámci 3GPP existovala proprietární nebo necíťová řešení, ale postrádala globální interoperabilitu, škálovatelnost a integraci s infrastrukturou mobilních operátorů.

Hlavním problémem, který BRID řeší, je poskytnutí standardizované, zabezpečené a spolehlivé metody, pomocí které drony mohou oznamovat svou identitu a základní telemetrii komukoli v blízkosti s vhodným přijímačem. To umožňuje orgánům činným v trestním řízení, bezpečnostním složkám, dalším uživatelům vzdušného prostoru a znepokojeným občanům identifikovat dron a jeho operátora bez nutnosti navázat síťové spojení. Řeší omezení předchozích přístupů, které byly často izolované, používaly nestandardní protokoly nebo postrádaly robustní bezpečnostní funkce, což je činilo zranitelnými vůči podvržení nebo rušení.

Historicky motivace pro jeho vytvoření ve verzi 3GPP 17 vycházela ze silné poptávky průmyslu a regulátorů po využití všudypřítomní mobilní technologie pro služby UAS. Mobilní sítě nabízejí široké pokrytí, vysokou spolehlivost, vestavěnou bezpečnost a možnosti správy. Definováním BRID v rámci ekosystému 3GPP je zajištěno, že drony mohou pro identifikaci používat stejný hardwarový hardware zařízení a spektrum (kde je to možné) jako pro komunikaci řízení letu a přenos dat, což zjednodušuje návrh a certifikaci zařízení. To staví mobilní sítě do role klíčového prvku digitální infrastruktury potřebné pro rozsáhlé operace UAS.

## Klíčové vlastnosti

- Standardizované vysílání ID UAS a polohy/výšky
- Podpora povinných i volitelných datových prvků (např. polohy pilota, rychlosti)
- Využití sidelink technologií 3GPP (LTE-V2X, NR sidelink) pro přímé zařízení-zařízení vysílání
- Integrované bezpečnostní mechanismy pro autentizaci zpráv a ochranu integrity
- Definovaná struktura zpráv a protokolů napříč aplikační, síťovou a rádiovou vrstvou
- Doplňuje síťové služby identifikace a sledování UAS

## Související pojmy

- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)

## Definující specifikace

- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.754** (Rel-17) — Study on UAS Connectivity, ID & Tracking
- **TS 24.577** (Rel-19) — A2X Services in 5GS
- **TS 24.578** (Rel-19) — UE policies for A2X services in 5GS
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 33.256** (Rel-19) — Security for Uncrewed Aerial Systems (UAS)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [BRID na 3GPP Explorer](https://3gpp-explorer.com/glossary/brid/)
