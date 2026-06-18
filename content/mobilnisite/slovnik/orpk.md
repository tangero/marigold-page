---
slug: "orpk"
url: "/mobilnisite/slovnik/orpk/"
type: "slovnik"
title: "ORPK – Operator Root Public Key"
date: 2025-01-01
abbr: "ORPK"
fullName: "Operator Root Public Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/orpk/"
summary: "Kryptografický veřejný klíč, který slouží jako důvěryhodný kotvící bod (trust anchor) pro infrastrukturu veřejných klíčů (PKI) operátora. Používá se k ověření pravosti dat podepsaných operátorem, jako"
---

ORPK je kořenový veřejný klíč operátora, který slouží jako důvěryhodný kotvící bod (trust anchor) pro ověřování pravosti dat podepsaných operátorem, jako jsou síťové politiky nebo softwarové aktualizace, a zajišťuje tak bezpečný provoz sítě.

## Popis

Operator Root Public Key (ORPK, kořenový veřejný klíč operátora) je základní součástí bezpečnostní infrastruktury definované standardy 3GPP pro operátory mobilních sítí. Představuje veřejnou část asymetrického klíčového páru, kde odpovídající soukromý klíč, kořenový soukromý klíč operátora, je držen a přísně chráněn síťovým operátorem. Tento klíčový pár tvoří kořen důvěry pro infrastrukturu veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) operátora. ORPK je distribuován do uživatelských zařízení (UE), jako jsou mobilní telefony a IoT zařízení, kde je uložen v zabezpečeném, proti neoprávněné manipulaci odolném prostředí, často na univerzální čipové kartě (UICC) nebo v důvěryhodné prováděcí oblasti (trusted execution environment) zařízení.

Funkčně se ORPK používá k ověřování digitálních podpisů vytvořených operátorem. Když síť potřebuje vybavit UE kritickými, na důvěře závislými daty – jako jsou seznamy [OPLMN](/mobilnisite/slovnik/oplmn/) (Operator Controlled [PLMN](/mobilnisite/slovnik/plmn/) Selector with Access Technology), konfigurační parametry [SMS](/mobilnisite/slovnik/sms/) nebo manifesty softwarových aktualizací – podepíše tato data pomocí svého soukromého klíče. UE přijme jak data, tak podpis. Pomocí předinstalovaného ORPK provede UE kryptografické ověření podpisu. Pokud je podpis platný, může UE důvěřovat, že data pocházejí od jejího legitimního domovského operátora a nebyla pozměněna, což zajišťuje integritu a pravost konfigurace.

Architektura zahrnuje několik specifikací, především TS 23.057, která podrobně popisuje bezpečnostní mechanismy pro data řízená operátorem. ORPK umožňuje škálovatelný model důvěry. Namísto zabezpečování každého jednotlivého komunikačního kanálu složitými symetrickými klíči operátor používá tento jediný kořen důvěry k podepisování různých dokumentů. To je klíčové pro provizionování a správu přes rozhraní ([OTA](/mobilnisite/slovnik/ota/)), které chrání před škodlivými subjekty, jež by se mohly pokusit přesměrovat zařízení na podvodné sítě nebo instalovat neautorizovaný software. Správa životního cyklu ORPK, včetně případného odvolání a obnovy, je kritickým procesem operační bezpečnosti pro operátora, který udržuje trvalou důvěru.

## K čemu slouží

ORPK byl zaveden, aby řešil rostoucí potřebu bezpečného, ověřeného provizionování a řízení mobilních zařízení jejich domovskými síťovými operátory. Před takovými mechanismy založenými na [PKI](/mobilnisite/slovnik/pki/) se řízení chování zařízení pro výběr sítě nebo konfiguraci služeb více spoléhalo na méně bezpečné metody nebo implicitní důvěru, které byly zranitelné vůči falšování a manipulaci. S vývojem sítí a rostoucí složitostí zařízení se zvýšilo riziko škodlivého přesměrování (např. navedení zařízení na falešnou základnovou stanici) nebo neoprávněných konfiguračních změn.

Jeho vytvoření ve vydání (Release) 5 bylo motivováno potřebou standardizovaného, kryptograficky silného základu pro kontrolu operátora. Řeší problém vytvoření důvěryhodného kanálu pro jednosměrnou, vysílací (broadcast) nebo push komunikaci od operátora k potenciálně milionům zařízení. Poskytnutím ověřitelného kořene důvěry umožňuje operátorům bezpečně nasazovat síťové politiky, spravovat preferované roamingové seznamy a řídit chování zařízení v oblasti konektivity v nepřátelském rádiovém prostředí. To je nezbytné pro udržení integrity sítě, optimalizaci provozu a zajištění souladu zařízení s provozními smlouvami a regulatorními požadavky operátora, a to vše při ochraně koncového uživatele před útoky typu man-in-the-middle.

## Klíčové vlastnosti

- Slouží jako důvěryhodný kotvící bod (trust anchor) pro PKI operátora
- Předinstalován v zabezpečeném úložišti UE (např. na UICC)
- Používá se k ověření digitálních podpisů na datech podepsaných operátorem
- Umožňuje bezpečné OTA provizionování síťových politik (např. seznamů OPLMN)
- Chrání před falšováním a neoprávněnými konfiguračními změnami
- Základní prvek pro zabezpečení Operator Controlled PLMN Selector

## Související pojmy

- [PKI – Public Key Infrastructure](/mobilnisite/slovnik/pki/)
- [OPLMN – Operator Controlled PLMN (Selector List)](/mobilnisite/slovnik/oplmn/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [ORPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/orpk/)
