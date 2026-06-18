---
slug: "c-msisdn"
url: "/mobilnisite/slovnik/c-msisdn/"
type: "slovnik"
title: "C-MSISDN – Correlation Mobile Station International Subscriber Directory Number"
date: 2025-01-01
abbr: "C-MSISDN"
fullName: "Correlation Mobile Station International Subscriber Directory Number"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/c-msisdn/"
summary: "C-MSISDN je dočasné MSISDN přidělené uživatelskému zařízení (UE) během relace kontinuity hlasového hovoru (VCC), které umožňuje plynulé předávání hovoru mezi okruhově spínanou (CS) a IP multimediální"
---

C-MSISDN je dočasné MSISDN přidělené uživatelskému zařízení (UE) během relace VCC, které slouží ke korelaci okruhově spínané (CS) a IMS větve hovoru, což umožňuje plynulý předávání hovoru a kontinuitu mezi těmito doménami.

## Popis

C-MSISDN je klíčový identifikátor v architektuře kontinuity hlasového hovoru ([VCC](/mobilnisite/slovnik/vcc/)) definované ve 3GPP Release 8 a novějších. Funguje jako dočasné, relaci specifické telefonní číslo mobilní stanice ([MSISDN](/mobilnisite/slovnik/msisdn/)) přidělené VCC aplikací v IMS síti, když uživatelské zařízení (UE) iniciuje nebo přijímá hovor s podporou VCC. Toto dočasné číslo se liší od primárního MSISDN uživatele a používá se výhradně po dobu trvání VCC relace k usnadnění procedur přechodu mezi doménami.

Architektonicky C-MSISDN funguje v rámci VCC aplikace, která sídlí v jádru IMS sítě. Když se VCC schopné UE zaregistruje v síti, může VCC aplikace předem přidělit fond čísel C-MSISDN nebo je přidělovat na požádání. Při sestavování hovoru, pokud je hovor předmětem VCC procedur, VCC aplikace přidělí UE číslo C-MSISDN a uloží mapování mezi tímto dočasným identifikátorem, primární identitou uživatele (např. veřejnou IMS identitou uživatele) a informacemi o aktuální hovorové relaci. Toto mapování je udržováno v databázi VCC aplikace po celou dobu trvání hovorové relace.

C-MSISDN umožňuje síti korelovat dvě větve VCC hovoru: okruhově spínanou ([CS](/mobilnisite/slovnik/cs/)) větev (typicky přes [GERAN](/mobilnisite/slovnik/geran/)/[UTRAN](/mobilnisite/slovnik/utran/)) a IMS větev (přes [E-UTRAN](/mobilnisite/slovnik/e-utran/) nebo jiný [IP-CAN](/mobilnisite/slovnik/ip-can/)). Když je iniciován přechod mezi doménami (například z IMS do CS), VCC aplikace použije C-MSISDN k identifikaci cílového UE v CS doméně. Síť směruje CS větev hovoru na toto dočasné číslo, které je rozpoznáno VCC aplikací. Aplikace následně propojí příchozí CS větev s existující IMS větví, čímž zachová kontinuitu hovoru bez nutnosti, aby volaná strana znovu vytočila nebo znovu navázala spojení.

Mezi klíčové komponenty zapojené do manipulace s C-MSISDN patří samotná VCC aplikace, domácí registr účastníka ([HSS](/mobilnisite/slovnik/hss/)) pro správu účastnických dat, MSC Server pro řízení CS domény a obslužná funkce řízení hovorové relace (S-CSCF) pro řízení IMS relací. C-MSISDN musí být směrovatelné v obou doménách, CS i IMS, a typicky následuje stejný formát číslování jako běžná MSISDN, ačkoli je přidělováno z vyhrazeného číselného rozsahu spravovaného operátorem.

Z pohledu protokolů se C-MSISDN objevuje v různých signalizačních zprávách, včetně SIP zpráv v IMS (zejména v hlavičce P-Asserted-Identity) a ISUP/BICC zpráv v CS doméně. VCC aplikace zajišťuje, že je C-MSISDN správně vloženo do relevantních signalizačních cest a že korelace mezi doménami je udržována po celou dobu hovorové relace, včetně přechodů během hovoru a procedur ukončení hovoru.

## K čemu slouží

C-MSISDN bylo vytvořeno k vyřešení zásadního problému udržení kontinuity hlasového hovoru, když se uživatelské zařízení pohybuje mezi různými technologiemi přístupové sítě, konkrétně mezi okruhově spínanými (CS) doménami (jako sítě 2G/3G) a IP multimediálními podsystémovými (IMS) doménami (jako sítě LTE/5G). Před VCC a mechanismem C-MSISDN by se hovory typicky přerušily při přechodu mezi těmito zásadně odlišnými síťovými architekturami, protože neexistoval standardizovaný způsob, jak korelovat dvě nezávislé větve hovoru existující v oddělených doménách.

Historicky, když operátoři začali nasazovat hlasové služby založené na IMS (VoLTE) vedle tradičních CS hlasových sítí, potřebovali řešení pro plynulé předávání hovoru mezi těmito doménami, zejména pro oblasti s nerovnoměrným pokrytím LTE. C-MSISDN poskytuje nezbytný korelační mechanismus, který umožňuje správné fungování kontinuity hlasového hovoru pro jedno rádio (SRVCC) a dalších variant VCC. Bez tohoto dočasného identifikátoru by síť neměla způsob, jak spojit příchozí CS větev hovoru s probíhající IMS relací, což by znemožnilo přechody mezi doménami bez přerušení hovoru.

C-MSISDN řeší několik konkrétních omezení předchozích přístupů: odstraňuje nutnost vystavit skutečné MSISDN uživatele během procedur přechodu mezi doménami (což zvyšuje soukromí), poskytuje čisté oddělení mezi identitou uživatele a směrováním relace a umožňuje standardizovanou vzájemnou spolupráci mezi CS a IMS sítěmi od různých dodavatelů. Tím, že slouží jako relaci specifická směrovací adresa, umožňuje C-MSISDN operátorům implementovat VCC bez nutnosti změn stávajících CS síťových prvků nebo narušení existujících systémů účtování a zákonného odposlechu.

## Klíčové vlastnosti

- Přidělování dočasného, relaci specifického identifikátoru
- Umožňuje korelaci mezi CS a IMS větvemi hovoru
- Podporuje procedury kontinuity hlasového hovoru pro jedno rádio (SRVCC)
- Chrání soukromí uživatele skrytím primárního MSISDN během přechodů
- Standardizované směrování napříč CS a IMS doménami
- Integrace se stávajícími systémy účtování a zákonného odposlechu

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [C-MSISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-msisdn/)
