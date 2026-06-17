---
slug: "nprach"
url: "/mobilnisite/slovnik/nprach/"
type: "slovnik"
title: "NPRACH – Narrowband Physical Random Access Channel"
date: 2025-01-01
abbr: "NPRACH"
fullName: "Narrowband Physical Random Access Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nprach/"
summary: "Fyzický kanál pro náhodný přístup (random access channel) pro NB-IoT (Narrowband IoT). Používají jej zařízení k zahájení komunikace se sítí, provedení počátečního přístupu, vyžádání si uplinkových zdr"
---

NPRACH je úzkopásmový fyzický kanál pro náhodný přístup (Narrowband Physical Random Access Channel) pro NB-IoT, používaný zařízeními k zahájení komunikace se sítí, vyžádání si uplinkových zdrojů a synchronizaci časování v energeticky úsporných scénářích s rozšířeným pokrytím.

## Popis

Úzkopásmový fyzický kanál pro náhodný přístup (Narrowband Physical Random Access Channel, NPRACH) je klíčový uplinkový fyzický kanál v rádiové technologii Narrowband Internet of Things (NB-IoT), standardizované 3GPP. Je protějškem kanálu PRACH v LTE, ale je specificky navržen pro jedinečná omezení IoT zařízení: ultra-nízkou spotřebu energie, rozšířené pokrytí (až 164 dB maximální ztráty spojení) a provoz v úzkém pásmu 180 kHz. NPRACH používá uživatelské zařízení (UE) k provedení procedury náhodného přístupu, což je počáteční krok pro zařízení k synchronizaci v uplinku, vyžádání si uplinkových zdrojů a navázání spojení se sítí.

Z architektonického hlediska není NPRACH kontinuálně vysílaný kanál. Skládá se z preambulí, které UE vysílají na vyhrazených časově-frekvenčních zdrojích nakonfigurovaných sítí prostřednictvím systémových informací. Klíčovým konstrukčním prvkem je přenos jedním tónem (single-tone), což znamená, že preambule je vysílána vždy pouze na jednom subnosném (s roztečí 3,75 kHz nebo 15 kHz). Samotná preambule je sekvence skupin symbolů, přičemž každá skupina podléhá frekvenčnímu přeskoku podle předdefinovaného vzoru. Tento frekvenční přeskok poskytuje frekvenční diverzitu, která je klíčová pro překonání hlubokých útlumů a dosažení extrémních cílů pokrytí NB-IoT. Základnová stanice (eNodeB pro LTE-NB nebo gNB pro NR-NB) tyto preambule detekuje a odhaduje časový předstih (timing advance) zařízení, což je nezbytné pro zarovnání uplinkových přenosů od zařízení v různých vzdálenostech.

Jak funguje: Síť vysílá konfigurační parametry NPRACH, včetně periodicity, počátečního času, dostupných subnosných a počtu opakování pro každý formát preambule. Zařízení, které si přeje přistoupit k síti, náhodně vybere sekvenci preambule a subnosné z povolené sady. Poté preambuli vysílá a opakuje ji podle konfigurace, aby zajistilo spolehlivou detekci i ve velmi špatných signálových podmínkách. Základnová stanice po detekci odešle odpověď na náhodný přístup (Random Access Response, RAR) na [NPDSCH](/mobilnisite/slovnik/npdsch/), která obsahuje příkaz časového předstihu, počáteční přidělení uplinkových zdrojů (uplink grant) a dočasný identifikátor. Celý tento proces je optimalizován pro minimální složitost zařízení a spotřebu energie a podporuje tři úrovně rozšíření pokrytí (coverage enhancement, [CE](/mobilnisite/slovnik/ce/)) s různými počty opakování, aby se přizpůsobil aktuálním rádiovým podmínkám zařízení.

## K čemu slouží

NPRACH byl vytvořen speciálně pro NB-IoT, aby řešil výzvy náhodného přístupu, které představují zařízení hromadné komunikace strojového typu (massive machine-type communication, mMTC). Tradiční PRACH z LTE, navržený pro smartphony, nebyl vhodný pro IoT zařízení, která potřebují fungovat roky na baterii, často v náročných rádiových podmínkách, jako jsou sklepy nebo venkovské oblasti. Klíčovými problémy byla vysoká spotřeba energie způsobená širokopásmovými přenosy a nedostatečné pokrytí pro zařízení na okraji buňky.

Motivací bylo navrhnout kanál pro náhodný přístup, který by mohl dosáhnout až o 20 dB většího pokrytí než LTE, a zároveň byl extrémně energeticky úsporný. Přenos jedním tónem (single-tone) u NPRACH snižuje poměr špičkového a průměrného výkonu (peak-to-average power ratio, PAPR), což umožňuje výkonovému zesilovači zařízení pracovat efektivněji a šetřit baterii. Podpora masivních opakování (až 128) umožňuje, aby byl signál na přijímací straně integrován v čase, čímž se detekční citlivost posouvá na hranice možností. Řeší omezení standardního LTE PRACH tím, že funguje v rámci úzkopásmových omezení NB-IoT a zavádí strukturu preambule založenou na přeskakování a rozšiřující pokrytí. To umožňuje miliardám levných, nízkopříkonových IoT zařízení spolehlivě navázat kontakt se sítí prakticky z jakéhokoli místa, což tvoří základ pro cíle NB-IoT v oblasti masivní konektivity a hlubokého pokrytí.

## Klíčové vlastnosti

- Navržen pro NB-IoT v rámci systémové šířky pásma 180 kHz
- Používá přenos jedním tónem (subnosné 3,75 kHz nebo 15 kHz) pro energetickou účinnost
- Využívá strukturu preambule s frekvenčním přeskakováním pro rozšíření pokrytí a randomizaci interference
- Podporuje více úrovní rozšíření pokrytí (coverage enhancement, CE) s konfigurovatelnými opakováními preambule
- Konfigurovatelná periodicita a zdroje pro podporu masivního počtu zařízení
- Umožňuje synchronizaci časování v uplinku prostřednictvím odhadu časového předstihu (timing advance) sítí

## Související pojmy

- [NPDSCH – Narrow Band Physical Downlink Shared Channel](/mobilnisite/slovnik/npdsch/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NPRACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/nprach/)
