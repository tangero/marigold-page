---
slug: "bci"
url: "/mobilnisite/slovnik/bci/"
type: "slovnik"
title: "BCI – Backward Call Indicators"
date: 2025-01-01
abbr: "BCI"
fullName: "Backward Call Indicators"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bci/"
summary: "BCI je sada informačních elementů ve 3GPP signalizačních protokolech, které přenášejí parametry související s hovorem z ukončovací strany zpět k volající straně během sestavování hovoru. Umožňuje sprá"
---

BCI je sada signalizačních informačních elementů, které se vysílají od ukončovací strany k volající straně během sestavování hovoru za účelem umožnění správného zpracování hovoru a spolupráce sítí (interworking) předáním informací o schopnostech volaného účastníka a stavu sítě.

## Popis

Indikátory zpětného volání (Backward Call Indicators, BCI) jsou souborem parametrů přenášených v obráceném směru (ze sítě volaného účastníka k síti volajícího účastníka) v signalizačních zprávách uživatelské části [ISDN](/mobilnisite/slovnik/isdn/) ([ISUP](/mobilnisite/slovnik/isup/)) a nezávislého řízení hovoru na přenosu (BICC). Tyto indikátory jsou definovány v 3GPP TS 29.163 jako součást specifikace pro spolupráci (interworking) mezi jádrovou sítí (CN) subsystému IP multimédií ([IM](/mobilnisite/slovnik/im/)) a sítěmi s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Parametry BCI jsou neseny ve specifických informačních elementech, které poskytují základní podrobnosti o straně ukončení hovoru pro síť v místě vzniku.

Během procedur sestavování hovoru, když hovor prochází ze sítě CS do sítě IP Multimedia Subsystem (IMS) nebo naopak, jsou parametry BCI extrahovány z příchozích zpráv ISUP a mapovány na příslušné hlavičky SIP nebo parametry BICC. K tomuto mapování dochází na funkci řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo na jiných interworking funkcích. BCI obsahuje klíčové informace, jako je povaha linky volaného účastníka, zda se jedná o telefonní automat, zda jsou přítomna zařízení pro potlačení ozvěny, a další charakteristiky specifické pro síť, které ovlivňují zpracování hovoru.

Klíčovými složkami BCI jsou parametry jako indikátor stavu volaného účastníka, který ukazuje, zda je volaný účastník volný, obsazený nebo má neznámý stav; indikátor účtování, který poskytuje informace o platebních podmínkách; a indikátor zařízení pro potlačení ozvěny, který signalizuje, zda je vyžadována kontrola ozvěny. Tyto parametry jsou kódovány jako bitová pole ve specifických oktetech signalizačních zpráv, což umožňuje efektivní přenos při zachování zpětné kompatibility se staršími systémy.

Úloha BCI v síti je zásadní pro udržení kvality služeb a správné směrování hovorů napříč heterogenními síťovými prostředími. Když hovor vzniká v síti CS a je ukončen v síti IMS, parametry BCI zajišťují, že síť IMS může uplatnit odpovídající politiky a postupy na základě charakteristik původní sítě. Podobně, když hovory směřují opačným směrem, BCI pomáhá síti CS pochopit schopnosti a požadavky sítě IMS, což umožňuje plynulé poskytování služeb přes hranice sítí.

## K čemu slouží

BCI bylo vytvořeno k řešení výzev spolupráce mezi sítěmi s přepojováním okruhů a paketů během přechodu na plně IP sítě. Jak telekomunikace přešly z tradičních sítí PSTN/[ISDN](/mobilnisite/slovnik/isdn/) na IP architektury IMS, vznikl kritický požadavek na zachování informací souvisejících s hovory, které byly nezbytné pro správné zpracování hovoru, účtování a kvalitu služeb. Bez BCI by při přechodu hovorů přes hranice sítí docházelo ke ztrátě důležitých parametrů o charakteristikách linky volaného účastníka a stavu sítě, což by vedlo ke snížené kvalitě služeb a nesprávnému účtování.

Historicky signalizace [ISUP](/mobilnisite/slovnik/isup/) v sítích [CS](/mobilnisite/slovnik/cs/) obsahovala četné parametry, které poskytovaly podrobné informace o charakteristikách hovoru, ale tyto parametry nebyly nativně podporovány v IP signalizačních protokolech jako je SIP. Vytvoření BCI poskytlo standardizovaný mechanismus pro mapování těchto klíčových parametrů mezi různými signalizačními doménami. To bylo obzvláště důležité během počátečních fází nasazení IMS, kdy většina hovorů stále vznikala nebo byla ukončena v legacy sítích CS, což vyžadovalo robustní řešení pro spolupráci.

BCI řeší problém ztráty informací při přechodech mezi sítěmi tím, že zajišťuje zachování a správnou interpretaci základních parametrů hovoru napříč různými generacemi sítí. Řeší omezení předchozích přístupů, které buď zavrhovaly důležité signalizační informace, nebo používaly proprietární mapovací řešení, která bránila interoperabilitě zařízení od různých výrobců. Standardizací indikátorů zpětného volání ve specifikacích 3GPP mohli síťoví operátoři nasazovat řešení od více dodavatelů a přitom zachovat konzistentní zpracování hovorů a kvalitu služeb v hybridních síťových prostředích.

## Klíčové vlastnosti

- Poskytuje mapování mezi parametry ISUP a hlavičkami SIP pro spolupráci sítí
- Přenáší charakteristiky linky volaného účastníka k volající síti
- Podporuje indikaci zařízení pro potlačení ozvěny pro správu kvality hlasu
- Umožňuje správný přenos informací pro účtování přes hranice sítí
- Zachovává zpětnou kompatibilitu se staršími sítěmi s přepojováním okruhů
- Napomáhá konzistentním politikám zpracování hovorů v hybridních síťových prostředích

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [BCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/bci/)
