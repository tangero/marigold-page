---
slug: "spd"
url: "/mobilnisite/slovnik/spd/"
type: "slovnik"
title: "SPD – Security Policy Database"
date: 2025-01-01
abbr: "SPD"
fullName: "Security Policy Database"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spd/"
summary: "Databáze, která ukládá bezpečnostní politiky IPsec a definuje bezpečnostní služby, jež mají být aplikovány na IP pakety procházející zabezpečeným rozhraním. Je základní součástí architektury IPsec, um"
---

SPD (databáze bezpečnostních politik) je databáze, která ukládá bezpečnostní politiky IPsec, aby definovala a vynucovala bezpečnostní služby aplikované na IP pakety procházející zabezpečeným rozhraním.

## Popis

Databáze bezpečnostních politik (SPD) je základním prvkem v architektuře zabezpečení [IPsec](/mobilnisite/slovnik/ipsec/) podle 3GPP, jak je definována ve specifikacích jako 33.210. Funguje ve spojení s databází bezpečnostních asociací ([SAD](/mobilnisite/slovnik/sad/)) k vynucování bezpečnostních politik pro IP provoz. SPD obsahuje uspořádaný seznam záznamů politik, z nichž každý specifikuje selektory (jako zdrojové/cílové IP adresy, transportní protokol a čísla portů) a přidruženou akci pro pakety odpovídající těmto selektorům. Možné akce jsou typicky PROTECT (aplikovat IPsec), BYPASS (povolit bez IPsec) nebo DISCARD (zablokovat). Při zpracování paketu (příchozího nebo odchozího) systém konzultuje SPD, aby na základě polí hlavičky paketu určil příslušné bezpečnostní zacházení.

Role SPD je klíčová pro klasifikaci paketů. U odchozího provozu záznam v SPD určuje, zda paket vyžaduje ochranu IPsec, a pokud ano, odkazuje na konkrétní bezpečnostní asociaci ([SA](/mobilnisite/slovnik/sa/)) v SAD, která obsahuje kryptografické algoritmy, klíče a parametry k použití. Systém používá selektory z odpovídajícího záznamu SPD k vyhledání existující SA v SAD nebo k aktivaci vytvoření nové prostřednictvím IKEv2. U příchozího provozu je paket po zpracování IPsec (dešifrování/autentizace) znovu kontrolován vůči SPD, aby bylo zajištěno, že aplikovaná bezpečnost odpovídá politice, což poskytuje finální bezpečnostní validaci.

Architektonicky je SPD logická konstrukce, kterou lze implementovat v různých síťových prvcích vyžadujících IPsec, jako je bezpečnostní brána ([SEG](/mobilnisite/slovnik/seg/)) v rámci [NDS/IP](/mobilnisite/slovnik/nds-ip/) nebo uživatelské zařízení. Její správa je zásadní; politiky mohou být zřízeny staticky nebo dynamicky. Uspořádaná povaha SPD znamená, že se použije první odpovídající pravidlo, což vyžaduje pečlivý návrh politik, aby se předešlo konfliktům. Umožňuje detailní kontrolu, což operátorům definovat různé úrovně zabezpečení pro různé typy provozu (např. signalizační vs. uživatelská rovina) mezi síťovými doménami, čímž tvoří základní kámen vynucování politik v modelu zabezpečení síťových domén (NDS) 3GPP.

## K čemu slouží

SPD byla zavedena, aby řešila kritickou potřebu standardizovaného, politikami řízeného zabezpečení na rozhraních jádra sítě založených na IP, jak je definuje 3GPP. Jak se mobilní sítě vyvíjely z přepojování okruhů na architektury plně založené na IP, signalizace a uživatelská data procházející mezioperátorskými a vnitrooperátorskými rozhraními se stala zranitelnými vůči odposlechu, podvržení a dalším útokům. Hlavním problémem byl nedostatek jednotného, konfigurovatelného mechanismu, který by selektivně nařizoval a aplikoval kryptografickou ochranu na různé toky provozu.

Před formalizací SPD v rámci [NDS/IP](/mobilnisite/slovnik/nds-ip/) 3GPP byla bezpečnostní řešení často ad-hoc. SPD, jako koncept převzatý a adaptovaný ze standardů [IPsec](/mobilnisite/slovnik/ipsec/) [IETF](/mobilnisite/slovnik/ietf/), poskytuje strukturovanou databázi, která řeší problém 'co chránit'. Umožňuje síťovým architektům a bezpečnostním pracovníkům explicitně definovat, které IP pakety musí být chráněny, které mohou projít nešifrované a které mají být blokovány. Tím přesouvá zabezpečení z implicitní, pevně zakódované vlastnosti na explicitně spravovanou politiku. Její vytvoření bylo motivováno požadavkem na škálovatelný, interoperabilní bezpečnostní rámec, který by dokázal pojmout různorodý a rostoucí počet síťových rozhraní (např. Nn, Np, S1, X2), a zároveň poskytoval operátorům flexibilitu v jejich bezpečnostním postoji na základě posouzení rizik a regulatorních požadavků.

## Klíčové vlastnosti

- Ukládá uspořádaná pravidla bezpečnostních politik pro klasifikaci IP paketů
- Definuje akce: PROTECT (IPsec), BYPASS nebo DISCARD pro odpovídající pakety
- Používá selektory paketů (IP adresy, porty, protokol) pro porovnávání s pravidly
- Spolupracuje s databází bezpečnostních asociací (SAD) k vynucení kryptografie
- Aplikuje se na příchozí i odchozí provoz pro komplexní vynucování politik
- Ústřední prvek architektury zabezpečení síťových domén 3GPP/IP (NDS/IP)

## Související pojmy

- [SAD – Security Association Database](/mobilnisite/slovnik/sad/)
- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [SPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/spd/)
